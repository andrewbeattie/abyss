import pandas as pd
import seaborn as sb

def filter_by_names(df, names):
    """
    Filter a dataframe by character names
    """
    return df[df["name"].isin(names)]

def display_usage_over_versions(df):
    """
    Create a time series line plot
    Columns are: 
        character_name which will be the label
        rate which will be the y-axis
        version_id which will be the x-axis
    """
    sb.lineplot(data=df, x="version_id", y="rate", hue="name")

def exclude_by_version(df, version):
    """
    Filter a dataframe by version exluding
    """
    return df[df["version_id"] != version]

usage = pd.read_csv(r"data\character_usage.csv")
names = pd.read_csv(r"data\character_name.csv")
usage_names = usage.merge(right=names, how="left", left_on="character_id", right_on="id")

def pprint_df(df):
    print(df[["name", "rate"]])

idx = usage_names["version_id"] == 0
pprint_df( usage_names[idx].head(5))

top_25 = usage_names[idx].sort_values(by="rate", ascending=False).head(25)
names = top_25["name"].tolist()
usage_names_top = filter_by_names(usage_names, names)

DPS = [
    "Neuvillette",
    "Raiden Shogun",
    "Alhaitham",
    "Hu Tao",
    "Kamisato Ayaka",
    "Nilou",
    "Navia",
    "Tartaglia",
    "Ganyu",
    "Kamisato Ayato"
]
BUFF = [
    "Kaedehara Kazuha",
    "Furina",
    "Bennett",
    "Zhongli",
    "Yelan",
    "Xianyun",
    "Shenhe",
    "Venti"
]
OFFFIELD = [
    "Nahida",
    "Furina",
    "Yelan",
    "Xingqiu",
    "Raiden Shogun",
    "Sangonomiya Kokomi",
    "Baizhu",
    "Xiangling",
    "Kuki Shinobu"
]

top_dps = filter_by_names(usage_names, DPS)
top_off = filter_by_names(usage_names, OFFFIELD)
top_buff = filter_by_names(usage_names, BUFF)

def plot_interactive(df):
    """
    Time series line plot using plotly 
    Columns are: 
        character_name which will be the label
        rate which will be the y-axis
        version_id which will be the x-axis
        rank is meta data
    """
    import plotly.express as px
    fig = px.line(df, x="version_id", y="rate", color="name", title="Character Usage Over Time")
    return fig
   

dps_fig = plot_interactive(exclude_by_version(top_dps, 0))
dps_fig.write_html("local_plot/dps.html")
off_fig = plot_interactive(exclude_by_version(top_off, 0))
off_fig.write_html("local_plot/off.html")
buff_fig = plot_interactive(exclude_by_version(top_buff, 0))
buff_fig.write_html("local_plot/buff.html")
