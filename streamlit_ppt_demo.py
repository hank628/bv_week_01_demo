# 配合Streamlit教學PPT的範例內容

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ===============================
# 頁面設定
# ===============================
st.set_page_config(
    page_title="NBA Player Dashboard",
    layout="wide"
)

st.title("🏀 NBA Player Dashboard")
st.header("這是配合Streamlit Sliders的說明")
st.subheader("Teaching Demo: Streamlit x Plotly")
st.markdown(
    """
    本範例示範內容：
    - 虛擬產生一筆 NBA 數據資料
    - 使用 Sidebar 控制分析條件
    - 呈現表格與互動式圖表
    """
)

# ===============================
# 產生教學用假資料
# ===============================
np.random.seed(42)

players = ["LeBron James", "Stephen Curry", "Kevin Durant"]
teams = ["Lakers", "Warriors", "Suns"]
seasons = list(range(2018, 2025))

data = []

for season in seasons:
    for player, team in zip(players, teams):
        data.append({
            "Season": season,
            "Player": player,
            "Team": team,
            "Points": np.random.randint(20, 35),
            "Rebounds": np.random.randint(4, 12),
            "Assists": np.random.randint(4, 10)
        })

df = pd.DataFrame(data)

# ===============================
# Sidebar（控制區）
# ===============================
st.sidebar.title("🔧 篩選條件")

selected_team = st.sidebar.selectbox(
    "選擇球隊",
    df["Team"].unique()
)

selected_season = st.sidebar.slider(
    "選擇年度",
    min_value=int(df["Season"].min()),
    max_value=int(df["Season"].max()),
    value=2022
)

# ===============================
# 資料篩選
# ===============================
df_filtered = df[
    (df["Team"] == selected_team) &
    (df["Season"] <= selected_season)
]

# ===============================
# 資料表呈現
# ===============================
st.header("📋 資料表")
st.dataframe(df_filtered, use_container_width=True)

# ===============================
# KPI 指標
# ===============================
st.header("📊 主要指標")

col1, col2, col3 = st.columns(3)

col1.metric(
    "平均得分",
    round(df_filtered["Points"].mean(), 1)
)

col2.metric(
    "平均籃板",
    round(df_filtered["Rebounds"].mean(), 1)
)

col3.metric(
    "平均助攻",
    round(df_filtered["Assists"].mean(), 1)
)

# ===============================
# 折線圖（生涯趨勢）
# ===============================
st.header("📈 球員生涯趨勢（得分）")

fig_line = px.line(
    df_filtered,
    x="Season",
    y="Points",
    color="Player",
    markers=True
)

st.plotly_chart(fig_line, use_container_width=True)

# ===============================
# 長條圖（同年度比較）
# ===============================
st.header("📊 球員表現比較（最新年度）")

df_latest = df_filtered[df_filtered["Season"] == selected_season]

fig_bar = px.bar(
    df_latest,
    x="Player",
    y="Points",
    text="Points"
)

st.plotly_chart(fig_bar, use_container_width=True)

# ===============================
# 教學說明（可收合）
# ===============================
with st.expander("📘 教學說明"):
    st.markdown(
        """
        - **Plotly**：負責畫圖  
        - **Streamlit**：負責互動與版面  
        - Sidebar 是 Dashboard 的控制核心  
        - App 每次互動都會重新執行一次程式
        """
    )
