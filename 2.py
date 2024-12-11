import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# 클릭 상태에 따라 출력될 텍스트 설정
output_text = (
    "현재 상태: ON" if st.session_state["button_clicked"] else "현재 상태: OFF"
)

# CSS로 출력창과 투명 버튼 겹치기
st.markdown(
    f"""
    <style>
    .container {{
        position: relative;
        width: 300px;
        height: 100px;
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        border-radius: 5px;
        text-align: center;
        line-height: 100px; /* 텍스트 가운데 정렬 */
        font-size: 18px;
        z-index: 1;
    }}
    .hidden-button {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: transparent;
        border: none;
        cursor: pointer;
        z-index: 2; /* 출력창보다 위에 배치 */
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 출력창 생성
st.markdown(
    f"""
    <div class="container">
        {output_text}
        <button class="hidden-button" onclick="window.location.href = window.location.href + '&hidden_button=true'"></button>
    </div>
    """,
    unsafe_allow_html=True,
)

# 버튼 클릭 이벤트 처리
query_params = st.experimental_get_query_params()
if "hidden_button" in query_params:
    st.session_state["button_clicked"] = not st.session_state["button_clicked"]
    st.experimental_set_query_params()  # 상태 초기화
