import streamlit as st

# 데이터 상태 정의
rows = ["WSKHZN1", "WSKHZN2", "WSKHZN3", "WILHZT1", "WILHZT2", "WILHZT3", "WILHZT4"]
columns = ["CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7", "CH8"]

# 초기 상태 (ON=Green, OFF=Red, Yellow=Pending)
if "status" not in st.session_state:
    st.session_state["status"] = [[0 for _ in columns] for _ in rows]  # 0: Green, 1: Red, 2: Yellow

# 색상 매핑
color_map = {0: "#4CAF50", 1: "#FF0000", 2: "#FFD700"}  # Green, Red, Yellow

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .circle {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        display: inline-block;
        margin: auto;
    }
    .table-container {
        display: grid;
        grid-template-columns: repeat(9, 100px); /* 8 CHs + 1 Row Label */
        gap: 5px;
    }
    .header, .cell {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 30px;
        font-size: 14px;
        border: 1px solid #ddd;
        background-color: #f9f9f9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 표 출력
st.markdown('<div class="table-container">', unsafe_allow_html=True)

# 헤더 출력
st.markdown('<div class="header"></div>', unsafe_allow_html=True)  # 빈 셀
for col in columns:
    st.markdown(f'<div class="header">{col}</div>', unsafe_allow_html=True)

# 데이터 행 출력
for row_idx, row in enumerate(rows):
    st.markdown(f'<div class="cell">{row}</div>', unsafe_allow_html=True)  # 행 이름
    for col_idx in range(len(columns)):
        color = color_map[st.session_state["status"][row_idx][col_idx]]
        if st.button("", key=f"btn_{row_idx}_{col_idx}"):
            st.session_state["status"][row_idx][col_idx] = (st.session_state["status"][row_idx][col_idx] + 1) % 3
        st.markdown(f'<div class="cell"><div class="circle" style="background-color: {color};"></div></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
