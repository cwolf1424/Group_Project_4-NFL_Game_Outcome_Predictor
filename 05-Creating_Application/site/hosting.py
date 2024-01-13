#########################
# Import the dependencies
#########################
import pandas as pd
import json
from flask import Flask, render_template, request

#########################
# Helper functions
#########################

def getReferenceDataFrameAsJSON(ref, subcat=''):
    ref_df = pd.read_csv(f'../Reference_Data/{ref}_Data.csv')
    ref_df = ref_df.rename(columns={"Unnamed: 0": f"{ref}_ID"})
    if (subcat != ''):
        ref_df = ref_df.rename(columns={f"{ref}": f"{subcat}{ref}"})
    json_data = ref_df.to_json(orient='records')
    return json.loads(json_data)

#########################
# Setup the Flask app
#########################
hosting = Flask(__name__)

#########################
# Base route
#########################
@hosting.route("/")
def home():
    return render_template('wizard.html');

#########################
# Dropdown data source routes
#########################
@hosting.route("/api/v1.0/cities")
def getCities():
    return getReferenceDataFrameAsJSON('Cities')

@hosting.route("/api/v1.0/months")
def getMonths():
    return getReferenceDataFrameAsJSON('Months')

@hosting.route("/api/v1.0/states")
def getStates():
    return getReferenceDataFrameAsJSON('States')

@hosting.route("/api/v1.0/times")
def getTimes():
    return getReferenceDataFrameAsJSON('Times')

@hosting.route("/api/v1.0/venues")
def getVenues():
    return getReferenceDataFrameAsJSON('Venues')

@hosting.route("/api/v1.0/weather")
def getWeather():
    return getReferenceDataFrameAsJSON('Weather')

@hosting.route("/api/v1.0/hometeams")
def getHomeTeams():
    return getReferenceDataFrameAsJSON('Teams', 'Home')

@hosting.route("/api/v1.0/awayteams")
def getAwayTeams():
    return getReferenceDataFrameAsJSON('Teams', 'Away')

#########################
# Route used to 
#########################
@hosting.route("/api/v1.0/make_prediction", methods=['POST'])
def makePredition():
    form = json.loads(request.form['data'])

    # get the results
    #   1 = home team
    #   2 = away team
    #   3 = tie

    outcome = "1"

    winning_team = "nfl_logo"

    if outcome == "1":
        winning_team = form['home_team']
    elif outcome == "2":
        winning_team = form['away_team']
    elif outcome == "3":
        winning_team = "tie"     

    matchup_results = {
        "winning_team": winning_team
    }

    return json.dumps(matchup_results)

if __name__ == '__main__':
    hosting.run(port=8000, debug=True)