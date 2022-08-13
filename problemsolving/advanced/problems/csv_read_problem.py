import pandas as pd
from pathlib import Path
base_path = Path(__file__).parent
csv_directory_path = str((base_path / "../../../data/").resolve())

city_names_df = pd.read_csv(csv_directory_path+'/city-names.csv')
city_pop_df = pd.read_csv(csv_directory_path+'/city-populations.csv')
merged_df = city_names_df.merge(city_pop_df)
print(merged_df)
