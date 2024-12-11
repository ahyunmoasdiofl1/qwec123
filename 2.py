import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False

# CSS 스타일 정의
st.markdown(
    """
    <style>
    .combined-button {
        display: inline-block;
        text-align: center;
        cursor: pointer;
        border: none;
        border-radius: 10px;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background: linear-gradient(to bottom, #ffffff, #4CAF50); /* 위에서 아래로 색상 변화 */
        transition: background 0.3s;
    }
    .combined-button:hover {
        background: linear-gradient(to bottom, #4CAF50, #ffffff); /* 호버 시 반대 방향으로 색상 변화 */
    }
    .combined-button:active {
        background-color: #FF5733; /* 클릭 시 버튼 색상 변경 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 버튼 클릭 처리
if st.button("Click Me", key="combined_button"):
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]

# 버튼 출력
st.markdown(
    f"""
    <button class="combined-button">Click Me</button>
    """,
    unsafe_allow_html=True,
)

# 상태 출력
if st.session_state["button_clicked"]:
    st.success("버튼이 클릭되었습니다!")
else:
    st.info("버튼을 클릭하세요.")
