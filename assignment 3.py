#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import datetime
import pandas as pd

def tripCreator(tripdays = 24, seed = 154):
        
    global df
    global first_day

    np.random.seed(seed)

    random_day_add = np.random.randint(low=1,high=3, size = tripdays)


    trip_dates = []
        
    for days in range(len(random_day_add)):
        date = datetime.datetime.now() + datetime.timedelta(days)
        formatted_date = datetime.date.fromordinal(date.toordinal()).strftime("%F")
        trip_dates = np.append(trip_dates, [formatted_date])

        mileage = np.random.randint(low=1,high=1443, size = tripdays)

        sorted_mileage = np.sort(mileage)

        data = []

        data.extend(zip(trip_dates, sorted_mileage))

        df = pd.DataFrame(data=data, columns=['Date of Trip', 'Odometer Reading'])

        first_day = df.iloc[0]['Odometer Reading']

        first_day = [first_day]

    print(df)

