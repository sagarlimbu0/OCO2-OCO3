'''
- Creates patches from vertices(corner) points to create polygon shapes
- Visualize the polygon shaped with XCO2 values
'''

import numpy as np
import matplotlib.patches as mpatches
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib.collections import PatchCollection

# Pass the pandas dataframe
# columns included; xco2, longitude_vertices, latitude_vertices, quality_flag
def get_patches(df):
    #################################################
    # 2. DSTACK the vertices of corner points together
    flat_vertices=[]
    for j in range(0, len(df)):
        flat_vertices.append(np.dstack([df["Longitude_vertices"].iloc[j], df["Latitude_vertices"].iloc[j] ]))

    ##################################################
    # 3. GET patches from the vertices
    ## unpack the values from the list
    unpack_vertices= [elem for sublist in flat_vertices for elem in sublist]
    patches_total= [mpatches.Polygon(row) for row in unpack_vertices]

    return patches_total