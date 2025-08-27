import pandas as panda

sem1_1_file=r"btech_jntu_resultsmodified\modifiedSS-5-II B.Tech. I Semester (R18) Regular.xlsx"
sem1_2_file=r"btech_jntu_resultsmodified\modifiedSS-5-II B.Tech. II Semester (R18) Regular.xlsx"

#importing the excel files into the dataframe

gpa={}
yr1_1=panda.read_excel(sem1_1_file)
yr1_2=panda.read_excel(sem1_2_file)
htno=list(yr1_1.HTNO)
temp1_1=yr1_1.copy()
# print(temp1_1)
def semester1_1():
    for i in htno:
        studentdata1_1=yr1_1[yr1_1["HTNO"]==i]
        std1_1=studentdata1_1.iloc[:,1:]
        # print()
        # print("HTNO : ",htno)
        # print()
        # print("year:1 semester : 1 ")
        # print(std1_1)
        # print()
        student_results(i,std1_1)

def gradecheck(grade,stdr):
    x=''
    subject=list(stdr.SUBJECT_NAME)
    for i in range(len(grade)):
            if((grade[i]=="F") or (grade[i]=="Ab")):
                backlogs.append(subject[i])
                x=grade[i]
    return x
    


cgpa=[]
#calculating sgpa of the student
def student_results(htno,stdr):
    credits=list(stdr.CREDITS)
    grade_points=list(stdr.GRADE_POINTS)
    grade=list(stdr.GRADE)
    gradeval=gradecheck(grade,stdr)
    if gradeval=="F":
        # print("SGPA : ")
        calculating_cgpa(gradeval)
    else:   
        sumcg=[]
        for i in range(len(credits)):
            sumcg.append(credits[i]*grade_points[i])

        sgpa=sum(sumcg)/sum(credits)
        gpa[htno]=round(sgpa,2)
        calculating_cgpa(round(sgpa,2))

        # print("SGPA : ",round(sgpa,2))


#storing all sgpa into the list
def calculating_cgpa(sgpa):
    cgpa.append(sgpa)

backlogs=[]  
def topperlist():
    #creating the topper list
    p=list(gpa.values())
    p.sort(reverse=True)
    #top 10 topper list
    toppers={}
    for i in p:
        for key in gpa:
            if gpa[key]==i:
                toppers[key]=gpa[key]

    for i,key in zip(range(10),toppers):
        print(key,':',toppers[key])

semester1_1()
topperlist()

    





    