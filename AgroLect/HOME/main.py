import pandas
import statistics
crop_data=pandas.read_csv
data=pandas.read_csv("database.csv")
city=data['city'].to_list()
max_temp=list(map(int,data['max temperature'].to_list()))
min_temp=list(map(int,data['min temperature'].to_list()))
max_humid=list(map(int,data['max humidity'].to_list()))
min_humid=list(map(int,data['min humidity'].to_list()))
min_ph=list(map(int,data['min ph'].to_list()))
max_ph=list(map(int,data['max ph'].to_list()))
wheat_humidity=75
wheat_ph=9
avg_humi={}
avg_humidity=[]
for i in range(27):
    avg_humi[city[i]]=max_humid[i]+min_humid[i]/2
    avg_humidity.append(max_humid[i]+min_humid[i]/2)
mn=statistics.mean(avg_humidity)
dev=statistics.stdev(avg_humidity,mn)
for i in avg_humi:
    if avg_humi[i]>=wheat_humidity-(0.5*dev) and avg_humi[i]<=wheat_humidity+(0.5*dev):
        print(i,'A')
    elif avg_humi[i]>=wheat_humidity-(1*dev) and avg_humi[i]<=wheat_humidity-(0.5*dev) or avg_humi[i]>=wheat_humidity+(1*dev) and avg_humi[i]<=wheat_humidity+(0.5*dev):
        print(i,'B')
    elif avg_humi[i]>=wheat_humidity+(1*dev) and avg_humi[i]<=wheat_humidity+(1.5*dev) or avg_humi[i]>=wheat_humidity-(1*dev) and avg_humi[i]<=wheat_humidity-(1.5*dev):
        print(i,'C')
    elif avg_humi[i]<=wheat_humidity+(1.5*dev) or avg_humi[i]<=wheat_humidity-(1.5*dev):
        print(i,'D')
print("ph Data")
avg_phs={}
avg_ph=[]
for i in range(27):
    avg_phs[city[i]]=max_ph[i]+min_ph[i]/2
    avg_ph.append(max_ph[i]+min_ph[i]/2)
mn_ph=statistics.mean(avg_ph)
dev_ph=statistics.stdev(avg_ph,mn_ph)
for i in avg_phs:
    if avg_phs[i]>=wheat_ph-(0.5*dev_ph) and avg_phs[i]<=wheat_ph+(0.5*dev_ph):
        print(i,'A')
    elif avg_phs[i]>=wheat_ph-(1*dev_ph) and avg_phs[i]<=wheat_ph-(0.5*dev_ph) or avg_phs[i]>=wheat_ph+(1*dev_ph) and avg_phs[i]<=wheat_ph+(0.5*dev_ph):
        print(i,'B')
    elif avg_phs[i]>=wheat_ph+(1*dev_ph) and avg_phs[i]<=wheat_ph+(1.5*dev_ph) or avg_phs[i]>=wheat_ph-(1*dev_ph) and avg_phs[i]<=wheat_ph-(1.5*dev_ph):
        print(i,'C')
    elif avg_phs[i]<=wheat_ph+(1.5*dev_ph) or avg_phs[i]<=wheat_ph-(1.5*dev_ph):
        print(i,'D')
