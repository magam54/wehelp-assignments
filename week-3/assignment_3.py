coding:"utf-8"
import urllib.request as req
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response :
    data = response.read().decode("utf-8")
import json
data = json.loads(data)
import re
x = len(data["result"]["results"])
y =  0
with open("data.csv",mode="w", encoding="utf-8") as file:
    while y<x :
        title = (data["result"]["results"][y]["stitle"])
        location = (data["result"]["results"][y]["address"]) #要怎麼只取三個字
        pattern = re.compile(r"..區")
        location1 = pattern.search(location)
        location2 = location1.group()
        longitude = (data["result"]["results"][y]["longitude"])
        latitude = (data["result"]["results"][y]["latitude"])
        image = (data["result"]["results"][y]["file"]) #要怎麼只取第一張圖
        patternlocate = re.split(r".jpg|.JPG",image)
        image1 = patternlocate[0]+".jpg"
        line = str(title+","+location2+","+longitude+","+latitude+","+image1)
        y+=1
        file.write(line+"\n")