import pandas as panda

sem1_1_file=r"btech_jntu_resultsmodified\modified-SS-5-I B.Tech. I Semester (R18) Regular.xlsx"
sem1_2_file=r"btech_jntu_resultsmodified\modifiedSS-5-I B.Tech. II Semester (R18) Regular 1.xlsx"
sem2_1_file=r"btech_jntu_resultsmodified\modifiedSS-5-II B.Tech. I Semester (R18) Regular.xlsx"
sem2_2_file=r"btech_jntu_resultsmodified\modifiedSS-5-II B.Tech. II Semester (R18) Regular.xlsx"
sem3_1_file=r"btech_jntu_resultsmodified\modifedSS-5-III B.Tech. I Semester (R18) Regular.xlsx"
sem3_2_file=r"btech_jntu_resultsmodified\modifedSS-5-III B.Tech. II Semester (R18) Regular.xlsx"
sem4_1_file=r"btech_jntu_resultsmodified\modifiedSS-5-IV B.Tech. I Semester (R18) Regular 2.xlsx"
sem4_2_file=r"btech_jntu_resultsmodified\modifiedSS-5-IV B.Tech. II Semester (R18) Regular.xlsx"
#importing the excel files into the dataframe


yr1_1=panda.read_excel(sem1_1_file)
yr1_2=panda.read_excel(sem1_2_file)
yr2_1=panda.read_excel(sem2_1_file)
yr2_2=panda.read_excel(sem2_2_file)
yr3_1=panda.read_excel(sem3_1_file)
yr3_2=panda.read_excel(sem3_2_file)
yr4_1=panda.read_excel(sem4_1_file)
yr4_2=panda.read_excel(sem4_2_file)



htno=input("enter hall ticket number : ")
cgpa=[] #storing all the sgpa in to saperate list 
backlogs=[]#storing the backlogs of the student 
#all students semester's info 
def semester1_1(htno):
    studentdata1_1=yr1_1[yr1_1["HTNO"]==htno]
    std1_1=studentdata1_1.iloc[:,1:]
    print()
    print("HTNO : ",htno)
    print()
    print("year:1 semester : 1 ")
    print(std1_1)
    print()
    student_results(std1_1)
    

def semester1_2(htno):
    studentdata1_2=yr1_2[yr1_2["HTNO"]==htno]
    std1_2=studentdata1_2.iloc[:,1:]
    print()
    print("year : 1  semester : 2  ")
    print()
    print(std1_2)
    print()
    student_results(std1_2)


def semester2_1(htno):
    studentdata2_1=yr2_1[yr2_1['HTNO']==htno]
    std2_1=studentdata2_1.iloc[:,1:]
    print()
    print("year : 2  semester : 1 ")
    print()
    print(std2_1)
    print()
    student_results(std2_1)
    
def semester2_2(htno):
    studentdata2_2=yr2_2[yr2_2["HTNO"]==htno]
    std2_2=studentdata2_2.iloc[:,1:]
    print()
    print("year : 2 semester : 2")
    print()
    print(std2_2)
    print()
    student_results(std2_2)

def semester3_1(htno):
    studentdata3_1=yr3_1[yr3_1["HTNO"]==htno]
    std3_1=studentdata3_1.iloc[:,1:]
    print()
    print("year : 3 semester : 1")
    print()
    print(std3_1)
    print()
    student_results(std3_1)

def semester3_2(htno):
    studentdata3_2=yr3_2[yr3_2["HTNO"]==htno]
    std3_2=studentdata3_2.iloc[:,1:]
    print()
    print("year : 3 semester : 2")
    print()
    print(std3_2)
    print()
    student_results(std3_2)

def semester4_1(htno):
    studentdata4_1=yr4_1[yr4_1["HTNO"]==htno]
    std4_1=studentdata4_1.iloc[:,1:]
    print()
    print("year : 4 semester : 1")
    print()
    print(std4_1)
    print()
    student_results(std4_1)

def semester4_2(htno):
    studentdata4_2=yr4_2[yr4_2["HTNO"]==htno]
    std4_2=studentdata4_2.iloc[:,1:]
    print()
    print("year : 4 semester : 2")
    print()
    print(std4_2)
    print()
    student_results(std4_2)
    
#checking the grade of th student
def gradecheck(grade,stdr):
    x=''
    subject=list(stdr.SUBJECT_NAME)
    for i in range(len(grade)):
            if((grade[i]=="F") or (grade[i]=="Ab")):
                backlogs.append(subject[i])
                x=grade[i]
    return x
    



#calculating sgpa of the student
def student_results(stdr):
    credits=list(stdr.CREDITS)
    grade_points=list(stdr.GRADE_POINTS)
    grade=list(stdr.GRADE)
    gradeval=gradecheck(grade,stdr)
    if gradeval=="F":
        print("SGPA : ")
        calculating_cgpa(gradeval)
    else:   
        sumcg=[]
        for i in range(len(credits)):
            sumcg.append(credits[i]*grade_points[i])

        sgpa=sum(sumcg)/sum(credits)

        calculating_cgpa(round(sgpa,2))

        print("SGPA : ",round(sgpa,2))


#storing all sgpa into the list
def calculating_cgpa(sgpa):
    cgpa.append(sgpa)


#calculating cgpa of the student
def student_result(cgpa):
    backlog=0
    for i in range(len(cgpa)):
        if(cgpa[i]=="F"):
            backlog=backlog+1
    if(backlog>0):
        print("Total black logs :",backlog)
        print(backlogs)
    else:
        total=sum(cgpa)/len(cgpa)            
        print("CGPA :",round(total,2))
        
           

def consolidate_results(htno):
    try :

         semester1_1(htno)
         semester1_2(htno)
    except:
        print("later entries : ")
    semester2_1(htno)
    semester2_2(htno)
    semester3_1(htno)
    semester3_2(htno)
    semester4_1(htno)
    semester4_2(htno)
    student_result(cgpa)


consolidate_results(htno)




