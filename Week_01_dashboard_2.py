import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NBA 視覺化儀表板", layout="wide")

st.title("🏀 NBA 運動視覺化成果展示")
st.subheader("導論 x 互動儀表板 x 學習動機引發")

# =========================
# 建立 NBA 球員資料
# =========================
player_df = pd.DataFrame({
    "Season": [2019, 2020, 2021, 2022, 2023],
    "Player": ["Stephen Curry"] * 5,
    "PTS": [27, 32, 25, 29, 30],
    "AST": [6, 5, 6, 6, 5],
    "REB": [5, 5, 6, 6, 5],
    "PER": [24, 26, 22, 25, 27],
    "WS": [8, 9, 7, 10, 11]
})

# =========================
# 建立 NBA 球隊資料
# =========================
team_df = pd.DataFrame({
    "Season": [2019, 2020, 2021, 2022, 2023],
    "Team": ["Golden State Warriors"] * 5,
    "WinRate": [0.42, 0.60, 0.53, 0.63, 0.58],
    "PTS": [106, 113, 111, 115, 114],
    "OPP_PTS": [110, 109, 108, 107, 109],
    "AST": [25, 27, 26, 28, 27],
    "REB": [44, 45, 46, 47, 46]
})

# =========================
# 選擇儀表板
# =========================
dashboard = st.sidebar.radio("選擇展示內容", ["球員儀表板", "球隊儀表板"])

# =========================
# 球員儀表板
# =========================
if dashboard == "球員儀表板":
    st.header("🧍‍♂️ NBA 球員互動儀表板")

    col1, col2 = st.columns(2)

    with col1:
        fig_line = px.line(
            player_df,
            x="Season",
            y="PTS",
            title="年度得分趨勢",
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        fig_bar = px.bar(
            player_df,
            x="Season",
            y=["AST", "REB"],
            title="年度助攻與籃板",
            barmode="group"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        fig_scatter = px.scatter(
            player_df,
            x="AST",
            y="PTS",
            size="REB",
            title="得分 x 助攻 x 籃板"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col4:
        radar_fig = go.Figure()
        radar_fig.add_trace(go.Scatterpolar(
            r=[30, 6, 5, 27, 11],
            theta=["PTS", "AST", "REB", "PER", "WS"],
            fill="toself"
        ))
        radar_fig.update_layout(
            title="球員能力雷達圖",
            polar=dict(radialaxis=dict(visible=True))
        )
        st.plotly_chart(radar_fig, use_container_width=True)

# =========================
# 球隊儀表板
# =========================
if dashboard == "球隊儀表板":
    st.header("🏀 NBA 球隊年度分析儀表板")

    col1, col2 = st.columns(2)

    with col1:
        fig_line_team = px.line(
            team_df,
            x="Season",
            y="WinRate",
            title="球隊勝率年度變化",
            markers=True
        )
        st.plotly_chart(fig_line_team, use_container_width=True)

    with col2:
        fig_bar_team = px.bar(
            team_df,
            x="Season",
            y="PTS",
            title="球隊平均得分"
        )
        st.plotly_chart(fig_bar_team, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        fig_scatter_team = px.scatter(
            team_df,
            x="PTS",
            y="OPP_PTS",
            title="得分 x 失分關係",
            size="WinRate"
        )
        st.plotly_chart(fig_scatter_team, use_container_width=True)

    with col4:
        radar_team = go.Figure()
        radar_team.add_trace(go.Scatterpolar(
            r=[114, 27, 46, 0.58],
            theta=["PTS", "AST", "REB", "WinRate"],
            fill="toself"
        ))
        radar_team.update_layout(
            title="球隊整體能力雷達圖",
            polar=dict(radialaxis=dict(visible=True))
        )
        st.plotly_chart(radar_team, use_container_width=True)
