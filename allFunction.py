
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
#    # get name = to or id not =

'''
# search key term
filt = df(df['name'] == 'Doe')
df[filt] = df.loc[filt]

only return reqired column
 df.loc[filt, 'email']
'''

"""
to do list:

!key term search ability # keyword

!add more button

!open external matlab figure # with price properties

! implement sqlite database

Required Features:

For a user-selected period, report the information of all listings in a suburb

For a user-selected period, produce a chart to show the distribution of prices of properties

For a user-selected period, retrieve all records that contain a keyword (user entered), e.g. pool, pet.

Analysing how many customers commented on factors related to cleanliness (multiple key words

may be associated with cleanliness – justify your selection).

One other ‘insight’ or analysis tool of your choic
"""