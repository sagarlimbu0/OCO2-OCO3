## oco2-oco3_data_access_visualization
- Creating Docker container to host jupyter notebook with provided versions of dependency packages
- Further development:
  * Deploying on cloud provider
  * Handling Requests via Kubernetes pods
### PYDAP, Data Access GES DISC using python
source: (https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Access%20GES%20DISC%20Data%20Using%20Python)

## Reading the data:
![options](https://github.com/sagarlimbu0/oco2-oco3_data_access_visualization/blob/main/screenshots/data_access_visualization.jpeg)

## Converting the OCO netCDF files to geoTIFF
- We cannot convert netCDF file directly to geoTIFF version, since the data are L2 gridded data
- We need to convert to `JSON` format and convert to geoTIFF

![conv](https://github.com/sagarlimbu0/oco2-oco3_data_access_visualization/blob/main/screenshots/creating_tiff_file.jpg)


