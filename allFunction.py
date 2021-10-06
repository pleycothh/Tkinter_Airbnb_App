import pandas as pd

def load(path="src/listings_summary_dec18.csv"):
    df = pd.read_csv(path)
    return df

def getSuburb(name, data):
    new_data = data[name]
    return new_data