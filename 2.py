import streamlit as st
import pandas as pd

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .custom-button {
        background-color: #4CAF50; /* 버튼 배경색 (초록색) */
        color: white; /* 버튼 텍스트 색상 */
        border: none; /* 테두리 제거 */
        padding: 10px 20px; /* 버튼 여백 */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px; /* 버튼 모서리 둥글게 */
        cursor: pointer; /* 마우스를 올리면 포인터 표시 */
    }
    .custom-button:hover {
        background-color: #45a049; /* 호버 시 배경색 변경 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 버튼 UI 생성
if st.markdown('<button class="custom-button">Click Me</button>', unsafe_allow_html=True):
    st.write("버튼이 클릭되었습니다!")
