import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .output-container {
        position: relative;
        width: 300px;
        height: 100px;
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        z-index: 0;
    }
    .hidden-button {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: transparent; /* 완전 투명 */
        border: none;
        cursor: pointer;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 출력창 생성
output_text = (
    "현재 상태: ON" if st.session_state["button_clicked"] else "현재 상태: OFF"
)
st.markdown(
    f"""
    <div class="output-container">
        <p>{output_text}</p>
        <button class="hidden-button" onclick="document.querySelector('[data-testid^=stButton]').click();"></button>
    </div>
    """,
    unsafe_allow_html=True,
)

# 히든 버튼 클릭 처리
if st.button("Hidden Button", key="hidden_button", help="You won't see me!"):
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]
