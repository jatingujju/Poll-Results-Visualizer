import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Poll Results Visualizer", layout="wide")

st.title("📊 Poll Results Visualizer Dashboard")

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("poll_data.csv")

df = load_data()

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("🔍 Filters")

selected_tool = st.sidebar.multiselect(
    "Select Preferred Tool",
    options=df["Preferred Tool"].unique(),
    default=df["Preferred Tool"].unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Preferred Tool"].isin(selected_tool)) &
    (df["Gender"].isin(selected_gender))
]

# -------------------------
# Show Raw Data
# -------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# -------------------------
# KPI Section
# -------------------------
st.subheader("📌 Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered_df))
col2.metric("Avg Satisfaction", round(filtered_df["Satisfaction"].mean(), 2))
col3.metric("Top Tool", filtered_df["Preferred Tool"].mode()[0])

# -------------------------
# Bar Chart
# -------------------------
st.subheader("📊 Preferred Tool Distribution")

tool_counts = filtered_df["Preferred Tool"].value_counts()

fig1, ax1 = plt.subplots()
tool_counts.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# -------------------------
# Pie Chart
# -------------------------
st.subheader("🥧 Tool Share")

fig2, ax2 = plt.subplots()
tool_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# -------------------------
# Gender Analysis
# -------------------------
st.subheader("👨‍👩‍👧 Tool Preference by Gender")

fig3, ax3 = plt.subplots()
sns.countplot(x="Preferred Tool", hue="Gender", data=filtered_df, ax=ax3)
st.pyplot(fig3)

# -------------------------
# Satisfaction Histogram
# -------------------------
st.subheader("⭐ Satisfaction Distribution")

fig4, ax4 = plt.subplots()
sns.histplot(filtered_df["Satisfaction"], bins=5, kde=True, ax=ax4)
st.pyplot(fig4)

# -------------------------
# Word Cloud
# -------------------------
st.subheader("☁️ Feedback Word Cloud")

text = " ".join(filtered_df["Feedback"].astype(str))

if text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    fig5, ax5 = plt.subplots()
    ax5.imshow(wordcloud, interpolation='bilinear')
    ax5.axis("off")
    st.pyplot(fig5)
else:
    st.write("No feedback available")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("Built by Jatin Gujarathi 🚀")