# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas
import pandas as pd 

#url = "D:\geo\guijiang_final\guijiang_river_osm.shp"
url = "D:/geo/dongjiang/dongjiang_river_osm.shp"
df = geopandas.read_file(url)

df = df.reset_index()
kvDict = {}
for index, row in df.iterrows():
    first, last = row['geometry'].boundary
    entity = {'data':row,'next': None, 'last': None, 'lastPoint': last.wkt}
    kvDict[first.wkt] = entity


theFirstLineKey = ''

for key, val in kvDict.items():
    lastPoint = val['lastPoint']
    nextLine = kvDict.get(lastPoint,None)
    if nextLine is not None:
        val['next'] = nextLine
        nextLine['last'] = val

newList = []
iterator = None
index = 0
issueList = []
issue1List = []
for key, val in kvDict.items():
    lastLine = val['last']
    nextLine = val['next']
    if lastLine is None and nextLine is not None:
        val['data']['index'] = index
        val['data']['sort'] = index
        index  = index + 1
        newList.append(val['data'])
        iterator = val
        issueList.append(val)
        print('-----------------------')
        break
    elif lastLine is None or nextLine is None:
        issue1List.append(val)

while iterator['next'] is not None:
    iterator = iterator['next']
    iterator['data']['index'] = index
    iterator['data']['sort'] = index
    index = index + 1
    newList.append(iterator['data'])

#df2 = pd.DataFrame(newList)
df2 = geopandas.GeoDataFrame(newList)
df2.set_crs('EPSG:4326')
#df2.to_file("D:\geo\guijiang_final\guijiang_river_osm2.shp")
df2.to_file("D:/geo/dongjiang/dongjiang_river_osm_sorted.shp",encoding='utf-8')
