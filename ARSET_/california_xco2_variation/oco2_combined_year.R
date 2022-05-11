###############################################
# Reading the combined files for OCO2 by California region only
# Multiple files concatenated and filtered by coordinates to get California region
# Captured dotted points represent by every 10th row due to large file size 

library(gapminder)
library(ggplot2)
library(gganimate)
library(tidyverse)
library(raster)
library(sp)
library(dplyr)
library(ggthemes)
library(scales)

# READ the combined concatenated file
oco2 <- read.csv("combined_2014_2020.csv")

# Reading the files
data_row<-nrow(oco2)

# total row -1 
total_counts<- c(0: (data_row - 1))
total_counts

head(oco2)

# using ggplot for animation
# NOTE: color apply using FACTOR(<feature>)
# Attributes for visuals: XCO2

graph1<- oco2 %>%
  ggplot( aes (x= Index, y= Xco2,
               color= factor(Year))) +
  #  geom_point(alpha= 0.3, stroke= 1)+
  geom_point(alpha= .25, stroke= 1)+
  theme_fivethirtyeight()+
  scale_size(range= c(2,12), guide= "none") +
  labs(
    title= "XCO2 variation, (CALIFORNIA)",
    x= "Years, combined in range (2014-2017)",
    y='XCO2 (ppm)'
  )+
  theme(axis.title= element_text(),
        text= element_text(family= "Rubik"),
        legend.text= element_text(size= 20)) +
  scale_color_brewer(palette= "Set2")+
  geom_hline(yintercept = 410, color='red',
             linetype="dashed")+
  scale_fill_manual(values= c("red", "yellow",
                              "green", "blue"))


# Scatter plot for combined datasets
# Different color scales represents dotted points by different years
graph1 + scale_x_continuous(labels= comma)

########################
# Graph of total data points
# XCO2 variation by MONTH in different years

by_month <- graph1+ transition_time(Month)+
  labs(title= "California, XCO2(2014-2020), Month: {frame_time}")+
  shadow_mark(alpha= 0.45, wake_length= 0.1,
              size= 0.7)

# NOTE: OCO2 satellite started measurements in the ending year of 2014. Therefore, for 2014 year we can see the data points 
# starting from August month only

gganimate::animate(by_month, height= 600, width= 1000)

# Saving the animation
anim_save("variation_by_months_oco2_2014_2020.gif")




