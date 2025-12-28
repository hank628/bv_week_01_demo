# streamlit_plotly_dashboard_sidebar.py
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 1. 標題與說明
# -----------------------------
st.title("運動數據互動儀表板範例（側邊選單版）")
st.write("使用 Streamlit + Plotly Express 的範例儀表板。可從左側選擇指標，動態呈現圖表。")

# -----------------------------
# 2. 模擬數據
# -----------------------------
data = {
    "球員": ["LeBron", "Curry", "Durant", "Harden", "Giannis"],
    "得分": [27, 30, 29, 25, 28],
    "助攻": [8, 6, 5, 7, 6],
    "籃板": [7, 5, 6, 5, 11],
    "三分球命中率": [0.36, 0.42, 0.38, 0.34, 0.30]
}
df = pd.DataFrame(data)

# -----------------------------
# 3. 側邊欄選單
# -----------------------------
st.sidebar.header("選擇顯示設定")
metric = st.sidebar.selectbox("選擇指標", ["得分", "助攻", "籃板", "三分球命中率"])
show_line = st.sidebar.checkbox("折線圖", value=True)
show_bar = st.sidebar.checkbox("長條圖", value=True)
show_pie = st.sidebar.checkbox("圓餅圖", value=False)
show_radar = st.sidebar.checkbox("雷達圖", value=False)

# -----------------------------
# 4. 折線圖
# -----------------------------
if show_line:
    st.subheader(f"{metric} 折線圖")
    fig_line = px.line(df, x="球員", y=metric, markers=True, title=f"{metric} 折線圖")
    st.plotly_chart(fig_line)

# -----------------------------
# 5. 長條圖
# -----------------------------
if show_bar:
    st.subheader(f"{metric} 長條圖")
    fig_bar = px.bar(df, x="球員", y=metric, color="球員", title=f"{metric} 長條圖")
    st.plotly_chart(fig_bar)

# -----------------------------
# 6. 圓餅圖
# -----------------------------
if show_pie:
    st.subheader(f"{metric} 圓餅圖")
    fig_pie = px.pie(df, names="球員", values=metric, title=f"{metric} 圓餅圖")
    st.plotly_chart(fig_pie)

# -----------------------------
# 7. 雷達圖
# -----------------------------
if show_radar:
    st.subheader(f"{metric} 雷達圖")
    fig_radar = px.line_polar(df, r=metric, theta="球員", line_close=True,
                              title=f"{metric} 雷達圖", markers=True)
    st.plotly_chart(fig_radar)

# -----------------------------
# 8. 函式說明
# -----------------------------
st.markdown("""
### 函式說明
- `st.sidebar.selectbox()` : 側邊欄下拉選單，讓使用者選擇指標。
- `st.sidebar.checkbox()` : 側邊欄勾選框，控制圖表是否顯示。
- `px.line()` : 繪製折線圖。
- `px.bar()` : 繪製長條圖。
- `px.pie()` : 繪製圓餅圖。
- `px.line_polar()` : 繪製雷達圖（極區圖）。
- `st.plotly_chart()` : 將 Plotly 圖表嵌入 Streamlit。
""")
