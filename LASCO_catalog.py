#!/usr/bin/env python
# coding: utf-8

# ### This module retrieves CME information from the LASCO CME catalog based on CME onset time and speed

# In[1]:


import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


def read_lasco_cat():

    """ This function reads in the LASCO CME catalog
    
    Input:
    
    NONE
    
    Output:
    
    lasco_df: full LASCO catalog scraped from LASCO CME database
        
    """
    
    #loop to retrieve all CME events from LASCO database


    #set counter
    n=0

    #create empty dataframe to append data to 
    lasco_df = pd.DataFrame()
    lasco_df = lasco_df.fillna(0)

    #first year of LASCO database
    year = 1996

    months = ['01','02','03','04','05','06','07','08','09','10','11','12']

    while year < 2019:
        year = 1996 + n
        for m in months:
            #access text files through url and create readable table
            url = "https://cdaw.gsfc.nasa.gov/CME_list/UNIVERSAL/text_ver/univ" + str(year) +"_" + m + ".txt"

            #clear dataframe with each iteration to avoid redundancy and append to cme dataframe
            df = pd.DataFrame()
            df = df.fillna(0)

            #make sure the file exists to avoid errors and create dataframe
            try:
                df = pd.read_table(url, delim_whitespace=True, skiprows=3, usecols=range(0,12), names=['Date','Time','Central_PA','Width','Speed','2nd_Order_Speed_Initial','2nd_Order_Speed_Final','20R','Accel','Mass','Kinetic_Energy','MPA'])
            except:
                pass

            #append monthly data to main cme dataframe
            lasco_df = lasco_df.append(df, ignore_index=True)

            #change counter to move on to the next year
            if m == '12':
                n = n + 1
    return lasco_df


# In[6]:


def add_cme_width(flare_df,lasco_df):
    
    '''Append CME width from LASCO to student catalog
    
    Inputs:
    
    flare_df: student catalog of all flares read in as pandas dataframe
    lasco_df: LASCO CME catalog in pandas dataframe
    
    Outputs:
    
    flare_df: student catalog updated with cme width appended
    
    '''

    #create column for cme width in student catalog
    flare_df['Width'] = np.nan

    cme_events = flare_df.query('cmeonset > "0"') 

    for q in range(0,len(cme_events)):
        #date and time info to match with LASCO
        cme_date = cme_events.iloc[q].cmeonset
        year = cme_date[0:4]
        month = cme_date[5:7]
        day = cme_date[8:10]
        hour = cme_date[11:13]
        minute = cme_date[14:16]
        second = cme_date[17:19]
        date = year + '/' + month + '/' + day 
        time = hour + ':' + minute + ':' + second

        #cme speed info to match with LASCO
        cme_speed1 = cme_events.iloc[q].cmespeed
        cme_speed2 = str(cme_speed1)

        time_search = lasco_df.query('Date == @date and Time == @time')

        match1 = time_search.query('Speed == @cme_speed1')
        match2 = time_search.query('Speed == @cme_speed2')

        if len(match1) > len(match2):
            wid = match1.Width
            width = int(wid)
            idx = cme_events.index[q]
            flare_df['Width'][idx] = width
        elif len(match2) > len(match1):
            wid = match2.Width
            width = int(wid)
            idx = cme_events.index[q]
            flare_df['Width'][idx] = width

    return flare_df


# In[ ]:




