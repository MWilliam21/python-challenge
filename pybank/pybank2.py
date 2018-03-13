import os 
import csv
import glob
totalmonth = 0
totalrevenue = 0
RevenueChange = []
date=[]

def mean(numbers):
   return float(sum(numbers)) / max(len(numbers), 1)
list_of_files=glob.glob('raw_data/*csv')

for file_name in list_of_files:


    with open(file_name, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader, None)

        for row in csvreader:
            date.append(row[0])
            totalmonth = totalmonth + 1
            totalrevenue = totalrevenue + int(row[1])

            if (totalmonth == 1):
                PrRev = int(row[1])
            else:
                Change = (int(row[1]) - int(PrRev))
                RevenueChange.append(Change)
                
            

            PrRev = row[1]
            
        maximum=max(RevenueChange)
        minimum=min(RevenueChange)
        maximum_index=RevenueChange.index(maximum)
        minimum_index=RevenueChange.index(minimum)
        month_max=date[maximum_index +1]
        month_min=date[minimum_index +1]
        print("Total months = " + str(totalmonth))
        print("Total Revenue = "+str(totalrevenue))
        print ("Average Revenue Change = " +str(mean(RevenueChange)))
        print ("Greatest Increase in Revenue =" + month_min + "(" +str(minimum)+ ")")
        print ("Greatest Decrease in Revenue =" + month_max + "(" +str(maximum)+")")
    
    with open(os.path.join('',os.path.basename(file_name)), 'w',) as textFile:
   
        textFile.write("Total months = "+ str(totalmonth))
        textFile.write("\n" + "Total Revenue = "+str(totalrevenue))
        textFile.write("\n"+ "Average Revenue Change = " +str(mean(RevenueChange)))
        textFile.write("\n"+ "Greatest Increase in Revenue =" + month_min + "(" +str(minimum)+ ")")
        textFile.write("\n"+ "Greatest Decrease in Revenue =" + month_max + "(" +str(maximum)+")")
