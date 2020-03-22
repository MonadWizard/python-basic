import csv


# read csv
with open('example.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
#    print(csv_reader,"\n\n\n")
    
#    next(csv_reader)   # read after first execute line
    
#    for line in csv_reader:   #all column
#        print("total line : ",line, "\t column 3 :", line[2])

    
# write csv as duplicate
    with open('new_duplicate.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t') # use \t for tabs replace by , on separate string
        
        for line in csv_reader:
            csv_writer.writerow(line)
        
        
        
        
        
        