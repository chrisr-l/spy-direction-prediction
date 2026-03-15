from pathlib import Path
import yfinance as yf

project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"

df = yf.download("SPY", start="2010-01-01", auto_adjust=True)
df.to_csv(data_dir / "spy_raw.csv")

print("saved to:", data_dir / "spy_raw.csv")
print(df.head())