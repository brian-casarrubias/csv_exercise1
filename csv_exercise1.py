

import csv
'''
date,temperature(F)
Jan 1,27
Jan 2,31
Jan 3,23
Jan 4,34
Jan 5,37
Jan 6,38
Jan 7,29
Jan 8,30
Jan 9,35
Jan 10,30
'''
'''
  (a) What was the average temperature in first week of Jan

  (b) What was the maximum temperature in first 10 days of Jan

  Figure out data structure that is best for this problem
'''


def sort_it(lis):
    for x in range(len(lis)-1, -1, -1):
        
        for y in range(x):
            if lis[y] > lis[y+1]:
                lis[y], lis[y+1] = lis[y+1], lis[y]


with open ('nyc_weather.csv', 'r') as f:
    csv_reader = csv.reader(f)
    weather_week = []
    average_temp = 0


    next(csv_reader)

    for line in csv_reader:
        weather_week.append(line[1])
    
    weather_week = weather_week[0:7]
    
    
    # for index, element in enumerate(weather_week):
    #     average_temp+=int(weather_week[index])
    # average_temp = average_temp / len(weather_week)
    for element in weather_week:
        average_temp+=int(element)
    average_temp = average_temp / len(weather_week)
    
    print(f'Average Temperature Of First Week Of January: {average_temp:.2f}F')



with open('nyc_weather.csv', 'r') as f:
    csv_reader = csv.reader(f)

    weather_ten_day = []
    maximum_temp = 0

    next(csv_reader)
    for line in csv_reader:
        weather_ten_day.append(line[1])
        #could have used this easier, but wanted to do more code 
        #print(max(weather_ten_day))
    sort_it(weather_ten_day)
    maximum_temp = weather_ten_day[-1]
    print(f'Maximum Temperature In The First 10 Days Of January: {maximum_temp}F')
    

    


   