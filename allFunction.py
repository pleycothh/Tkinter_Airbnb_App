import pandas as pd

def load(path="src/listings_summary_dec18.csv"):
    df = pd.read_csv(path)
    return df

#    print(df.head(3)) # print first 3 rows in database
#    print(df['name']) # get the item id and columns named 'name'
#    print(df[['name', 'neighbourhood']]) # use [[]] to return more values
#    print(df['neighbourhood'] == " Leichhardt") # return true or false when compare
#    print(df[df['name']=='Sydney City & Harbour at the door']) # return value with required

#    print(
#        df[
#            (df['name'] == 'Sydney City & Harbour at the door' | df['id'] != 10)
#        ]
#    )
#    # get name = to or id not = 10



load()