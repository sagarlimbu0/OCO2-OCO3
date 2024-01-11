# for visualization 
import matplotlib.pyplot as plt # to create plots and graphs
from mpl_toolkits.basemap import Basemap # to create geo-spatial map, requires dependencies installation
import matplotlib.patches as mpatches # to create patches of POLYGON shapes
from matplotlib.collections import PatchCollection
import matplotlib as mpl

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


"""
1. Pass the xco2 values from netCDF file and Patches values generated from POLYGON shape
2. Use either `Dark` or `ArcGis` Theme
3. Pass the bounding box information
4. Pass OFFSet points for map to visuzlize a bit extent outside the actual MAP
5. Pass the location string
6. Pass the YEAR and MONTH from previous search criteria to OPENDA
"""
def plot_vertices(xco2_total, patches_total, bbx_list_info, location, year, month):
    # ## XCO2 values
    # xco2_total= xco2_list

    ## plot to graph using basemap
    fig= plt.figure(111)
    ax= fig.add_subplot(111)

    ## SET the min and max boundaries for XCO2
    xco2_min_= 405
    xco2_max_= 420

### world map: 
    # set the boundaries: llcrnrlon, urcrnrlon, llcrnrlat, urcrnrlat= -180, 90, -90, 90 
    
    
##   Pass OFFSet points for map to visuzlize a bit extent outside the actual MAP
    offset= 2
    llcrnrlon= bbx_list_info[2] - offset
    urcrnrlon= bbx_list_info[3] + offset
    llcrnrlat= bbx_list_info[0] - offset
    urcrnrlat= bbx_list_info[1] + offset
    
    # ###worldmap (FULL_OUTER_MAP)
    m= Basemap(projection= 'cyl',
            llcrnrlon= llcrnrlon,
            urcrnrlon= urcrnrlon,
            llcrnrlat= llcrnrlat,
            urcrnrlat= urcrnrlat,   
            resolution='l', 
            epsg= 4269
            )

    ## DARK theme map
    # m.fillcontinents(color='#191919',lake_color='#000000') # dark grey land, black lakes
    # m.drawmapboundary(fill_color='#000000') 

    ### ArcGIS map
    m.arcgisimage(server='http://server.arcgisonline.com/ArcGIS', 
                  #service='World_Shaded_Relief', 
                  service='World_Imagery',
                  xpixels=2000, ypixels=None, dpi= 2000, verbose=False)


    cmap= plt.get_cmap('viridis')
    colors= cmap(xco2_total)

    ## PATCHES object passed to this function
    ## patch collection and plt show
    ## Normalize
    norm = mpl.colors.Normalize(vmin=xco2_min_, vmax=xco2_max_)
    p= PatchCollection(patches_total,
                       cmap= mpl.cm.viridis, 
                       #alpha= 0.95, 
                      # linewidths= 4
                       edgecolor='none',
                       norm= norm
                      )

    # set color range from XCO2
    #p.set_color(colors)
    p.set_array(xco2_total)
    #p.set_clim(np.min(xco2), np.max(xco2))

    plt.gcf().set_size_inches(10, 10)
    ax.add_collection(p)

    ## COLOR bar
    cmap = mpl.cm.viridis
    # ## Normalize; use the same normalized form from above
    # norm = mpl.colors.Normalize(vmin=xco2_min_, vmax=xco2_max_)
    cbar= plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                       orientation='horizontal', label='OCO3, XCO2 ppm\n'+'Year: '+
                       str(year)+ ' Months: '+ str(month)+'\n'+
                      str(location).upper())
    #    plt.savefig('dark'+str(year)+'_'+str(months_sel)+"_oco2_oco3_comb.jpg", dpi= 3500, bbox_inches='tight', pad_inches= 2)
    plt.show();