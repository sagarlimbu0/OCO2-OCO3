'''
- WEB SCRAP the contents from OpenDap server
- Get all the data, filenames from the content
- Grab data from entire year, month

'''
import re
from bs4 import BeautifulSoup
import requests

'''
- Pass the name of main website: main_url='https://oco2.gesdisc.eosdis.nasa.gov/opendap'
- content of the file: '/contents.html'

'''
def get_total_files(main_url, lite_file, ver_, year):

########################################################################
# GET THE files from OpenDap source. Open the netcdf file and store in dataframe
# Beautiful soup to retrieve all data for the MONTH
# EXAMPLE: in this test, we will use SINGLE file of the month
########################################################################

    # main_url='https://oco2.gesdisc.eosdis.nasa.gov/opendap'
    content= '/contents.html' # GET THE content of the webpage

    s= requests.get(main_url + lite_file + content)

    ## Scrap the content by specified URL
    ## Get the entire filenames of the searched YEAR
    soup= BeautifulSoup(s.content, 'html.parser')

    list_files=[]
    ## regex expression to GET netCDF files
    html_links= soup.select('a[href$=".nc4.html"]')

    for link in html_links:
        list_files.append(link['href'])

    ### DATA CLEANING on the webcontents
    ## pre-process the filenames; strings, CLEAN the files
    ## removing last strings '.html' to download the files from PYDAP library to match file names
    files_oco2= [f[:-5] for f in list_files]

    ## total_files= ['opendap'+lite_file+'/'+ f for f in files_oco2[:3]]
    total_files= [lite_file+'/'+ f for f in files_oco2]

    ## get alternate row files; duplicate ROWS on html LINKS
    total_files= total_files[::2]

    ## Returns the total files from the web content
    return total_files