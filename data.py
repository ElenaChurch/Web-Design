
import pandas as pd
file_one = "Resources/cities.csv"
cities_df = pd.read_csv(file_one, encoding="ISO-8859-1")
cities_df.set_index('City_ID')
cities_df.to_html('cities.html')