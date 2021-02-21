# Case: 2 

## Links:
Please look over the exploratory analysis Jupyter Notebook with this link hosted via NBViewer: 
https://nbviewer.jupyter.org/github/ramsun/stout-case2/blob/master/exploratory_analysis.ipynb

This app is being hosted for free via Heroku.  Bear in mind that since this app is being hosted for free, it can take up to 10 seconds for the Summary Data table to update with new values when selecting a different year from the drop down menu on the left side of the webpage.  Just be a little patient and the table will fill up with the relavant values for the year.  You can find the link below:  
https://stout-case2.herokuapp.com/

## Website screenshots
I have added two screenshots below to show off the web page.  __Image 1__ shows the landing page when you click on the link (by default, the table populated with data from 2015).  __Image 2__ shows data for 2016 and the drop down menu in action.
### Image 1  
![2015 Data](/readme_assets/2015_data.png "2015 Data")
### Image 2
![2016 Data](/readme_assets/2016_data_with_dropdown_menu.png "2016 Data And Dropdown")

## Purpose:
In this challenge, we are tasked with performing aggregate analysis and reporting our findings on a website.

## How?:
I used Plotly.js to create a table, which populates with aggregate analysis served from the Flask routes.  In the backend, Flask is performing complex calculations with the help of the analytics package Pandas.  The website was made pretty with CSS and Bootstrapping.  D3.js was used soley for its useful d3.json function to handle API calls.  You can run the website by compiling app.py in bash/zsh and copying and pasting the localhost url into your webbrowser of choice.  This website is being hosted on Heroku as well, so feel free to check out the link towards the top of this README.

## Data Sources:
Data was stored in a CSV.  It can be found in the resources folder in a file called casestudy.csv.

## Tools used:
Python
Jupyter Notebook  
Flask  
JavaScript  
Plotly  
D3.js  
HTML  
CSS  
API  
Bootstrap
Heroku  