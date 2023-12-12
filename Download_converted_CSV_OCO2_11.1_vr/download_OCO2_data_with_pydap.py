'''
## objective:
    - Get access to OpenDAP NASA public server to retrieve OCO2-11.1 vr data
    - Earthdata user credentials required to download the data
    - Specify the start and end YEAR. Specify the month period

'''

## libraries for data access and pre-processing
## preprocessing: retireve data from netCDF and convert to pandas columns
import netCDF4 # packages to open 'netcdf' file
import numpy as np # numpy and pandas packages to pre-process the dataset
import pandas as pd

# for visualization
import matplotlib.pyplot as plt # to create plots and graphs
from mpl_toolkits.basemap import Basemap # to create geo-spatial map, requires dependencies installation
import plotly.express as px
import matplotlib.patches as mpatches
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection
import time
import matplotlib
from datetime import datetime


## Data ACCESS from OPENDAD source
## Libraries
from urllib import request, parse
import getpass
import netrc
import os
import requests
import matplotlib.image as mpimg
import os
import time
import maskpass
from netCDF4 import Dataset

# pydap library to open session
from pydap import client
from pydap.cas.urs import setup_session
from pydap.client import open_url
import json

# to load webcontent and retrieve data from link
from IPython.display import display, HTML
from IPython import display
from datetime import datetime

## Loading Screen
from tqdm import tqdm
import time

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

## CLEANING
import gc
import sys

## GEOPY package to locate the region
from geopy.geocoders import Nominatim
import geopy

# WEB SCRAP the contents
import re
# to grab data from entire year, month
from bs4 import BeautifulSoup #
from IPython.display import Image


## Create a session on EarthDat bypassing the credentials
def get_session(url, file_name):
    """
    Creating a session with url and filename in openDap for data retrieval
    https://oco2.gesdisc.eosdis.nasa.gov/opendap/
    """
    try:
        login_credentials= 'uat.urs.earthdata.nasa.gov'
        username, _, password = netrc.netrc().authenticators(login_credentials)
    except (FileNotFoundError, TypeError):
        # FileNotFound = There's no .netrc file
        # TypeError = The endpoint isn't in the netrc file, causing the above to try unpacking None
        print('\n*******************************************\n')
        print('Please provide your Earthdata Login credentials to allow data access\n')
        print('Your credentials will only be passed to %s' % (url))
        print('\n')
        # username = input('Username: ')
        
        username = maskpass.askpass(prompt="Username: ", mask="*")
        password = getpass.getpass()
        print('\n*******************************************\n')

    # pydap session
    session = setup_session(username, password, check_url= url + file_name)

    # using the session to get access the data
    return session


#################################################
#################################################
### Get list of the URLs
## URLs include fileanames of the data specified by the given year

def get_full_list(year_range):

    ## Iterate over diff. years
    full_year_list= []

    full_years= [year_range]

    
    ## Retrieve the content to create a session token
    lite_file= '/OCO2_L2_Lite_FP.11.1r/' + str(full_years[0])

    for year in range(0, len(full_years)):
    # for year in full_years:
        ## FORMAT the filenames by VERSION and YEAR
        ## RETRIEVE all filenames for the YEAR using webscraping
        ## OCO3
        #lite_file= '/OCO3_L2_Lite_FP.'+ str(ver_)+ '.4r' +'/'+ year

        #########################
        ## OCO2
        # lite_file= '/OCO2_L2_Lite_FP.11.1r/' + str(full_years[year])
        

        ########################################################################
        # GET THE files from OpenDap source. Open the netcdf file and store in dataframe
        # Beautiful soup to retrieve all data for the MONTH
        # EXAMPLE: in this test, we will use SINGLE file of the month
        ########################################################################

        #main_url= 'https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/'

        main_url='https://oco2.gesdisc.eosdis.nasa.gov/opendap'
        content= '/contents.html'

        ## Handlin Network Error
        try:
            s= requests.get(main_url + lite_file + content)
            s.raise_for_status()
        
        except requests.RequestException as e:
            print(f"Error fetching the content: {e}")

        if s.status_code == 200:
            ## Scrap the content by specified URL
            ## Get the entire filenames of the searched YEAR
            soup= BeautifulSoup(s.content, 'html.parser')

            list_files=[]
            ## regex expression to GET netCDF files
            html_links= soup.select('a[href$=".nc4.html"]')

            # html_links= soup.select('a[href$=".nc4"]')

            for link in html_links:
                list_files.append(link['href'])

            ## pre-process the filenames; strings, CLEAN the files
            # removing last strings '.html' to download the files from PYDAP library to match file names
            files_oco2= [f[:-5] for f in list_files]

            # total_files= ['opendap'+lite_file+'/'+ f for f in files_oco2[:3]]
            total_files= [lite_file+'/'+ f for f in files_oco2]

            ## get alternate row files; duplicate ROWS on html LINKS
            total_files= total_files[::2]

            ## Append the files by diff. years
            full_year_list.append(total_files)
    
    return full_year_list


#################################################
#################################################
### USER prompts for START and END year
print('\n*******************************************\n')
print('Extract OCO2-11.1 vr data from OpenDap Server. This requires to passing user credentials to retreive data from the server.\n')
print('Instructions:\n')
print('\t- Enter the start and end year:. EG: Start year: 2015 and End Year: 2018.')
print('\t- If data requested for single year, then start and end year should be same year. EG: Start year: 2015 and End Year: 2015.')
print("\t- Next, Pass user credentials.")
print('\n*******************************************\n')

start_year = input("Start Year: ")
end_year = input("End Year: ")

total_years = []

# Code blocks for multiple Exceptions on user input
try:
    # Convert user input to integers
    start_year = int(start_year)
    end_year = int(end_year)

    # Assert the years within the MISSION data
    assert start_year >= 2014, "Start year after 2014."

    cur_year = datetime.now() # Extract the year from today's date
    assert end_year <= cur_year.year, "End year should be current year or earlier."

    # Assert the years has 4 length
    assert len(str(start_year) )== 4, "Invalid year format."
    assert len(str(end_year)) == 4, "Invalid year format."

    # Add the years to the list
    if start_year == end_year:
        total_years.append(start_year)
    else:
        total_years = list(np.arange(start_year, end_year + 1))

    print("Total years:", total_years)

except ValueError:
    print("Invalid Date. Enter years in numbers. Example: '2014, 2015, etc.'")

except AssertionError as e:
    print("User Input Error:", e)


## get the total files by specified year
total_files= get_full_list(total_years)

## function to conv. dateTime var
def conv_time(d):
    return datetime.utcfromtimestamp(d)

#################################################
#################################################
### PROMPT user for credentials to create session
# main_url='https://oco2.gesdisc.eosdis.nasa.gov/opendap'
# content= '/contents.html'

# url=main_url
# session= get_session(url, total_files[0])


################################################
### Iterate over the server to retrieve the data
# def extract_oco2_data(session, total_years):

def extract_oco2_data(total_years):

    ##########################################
    ## set the total years to extract the data
    years= total_years

    ### Create session
    main_url='https://oco2.gesdisc.eosdis.nasa.gov/opendap'
    content= '/contents.html'

    ## to open a session, passing the first URL
    varCreateSession= get_full_list(years[0])
    
    url=main_url
    session= get_session(url, varCreateSession[0][0])

    ## session.post
    if session:
    #     print("alive")

        for i in range(0, len(years)):
            ## Get the list by diff. YEAR
            ## includes the URLs of OCO2 data by diff. year
            total_= get_full_list(years[i])
            
            ## create new dir.
            new_year= years[i]
            
            ### make new dir.
            if not os.path.exists(str(new_year)):
                os.mkdir(str(new_year))
            else:
                continue

            ### Iterate over the URLs to retreive the data
            for j in range(0, len(total_)):

                ## complete full list of URLs from the selected year
                ## URLs include the path to individuals files
                new_data= total_[j]

                ### progress bar to show download completion
                total_iterations= len(new_data)
                progress_bar= tqdm( total= total_iterations, unit= "MB")
                
                for k in range(0, len(new_data)):

                    pydap_df= open_url(main_url + new_data[k], session=session)

                    #################################################
                    # collect the data
                    df_xco2= pd.DataFrame()

                    df_xco2['Xco2']= np.array(pydap_df["xco2"][:])
                    df_xco2['Latitude']= np.array(pydap_df["latitude"][:])
                    df_xco2['Longitude']= np.array(pydap_df["longitude"][:])
                    df_xco2['quality_flag']=  np.array(pydap_df["xco2_quality_flag"][:])
                    # Date
                    df_xco2['DateTime']= np.array(pydap_df["time"][:])

                    #Convert soundingID to datetime format
                    df_xco2['DateTime']= df_xco2['DateTime'].apply(conv_time)
                    df_xco2['DateTime']= pd.to_datetime(df_xco2['DateTime'])

            #         # YEAR and month column
                    df_xco2['Year']= df_xco2['DateTime'].dt.year
                    df_xco2['Month']= df_xco2['DateTime'].dt.month
                    df_xco2['Day']= df_xco2['DateTime'].dt.day

            #         # Refine the ENTIRE dataframe by GOOD quality_flag->0
            #         # NOTE: REDUCES the size of the file
#                     df_xco2= df_xco2[(df_xco2['quality_flag'] == 0)]

                    # create a CSV and store on new folder: csv_files
                    df_xco2.to_csv( str(new_year) + '/' + str(new_data[k][39:-4])+ '_.csv', index= False)
#                     print('***********************/n')      
                
                    progress_bar.update(1)
                
                print("NEXT Year file iteration:\n")
                progress_bar.close()
    else:
        print("request new session")

#############################################
### Extract data
extract_oco2_data(total_years)

#print(total_years)
print("Downloads Complete!!!!!!!")