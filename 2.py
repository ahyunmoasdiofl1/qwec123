import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 5px; /* 버튼 사이 간격 */
    }
    .button-top, .button-bottom {
        border: none;
        padding: 10px 20px;
        text-align: center;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        width: 150px; /* 버튼 폭 고정 */
    }
    .button-top {
        background-color: white;
        color: black;
        border: 1px solid #ddd;
    }
    .button-bottom {
        background-color: #4CAF50;
        color: white;
    }
    .button-top:hover, .button-bottom:hover {
        opacity: 0.8; /* 호버 시 투명도 효과 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 클릭 이벤트 처리
if st.button("Click Here (Fake Combined Button)", key="combined_button"):
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]

# 버튼 컨테이너 렌더링
st.markdown(
    f"""
    <div class="button-container">
        <button class="button-top" onclick="document.querySelector('[data-testid^=stMarkdownContainer]').click();">Click Me</button>
        <button class="button-bottom" onclick="document.querySelector('[data-testid^=stMarkdownContainer]').click();">Click Me</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# 버튼 상태 출력
st.write(f"버튼 상태: {'클릭됨' if st.session_state['button_clicked'] else '미클릭'}")
