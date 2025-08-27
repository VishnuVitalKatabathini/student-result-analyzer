import pandas as pd

#importing data from excel file below
xf=r"btech_jntu_resultsmodified\modifiedSS-5-I B.Tech. II Semester (R18) Regular 1.xlsx"
#taking it into dataframe
df=pd.read_excel(xf)
#printing the data frame
#print(df)
#taking the input from the userr
htno=input('enter hallticket no:')
#storing the specific data from the original dataframe to a temporary data frame
specificdata=df[df['HTNO']==htno]
#filtering the data we need and storing it onto another dataframe
#specificdata[1:]
print(specificdata.iloc[:,1:])
#results=specificdata[['SUBJECT_CODE', 'SUBJECT_NAME', 'INTERNALMARKS','EXTERNALMARKS', 'TOTALMARKS', 'GRADE', 'GRADE_POINTS', 'CREDITS']]
#here i have used two square barackets as like "[[]]" this indicate we are extracting the data of specific columns
#here in the above code line.
# We use the outer square brackets to indicate a subset of a DataFrame, and the inner square brackets to create a list.  
#printing the specific data we need
#print(results)
#calculating  total credits and cgpa
credits=specificdata.CREDITS
print('TOTAL CREDITS=',credits.aggregate("sum"))
gpa=specificdata.GRADE_POINTS
cgpa=gpa.aggregate("mean")
print('CGPA=',cgpa)
#print('student summary statistics overall performance:')
#print(results.describe(include=[int]).T)
#print('OVERALL STUDENTS PERFORMANCE:   ')
#print(df.describe(include=[int]).T)

