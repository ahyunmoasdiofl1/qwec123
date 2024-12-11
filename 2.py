import streamlit as st
import pandas as pd
import os

# 파일 이름 정의
FILE_NAME = "table_data.csv"
CAUSE_EFFECT_FILE = "cause_effect_data.csv"

# 10x10 데이터프레임 생성 함수

def create_default_table():
    return pd.DataFrame([[
        "Run" for _ in range(10)] for _ in range(10)],
        columns=[f"Col {i+1}" for i in range(10)]).astype(str)  # 모든 데이터를 문자열로 설정

# 원인/대책 데이터프레임 생성 함수
def create_cause_effect_table():
    return pd.DataFrame(columns=["Cause", "Effect"]).astype(str)  # 모든 데이터를 문자열로 설정

# 데이터 저장 함수
def save_table_to_file(df, filename):
    df.to_csv(filename, index=False, encoding="utf-8-sig")

# 데이터 불러오기 함수
def load_table_from_file(filename, default_creator):
    if os.path.exists(filename):
        try:
            return pd.read_csv(filename, encoding="utf-8").astype(str)  # 데이터를 문자열로 변환
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return default_creator()
    else:
        return default_creator()

# Streamlit App 시작
st.set_page_config(layout="wide")
st.title("Editable Table with Save/Load")

# 메뉴 설정
menu = ["Home", "TIP DOWN", "Cause & Effect", "Settings", "Upload Excel"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Home Page")
    st.write("Use the sidebar to navigate to other sections.")

elif choice == "TIP DOWN":
    st.subheader("TIP DOWN")

    # 데이터 불러오기 또는 기본 테이블 생성
    data = load_table_from_file(FILE_NAME, create_default_table)

    # 셀 상태 관리 변수
    if "cell_states" not in st.session_state:
        st.session_state.cell_states = pd.DataFrame([[
            "Run" for _ in range(10)] for _ in range(10)],
            columns=[f"Col {i+1}" for i in range(10)]).astype(str)

    def get_next_state(current_state):
        if current_state == "Run":
            return "Tip", "#FFFF00"  # 노랑
        elif current_state == "Tip":
            return "Down", "#FF0000"  # 빨강
        else:
            return "Run", "#00FF00"  # 초록

    # 테이블 렌더링
    table_html = "<table style='border-collapse: collapse; width: 100%;'>"
    for row_idx in range(len(data)):
        table_html += "<tr>"
        for col_idx, col in enumerate(data.columns):
            if row_idx == 0 or col_idx == 0:  # 첫 행과 첫 열은 수정 가능
                cell_value = data.iloc[row_idx, col_idx]
                editable = f"<input type='text' value='{cell_value}' style='width: 100%; border: 1px solid black;'>"
                table_html += f"<td style='border: 1px solid black; text-align: center;'>{editable}</td>"
            else:
                cell_key = f"cell_{row_idx}_{col_idx}"
                current_state = st.session_state.cell_states.iloc[row_idx, col_idx]
                next_state, color = get_next_state(current_state)

                # 버튼과 원을 가로로 정렬
                button_html = f"<button style='background-color:transparent; border:none; cursor:pointer;' onclick='window.location.reload();'>{current_state}</button>"
                circle_html = f"<div style='margin-left: 5px; width: 20px; height: 20px; background-color:{color}; border-radius: 50%; display: inline-block;'></div>"
                content_html = f"<div style='display: flex; align-items: center;'>{button_html}{circle_html}</div>"

                table_html += f"<td style='border: 1px solid black; text-align: center;'>{content_html}</td>"
        table_html += "</tr>"
    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

    # 저장 및 불러오기 버튼을 한 줄에 배치
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save Table"):
            save_table_to_file(st.session_state.cell_states, FILE_NAME)
            st.success("Table has been saved successfully!")
    with col2:
        if st.button("Load Table"):
            st.session_state.cell_states = load_table_from_file(FILE_NAME, create_default_table)
            st.experimental_rerun()  # 새로고침
