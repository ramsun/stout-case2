# This script contains the helper functions that perform the analytics 

import pandas as pd

# Return a dataframe from the year's data
def data_for_year(df,year):
  new_df = df.loc[df['year'] == year]
  return new_df

# Get sorted list of unique years in full dataset
# Smallest year is in position zero
def years_in_data(df):
  years = sorted(set(df['year']))
  return years 

# Input parameters: current years data (dataframe), previous year's data 
# (dataframe), type of join (string of inner, outer, left, or right), 
def merged_data(df_current, df_prior, how, joined_type):
  df_merged = pd.merge(df_current,df_prior, how = how, on = ['customer_email']
                       ,indicator=True)
  df = df_merged.loc[df_merged['_merge'] == joined_type]
  return df

# Returns the total revenue for the given year
def total_revenue(df, year):
  sub_df = data_for_year(df, year)
  total_revenue = round(sum(sub_df['net_revenue']),2)
  return total_revenue

# Returns revunue made from new customers.  Only compares with the previous year
def new_customer_revenue(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_unique = merged_data(df_year_current, df_year_prior, 'left', 'left_only')
    return round(sum(df_unique['net_revenue_x']),2)

# Returns revenue of existing customers from current year
def existing_customer_revenue_current_year(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_common = merged_data(df_year_current, df_year_prior, 'inner', 'both')
    return round(sum(df_common['net_revenue_x']),2)

# Returns revenue of existing customers from prior year
def existing_customer_revenue_prior_year(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_common = merged_data(df_year_current, df_year_prior, 'inner', 'both')
    return round(sum(df_common['net_revenue_y']),2)

# Revenue of existing customers for current year minus 
# Revenue of existing customers from prior year  
def existing_customer_growth(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    return round(existing_customer_revenue_current_year(df, year) - existing_customer_revenue_prior_year(df, year),2)

# Calculates the revnue lost from customers who did not make any purchases 
# this year.  
def revenue_lost_from_attrition(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_unique = merged_data(df_year_current, df_year_prior,'right','right_only')
    return round(sum(df_unique['net_revenue_y']),2)

# Returns the total number of customer from a given year
def total_customers_by_year(df, year):
  years = years_in_data(df)
  if year not in years:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    unique_emails = set(df_year_current['customer_email'])
    return len(unique_emails)

# Returns a list of customers who did not make any puchases last year but
# did make purchases this year
def new_customers(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_unique = merged_data(df_year_current, df_year_prior, 'left', 'left_only')
    return len(df_unique['customer_email'].tolist())

# Retuns a list of all the customers who did not make any purchases this year
def lost_customers(df, year):
  years = years_in_data(df)
  if years[0] == year:
    return "N/A"
  else:
    df_year_current = data_for_year(df, year)
    df_year_prior = data_for_year(df, year - 1)
    df_unique = merged_data(df_year_current, df_year_prior,'right','right_only')
    return len(df_unique['customer_email'].tolist())

