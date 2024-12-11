import streamlit as st

# 초기 세션 상태 설정
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False  # 버튼 클릭 여부 저장

# 버튼 클릭 처리
col1, col2 = st.columns(2)

with col1:
    if st.button("Click Me (Top Button)", key="top_button"):
        st.session_state["button_clicked"] = not st.session_state["button_clicked"]

with col2:
    if st.button("Click Me (Bottom Button)", key="bottom_button"):
        st.session_state["button_clicked"] = not st.session_state["button_clicked"]

# 버튼 상태 출력
if st.session_state["button_clicked"]:
    st.success("버튼이 클릭되었습니다!")
else:
    st.info("버튼을 클릭하세요.")
