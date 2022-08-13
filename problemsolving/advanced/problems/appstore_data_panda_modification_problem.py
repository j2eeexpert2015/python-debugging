import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
csv_directory_path = str((base_path / "../../../data/").resolve())
df = pd.read_csv(csv_directory_path + '/googleplaystore.csv')
# Check Data Types
print(df.info())
# perform data type conversion on 'Rating' and 'Reviews' column
df['Reviews'].astype('float')
print(df.info())
