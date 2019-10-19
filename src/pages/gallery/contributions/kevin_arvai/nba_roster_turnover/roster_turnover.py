"""Explore NBA roster turnover from year to year and the correlation it has with team wins.
Roster turnover is defined as the sum of the total difference between minutes played by each player from year to year.
There is a significant negative correlation with higher turnover and regular season wins.

This was built with streamlit and deployed with heroku.
"""

import os
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
from sportsreference.nba.teams import Teams

st.markdown(
    """
    ## nba-roster-turnover

    Explore NBA roster turnover from year to year and the correlation it has with team wins. 
    Roster turnover is defined as the sum of the total difference between minutes played by each player 
    from year to year. There is a significant negative correlation with higher turnover and regular season wins.

    Author: [YKevin Arvai](https://github.com/arvkevi))\n
    Source: [Github](https://github.com/arvkevi/nba-roster-turnover)
    """
)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# load the data
player_minutes = pd.read_csv(os.path.join(ROOT_DIR, 'data/NBA_player_minutes.2004-2019.csv'))
roster_turnover = pd.read_csv(os.path.join(ROOT_DIR, 'data/NBA_roster_turnover_wins.2004-2019.csv'))

#
# player_minutes = pd.read_csv('s3://nba-roster-turnover/NBA_player_minutes.2004-2019.csv')
# roster_turnover = pd.read_csv('s3://nba-roster-turnover/NBA_roster_turnover_wins.2004-2019.csv')
roster_turnover.set_index('team', inplace=True)

wins_turnover_corr = {}
years = range(2004, 2020)
for year_ in years:
    # calculate the correlation between wins and roster turnover
    wins_turnover_corr[year_] = roster_turnover.loc[roster_turnover['year'] == year_].corr()['wins']['turnover'].round(2)

# scrape a team's primary colors for the graphs below.
raw_team_colors = pd.read_json('https://raw.githubusercontent.com/jimniels/teamcolors/master/src/teams.json')
team_colors = {}

# all team colors
for team in Teams(year=2019):
    team_rgb_strings = raw_team_colors.loc[raw_team_colors['name'] == team.name]['colors'].item()['rgb'][0].split(' ')
    team_colors[team.name.upper()] = tuple(int(c) for c in team_rgb_strings)

# add old teams, the SuperSonics, and New Jersey Nets
team_colors['SEATTLE SUPERSONICS'] = tuple((0, 101, 58))
team_colors['NEW JERSEY NETS'] = tuple((0, 42, 96))
team_colors['NEW ORLEANS HORNETS'] = tuple((0, 119, 139))
team_colors['NEW ORLEANS/OKLAHOMA CITY HORNETS'] = tuple((0, 119, 139))
team_colors['CHARLOTTE BOBCATS'] = tuple((249, 66, 58)) # <--guess

st.title('NBA Roster Turnover')

# team colors for the currently selected year
year = st.slider('Select a Year', 2004, 2019)
teams = Teams(year=year)
teams = sorted([team.name.upper() for team in teams])
teams_colorscale = [f'rgb{team_colors[team]}' for team in teams]

st.write(f'Correlation Coefficient: {wins_turnover_corr[year]}')

image = Image.open(os.path.join(ROOT_DIR, 'images/basketball.jpg'))
st.sidebar.image(image, use_column_width=True)
st.sidebar.text('Explore NBA roster turnover since\nthe 2003-04 season. Roster turnover is \ndefined as the '
                'sum of the difference\nin total minutes played by each player\non a given team between any two '
                'years.')
st.sidebar.dataframe(pd.DataFrame.from_dict(wins_turnover_corr, orient='index', columns=['correlation']))

# Data frame for the plot
scatter_data = roster_turnover.dropna().reset_index()
scatter_data = scatter_data.astype(dtype={'turnover': 'int32', 'wins': 'int32', 'year': 'int32'})

# Main figure
fig = px.scatter(scatter_data.loc[scatter_data.reset_index()['year'] == year],
                 x='turnover',
                 y='wins',
                 labels={'turnover': 'Roster Turnover (Difference in minutes played by player -- see below)',
                         'wins': 'Regular Season Wins'},
                 color='team',
                 color_discrete_sequence=teams_colorscale)
st.plotly_chart(fig, width=1080, height=600)

# Show the roster DataFrame
@st.cache
def roster_turnover_pivot(player_minutes, team='ATLANTA HAWKS', year=2004):
    pm_subset = player_minutes.loc[((player_minutes['year'] == year)
                                     | (player_minutes['year'] == year - 1))
                                    & (player_minutes['team'] == team)]
    return pd.pivot_table(pm_subset,
                          values='minutes_played',
                          index=['team', 'name'],
                          columns=['year']
                          )\
        .fillna(0)\
        .reset_index()\
        .drop(columns=['team'])\
        .set_index('name')


st.header('Team Roster: Minutes Played Breakdown')
selected_team = st.selectbox('Choose a team to view roster', teams)
st.write(roster_turnover_pivot(player_minutes, team=selected_team, year=year))
