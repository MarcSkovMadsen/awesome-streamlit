"""
App: NBA Roster Turnover
Author: [Kevin Arvai](https://github.com/arvkevi))\n
Source: [Github Original](https://github.com/arvkevi/nba-roster-turnover)
Credits: Marc Skov Madsen (for refactoring and improving)

Explore NBA roster turnover from year to year and the correlation it has with team wins.

*Roster turnover* is defined as the sum of the absolute difference between minutes played by each
player from year to year There is a significant negative correlation with higher turnover and
regular season wins.

This was built with Streamlit and originally deployed to heroku.

Ideas for improvements:

- Added summary section on total correlation across all years
- Add something about statistical significance
- Add best fit, linear regression to plot
- Add coloring to the two tables identicating high/ low values
- Get dataframe to be wider
- remove team= from plot
- Maybe show source dataframes somewhere to easier understand what is possible with the data
- Create an animation automatically incrementing the year every 4 seconds or so.
"""

from io import BytesIO

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from PIL import Image
from sportsreference.nba.teams import Teams

PLAYER_MINUTES_SOURCE = "s3://nba-roster-turnover/NBA_player_minutes.2004-2019.csv"
ROSTER_TURNOVER_SOURCE = "s3://nba-roster-turnover/NBA_roster_turnover_wins.2004-2019.csv"
TEAMS_DATA_SOURCE = "https://raw.githubusercontent.com/jimniels/teamcolors/master/src/teams.json"
PLAYER_MINUTES = "data/NBA_player_minutes.2004-2019.csv"
ROSTER_TURNOVER = "data/NBA_roster_turnover_wins.2004-2019.csv"
IMAGE = "images/basketball.jpg"

GITHUB_ROOT = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/"
    "gallery/nba_roster_turnover/"
)
PLAYER_MINUTES_GITHUB = GITHUB_ROOT + PLAYER_MINUTES
ROSTER_TURNOVER_GITHUB = GITHUB_ROOT + ROSTER_TURNOVER
TEAMS_DATA_GITHUB = "https://raw.githubusercontent.com/jimniels/teamcolors/master/src/teams.json"
IMAGE_GITHUB = GITHUB_ROOT + "images/basketball.jpg"


def main():
    st.title("NBA Roster Turnover vs Wins")
    st.header("Summary")
    st.info(
        """
**Roster turnover** is defined as the sum of the absolute difference between minutes played by each
player from year to year. There is a **significant negative correlation** with higher turnover and
regular season wins."""
    )
    st.markdown(
        f"""
    Source Data: [Player Minutes]({PLAYER_MINUTES_GITHUB}), [Roster Turnover]({ROSTER_TURNOVER_GITHUB}),
    [Teams Data]({TEAMS_DATA_GITHUB})
        """
    )

    # Loading data
    with st.spinner("Loading data ..."):
        image = get_image()
        player_minutes = load_player_minutes().copy(deep=True)
        roster_turnover = load_roster_turnover().copy(deep=True)
        team_colors = load_teams_colors()
        wins_turnover_corr = load_wins_turnover_corr(roster_turnover)

    st.header("Correlation by year")
    year = st.slider("Select a Year", 2004, 2019)
    teams = get_teams(year)
    teams_colorscale = get_teams_colorscale(teams, team_colors)

    st.write(f"Correlation Coefficient: {wins_turnover_corr[year]}")
    st.sidebar.image(image, use_column_width=True)
    st.sidebar.markdown(
        "Explore NBA roster turnover since\nthe 2003-04 season. **Roster turnover** is \ndefined as the "
        "sum of the difference\nin total minutes played by each player\non a given team between any two "
        "years."
    )
    st.sidebar.table(
        pd.DataFrame.from_dict(wins_turnover_corr, orient="index", columns=["correlation"]).round(2)
    )

    # Data frame for the plot
    fig = get_turnover_vs_wins_plot(roster_turnover, year, teams_colorscale)
    st.plotly_chart(fig)

    # Show the roster DataFrame
    st.header("Minutes Played Breakdown by Team")
    selected_team = st.selectbox("Select a team", teams)
    st.dataframe(roster_turnover_pivot(player_minutes, team=selected_team, year=year), width=1080)
    st.text("* The numbers in the table are minutes played")


@st.cache
def load_player_minutes():
    return pd.read_csv(PLAYER_MINUTES_GITHUB)


@st.cache
def load_roster_turnover():
    roster_turnover = pd.read_csv(ROSTER_TURNOVER_GITHUB)
    roster_turnover.set_index("team", inplace=True)
    return roster_turnover


@st.cache
def load_teams_colors():
    raw_team_colors = pd.read_json(TEAMS_DATA_GITHUB)
    # scrape a team's primary colors for the graphs below.
    team_colors = {}

    # all team colors
    for team in Teams(year=2019):
        team_rgb_strings = (
            raw_team_colors.loc[raw_team_colors["name"] == team.name]["colors"]
            .item()["rgb"][0]
            .split(" ")
        )
        team_colors[team.name.upper()] = tuple(int(c) for c in team_rgb_strings)

    # add old teams, the SuperSonics, and New Jersey Nets
    team_colors["SEATTLE SUPERSONICS"] = tuple((0, 101, 58))
    team_colors["NEW JERSEY NETS"] = tuple((0, 42, 96))
    team_colors["NEW ORLEANS HORNETS"] = tuple((0, 119, 139))
    team_colors["NEW ORLEANS/OKLAHOMA CITY HORNETS"] = tuple((0, 119, 139))
    team_colors["CHARLOTTE BOBCATS"] = tuple((249, 66, 58))  # <--guess
    return team_colors


@st.cache
def load_wins_turnover_corr(roster_turnover):
    wins_turnover_corr = {}
    years = range(2004, 2020)
    for year_ in years:
        # calculate the correlation between wins and roster turnover
        wins_turnover_corr[year_] = (
            roster_turnover.loc[roster_turnover["year"] == year_]
            .corr()["wins"]["turnover"]
            .round(2)
        )
    return wins_turnover_corr


@st.cache
def get_image():
    response = requests.get(IMAGE_GITHUB)
    return Image.open(BytesIO(response.content))


@st.cache
def get_teams(year):
    teams = Teams(year=year)
    return sorted([team.name.upper() for team in teams])


@st.cache
def get_teams_colorscale(teams, team_colors):
    return [f"rgb{team_colors[team]}" for team in teams]


@st.cache
def roster_turnover_pivot(player_minutes, team="ATLANTA HAWKS", year=2004):
    pm_subset = player_minutes.loc[
        ((player_minutes["year"] == year) | (player_minutes["year"] == year - 1))
        & (player_minutes["team"] == team)
    ]
    result = (
        pd.pivot_table(pm_subset, values="minutes_played", index=["team", "name"], columns=["year"])
        .fillna(0)
        .reset_index()
        .drop(columns=["team"])
        .set_index("name")
    )
    result["Change"] = result[year] - result[year - 1]
    return result


@st.cache
def get_turnover_vs_wins_plot(roster_turnover, year, teams_colorscale):
    scatter_data = roster_turnover.dropna().reset_index()
    scatter_data = scatter_data.astype(
        dtype={"turnover": "int32", "wins": "int32", "year": "int32"}
    )
    scatter_data = scatter_data.loc[scatter_data.reset_index()["year"] == year]
    return px.scatter(
        scatter_data,
        x="turnover",
        y="wins",
        labels={
            "turnover": "Roster Turnover (Difference in minutes played by player -- see below)",
            "wins": "Regular Season Wins",
        },
        color="team",
        color_discrete_sequence=teams_colorscale,
        height=600,
    )


main()
