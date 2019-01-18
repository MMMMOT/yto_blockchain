import requests 
from pprint import pprint 
from urllib import parse
 

#http请求中的url如果带有特殊字符时，需要转码。如此处，加号+应改为%2B

#r = requests.get("http://112.65.156.58:9000/v2/odata/devices?$filter=devNumber eq 'xwfwz2'") 
#r = requests.get("http://112.65.156.58:9000/v2/odata/datapoints?$filter=DeviceNumber eq '000000004' and SensorTypeNum eq 20402&$orderby=dpCreationTime desc&$top=1") 
#r = requests.get("http://112.65.156.58:9000/v2/odata/datapoints?$filter=DeviceNumber eq '000000004' and SensorTypeNum eq 20402&$orderby=dpCreationTime desc") 
#r = requests.get("http://112.65.156.58:9000/v2/odata/datapoints?$filter=DeviceNumber eq '000000004' and dpCreationTime gt 2018-11-29T18:13:20%2B08:00") 
r = requests.get("http://112.65.156.58:9000/v2/odata/datapoints?$filter=DeviceNumber eq '000000004' and dpCreationTime gt 2018-12-31T17:46:50%2B08:00&$orderby=dpCreationTime desc")
#rjs = r.json() 
#rlist = rjs['value']
#rdict = rlist[1]
#print(rdict)
#print(rdict['ID'])
#print(type(rlist[0]))
#print(rjs['value'])
#print(type(r.json()))
pprint(r.json())  
#print(type(rjs))