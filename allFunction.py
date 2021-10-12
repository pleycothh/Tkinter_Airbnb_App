############################check list########################################
import numpy as np
import matplotlib.pyplot as plt
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
"""

1. local database

leget
unit test
clean code

"""


##############################end check list##########################################
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

! apply new frame within button frame

Required Features:

For a user-selected period, report the information of all listings in a suburb

For a user-selected period, produce a chart to show the distribution of prices of properties

For a user-selected period, retrieve all records that contain a keyword (user entered), e.g. pool, pet.

Analysing how many customers commented on factors related to cleanliness (multiple key words

may be associated with cleanliness – justify your selection).

One other ‘insight’ or analysis tool of your choic
"""