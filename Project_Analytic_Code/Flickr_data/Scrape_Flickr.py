#!/usr/bin/env python
# coding: utf-8

import flickr_api
from tqdm import tqdm


### For first time only

# a = flickr_api.auth.AuthHandler() # creates a new AuthHandler object
# perms = "read" # set the required permissions
# url = a.get_authorization_url(perms)
# url

# a.set_verifier('9dff796ed76beaad')
# flickr_api.set_auth_handler(a)

# a.save('auth.txt')

flickr_api.set_keys(api_key = 'xxxxxxx', api_secret = 'xxxxxxx')
flickr_api.set_auth_handler('auth.txt')

# Centroid of NYC calculated using borough boundaries shapefile
lon_NYC ,lat_NYC = (-73.93059104631958,40.69451831689019)
radius = 32
hashtag = ['graffiti']
date = '01-01-2010'

photo_list = flickr_api.Photo.search(tags=hashtag, lat=lat_NYC, lon=lon_NYC, radius=32,has_geo=True,page=1,min_upload_date=date)

# Scrape the posts with tag graffiti in NYC area
for page_num in tqdm(range(2,photo_list.info.pages),position=0): # Will not execute if only 1 page in result
    photo_list += flickr_api.Photo.search(tags=hashtag, lat=lat_NYC, lon=lon_NYC, radius=32,has_geo=True,page=page_num,min_upload_date=date)

# Get the location for the scraped photos    
locations = []
for photo in tqdm(range(len(photo_list)),position=0):
    locations.append(flickr_api.Photo.getLocation(photo_list[photo]))
 
lat = []
long = []
photo_id = [] 
for i in tqdm(range(len(photo_list)),position=0):
    photo_id.append(int(photo_list[i].id))
    lat.append(locations[i].latitude)
    long.append(locations[i].longitude)   

final_data = list(zip(photo_id,lat,long))
with open('flickr_scraped_07_21.txt','w') as f:
    f.write('\n'.join('%s,%s' % x for x in final_data))