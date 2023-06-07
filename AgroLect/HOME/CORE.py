from statistics import mean,stdev

def BESTU_BESTU(Crop_list,city):
    crop_name,avg_humidity=[i[1] for i in Crop_list],[i[2] for i in Crop_list]
    print("okokoko",avg_humidity)
    avg_ph,avg_temp=[i[3] for i in Crop_list],[i[4] for i in Crop_list]
    grade={'A':10,'B':9,'C':8,'D':7,'E':6,'F':5,'N':0}
    credits={'H':3,'T':4,'PH':2,'P':1}
    C_gpa={}
    print(Crop_list)
    
    temp=['avg_humidity','avg_ph','avg_temp']
    print("crop",Crop_list)
    for i in range(len(Crop_list)):
        grade_D=[1,2,3]
        for j in range(0,len(temp)):
            print("ok",eval(temp[j]),temp[j])
            m,sd=mean(eval(temp[j])),stdev(eval(temp[j]))
            if eval(temp[j])[i]>=(m+1.5*sd):
                grade_D[j]='A'
            elif eval(temp[j])[i]>=(m+1*sd):
                grade_D[j]='B'
            elif eval(temp[j])[i]>=(m+0.5*sd):
                grade_D[j]='C'
            elif eval(temp[j])[i]>=(m-0.5*sd):
                grade_D[j]='D'
            elif eval(temp[j])[i]>=(m-1*sd):
                print(i,"\n\n")
                grade_D[j]='E'
            elif eval(temp[j])[i]>=(m-1.5*sd):
                grade_D[j]='F'
            else:
                grade_D[j]='N'
        print(grade_D)
        gpa=(grade[grade_D[0]]*credits['H']+grade[grade_D[2]]*credits['T']+grade[grade_D[1]]*credits['PH'])/9
        C_gpa[crop_name[i]]=gpa
    name,grade=[],[]
    for i in sorted(C_gpa.values()):
        for j in C_gpa:
            if C_gpa[j]==i:
                name.append(j)
                grade.append(i)
    grade.reverse()
    name.reverse()
    print("NAME\n",name,"Grade\n",grade)
    return [name,grade]

