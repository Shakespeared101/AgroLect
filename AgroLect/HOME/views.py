from multiprocessing import connection
from sqlite3 import Cursor
from django.shortcuts import render
from django.db import connection
from . import CORE
# Create your views here.


G=0
li,li1=[],[] #country and cities list


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")

def home(request):
    global li,li1
    '''
    cursor=connection.cursor()
    cursor.execute('Select Crop_name from home_crop where max_ph > 50')
    Li=cursor.fetchall()
    print(Li)
    '''
    cursor=connection.cursor()
    if request.method =="POST":
        if 'CNT1' in request.POST:
            print("YESSn\n\n\n")
            continent=request.POST['CNT1']
            print(continent)
            cursor.execute("select Distinct country from home_map where Regionname= '"+continent+"'")
            li=[i[0] for i in list(cursor.fetchall())]
            G=1
            print(G)
            return render(request,"home.html",{'li':li})
        
        if 'countries' in request.POST:
            country= request.POST['countries']
            print("YESSn\n\n\n")
            cursor.execute("select Distinct cities from home_map where country= '"+country+"'")
            li1=[i[0] for i in list(cursor.fetchall())]
            print(li1)
            return render(request,"home.html",{'li1':li1,'li':li})
        
        if 'cities' in request.POST:
            cities= request.POST['cities']
            print("YESSn\n\n\n")
            cursor.execute("select * from home_location where location='"+cities+"'")
            temp=list(cursor.fetchall())
            city=list(map(str,[temp[0][i] for i in range(1,len(temp[0]))]))
            print(city)
            cursor.execute("Select * from home_crop where avg_humidity between "+city[2]+" and "+city[1]+" and avg_ph between "+city[5]+" and "+city[3]+" and avg_temp between "+city[6]+" and "+city[4]+"")
            Crop_list=[i for i in list(cursor.fetchall())]
            print(Crop_list)
            Cro,Score=CORE.BESTU_BESTU(Crop_list,city)
            Score=[round(i,2) for i in Score]
            Crop_details=[]
            for i in range(0,len(Cro)):
                cursor.execute("Select * from home_crop where Crop_name= '"+Cro[i]+"'")
                temp2=list(cursor.fetchall())
                Crop_details.append([temp2[0][i] for i in range(2,len(temp2[0]))])
            print(Crop_details)
            mylist=zip(Cro,Score,[i for i in range(1,len(Cro)+1)],Crop_details)
            context={ 'li': li,'li1':li1,
                'mylist':mylist
            }            
            return render(request,"home.html",context)
    Crop_list_Name=[1,2,3,4]
    Score=[5,6,7,8]
    return render(request, "home.html",{'name':Crop_list_Name,'score':Score})

