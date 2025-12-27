# 「這門課我們來用資料說故事！」
# 「第一週，我們先看做得出來的東西，後面再慢慢拆解怎麼做。」

import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------
# 建立一筆 NBA 示範資料
# ---------------------------
data = {
    "Player": [
        "LeBron James", "Stephen Curry", "Kevin Durant",
        "Giannis Antetokounmpo", "Nikola Jokic"
    ],
    "Team": [
        "Lakers", "Warriors", "Suns",
        "Bucks", "Nuggets"
    ],
    "Season": ["2023-24"] * 5,
    "Points": [25.7, 27.3, 28.1, 30.4, 26.4],
    "Assists": [7.3, 5.1, 5.6, 6.5, 9.0],
    "Rebounds": [7.5, 4.3, 6.7, 11.5, 12.4]
}

df = pd.DataFrame(data)

# ---------------------------
# Streamlit 版面設定
# ---------------------------
st.set_page_config(page_title="NBA Player Dashboard", layout="wide")

st.title("🏀 NBA 球員互動儀表板（示範）")
st.markdown("### 導論與運動視覺化成果展示")

# ---------------------------
# 側邊欄：球員選擇
# ---------------------------
selected_player = st.sidebar.selectbox( # 選單__選擇球員
    "選擇球員",
    df["Player"].unique()
)

filtered_df = df[df["Player"] == selected_player]

# ---------------------------
# KPI 指標區
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("平均得分 (PTS)", f"{filtered_df['Points'].values[0]}")
col2.metric("平均助攻 (AST)", f"{filtered_df['Assists'].values[0]}")
col3.metric("平均籃板 (REB)", f"{filtered_df['Rebounds'].values[0]}")

# ---------------------------
# 長條圖：球員數據比較
# ---------------------------
long_df = filtered_df.melt(
    id_vars=["Player"],
    value_vars=["Points", "Assists", "Rebounds"],
    var_name="Statistic",
    value_name="Value"
)

fig_bar = px.bar(
    long_df,
    x="Statistic",
    y="Value",
    text="Value",
    title=f"{selected_player}｜球員表現概覽"
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------
# 散點圖：NBA 球員整體比較
# ---------------------------
fig_scatter = px.scatter(
    df,
    x="Points",
    y="Assists",
    size="Rebounds",
    color="Team",
    hover_name="Player",
    title="NBA 球員得分 x  助攻 x 籃板（互動示意）"
)

st.plotly_chart(fig_scatter, use_container_width=True)
