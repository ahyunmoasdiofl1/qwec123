import streamlit as st

# 데이터 상태 정의
rows = [f"Row {i+1}" for i in range(8)]
columns = [f"CH{i+1}" for i in range(9)]

# 초기 상태 (0=Green, 1=Red, 2=Yellow)
if "status" not in st.session_state:
    st.session_state["status"] = [[0 for _ in columns] for _ in rows]  # 초기 상태

# 색상 매핑
color_map = {0: "#4CAF50", 1: "#FF0000", 2: "#FFD700"}  # Green, Red, Yellow

# 스타일 정의
st.markdown(
    """
    <style>
    .table {
        display: grid;
        grid-template-columns: 150px repeat(9, 100px);
        gap: 2px;
        border-collapse: collapse;
    }
    .header {
        background-color: #f1f1f1;
        text-align: center;
        font-weight: bold;
        border: 1px solid #ddd;
        padding: 8px;
    }
    .cell {
        text-align: center;
        border: 1px solid #ddd;
        padding: 8px;
        background-color: white;
    }
    .circle {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 표 출력
st.markdown('<div class="table">', unsafe_allow_html=True)

# 헤더 출력
st.markdown('<div class="header">Name</div>', unsafe_allow_html=True)
for col in columns:
    st.markdown(f'<div class="header">{col}</div>', unsafe_allow_html=True)

# 데이터 출력
for row_idx, row_name in enumerate(rows):
    # 행 이름 출력
    st.markdown(f'<div class="cell">{row_name}</div>', unsafe_allow_html=True)
    for col_idx in range(len(columns)):
        # 현재 상태 가져오기
        status = st.session_state["status"][row_idx][col_idx]
        color = color_map[status]
        # 버튼 생성
        if st.button(" ", key=f"btn_{row_idx}_{col_idx}"):
            st.session_state["status"][row_idx][col_idx] = (status + 1) % 3
        # 원 출력
        st.markdown(
            f'<div class="cell"><div class="circle" style="background-color: {color};"></div></div>',
            unsafe_allow_html=True,
        )

st.markdown('</div>', unsafe_allow_html=True)
