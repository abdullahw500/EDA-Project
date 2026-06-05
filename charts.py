import plotly.express as px


def content_type_chart(df):
    data = df["type"].value_counts().reset_index()
    data.columns = ["Type", "Count"]

    fig = px.pie(
        data,
        names="Type",
        values="Count",
        title="Movies vs TV Shows"
    )
    return fig


def top_countries_chart(df):
    countries = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
        .reset_index()
    )

    countries.columns = ["Country", "Count"]

    fig = px.bar(
        countries,
        x="Country",
        y="Count",
        title="Top 10 Countries"
    )

    return fig


def release_year_chart(df):
    years = (
        df["release_year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    years.columns = ["Year", "Count"]

    fig = px.line(
        years,
        x="Year",
        y="Count",
        title="Content Released By Year"
    )

    return fig


def rating_chart(df):
    ratings = (
        df["rating"]
        .dropna()
        .value_counts()
        .reset_index()
    )

    ratings.columns = ["Rating", "Count"]

    fig = px.bar(
        ratings,
        x="Rating",
        y="Count",
        title="Content Ratings"
    )

    return fig