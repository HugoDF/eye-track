import json

f = open('data.json')
data = json.load(f)

# filter the data with none elements
data = [x for x in data if x['data'] is not None]

# define a hashmap
verticalSections = {
    'section1': [],
    'section2': [],
    'section3': [],
    'section4': []
}

section1Counter = 0
section2Counter = 0
section3Counter = 0
section4Counter = 0

print 'data format: ', data[0]
print 'total data points:', len(data)

for dataPoint in data:
    x = dataPoint['data']['x']
    y = dataPoint['data']['y']
    
    # print x, y
    # print dataPoint['data']

    if(x > 0 and x <=300):
        verticalSections['section1'].append((x, y))
        section1Counter += 1
    
    if(x > 300 and x <=600):
        verticalSections['section2'].append((x, y))
        section2Counter += 2

    if(x > 600 and x <=900):
        verticalSections['section3'].append((x, y))
        section3Counter += 3

    if(x > 900 and x <=1200):
        verticalSections['section4'].append((x, y))
        section4Counter += 4

    # print dataPoint['data']

print 'frequencies in vertical section 1, 2, 3, 4:', section1Counter, section2Counter, section3Counter, section4Counter

subsectionArray = []
sectionNumber = 1
for section in verticalSections:
    subsection1Counter = 0
    subsection2Counter = 0
    subsection3Counter = 0
    subsection4Counter = 0
    print '\nsection:', sectionNumber

    print 'total data points in section:', len(verticalSections[section])

    for dataPoint in verticalSections[section]:
        y = dataPoint[1]
        
        if(y > 0 and y <=250):
            subsection1Counter += 1

        if(y > 250 and y <=500):
            subsection2Counter += 1
    
        if(y > 500 and y <=750):
            subsection3Counter += 1

        if(y > 750 and y <=1000):
            subsection4Counter += 1

    subsectionArray.append(subsection1Counter)
    subsectionArray.append(subsection2Counter)
    subsectionArray.append(subsection3Counter)
    subsectionArray.append(subsection4Counter)
    print 'subsection 1 frequency:', subsection1Counter
    print 'subsection 2 frequency:', subsection2Counter
    print 'subsection 3 frequency:', subsection3Counter
    print 'subsection 4 frequency:', subsection4Counter
    sectionNumber += 1

print subsectionArray

# plotting
import numpy as np
import matplotlib.pyplot as plt
graph = plt.subplot(1,2,1)
graph.set_title("Frequencies of different sections")
graph.set_xlabel("Sections")
graph.set_ylabel("Frequencies")

graph2 = plt.subplot(1,2,2)
graph2.set_title("Frequencies of different sections")
graph2.set_xlabel("Sections")
graph2.set_ylabel("Frequencies")

graph.plot(np.arange(0, len(subsectionArray)), subsectionArray, 'x', color='r', markersize=10)
graph2.plot(np.arange(0, len(subsectionArray)), subsectionArray, color='r', markersize=10)
plt.show()
