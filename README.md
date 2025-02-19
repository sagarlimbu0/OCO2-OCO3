## OCO2-OCO3

[Arset 2022_Training](https://appliedsciences.nasa.gov/get-involved/training/english/arset-measuring-atmospheric-carbon-dioxide-space-support-climate)

* Sagar Limbu
* <b>Mentors:</b> Karen Yuen and Charles Thompson
![OCO2_OCO3](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/OCO2_OCO3.png)

<b>OCO2</b> is the first dedicated satellite to study Carbon Dioxide launched in July 2, 2014 and <b>OCO3</b> 
is the sister of OCO2 because it has similar instrument sensitivity and performance characteristics to OCO2.
When flying a payload on the International Space Station (ISS), the OCO3 mission was designed to fly with the flight spare.
This means we have 2 of the same instruments that is currently flying and since they fly differently - polar orbit versus a processing orbit
This is really fantastic opportunity for science because It really permits NASA to study CO2 over different areas of the globe. 

### Google Collab Demo; Data visualization of xco2
- Users are encouraged to revisit this section after completing the tutorials and attempt to execute the provided script on Google Colab.
- Execute the Google Colab script to gain access to OCO data from the PyDAP server. Subsequently, we may utilize the carbon footprint vertices for visualization purposes within a specified geographic region.
  - (Ctrl + Click) [Collab Script](https://colab.research.google.com/drive/1Qda7ldoIl1HHXskGfa-D9zrWp_8noWBT?authuser=2)

<img src="https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/pydap_access.jpg" alt="Google Colab" width="800" height="400">

## Table of Contents:
1. [Accessing the OCO2/OCO3 Datasets](#Accessing-the-OCO2/OCO3-Datasets)
2. [Data Pre-processing](#Data-Pre-processing)
3. [Data Visualization](#Data-Visualization)
4. [Setup environment using Docker](#Setup-environment-using-Docker)
5. [Demonstration](#Demonstration)

### 1. Accessing the OCO2/OCO3 Datasets
- In this tutorial, we will guide you through the process of using a Python script. We'll assume that you have some basic programming knowledge.
- To download OCO2/OCO3 data files from the Earth Data Search website, you can follow these steps: First, access the Earth Data Search website and navigate to the OCO2/OCO3 dataset of interest. Then, specify your search criteria such as time range, geographical area, and data product type. You may need to log in or create an account if prompted. Finally, follow the on-screen instructions to complete the download process, and once the files are downloaded, they can be accessed and utilized for further analysis or visualization.
- Prior to proceeding with this tutorial, users can visit the following hyperlink. Within the EarthData platform, a variety of Data Application tools are available for access. Each of these data tools is designed to perform distinct functions, encompassing search criteria utilization, data handling, subsetting and filtering, as well as data visualization and analysis capabilities.
- (Ctrl + Click) [Data Tools provided by EarthData](https://www.earthdata.nasa.gov/learn/use-data/tools)
- (Ctrl + Click) [EarthDataSearch: FAQ](https://www.earthdata.nasa.gov/faq/earthdata-search-faq)

#### 1.b. Getting Data Access via APIs
- The Earthdata Developer Portal serves as a hub for application developers interested in constructing software applications for searching, accessing, and exploring Earth science data hosted by EOSDIS
- (Ctrl+click) [earthdataAPI](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api#edsc)
- Below example demonstrates the API access to OpenDAP using **pydap** tool (client/server software). Above Google collab demonstrates similar example.
  -  Eg: with python's `pydap` we can request to get access the OCO2 datasets using credentials from EarthData login: (Ctrl + Click) [using openDap](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/Data_Visualization_OCO2_OCO3)

### 2. Data Pre-processing
- primary data format for OCO2/OCO3 is netCDF4, affording users the capability to generate visualizations through software tools such as **Panalopy, QGIS, and ArcGIS** directly
- For enhanced accessibility, netCDF files can also be converted into CSV format, providing users with a more straightforward means of data manipulation and analysis. Additionally, for the purpose of optimizing scalability and conserving storage space, the option to save files in the parquet format is also available.
  - Converting netCDF files to CSV format (Ctrl + Click)[netCDF->csv]()
  - Converting netCDF files to parquet format (Ctrl + Click)[netCDF->parquet](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/Convert_netCDF_to_CSV_files/Convert_netCDF_to_PARQUET.ipynb)
- Other GIS software tools:
  - [Panolopy](https://www.giss.nasa.gov/tools/panoply/)
  - [QGIS](https://www.qgis.org/en/site/forusers/download.html)

### 3. Data Visualization
#### 3.a Single day file
  - (Ctrl + Click) [Arset Tutorial 2022](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/ARSET_2022_Training)
  - Utilization of the ARSET training script facilitates the visualization of OCO2/OCO3 data for a single day file, showcasing its practical application.
  - Libraries: 
    - netCDF, pandas, numpy, matplotlib, pydap, plotly, Basemap, seaborn
    - dask // to perfrom data aggregation and data-preprocessing
    
#### 3.b Multiple files
- We can use Dask Library to read multiple files and preprocess, visualize the data
- (Ctrl + Click) [Data_Visualization Multiple files](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/Data_Visualization_OCO2_OCO3)

### 4. Setup environment using Docker
- **Docker-Based Environment Setup:** To facilitate the installation of the necessary packages and libraries, the deployment of Docker containers is recommended. This approach streamlines the environment configuration process and ensures consistent dependencies.
- **Containerization as Docker Image:** For further versatility, the environment can be containerized into a Docker image. This Docker image can subsequently be deployed as a web application or a Jupyter server on Amazon Web Services (AWS). Comprehensive guidelines on these deployment processes can be found within the repository documentation, offering in-depth insights into the steps required for successful implementation.
- These procedures enhance the efficiency and reproducibility of the environment setup, enabling the seamless installation of essential components while providing flexibility in deploying the system as a web application or Jupyter server via AWS infrastructure. Further details are available in the repository documentation for comprehensive guidance.
- (Ctrl + Click) [Setting-up-Environment](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/Setup_Environment)

### 5. Demonstration of XCO2 using vertices (OCO2/OCO3)
The principal aim of this project is to present data points representing XCO2 and illustrate their temporal evolution, thereby offering insight into the variability of the atmospheric carbon cycle for a specified year. In this context, the project utilizes the "vertices" attributes of carbon footprints to generate polygonal shapes, facilitating the visualization of carbon footprint patterns. 

### target region: San Francisco
![alt_text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/oco3_xco2_visualization.png)

### Global Scale of XCO2 seasonality trends
![alt text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/2019_half_year.gif)

### OCO2, XCO2 variation by months
OCO2 data representing the variation of XCO2 by different years. THe visualization built on R code located inside ARSET/ directory representing the california region. <b>NOTE:</b> OCO2 launched on 2014 July, so for this reason the plots displayed in the later months.

![alt text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/static_data/variation_by_months_oco2_2014_2020.gif)

- for any questions, please raise issue in this repository. Thanks
