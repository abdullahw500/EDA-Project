import streamlit as st


def apply_filters(df):

    content_types = st.sidebar.multiselect(
        "Content Type",
        options=df["type"].dropna().unique(),
        default=df["type"].dropna().unique()
    )

    countries = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .unique()
    )

    selected_country = st.sidebar.selectbox(
        "Country",
        ["All"] + sorted(list(countries))
    )

    min_year = int(df["release_year"].min())
    max_year = int(df["release_year"].max())

    year_range = st.sidebar.slider(
        "Release Year",
        min_year,
        max_year,
        (min_year, max_year)
    )

    filtered_df = df[
        (df["type"].isin(content_types))
        &
        (
            (df["release_year"] >= year_range[0])
            &
            (df["release_year"] <= year_range[1])
        )
    ]

    if selected_country != "All":
        filtered_df = filtered_df[
            filtered_df["country"]
            .fillna("")
            .str.contains(selected_country)
        ]

    return filtered_df