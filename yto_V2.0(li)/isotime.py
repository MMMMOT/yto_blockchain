import datetime as date

timestr = '2018-11-09T17:46:50.3021997+08:00'


def iso8601ToNormal(isostr):
    timelist = list(isostr)
    dotindex = timelist.index('.')
    normalstr = "".join(timelist[:dotindex])
    return normalstr

#print(iso8601ToNormal(timestr))
#tstr = iso8601ToNormal(timestr)

#date = datetime.datetime.strptime(tstr,'%Y-%m-%dT%H:%M:%S')
#print(type(date))

date = date.datetime.strptime('2018-11-08T17:46:50','%Y-%m-%dT%H:%M:%S')
print(date)