import mysql.connector
from datetime import datetime,date,timedelta

import model.ResponseGeneralObject
import model.Years
import model.Data
from model.KpiComposition import KpiComposition
from model.Days import Days
from model.Months import Months
from model.Years import Years
from model.Data import Data
from model.ResponseGeneralObject import ResponseGeneralObject
from utils.Notifications import send_push_notification
from utils.bashLinuxOperations import execute_shell_to_commit_push_jsonkpifile


print("__name__ value: ", __name__)

#Initialize main response objects DTO'S
kpi_global=KpiComposition(hist_EjecEther=0,hist_EjecHost=0,hist_kpiEstimado=0,hist_kpiReal=0)
kpi_core=KpiComposition(hist_EjecEther=0,hist_EjecHost=0,hist_kpiEstimado=0,hist_kpiReal=0)
kpi_online=KpiComposition(hist_EjecEther=0,hist_EjecHost=0,hist_kpiEstimado=0,hist_kpiReal=0)
days=Days(date="",kpi_global=kpi_global,kpi_core=kpi_core,kpi_online=kpi_online)

month=Months([days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days])
#MonthCopy created to work the value of variables by assignation, not by reference
monthCopy2022=Months([days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days])
monthCopy2023=Months([days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days])
monthCopy2024=Months([days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days],[days])

year=Years(0,month)
years = []
yearsCopy=[] 
responseGeneralObject = ResponseGeneralObject



def connectionDB():
    print("Connecting with Database")
    mydb = mysql.connector.connect(
        host="devosfernando.com",
        port="9999",  
        user="lra",
        password="ARQ2023LRA",
        database="planbackend"
    )
    print(mydb)
    return mydb

def calculateDateFromGetData():
   today = date.today()    
   year=today.isoformat()[0:4]
   month=today.isoformat()[5:7]
   day=today.isoformat()[8:10]

   year= int(year)
   month=int(month)
   day = int(day)
   
   year = year - 1
   while month > 1:
       month=month-1
   while day > 1:
       day=day-1
   year = str(year)
   month = "0"+str(month)
   day = "0"+str(day)
   
   dateToQuery=year+"-"+month+"-"+day
   print("Finalized to retrieve date from last year to get data "+ dateToQuery)
   return dateToQuery
   


def getAndProcessData(databaseconnection):
    
    #Calculate date from 1st january on last year
    dateToQuery = calculateDateFromGetData()
    
    #print(date.today().isoformat()   )
    # Primary data to get all values from dataset history table and segment the information on lists
    mycursor = databaseconnection.cursor()
    sql="SELECT * FROM history WHERE hist_date BETWEEN "+"'"+dateToQuery+"'" +" AND "+"'"+date.today().isoformat()+"'"  
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    dateList=[]
    hist_EjecEtherList=[]
    hist_EjecEtherHostList=[]
    hist_kpiEstimadoList=[]
    hist_kpiRealList=[]
    

    print("Starting conversion of response to Object KPI To front app")
    for x in myresult:
        dateList.append(x[0].strftime("%m/%d/%Y"))
        hist_EjecEtherList.append(x[1])
        hist_EjecEtherHostList.append(x[2])
        hist_kpiEstimadoList.append(x[3])
        hist_kpiRealList.append(x[4])
        jsonStandardObj(iterationRow=x)



def jsonStandardObj(iterationRow):
   
    kpiCompositionGlobal = KpiComposition(hist_EjecEther=0,hist_EjecHost=0,hist_kpiEstimado=0.0,hist_kpiReal=0.0)
    kpiCompositionCore = KpiComposition(hist_EjecEther=0,hist_EjecHost=0,hist_kpiEstimado=0.0,hist_kpiReal=0.0)
    kpiCompositionOnline= KpiComposition(iterationRow[1],iterationRow[2],iterationRow[3],iterationRow[4])
    day = Days(iterationRow[0].strftime("%m/%d/%Y")
                            ,  # Default value for KPI Core
                               kpiCompositionGlobal 
                            , # Default value for KPI Global
                               kpiCompositionCore 
                            , 
                               kpiCompositionOnline)
   
    if day.date[0:2] == '01':
        month.enero.append(day)
    elif day.date[0:2] == '02':
        month.febrero.append(day)
    elif day.date[0:2] == '03':
        month.marzo.append(day)
    elif day.date[0:2] == '04':
        month.abril.append(day)
    elif day.date[0:2] == '05':
        month.mayo.append(day)
    elif day.date[0:2] == '06':
        month.junio.append(day)
    elif day.date[0:2] == '07':
        month.julio.append(day)
    elif day.date[0:2] == '08':
        month.agosto.append(day)
    elif day.date[0:2] == '09':
        month.septiembre.append(day)
    elif day.date[0:2] == '10':
        month.octubre.append(day)
    elif day.date[0:2] == '11':
        month.noviembre.append(day)
    elif day.date[0:2] == '12':
        month.diciembre.append(day)
    
    #Limit to add information on inmediate last recent day 
    today = date.today()    
    y=today.isoformat()[0:4]
    m=today.isoformat()[5:7]
    d=today.isoformat()[8:10]

    y=int(y)
    m=int(m)
    if d == "01":
     this_first = date.today().replace(day=1)
     global prev_last_daymonth
     prev_last_daymonth = this_first - timedelta(days=1)
     prev_last_daymonth= prev_last_daymonth.strftime("%m/%d/%Y")
    else: 
     if d>="11":
        d = int(d)-1
     else:
        d = int(d)-1
        d = "0"+str(d)

    y=str(y)
    m="0"+str(m)
    d = str(d)
    if d == "01":
        dateToCompare=prev_last_daymonth
    else:
        dateToCompare=m+"/"+d+"/"+y
            
    if day.date == '12/31/2023':
        monthsCopy2023=createCopyObjMonthsPerYear(day.date[6:])
        year = Years(day.date[6:11],monthsCopy2023)
        years.append(year)
        global yearsCopy
        yearsCopy=years.copy()
        clearMonthListValues()     
    elif day.date ==  dateToCompare:
        monthsCopy2024=createCopyObjMonthsPerYear(day.date[6:])
        year = Years(day.date[6:11],monthsCopy2024)
        yearsCopy.append(year)
        data = Data(yearsCopy)
        global responseGeneralObject
        responseGeneralObject = ResponseGeneralObject(200, "OK",data)

def clearMonthListValues():
    month.enero.clear()
    month.febrero.clear()
    month.marzo.clear()
    month.abril.clear()
    month.mayo.clear()
    month.junio.clear()
    month.julio.clear()
    month.agosto.clear()
    month.septiembre.clear()
    month.octubre.clear()
    month.noviembre.clear()
    month.diciembre.clear()



def createCopyObjMonthsPerYear(year):
    if year == '2022':
        monthCopy2022.enero=month.enero.copy()
        monthCopy2022.febrero=month.febrero.copy()
        monthCopy2022.marzo=month.marzo.copy()
        monthCopy2022.abril=month.abril.copy()
        monthCopy2022.mayo=month.mayo.copy()
        monthCopy2022.junio=month.junio.copy()
        monthCopy2022.julio=month.julio.copy()
        monthCopy2022.agosto=month.agosto.copy()
        monthCopy2022.septiembre=month.septiembre.copy()
        monthCopy2022.octubre=month.octubre.copy()
        monthCopy2022.noviembre=month.noviembre.copy()
        monthCopy2022.diciembre=month.diciembre.copy()
        return monthCopy2022
    elif year=='2023':
        monthCopy2023.enero=month.enero.copy()
        monthCopy2023.febrero=month.febrero.copy()
        monthCopy2023.marzo=month.marzo.copy()
        monthCopy2023.abril=month.abril.copy()
        monthCopy2023.mayo=month.mayo.copy()
        monthCopy2023.junio=month.junio.copy()
        monthCopy2023.julio=month.julio.copy()
        monthCopy2023.agosto=month.agosto.copy()
        monthCopy2023.septiembre=month.septiembre.copy()
        monthCopy2023.octubre=month.octubre.copy()
        monthCopy2023.noviembre=month.noviembre.copy()
        monthCopy2023.diciembre=month.diciembre.copy()  
        return monthCopy2023
    elif year=='2024':
        monthCopy2024.enero=month.enero.copy()
        monthCopy2024.febrero=month.febrero.copy()
        monthCopy2024.marzo=month.marzo.copy()
        monthCopy2024.abril=month.abril.copy()
        monthCopy2024.mayo=month.mayo.copy()
        monthCopy2024.junio=month.junio.copy()
        monthCopy2024.julio=month.julio.copy()
        monthCopy2024.agosto=month.agosto.copy()
        monthCopy2024.septiembre=month.septiembre.copy()
        monthCopy2024.octubre=month.octubre.copy()
        monthCopy2024.noviembre=month.noviembre.copy()
        monthCopy2024.diciembre=month.diciembre.copy()  
        return monthCopy2024

def main():
    print("Start process to get data from history database Master")
    mydb=connectionDB()
    try:
        getAndProcessData(databaseconnection=mydb)
        write_out_put_file()
        execute_shell_to_commit_push_jsonkpifile();
        sendNotification()
        print("Proceso terminado satisfactoriamente")
    except Exception as e:
        print("Fallo en el proceso de extracción, transformación y cargue de tabla History", e )    
   
def write_out_put_file():
    f = open("dataKPIGeneralProd.json","w+")
    f.write(responseGeneralObject.toJSON())
    f.close()

def sendNotification():
    try:
        print("Enviando notificaciones a todos los usuarios ...")
        send_push_notification()
        print("Notificaciones enviadas")
    except Exception as e:
        print("Fallo enviando las notificaciones a todos los usuarios", e)



if __name__ == '__main__':
    main()

