#!/usr/bin/env python
# coding: utf-8

# # Extracting files directly from OPENDAC website
# 
# ### libraries : netCDF4, pydap.client (READ netCDF files)
# ### Library: 'BeautifulSoup' to read the contents of the webpage
# * Reading the contents from the desired web page (here, OCO2)
# * We pass the parameters: Instrument and year
# * Save the links of different datasets in a list
# * open up the lists using <b>netCDF</b>
# 
# # Data Retrieving from:
# ### Instrument and version: OCO2_L2_Lite_FP.10r
# ### Year: 2020

# In[1]:


import pydap.client
import netCDF4 as nc

# for data-preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot



# TESTING with netcdf file, SINGLE dataset
# read files from netCDF
# Reading Single file from the link


my_df= nc.Dataset('https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_FP.10r/2020/oco2_LtCO2_200109_B10206Ar_200728203551s.nc4')




len(my_df.variables['xco2'])




my_df.variables.keys()


# # Reading the contents from the WEB page and retrieving only the links
# ### Libraries: BeautifulSoup to read webElements
# - Collecting the lists and using the links to open datasets using <b>NETCDF</b>
# 
# ## WEB PAGE:
# - Here, we can pass the user input for <b>Instrument and Year</b>
# * url= 'https://oco2.gesdisc.eosdis.nasa.gov/opendap/'+str(instrument)+'/'+ str(year)+'/contents.html'

# In[6]:


import requests

import urllib3
from bs4 import BeautifulSoup


# In[7]:


url= 'https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_FP.10r/2020/contents.html'


# # USER INPUT: 
# * Instrument and Version
# * Year

# In[8]:


# Pass the following parameters for this test
# Instrument: current testing(Pass) -> OCO2_L2_Lite_FP.10r
# year: 2020

instrument= input()
year=input()


# # Your Passed Parameters:
# * Instrument
# * Year

instrument,year


# # READ contents from the URL:
# * By passing the parameters from the USER input

my_url= 'https://oco2.gesdisc.eosdis.nasa.gov/opendap/'+str(instrument)+'/'+ str(year)+'/contents.html'



my_url




## Example
url


# In[13]:


# Get the content from the webpage
reqs= requests.get(my_url)

# selecting the lxml parser
soup= BeautifulSoup(reqs.text, 'lxml')


# SOUP var, Here, returns the entire HTML contents


soup


# # Filtering: to Get contents from the tag 
# * "\<a>" only, which lists the contents
# ### Cleaning and saving the LINKS for the datasets only


# total links
oco2_links= []

for link in soup.find_all('a'):
    print(link.get('href'))
    oco2_links.append(link.get('href'))


# # Get the links ending with 'html' only
# ### Rest of the links have different purpose
# ### NOTE: another important link ending with 'info' gives information on Product
# 

# storing the html links
dataset_links=[]

for k in range(0, len(oco2_links)):
    if oco2_links[k].endswith(".html"):
        print(oco2_links[k])
        
        # Strip the 'html' from the links 
        dataset_links.append(oco2_links[k].strip('.html'))


# to avoid duplicate records
p=0
complete_oco2_links=[]

for i in range(0, len(dataset_links)):
    try:
        complete_oco2_links.append(dataset_links[i+p])
        p+=1
    # Ignoring the Out of Index error
    except IndexError as e:
        continue



# TESTING: for duplicate records, output: half
len(dataset_links),len(complete_oco2_links)


# # Other Important links:
# * Information on the product

# # Using the lists to Retrieve datasets
# * Using <b>netCDF</b> library to get the data

# CHECK: JAN to DEC dates on the filenames

complete_oco2_links[:5], print('****') ,complete_oco2_links[-4:]


# ### TEST
# * Attaching the full link + dataset
# * my_url= 'https://oco2.gesdisc.eosdis.nasa.gov/opendap/'+str(instrument)+'/'+ str(year)+ complete_oco2_links[0]


first_element_oco2= nc.Dataset('https://oco2.gesdisc.eosdis.nasa.gov/opendap/'+str(instrument)+'/'+ str(year)+'/'+complete_oco2_links[2])
first_element_oco2.variables.keys()



# # NEXT STEP:
# * Retrieving all datasets into pandas DataFrame for analysis
# * Rearrange the dateTime format
# 
# # Creating a Class object:
# * Function that reads the variables from the dataset

# In[ ]:


# class readData():
    
#     # objects to store variables
#     xco2=[]
#     sounding_id=[]
#     latitude= []
#     longitude= []
    
    
#     # initialization
#     def __init__(self):
        

