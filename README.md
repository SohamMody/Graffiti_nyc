# Graffiti Art or Graffiti Vandalism?

## Project Description:
We are trying to see the kind of response people have to various graffiti art in different neighborhoods and if that response can be correlated with crime in the area. For example, if the graffiti is very creative or has a positive social message, people are likely to find it attractive and post pictures of it on social media (Instagram, Flickr, etc). On the other hand, if the graffiti is related to gang symbols or violence, people might not want it in their vicinity and would complain to get it removed (311 complaints). We have compared this response to arrests in the neighborhood and have found that these two are strongly negatively correlated. That is, the neighborhoods having a positive response to graffiti have a lower crime rate and vice versa. Intuitively also, the results made sense as neighborhoods like Dumbo had positive response and less crime while neighborhoods like Bed-Stuy had a negative response and more crime. To prove that the results are statistically significant, we have used the Spearman's rank correlation test.  The team members for this project are Jianwei Li, Siddhanth Shetty and Soham Mody.

## Motivation:
* Proxy to determine the value of graffiti impact of the neighborhoods
* Local guide for artists, shop owners looking for graffiti hotspot and relative business
* Tool for policy makers or police officers to monitor violence

## Methodology:

* Data ingestion
* Create Data Hive Table for (311_Data, Flickr_Data and NYPD_Data)
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/311_hivetable.JPG "Logo Title Text 1")
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/flickr.png "Logo Title Text 1")
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/nypd_arrests.png "Logo Title Text 1")

* Create Zillow Neighborhoods table in hive
* Performing spatial join on these two datasets ( zillow1 and 311_data_graffiti)
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/311_spatialjoin_zillow_table.JPG "Logo Title Text 1")
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/flickr_zillow.png "Logo Title Text 1")
![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/nypd_zillow_year.png "Logo Title Text 1")

* Neighborhood graffiti perception score in Jupyter Notebook

_Neighborhood graffiti perception score_ = _Number of Flickr posts(norm.)_ – _Number of 311 complaints(norm.)_

![alt text](https://github.com/sds695/Graffiti_nyc/blob/master/screenshots/tableau.png "Logo Title Text 1")

## Reference & Data Source:

References:
* T. White. Hadoop: The Definitive Guide. O’Reilly Media Inc., Sebastopol, CA, May 2012.
* A. Gates. Programming Pig. O’Reilly Media Inc.,Sebastopol, CA,  October 2011.
* J. Dean and S. Ghemawat. MapReduce: Simplified data processing on large clusters. In proceedings of 6th Symposium on Operating Systems Design and Implemenation, 2004.
8 S. Ghemawat, H. Gobioff, S. T. Leung. The Google File System. In Proceedings of the nineteenth ACM Symposium on Operating Systems Principles – SOSP ‘03, 2003.
* E.Tokuda, R. Cesar-Jr., C. Silva. Quantifying the presence of graffiti in urban environments. The Google File System. In Proceedings of IEEE International Conference on Big Data and Smart Computing, 2019.
* John D. Boy and  Justus Uitermark. How to Study the City on Instagram. PLOS ONE, June 2016 
* MacDowall Lachlan, A Boneyard of Data: Graffiti and Street Art’s Temporalities. 2015
* MacDowall Lachlan, Graffiti, Street Art and Stigmergy” in Lossau, J. and Stevens, Q. The Uses of Art in Public Space (London: Routledge, 2015)

Data Sources:
* https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
* https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc
* https://www.flickr.com/

