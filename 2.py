import streamlit as st
import pandas as pd
import os

# 파일 이름 정의
FILE_NAME = "table_data.csv"
CAUSE_EFFECT_FILE = "cause_effect_data.csv"

# 10x10 데이터프레임 생성 함수
def create_default_table():
    return pd.DataFrame([[
        "" for _ in range(10)] for _ in range(10)],
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

    # 첫 행과 첫 열도 수정 가능하도록 표시
    try:
        with st.expander("Edit Table", expanded=True):
            data.reset_index(inplace=True)  # 첫 번째 열도 수정 가능하도록 인덱스를 열로 변환
            data = st.data_editor(data, use_container_width=True, height=800, key="editable_table")

        # 저장 버튼
        if st.button("Save Table"):
            if "index" in data.columns:
                data.set_index("index", inplace=True)  # 인덱스를 다시 설정
            save_table_to_file(data, FILE_NAME)
            st.success("Table has been saved successfully!")

        # 불러오기 버튼
        if st.button("Load Table"):
            data = load_table_from_file(FILE_NAME, create_default_table)
            st.experimental_rerun()  # 새로고침

    except Exception as e:
        st.error(f"Error editing table: {e}")

elif choice == "Cause & Effect":
    st.subheader("Cause & Effect")

    # 데이터 불러오기 또는 기본 테이블 생성
    cause_effect_data = load_table_from_file(CAUSE_EFFECT_FILE, create_cause_effect_table)

    # 입력 폼
    with st.form("cause_effect_form"):
        cause = st.text_input("Enter Cause:")
        effect = st.text_input("Enter Effect:")
        submitted = st.form_submit_button("Add Entry")

        if submitted and cause and effect:
            new_entry = pd.DataFrame([[cause, effect]], columns=["Cause", "Effect"]).astype(str)
            cause_effect_data = pd.concat([cause_effect_data, new_entry], ignore_index=True)
            save_table_to_file(cause_effect_data, CAUSE_EFFECT_FILE)
            st.success("Entry added successfully!")

    # 데이터 표시
    st.subheader("Current Cause & Effect Data")
    st.dataframe(cause_effect_data, use_container_width=True)

elif choice == "Settings":
    st.subheader("Settings")
    st.write("Settings page content here.")

elif choice == "Upload Excel":
    st.subheader("Upload Excel File")

    # 엑셀 파일 업로드
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # 업로드된 엑셀 파일 읽기
            excel_data = pd.read_excel(uploaded_file, engine='openpyxl')
            st.success("File uploaded successfully!")
            
            # 업로드된 데이터 표시
            with st.expander("Uploaded Excel Data", expanded=True):
                st.dataframe(excel_data, use_container_width=True, height=800)
        except ImportError:
            st.error("Missing dependency: openpyxl. Install it using 'pip install openpyxl'.")
        except Exception as e:
            st.error(f"Error loading file: {e}")
