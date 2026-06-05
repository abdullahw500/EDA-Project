import streamlit as st
import pandas as pd

from charts import (
    content_type_chart,
    top_countries_chart,
    release_year_chart,
    rating_chart
)

from filters import apply_filters

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    return df

df = load_data()

st.sidebar.header("Filters")

filtered_df = apply_filters(df)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", len(filtered_df))

with col2:
    st.metric("Movies", len(filtered_df[filtered_df["type"] == "Movie"]))

with col3:
    st.metric("TV Shows", len(filtered_df[filtered_df["type"] == "TV Show"]))

st.divider()

# Charts
c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(
        content_type_chart(filtered_df),
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        rating_chart(filtered_df),
        use_container_width=True
    )

st.divider()

c3, c4 = st.columns(2)

with c3:
    st.plotly_chart(
        top_countries_chart(filtered_df),
        use_container_width=True
    )

with c4:
    st.plotly_chart(
        release_year_chart(filtered_df),
        use_container_width=True
    )

st.divider()

st.subheader("Dataset Preview")
st.dataframe(filtered_df)