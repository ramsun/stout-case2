# Flask App

# Import dependencies
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import json
import analyze
import os
import pandas as pd


# Store the raw data csv file into a dataframe
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'resources/casestudy.csv')
df_full = pd.read_csv(filename)


# Initialize flask app
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# Home Route
@app.route("/")
def index():
    return render_template("index.html")

# Returns the years a list for the drop down menu
@app.route("/years")
def years():
    years = analyze.years_in_data(df_full)
    # Return a list of years (years in dataset)
    return jsonify(years)

# Performs summary analytics for the queried year selected from the drop down menu
@app.route("/data/<year>")
def stream_data(year):
    data = {}
    year = int(year)
    data['Total Revenue For Current Year'] = analyze.total_revenue(df_full,year)
    data['New Customer Revenue'] = analyze.new_customer_revenue(df_full,year)
    data['Existing Customer Growth'] = analyze.existing_customer_growth(df_full,year)
    data['Revenue Lost From Attrition'] = analyze.revenue_lost_from_attrition(df_full,year)
    data['Existing Customer Revenue Current Year'] = analyze.existing_customer_revenue_current_year(df_full,year)
    data['Existing Customer Revenue Prior Year'] = analyze.existing_customer_revenue_prior_year(df_full,year)
    data['Total Customers Current Year'] = analyze.total_customers_by_year(df_full,year)
    data['Total Customers Previous Year'] = analyze.total_customers_by_year(df_full,year-1)
    data['New Customers'] = analyze.new_customers(df_full,year)
    data['Lost Customers'] = analyze.lost_customers(df_full,year)
    # Return the "data" object as a json
    return jsonify(data)
    

# Main
if __name__ == "__main__":
    app.run(debug = True) 


