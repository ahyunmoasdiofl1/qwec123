import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .dynamic-button {
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        text-align: center;
        color: white;
        transition: background 0.3s;
    }
    .dynamic-button.default {
        background-color: #4CAF50; /* 기본 상태: 초록색 */
    }
    .dynamic-button.clicked {
        background-color: #FF5733; /* 클릭 상태: 주황색 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 클릭 상태에 따른 텍스트와 클래스 설정
if st.session_state["button_clicked"]:
    button_text = "Clicked! 상태: ON"
    button_class = "dynamic-button clicked"
else:
    button_text = "Click Me 상태: OFF"
    button_class = "dynamic-button default"

# 버튼 HTML 생성
button_html = f"""
<button class="{button_class}" onclick="document.querySelector('[data-testid^=stButton]').click();">{button_text}</button>
"""

# 버튼 클릭 처리
if st.button("Hidden Button", key="dynamic_button"):
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]

# 버튼 렌더링
st.markdown(button_html, unsafe_allow_html=True)
