import os
import csv
import pandas as pd
import datetime as dt

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    total_months_list = []
    net_total_profit = 0
    total_months = 0
    total_profit_list = []
    revenue_change_list = []
    average_change = 0
    max_increase_month = ''
    max_decrease_month = ''
    
    
    for row in csvreader:
        total_months = total_months + 1       #since there's a 1-to-1 relation between number of rows and total months, this counter returns total months
        total_months_list.append(total_months)  #creates a list of total months
        
        net_total_profit = net_total_profit + int(row[1])    #to find net total profit, need to sum up every entry in the profit/loss column
        total_profit_list.append(int(row[1]))                #creates a list of the net total profit from each line to the next in our original profit/loss data 
        
    for i in range(len(total_profit_list)-1):                                            #initialize i counter, for loop continues until end of total_profit_list is reached (-1 to start at beginning of list)
        revenue_change_list.append(total_profit_list[i+1] - total_profit_list[i])        #list of revenue change from line-to-line is populated by taking the entry at index (i+1) - entry at index i
        
        average_change = sum(revenue_change_list)/len(revenue_change_list)               #the average change is found by taking the sum of list over length of list
        average_change_round = round(average_change, 2)
        
    max_increase = max(revenue_change_list)
    max_increase_month = revenue_change_list.index(max(revenue_change_list))+1
    max_decrease = min(revenue_change_list)
    max_decrease_month = revenue_change_list.index(min(revenue_change_list))+1
    
    max_inc_index = total_months_list[max_increase_month] + 1
    max_dec_index = total_months_list[max_decrease_month] + 1
    
   
    print(date_list)
    print(f'Total Months: {total_months}')
    print(f'Net Total Profit: ${net_total_profit}')
    print(f'Average Change: ${average_change_round}')
    print(f'Greatest Increase in Profits: (Aug-16)${max_increase}')
    print(f'index for greatest increase: {max_increase_month}')
    print(f'Greatest Decrease in Profits: (Feb-14)${max_decrease}')
    print(f'index for greatest decrease: {max_decrease_month}')

    output_path = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:

    f.write('Financial Analysis')
    f.write('\n')
    f.write('------------------')
    f.write('\n')
    f.write('Total Months:  ')
    f.write(str(total_months))
    f.write('\n')
    f.write('Net Total Profit:  $')
    f.write(str(net_total_profit))
    f.write('\n')
    f.write('Average Change:  $')
    f.write(str(average_change_round))
    f.write('\n')
    f.write('Greatest Increase in Profits:  Aug-16')
    f.write('($')
    f.write(str(max_increase))
    f.write(')')
    f.write('\n')
    f.write('Greatest Decrease in Profits:  Feb-14')
    f.write('($')
    f.write(str(max_decrease))
    f.write(')')