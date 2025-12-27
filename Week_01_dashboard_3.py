import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 1️⃣ 範例資料（可自行替換）
# -------------------------------
data = pd.DataFrame({
    '球員': ['LeBron', 'Curry', 'Durant', 'Giannis'],
    '球隊': ['LAL', 'GSW', 'BKN', 'MIL'],
    '得分': [25, 30, 28, 27],
    '助攻': [8, 6, 5, 7],
    '籃板': [7, 5, 6, 11],
    '效率': [28, 27, 26, 29]
})

# -------------------------------
# 2️⃣ App 標題
# -------------------------------
st.title("NBA 四圖互動 Dashboard (側邊欄控制)")

# -------------------------------
# 3️⃣ 使用者選擇（左側側邊欄）
# -------------------------------
metric_options = ['得分', '助攻', '籃板', '效率']

metric1 = st.sidebar.selectbox("折線圖指標", metric_options)
metric2 = st.sidebar.selectbox("長條圖指標", metric_options)
metric3 = st.sidebar.selectbox("圓餅圖依據", ['球隊', '球員'])
metric4 = st.sidebar.selectbox("雷達圖指標", metric_options)

# -------------------------------
# 4️⃣ 折線圖
# -------------------------------
st.subheader(f"折線圖: {metric1} 變化")
fig_line = px.line(data, x='球員', y=metric1, markers=True, title=f"{metric1} 折線圖")
st.plotly_chart(fig_line)

# -------------------------------
# 5️⃣ 長條圖
# -------------------------------
st.subheader(f"長條圖: {metric2} 分布")
fig_bar = px.bar(data, x='球員', y=metric2, color='球員', title=f"{metric2} 長條圖")
st.plotly_chart(fig_bar)

# -------------------------------
# 6️⃣ 圓餅圖
# -------------------------------
st.subheader(f"圓餅圖: {metric3} 比例")
fig_pie = px.pie(data, names=metric3, values='得分', title=f"{metric3} 圓餅圖")
st.plotly_chart(fig_pie)

# -------------------------------
# 7️⃣ 雷達圖
# -------------------------------
st.subheader(f"雷達圖: {metric4} 比較")
radar_data = data.melt(id_vars=['球員'], value_vars=[metric4], var_name='指標', value_name='值')
fig_radar = px.line_polar(radar_data, r='值', theta='球員', line_close=True, title=f"{metric4} 雷達圖", markers=True)
st.plotly_chart(fig_radar)
