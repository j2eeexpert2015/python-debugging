import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
csv_directory_path = str((base_path / "../../../data/").resolve())


def handleIncorrecRecord(item):
    item = str(item)
    if 'M' in item:
        item = item.replace('M', '')
        item = float(item) * 1000000
    else:
        item = float(item)
    return item


df = pd.read_csv(csv_directory_path + '/googleplaystore.csv')
# Check Data Types
print(df.info())
df['Reviews'] = df['Reviews'].apply(handleIncorrecRecord)
# perform data type conversion on 'Rating' and 'Reviews' column
df['Reviews'].astype('float')
print(df.info())
