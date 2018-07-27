from pprint import pprint
city = raw_input('Enter your City: ')
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=6fa65e51dd396\                                                                                                                          
502e0229bc41b57003d'.format(city)
humidity = 0
humidity2 = 0
humidity3 = 0
humidity4 = 0
windspeed = 0
humidity_twice = True
humidity_list = []
res = requests.get(url)
data = str(res.json())
strform = data.strip('{').rstrip('}')
listform = strform.split(" u'")
temp = listform[26].split(': ')
temp2 = temp[1].replace(',','')
temp3 = float(temp2)
temp4 = temp3 - 273
temp5 = int(temp4 * 1.8 + 32)
country = listform[5]
condition = listform[12]
description = listform[17]
if len(listform) == 32:
    humidity = listform[27]
    windspeed = listform[29]
elif len(listform) == 33:
    humidity = listform[28]
    windspeed = listform[30]
else:
    humidity = listform[27]
    windspeed = listform[29]

humidity4 = humidity
display = [country, condition, description, windspeed]
for x in range(len(display)):
    display[x] = display[x].replace('[','').replace(']','')
for z in range(len(display)):
    display[x] = display[x].replace("'",'')
for y in range(len(display)):
    if y == 2:
        print display[2].replace('}','')
    elif y == 3:
        print display[3].replace('{','').replace("u",'').replace(':','')
    elif y == 0:
        print 'Country: ', display[0]
    else:
        print display[y]
if humidity_twice == True:
    humidity4 = humidity4.replace('}','')
    print  humidity4
else:
    print 'humidity: ', humidity4
print 'temp: ',  temp5