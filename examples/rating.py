import pandas as pd

RANK_MAP = {
    1: 30,
    2: 25,
    3: 20,
    4: 15,
    5: 10,
    6: 5,
    7: 5,
    8: 5,
    9: 5,
    10: 5
}

def apply_rating_by_rank(df, rank_col, rating_col="rating"):
    df[rating_col] = df[rank_col].map(RANK_MAP)
    df[rating_col] = df[rating_col].fillna(0)
    return df

usage = pd.read_csv(r"data\character_usage.csv")
names = pd.read_csv(r"data\character_name.csv")
usage_names = usage.merge(right=names, how="left", left_on="character_id", right_on="id")

with_points = apply_rating_by_rank(usage_names, "rank")
idx = with_points["version_id"] == 0
with_points = with_points[~idx]
rating_points_total = with_points.groupby("name")["rating"].sum().sort_values(ascending=False)
rating_points_avg = with_points.groupby("name")["rating"].mean().sort_values(ascending=False)

print(rating_points_total.head(25))
print(rating_points_avg.head(25))


def running_total_rating(df, rating_col="rating"):
    """
    Running total by character name
    """
    df["running_total"] = df.groupby("name")[rating_col].cumsum()
    return df

with_points = running_total_rating(with_points)


import plotly.express as px
fig = px.line(with_points, x="version_id", y="running_total", color="name")
fig.write_html("local_plot/rating.html")

print(usage_names[["name", "rating"]])