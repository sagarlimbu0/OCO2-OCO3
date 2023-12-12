## Objective: Download CSV files for OCO2-11.1.vr(latest 2023)
- This code is designed to cater specifically to users seeking data in CSV format. The OCO data, initially stored in netCDF format, can be retrieved in 
CSV format through the utilization of this script. The script allows users to download files based on a specified date: YEAR, in accordance with individual 
user requirements.
- To access this functionality, users are mandated to provide credentials, which can be generated on the Earthdata Login website: https://urs.earthdata.nasa.gov/.
- The script facilitates the retrieval of files from the OpenDap Server, subsequently converting them into CSV format. Key variables encompassed in the output 
include longitude, latitude, xco2_quality_flag (0 and 1), xco2, and dateTime.

### Note: 
- This is ongoing development code. Future work will be customized to perform Asynchronous operations on data requests to the server. This will perform multiple consecutive requests which should be significantly faster than the current operation.

### Instructions:
![download_files](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/instructions.jpg)
