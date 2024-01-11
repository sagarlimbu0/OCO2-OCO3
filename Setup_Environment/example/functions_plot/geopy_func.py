''' 
GEOPY is a python package to locate the region based on string passed
'''
from geopy.geocoders import Nominatim
import geopy

def get_location(location):
    geo_loc= Nominatim(user_agent="locate", timeout=4)

    info= geo_loc.geocode(str(location)).raw

    ## get the Bounding box information
    loc_bbx= info["boundingbox"]
    bbx_list= [float(i) for i in loc_bbx]
    print('\n************************************\n')
    print("Bbox information of :\n"+f'{location}')
    return bbx_list
