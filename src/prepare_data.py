from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

df = pd.read_csv(project_root / "data" / "spy_raw.csv", header=[0, 1], index_col=0)

df.columns = df.columns.get_level_values(0)
df.index.name = "Date"
df = df.reset_index()

print(df.head())