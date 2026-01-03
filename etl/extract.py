import pandas as pd
from pathlib import Path

def extract():
    source = "data/raw/ibm_hr_raw.csv"
    df = pd.read_csv(source)
    print("Extração concluída")

if __name__ == "__main__":
    extract()

