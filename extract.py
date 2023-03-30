# %% Import sql library
import sqlalchemy, pandas as pd, numpy as np, matplotlib.pyplot as plt, os, sys, yaml, time
from sqlalchemy import create_engine
from yaml import safe_load

# %% Make a connection to the database
info = safe_load(open(os.path.join(os.getcwd(), 'credentials.yaml')))
for key in info:
    # save each key as a variable
    globals()[str(key)] = info[key]
# Create the connection string
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
# Create the engine
engine = create_engine(connection_string)

# %% Define the query
view = 'public.view_basis_hourly_na_timeobs'
view_columns = ['label', 'statid', 'timeobs', 'elem_no', 'elem_val']
label = [2100, 10002100, 300002100, 310002100]
elem_no = [101, 123, 113, 201, 301, 371, 365, 401, 603, 801]
timeobs_start = '1958-01-01 00:00'
timeobs_end = '2023-01-01 00:00'

def every_year(start, end, order='ASC'):
    start_year = pd.to_datetime(start).year
    end_year = pd.to_datetime(end).year
    if order == 'ASC':
        return [f'{year}-01-01 00:00' for year in range(start_year, end_year+1)]
    elif order == 'DESC':
        return [f'{year}-01-01 00:00' for year in range(end_year, start_year-1, -1)]
    else:
        raise ValueError('order must be either ASC or DESC')
start = pd.to_datetime(timeobs_start)
end = pd.to_datetime(timeobs_end)
every_year = every_year(start, end)

time_very_start = time.time()
# create cirectory to save the data
directory = os.path.join(os.getcwd(), 'extractions')
if not os.path.exists(directory):
    os.makedirs(directory)

for year in every_year[:-1]:
    year_int = int(year.split('-')[0])
    next_year = year_int + 1
    print(f'Working on {year_int} to {next_year}')
    time_start = time.time()
    sql_query = f"""
    SELECT {', '.join(view_columns)}
    FROM {view}
    WHERE label IN {tuple(label)}
    AND elem_no IN {tuple(elem_no)}
    AND timeobs >= '{year_int}-01-01 00:00'
    AND timeobs < '{next_year}-01-01 00:00';
    """
    connection = engine.connect()
    print(sql_query)
    # Execute the query and store in numpy array
    df = pd.read_sql_query(sql_query, con = connection, parse_dates=['timeobs'])
    # Close the connection
    connection.close()
    # Save the data frame with the year as the name
    df.to_csv(os.path.join(directory, f'{year_int}.csv'), index=False)
    time_end = time.time()
    print(f'Time taken: {time_end - time_start} seconds')

time_very_end = time.time()
print(f'Total time taken: {time_very_end - time_very_start} seconds')

# %%
# one dir back
directory = os.path.join(os.path.dirname(os.getcwd()), 'extractions')
print(directory)

# %%
# Combine all the csv files into one
df = pd.concat([pd.read_csv(os.path.join(directory, file)) for file in os.listdir(directory)])
df.to_csv(os.path.join(directory, 'all.csv'), index=False)
