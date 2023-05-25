## OCO2-OCO3

* Sagar Limbu
* <b>Mentors:</b> Karen Yuen and Charles Thompson
![OCO2_OCO3](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/animation_visuals/OCO2_OCO3.png)

<b>OCO2</b> is the first dedicated satellite to study Carbon Dioxide launched in July 2, 2014 and <b>OCO3</b> 
is the sister of OCO2 because it has similar instrument sensitivity and performance characteristics to OCO2.
When flying a payload on the International Space Station (ISS), the OCO3 mission was designed to fly with the flight spare.
This means we have 2 of the same instruments that is currently flying and since they fly differently - polar orbit versus a processing orbit
This is really fantastic opportunity for science because It really permits NASA to study CO2 over different areas of the globe. 

### 1. Accessing the OCO2/OCO3 Datasets
#### 1.a. Getting started with EarthData Search website:
By visiting the website and following instructions provided on FAQ contents:
- (Ctrl + Click) [EarthDataSearch: FAQ](https://www.earthdata.nasa.gov/faq/earthdata-search-faq)

#### 1.b. Getting Data Access via APIs
- (Ctrl+click) [earthdataAPI](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api#edsc)
- In this example, we have used OpenDAP tool (client/server software)
-  Eg: with python's `pydap` we can request to get access the OCO2 datasets using credentials from EarthData login: 
[using openDap](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/Data_Visualization_OCO2_OCO3)

### 2.a. Libraries to READ datasets
- Data visualization of OCO2/OCO3 dataset:
- Example:
[Data_Visualization](https://github.com/sagarlimbu0/OCO2-OCO3/tree/main/Data_Visualization_OCO2_OCO3)
- Libraries: 
  - netCDF, pandas, numpy
  - dask // to perfrom data aggregation and data-preprocessing
  
### 3.a. Data Visualization
- Using different libraries for data visualization
- Libraries: 
  - matplotlib 
  - pydap
  - Plotly
  - Basemap
  - seaborn
### 4.a. Setup environment using Docker
- 4.b. Using the docker to setup environment to install required packages:
  - [setup env.](https://github.com/sagarlimbu0/oco2-oco3_data_access_visualization)

### 5.a. Introduction (OCO2/OCO3)
The Earth system maintains checks and balances on carbon dioxide through the carbon cycle and what we call sources and sinks. Carbon dioxide (CO2) is one of the most important Greenhouse Gases (GHG) that supports life on Earth and the primary GHG quantifiable from anthropogenic sources. Thus, it is important to understand the role of atmospheric CO2 in understanding the carbon cycle balance. The primary science objective of the OCO-2 and OCO-3 missions is to collect the atmospheric carbon dioxide (CO2) dry air mole fraction, XCO2, with the precision, resolution, and coverage needed to improve our understanding of surface CO2 sources and sinks (fluxes) on regional scales. 
The main objective of the project is to display datapoints of XCO2 and showing the change over time that can provide a status of the atmospheric Carbon cycle variability by the given year.

### Specific targetted region example:
![alt_text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/animation_visuals/oco3_xco2_visualization.png)

### Global Scale of XCO2 seasonality trends
![alt text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/animation_visuals/2019_half_year.gif)

### XCO2 variation by months
OCO2 data representing the variation of XCO2 by different years. THe visualization built on R code located inside ARSET/ directory representing the california region. <b>NOTE:</b> OCO2 launched on 2014 July, so for this reason the plots displayed in the later months.

![alt text](https://github.com/sagarlimbu0/OCO2-OCO3/blob/main/animation_visuals/variation_by_months_oco2_2014_2020.gif)

### Individual Files
- Each individual file has different instructions and steps
