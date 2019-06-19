#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
#from datetime import timedelta, datetime #, strptime, strftime
from sunpy.instr.goes import get_goes_event_list
from sunpy.time import parse_time, TimeRange, is_time_in_given_format
from sunpy.instr.goes import flareclass_to_flux
from sunpy.lightcurve import GOESLightCurve
from datetime import timedelta
import datetime
import operator
flare_df = pd.read_excel("ControlEvents_student.xls") #read in new SEP data 


# In[43]:


def flare_persistence(flare_pd, hours):

    '''This function finds the highest flare flux a specified amount of hours
    before the flare onset. We call this the flare persistence.
    
    Input:
    
    flare_pd: pandas dataframe of events
    hours: specifies the amount of hours before the flare that you want to find the max flux
    
    Output:
    
    flare_df: original file with the flare persistence appended for all events
    
    '''
    
    flare_df = flare_pd
    flare_start = flare_df['FlrOnset']
    flare_per = []

    for g in flare_start:    
        if isinstance(g,str) == True: #make sure its not nan
            error = 0 #to check whether or not we were able to match peak times (refer to nested for loop)
            flare_dt = datetime.datetime.strptime(g, "%Y-%m-%dT%H:%M:00.000")
            max_flux = []

            #convert to the format that needed for sunny TimeFrame function - add some time to the start and end times
            t1 = flare_dt - timedelta(seconds = (60*60*hours))   
            t2 = flare_dt - timedelta(seconds = (60*1))   

            t1_s = datetime.datetime.strftime(t1, '%Y/%m/%d %H:%M')  
            t2_s = datetime.datetime.strftime(t2, '%Y/%m/%d %H:%M')

            #query the goes event list for all flares before and after the flare peak time of the event you are interested in
            g_evt_list = get_goes_event_list(TimeRange(t1_s, t2_s))

            if len(g_evt_list) > 0:
                for k in range(len(g_evt_list)):
                    if len(g_evt_list[k]['goes_class']) > 1:
                        gc = g_evt_list[k]['goes_class']
                        try:
                            flx = flareclass_to_flux(gc)
                        except:
                            flx = 0
                        max_flux.append(flx)
                    else:
                        flx = 0
                        max_flux.append(flx)
            elif len(g_evt_list) == 0:
                flx = 0 
                max_flux.append(flx)

            index, value = max(enumerate(max_flux), key=operator.itemgetter(1))
            flare_per.append(value)

    flare_df['FlarePersistence'+str(hours)] = flare_per

    return flare_df

