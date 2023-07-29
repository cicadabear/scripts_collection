# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:17:34 2023

@author: jack
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas
import pandas as pd 
import os
#from shapely.geometry import Point
#from shapely import from_wkb, from_wkt
from shapely.ops import split

#url = "D:\geo\guijiang_final\guijiang_river_osm.shp"
#url = "D:/geo/dongjiang/dongjiang_river_osm.shp"
#url = "D:/geo/eergunahe/hailaerhe_network_osm.shp"
url = "D:/geo/xiangjiang/yongminghe_river_osm.shp"

# start osm_id 674455140
# starting_osm_id = '674455140'
# #starting_osm_id = '674452643'
# #starting_osm_id = '160446870'
# #starting_osm_id = '160446872'
# ending_osm_id = '27803429'
starting_osm_id = '1176286049'
ending_osm_ids = ['143811852']
abnormal_osm_ids = []

df = geopandas.read_file(url)

df = df.reset_index()
kvDict = {}
for index, row in df.iterrows():
    osm_id = row['osm_id']
    if osm_id in abnormal_osm_ids:
        continue
    first, last = row['geometry'].boundary.geoms
    # next 下一段， last 上一段
    entity = {'data':row,'next': None, 'last': None, 'lastPointWkt': last.wkt, 
              'osm_id': row['osm_id'], 'lastPoint': last }
    kvDict[first.wkt] = entity


theFirstLineKey = ''

for key, val in kvDict.items():
    lastPointWkt = val['lastPointWkt']
    nextLine = kvDict.get(lastPointWkt,None)
    if nextLine is not None:
        val['next'] = nextLine
        nextLine['last'] = val

newDataFrame = []
iterator = None
index = 0
issueList = []
issue1List = []
sortedOsmIdList = []
for key, val in kvDict.items():
    lastLine = val['last']
    nextLine = val['next']
    #if lastLine is None and nextLine is not None:
    if starting_osm_id is not None and val['osm_id'] == starting_osm_id:
            val['data']['index'] = index
            val['data']['sort'] = index
            index  = index + 1
            newDataFrame.append(val['data'])
            iterator = val
            issueList.append(val)
            #print('----------------------- osm_id', val['osm_id'])
            break
    elif lastLine is None or nextLine is None:
        issue1List.append(val)

#处理下一段
while iterator is not None and iterator['next'] is not None:
    iterator = iterator['next']
    iterator['data']['index'] = index
    iterator['data']['sort'] = index
    index = index + 1
    newDataFrame.append(iterator['data'])
    sortedOsmIdList.append(iterator['osm_id'])
    
#如果有大量半段半段首位连不上的
while iterator['osm_id'] not in ending_osm_ids:
    print('-----------------lastPointWkt', iterator['lastPointWkt'])
    for key, val in kvDict.items():
        osm_id = val['osm_id']
        #print('osm_id-----test-----', osm_id)
        line = val['data']['geometry']
        if osm_id not in sortedOsmIdList and iterator['lastPoint'].within(line):
            print('----------------------- next osm_id', val['osm_id'])
            val['data']['geometry'] = split(line, iterator['lastPoint']).geoms[1]
            iterator['next'] = val
            break
    if iterator['next'] is None:
        print('----------------------error----------------- osm_id--', iterator['osm_id'])
        break
    # 处理下一段
    while iterator['next'] is not None:
        iterator = iterator['next']
        iterator['data']['index'] = index
        iterator['data']['sort'] = index
        index = index + 1
        newDataFrame.append(iterator['data'])
        sortedOsmIdList.append(iterator['osm_id'])
    

        
print('..............writing to file.................')
#df2 = pd.DataFrame(newDataFrame)
df2 = geopandas.GeoDataFrame(newDataFrame)
df2.set_crs('EPSG:4326')
#df2.to_file("D:\geo\guijiang_final\guijiang_river_osm2.shp")
#df2.to_file("D:/geo/dongjiang/dongjiang_river_osm_sorted.shp",encoding='utf-8')
df2.to_file(os.path.splitext(url)[0]+'_sorted.shp', encoding='utf-8')

