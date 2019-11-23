# CSV = common separated variable
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
#    print(readCSV)
    
    dates = []
    colors = []
        
    for row in readCSV:
        print(row)
       
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)
                
    print("____________________________________________")
    print(dates)
    print(colors)
     
    try:
        # implement as dictionary  
        whatColor = input('What Color do you wish to know the date of ?')
        
        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of ', whatColor, 'is ', theDate)
        else:
            print('color not found or isn\'t a color..')


    except Exception as e:
        print(e)
        
    print("continuing.......")




