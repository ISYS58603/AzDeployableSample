import pandas as pd
from pathlib import Path
import sqlite3
    
# Set the path of where to find the data files
RAW_DATA_PATH = Path(__file__).parent / 'data'

# Set the path of where to save the SQLite database
DATABASE_PATH = Path(__file__).parents[1] / 'data'

# Load the data into the SQLite database
def load_data():
    # Read the data files into pandas dataframes
    movie_data = pd.read_csv(RAW_DATA_PATH / 'movies.csv')
    rating_data = pd.read_csv(RAW_DATA_PATH / 'ratings.csv')
    user_data = pd.read_csv(RAW_DATA_PATH / 'users.csv')
    
    # Create a SQLite database
    conn = sqlite3.connect(DATABASE_PATH / 'movie_data.db')
    
    # Write the dataframes to the database
    movie_data.to_sql('movies', conn, if_exists='replace', index=False)
    rating_data.to_sql('ratings', conn, if_exists='replace', index=False)
    user_data.to_sql('users', conn, if_exists='replace', index=False)
    print('Data loaded into SQLite database')

def test_data_load():
    # Query the database to make sure the data was loaded
    conn = sqlite3.connect(DATABASE_PATH / 'movie_data.db')
    query = 'SELECT * FROM movies'
    movies = pd.read_sql(query, conn)
    print(movies.head())

if __name__ == '__main__':
    load_data()
    test_data_load()
   