import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .custom-button {
        background-color: #4CAF50; /* 기본 버튼 색상 (초록색) */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .custom-button.clicked {
        background-color: #FF5733; /* 클릭 시 버튼 색상 (주황색) */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 버튼 클릭 처리
if st.button("Click Me"):
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]

# 버튼 상태에 따른 클래스 변경
button_class = "custom-button clicked" if st.session_state["button_clicked"] else "custom-button"

# 버튼 렌더링
st.markdown(f'<button class="{button_class}">Click Me</button>', unsafe_allow_html=True)

# 상태 출력 (테스트용)
st.write(f"버튼 상태: {'클릭됨' if st.session_state['button_clicked'] else '미클릭'}")
