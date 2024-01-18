import streamlit as st
import base64
from LaunchVM import launch_tljh, search_publicip, stop_tljh
import requests
import pandas as pd



# Add a sidebar and a selectbox inside sidebar
# Selectbox for choosing project
add_selectbox = st.sidebar.selectbox(
    "Which Homepage would you like to choose?",
    ("Sales", 'Funnel Analysis',"Database")     )


# Function to display PDF in Website
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1200" height="800" type="application/pdf">'
    
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    return 0
    
# Send SQL Code to backend and get the data back
# SQL Server is local hosted in Yuqiang´s Workstation
def sql_query(query):
    try:
        # Input format for post request in backend
        sql_query = {"code" : query,'description':'sql codes by users'}
        
        # Send the request to local hosted backend
        res = requests.post('http://127.0.0.1:8000/sql_query',json = sql_query)
        
        # Retrive the Data, which is sent back
        res_data = res.json()
        querydata = pd.DataFrame(res_data)
        
        # Write the returned data in the expander
        with st.expander(':date: Your search results: '):
            st.write(querydata)
            
    # If SQL Code not correct then just display Erro Code
    except:
        st.write('Your SQL Code is not correct')



def update_table(file):
    requests.post('http://127.0.0.1:8000/uploadfile/sales/engines/',
                            files = file)
    
    requests.post('http://127.0.0.1:8000/uploadfile/sales/sales_codes/',
                            files = file)
        
    return


# If User selected Sales Project in Selectbox
# A new page of description for project Sales is displayed
if add_selectbox == 'Sales':
    
    # Title of this page
    st.title('Sales Daimler Truck')
    
    # display the pdf for the Sales project
    displayPDF('salesprojekt.pdf')
    
    # show three buttons for launch TLJH in AWS
    # lauch_tljh function is in another script
    st.button("Start your Jupyterlab", type="secondary", on_click=launch_tljh)
    st.button("Lauch your Jupyterlab", type="secondary", on_click=search_publicip)
    st.button("Stop your Jupyterlab", type="primary", on_click=stop_tljh)


# If User selected Database in Selectbox
# A new page of description for data is displayed
if add_selectbox == 'Database':
    
    variable_dict = {}
    
    #  Create a selectbox in sidebar with databases for projects
    db_overview = st.sidebar.selectbox(
        "Which Database would you like to choose?",
        ("Daimler Truck Sale Database", 'Funnel Analysis') )    
    
    # Set the title of this page to the name of selected database
    st.title(db_overview)
    
    # Send request to backend, to get the data back
    res = requests.get('http://127.0.0.1:8000/database')
    # Get the returned data
    res_data = res.json()

    st.header('_Daimler Truck Sale Database_', divider='rainbow')
    

    # Show all of the returned data(tables) in this page
    for table,tables_info in zip(res_data[0],res_data[1]):
        
        df = pd.DataFrame(table,columns = tables_info[1])
        
        with st.expander(':date: Table: ' + tables_info[0]):
            st.dataframe(df)
            st.button("Upload data to " + tables_info[0])
            

    # Create a text area for user, to type their sql Code
    query = st.text_area("Enter your SQL Query")
    
    # Button for starting query
    b = st.button("Go query", type="secondary")
    
    if b:
        sql_query(query)
    
    
