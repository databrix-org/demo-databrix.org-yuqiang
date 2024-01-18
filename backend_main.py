from fastapi import FastAPI , File, UploadFile
import pandas as pd
import MySQLdb
from pydantic import BaseModel

# Create instance
app = FastAPI()

# Define a class
# posted Data in this API shouöd use this format
class sql_code(BaseModel):
    code: str
    description: str | None = None

# Send the data back to front, if front user sends get request
# If user choose database in sidebar of homepage, send the data back
@app.get("/database")
async def read_database():
    table_list = 'fail to get df'
    
    # connect to SQL database of sales project
    mydb = MySQLdb.connect(host="localhost",
                           user="root",
                           password="Databrix-2024",
                           db = 'sales_data')
    cursor = mydb.cursor()
    
    # list all tables in the database
    cursor.execute("SHOW TABLES")
    tables_name = cursor.fetchall()
    
    # get all table names in a list
    tables_name = [i[0] for i in tables_name]
    table_list = []
    
    # Store all the tables in a list
    try:
        for i,j in enumerate(tables_name):
            
            # store table body (data) in the list
            query = 'select * from '+ j
            cursor.execute(query)
            table = cursor.fetchall()
            table_list.append(table)
            
            # store table column_name in tha list
            query2 = 'SHOW COLUMNS FROM '+ j
            cursor.execute(query2)
            columns = cursor.fetchall()
            columns = [n[0] for n in columns]
            tables_name[i] = (tables_name[i],columns)
    except:
        table_list = 'fail to get df'
    
    # return the tablelist with table body and table colmn_name
    # return the table name
    # send them to front
    return table_list, tables_name


# Get the posted input(SQL Code) from front.
# Sent the required data back to front
@app.post("/sql_query/")
async def sql_query(sql: sql_code):

    try:
        # connect to salse database
        mydb = MySQLdb.connect( host="localhost",
                                          user="root",
                                          password="Databrix-2024",
                                          db = 'sales_data')
        cursor = mydb.cursor()
        
        # excute posted SQL code
        cursor.execute(sql.code)
        
        # get the returned data
        table = cursor.fetchall()
        cursor.close()
        mydb.close()

    except:
        table = 'falied'
        
    # Return the table to front
    return table




'''
These three functions are for upload data into SQL Server
It is probably not needed
'''
@app.post("/uploadfile/sales/engines")
async def upload_engines(file: UploadFile):
    print(file.file)
    df = pd.read_csv(file.file)
    read = 'read'
    try:
        mydb = MySQLdb.connect( host="localhost",
                                          user="root",
                                          password="Databrix-2024",
                                          db = 'sales_data')
        cursor = mydb.cursor()
        connect = 'connected'
        
        for row in df.values.tolist():
            
            cursor.execute('''INSERT INTO engines_truck (Code_Group_Id,
                          Code_Group_Name_En, Code_Group_Name_De,
                          Folder_Name, Sales_Code, Code_Description_En,
                          Code_Description_De)
                            Value (%s,%s,%s,%s,%s,%s,%s)
                          ''', (i for i in row[1:]) )
        mydb.commit()
        cursor.close()
        mydb.close()
        response = 'Inserted'
        
    except:
        connect = 'unable to connect'
        response = 'unable to INSERT'

    return [connect,response,read]


@app.post("/uploadfile/sales/sales_codes/")
async def upload_sales_codes(file: UploadFile):
    print(file.file)
    df = pd.read_csv(file.file)
    read = 'read'
    try:
        mydb = MySQLdb.connect( host="localhost",
                                          user="root",
                                          password="Databrix-2024",
                                          db = 'sales_data')
        cursor = mydb.cursor()
        connect = 'connected'
        
        for row in df.values.tolist():
            
            cursor.execute('''INSERT INTO sales_codes (columnunknown,
                          h_vehicle, production_date,
                          country, sales_code_array)
                            Value (%s,%s,%s,%s,%s)
                          ''', (i for i in row[1:]) )
        mydb.commit()
        cursor.close()
        mydb.close()
        response = 'Inserted'
        
    except:
        connect = 'unable to connect'
        response = 'unable to INSERT'

    return [connect,response,read]

@app.post("/uploadfile/sales/vehicle_hash/")
async def upload_vehicle_hash(file: UploadFile):
    print(file.file)
    df = pd.read_csv(file.file)
    read = 'read'
    try:
        mydb = MySQLdb.connect( host="localhost",
                                          user="root",
                                          password="Databrix-2024",
                                          db = 'sales_data')
        cursor = mydb.cursor()
        connect = 'connected'
        
        for row in df.values.tolist():
            
            cursor.execute('''INSERT INTO vehicle_hash (h_vehicle_hash,
                          fin, record_source,
                          load_ts)
                            Value (%s,%s,%s,%s,%s)
                          ''', (i for i in row[1:]) )
        mydb.commit()
        cursor.close()
        mydb.close()
        response = 'Inserted'
        
    except:
        connect = 'unable to connect'
        response = 'unable to INSERT'

    return [connect,response,read]