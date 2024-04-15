import pymssql
import pandas as pd 


def max(num1 , num2 ):
    if ( num1 > num2 ):
        print(f"{num1} > {num2}")
    elif( num2 > num1):
        print(f"{num2} > {num1}")
    else:
        print(f"{num1} equal {num2}")
        

def readDb():

    conn = pymssql.connect(
    server='192.168.12.244',
    user='sa',
    password='sa',
    database='wen_test'
    )  
       
    SQL_QUERY = "select top 2 * from wen_test.dbo.Datalog_ITEM_STATS2 ; "

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    

    records = cursor.fetchall()
    for r in records:
        print(f"{r}\n")


def writeDb():

    conn = pymssql.connect(
    server='192.168.12.244',
    user='sa',
    password='sa',
    database='wen_test'
    )    

    sqlInsert = "insert into wen_test.dbo.wen_test ( var1 ) values ( %s );"

    cursor = conn.cursor()
    cursor.execute(sqlInsert , ("aa") )


    cursor.close()
    conn.commit()

    conn.close()
    





#testCsv = pd.read_csv("D:\\temp\\iloop_on0X80_slop_comp0XA0_comp_R0x70_comp_C and CC0XEC.CSV" , ).dropna(how='all').sort_values(" Frequency (Hz)" , ascending=False)


#for data in testCsv:
#    print(f'{data}')


#print(f'{testCsv.columns[0]}')

#mydata = list(testCsv.loc[:, testCsv.columns[0] ]) ; 


#for val in mydata:
#    print(f'{val}')



#temp = 0

#for i , val in testCsv.iterrows():
#    temp = val[testCsv.columns[0]]  + 1 

#    print(f'{temp}') 
    #print(f'{val[testCsv.columns[0]]} , {val[testCsv.columns[1]]} , {val[testCsv.columns[2]]} , {val[testCsv.columns[3]]} , {val[testCsv.columns[4]]}')

