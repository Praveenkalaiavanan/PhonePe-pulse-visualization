import os
import json
import pandas as pd
import pymysql
import streamlit as st
from plotly import express as px
from streamlit_option_menu import option_menu


#dataframe of aggregated transaction

path1='C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/aggregated/transaction/country/india/state/'
agg_tran_list=os.listdir(path1)

columns1={'States':[],'Years':[],'Quarter':[],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}


for state in agg_tran_list:
    curstates=path1+state+'/'
    agg_year_list=os.listdir(curstates)
    
    for  year in agg_year_list:
        curyear=curstates+year+'/'
        agg_file_list=os.listdir(curyear)
       
        for file in agg_file_list:
            curfile=curyear+file
            data=open(curfile,'r')
            
            A=json.load(data)
            
            
            for i in A['data']['transactionData']:
                name=i['name']
                count=i['paymentInstruments'][0]['count']
                amount=i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['States'].append(' '.join(i.capitalize() for i in state.split('-')))
                columns1['Years'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))


agg_transaction=pd.DataFrame(columns1)

#dataframe of aggregated user

path2='C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/aggregated/user/country/india/state/'
agg_user_list = os.listdir(path2)

columns2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
for state in agg_user_list:
    cur_state = path2 + state + "/"
    agg_year_list = os.listdir(cur_state)
    
    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            B = json.load(data)       
            for i in B["data"]["usersByDevice"]:
                brand_name = i["brand"]
                counts = i["count"]
                percents = i["percentage"]
                columns2["Brands"].append(brand_name)
                columns2["Count"].append(counts)
                columns2["Percentage"].append(percents)
                columns2["State"].append(' '.join(i.capitalize() for i in state.split('-')))
                columns2["Year"].append(year)
                columns2["Quarter"].append(int(file.strip('.json')))

agg_user=pd.DataFrame(columns2)

agg_user

#Dataframe of map transactions

path3 ='C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/map/transaction/hover/country/india/state/'
map_trans_list = os.listdir(path3)

columns3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}

for state in map_trans_list:
    cur_state = path3 + state + "/"
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            C = json.load(data)
            
            for i in C["data"]["hoverDataList"]:
                district = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns3["District"].append(district)
                columns3["Count"].append(count)
                columns3["Amount"].append(amount)
                columns3['State'].append(' '.join(i.capitalize() for i in state.split('-')))
                columns3['Year'].append(year)
                columns3['Quarter'].append(int(file.strip('.json')))

map_trans=pd.DataFrame(columns3)

map_trans

#Dataframe of map user

path4 ='C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/map/user/hover/country/india/state/'
map_user_list = os.listdir(path4)

columns4 = {"State": [], "Year": [], "Quarter": [], "District": [],
            "RegisteredUser": [], "AppOpens": []}

for state in map_user_list:
    cur_state = path4 + state + "/"
    map_year_list = os.listdir(cur_state)
    
    for year in map_year_list:
        cur_year = cur_state + year + "/"
        map_file_list = os.listdir(cur_year)
        
        for file in map_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            D = json.load(data)
            
            for i in D["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appOpens = i[1]['appOpens']
                columns4["District"].append(district)
                columns4["RegisteredUser"].append(registereduser)
                columns4["AppOpens"].append(appOpens)
                columns4['State'].append(' '.join(i.capitalize() for i in state.split('-')))
                columns4['Year'].append(year)
                columns4['Quarter'].append(int(file.strip('.json')))

map_user=pd.DataFrame(columns4)

map_user

#Dataframe of top transactions

path5 ='C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/top/transaction/country/india/state/'

top_trans_list = os.listdir(path5)
columns5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans_list:
    cur_state = path5 + state + "/"
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year)
        
        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            E = json.load(data)
            
            for i in E['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                columns5['Pincode'].append(name)
                columns5['Transaction_count'].append(count)
                columns5['Transaction_amount'].append(amount)
                columns5['State'].append(' '.join(i.capitalize() for i in state.split('-')))
                columns5['Year'].append(year)
                columns5['Quarter'].append(int(file.strip('.json')))

top_trans=pd.DataFrame(columns5)

top_trans

#Dataframe of top users

path6 = "C:/Users/TAMIL TS/project/.venv/Phonepe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)
columns6 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}

for state in top_user_list:
    cur_state = path6 + state + "/"
    top_year_list = os.listdir(cur_state)
    
    for year in top_year_list:
        cur_year = cur_state + year + "/"
        top_file_list = os.listdir(cur_year) 
        
        for file in top_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            F = json.load(data)
            
            for i in F['data']['pincodes']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                columns6['Pincode'].append(name)
                columns6['RegisteredUsers'].append(registeredUsers)
                columns6['State'].append(' '.join(i.capitalize() for i in state.split('-')))
                columns6['Year'].append(year)
                columns6['Quarter'].append(int(file.strip('.json')))

top_user=pd.DataFrame(columns6)

top_user

#datainsert agg_trans
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234')
cursor=mydb.cursor()

cursor.execute('create database if not exists phonepe')

mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

cat='''create table if not exists  agg_trans (
                       States varchar(100),
                       Years int,
                       Quarter int,
                       Transaction_type varchar(100),
                       Transaction_count  BIGINT,
                       Transaction_amount BIGINT)'''
cursor.execute(cat)
 
icat='''insert ignore into agg_trans values(%s,%s,%s,%s,%s,%s)'''

for  index,row in agg_transaction.iterrows():
    ic=(row['States'],row['Years'],
     row['Quarter'],row['Transaction_type'],
     row['Transaction_count'],row['Transaction_amount'])
    cursor.execute(icat,ic)
    mydb.commit()


#data insert agg_user
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

cau='''create table if not exists agg_user (
                                       State varchar(100),
                                       Year int,
                                       Quarter int,
                                       Brands varchar(100),
                                       Count bigint,
                                    Percentage float)'''
cursor.execute(cau)

icau='''insert ignore into agg_user values(%s,%s,%s,%s,%s,%s)'''
    
for index, row in agg_user.iterrows():
    iu = (row['State'], row['Year'], row['Quarter'], row['Brands'], row['Count'], row['Percentage'])
    cursor.execute(icau, iu)
    mydb.commit()    


#data insert map transaction
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

cmt='''create table if not exists map_trans (
                                       State varchar(100),
                                       Year int,
                                       Quarter int,
                                       District varchar(100),
                                       Count bigint,
                                       Amount float)'''
cursor.execute(cmt)

imt='''insert ignore into map_trans values(%s,%s,%s,%s,%s,%s)'''
    
for index, row in map_trans.iterrows():
    im = (row['State'], row['Year'], row['Quarter'], row['District'], row['Count'], row['Amount'])
    cursor.execute(imt, im)
    mydb.commit()    

 #data insert map user
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

cmu='''create table if not exists map_user (
                                       State varchar(100),
                                       Year int,
                                       Quarter int,
                                       District varchar(100),
                                       RegisteredUser bigint,
                                       AppOpens bigint)'''
cursor.execute(cmu)

imu='''insert ignore into map_user values(%s,%s,%s,%s,%s,%s)'''
    
for index, row in map_user.iterrows():
    iu = (row['State'], row['Year'], row['Quarter'], row['District'], row['RegisteredUser'], row['AppOpens'])
    cursor.execute(imu, iu)
    mydb.commit()    

#insert top transaction
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

ctt='''create table if not exists top_trans (
                                       State varchar(100),
                                       Year int,
                                       Quarter int,
                                       Pincode int,
                                       Transaction_count bigint,
                                       Transaction_amount bigint)'''
cursor.execute(ctt)

itt='''insert ignore into top_trans values(%s,%s,%s,%s,%s,%s)'''
    
for index, row in top_trans.iterrows():
    it = (row['State'], row['Year'], row['Quarter'], row['Pincode'], row['Transaction_count'], row['Transaction_amount'])
    cursor.execute(itt, it)
    mydb.commit()  

#insert top user
mydb = pymysql.Connection(host='127.0.0.1',user='root',passwd='Praveen@1234',database='phonepe')
cursor=mydb.cursor()

ctu='''create table if not exists top_user (
                                       State varchar(100),
                                       Year int,
                                       Quarter int,
                                       Pincode int,
                                       RegisteredUsers bigint
                                       )'''
cursor.execute(ctu)

itu='''insert ignore into top_user values(%s,%s,%s,%s,%s)'''
    
for index, row in top_user.iterrows():
    tu = (row['State'], row['Year'], row['Quarter'], row['Pincode'], row['RegisteredUsers'])
    cursor.execute(itu, tu)
    mydb.commit()

cursor.execute("show tables")
cursor.fetchall()                       









#streamlit page 

st.set_page_config(page_title= "Phonepe Pulse Data Visualization ",                 
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )

st.sidebar.title(":violet[**Phonepe Pulse**]")
st.sidebar.caption(':black[Clone the Datas]')
st.sidebar.caption(':black[Transform the Data in SQL]')
st.sidebar.caption(':black[Streamlit And Plotly]')


# Creating connection with mysql workbench
mydb = pymysql.connect(host="127.0.0.1",
                   user="root",
                   password="Praveen@1234",
                   database= "phonepe"
                  )
mydb.cursor()

#option menu
option = option_menu(menu_title=None,
                     options=['Phonepe Map','Analysis'],
                     icons=['geo-alt', 'file-bar-graph'],
                     orientation='horizontal',
                     menu_icon="app-indicator",
                     styles={"nav-link": {"font-size": "25px", "text-align": "center", "margin": "-1px",
                                          "--hover-color": ""},
                             "nav-link-selected": {"background-color": "#9370DB"}})
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])
col3,col4=st.columns([1,4])
with col1:
    map_type = st.selectbox('', options=['Transactions', 'Users'], label_visibility='collapsed',
                            placeholder='Select Transactions or Users', index=None)
with col3:
    map_yr = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], label_visibility='collapsed',
                            placeholder='Select a Year to view',index=None)
# transaction :   
if map_type == 'Transactions' and map_yr is not None:
    map_query = f'''select state,sum(count) Transactions,sum(amount) from map_trans
    where year={map_yr}
    group by state;'''
    df = pd.read_sql_query(map_query, mydb)
    fig = px.choropleth(df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color="Transactions",
                        title=f'PhonePe India Transactions - {map_yr}',
                        color_continuous_scale='purples',
                        width=800, height=1000, hover_name='state')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
elif map_type == 'Transactions' and map_yr is  None:
    map_query = f'''select state,sum(count) Transactions,sum(amount) from map_trans
    group by state;'''
    df = pd.read_sql_query(map_query, mydb)
    fig = px.choropleth(df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color="Transactions",
                        title='PhonePe India Transactions',
                        color_continuous_scale='purples',
                        width=800, height=1000, hover_name='state')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)    
#Users :
elif map_type == 'Users' and map_yr is not None:
    query = f'''select state,sum(registereduser) Registerduser from map_user 
    where year = {map_yr} 
    group by state;'''
    df = pd.read_sql_query(query, mydb)
    fig = px.choropleth(df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color="Registerduser",
                        title=f'PhonePe India Transactions - {map_yr}',
                        color_continuous_scale='greens',
                        width=800, height=1000, hover_name='state')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
elif map_type == 'Users' and map_yr is None:
    query = f'''select state,sum(registereduser) Registerduser from map_user 
    group by state;'''
    df = pd.read_sql_query(query, mydb)
    fig = px.choropleth(df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color="Registerduser",
                        title='PhonePe India Transactions',
                        color_continuous_scale='greens',
                        width=800, height=1000, hover_name='state')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)

# Dashboard for Analysis
elif option == 'Analysis':
    # Sidebar Buttons (SelectBox)
    with st.sidebar:
        st.header(":blue[Choose Type,Year and Quarter to do Analysis]")
        st.divider()
        opt, dummy = st.columns([5, 1])
        with opt:
            trans = st.selectbox('', options=['Transactions', 'Users'], index=None, placeholder='Type',
                                 label_visibility='collapsed')
            year = st.selectbox('', options=[2018, 2019, 2020, 2021, 2022, 2023], placeholder='Year',
                                label_visibility='collapsed')
            quarter = st.selectbox('', options=[1, 2, 3, 4], placeholder='Quarter', label_visibility='collapsed')
    st.markdown(f'## ANALYSIS BASED ON :red[{year}] - QUARTER - :red[{quarter}]')

# When User selects transactions
    if trans == 'Transactions':
        tab1, tab2, tab3 = st.tabs(['Details', 'Category', 'TOP 10'])
        # Transaction Details Tab
        with tab1:
            st.markdown('#### :orange[PhonePe] :green[India]')
            col1, col2, col3 = st.columns(3)
            with col1:
                query1 = f'''select concat(sum(Transaction_Count)/10000000,' Cr') as trans from agg_trans 
                where years=years and quarter = quarter;'''
                all_trans = pd.read_sql_query(query1, mydb)
                st.dataframe(all_trans, column_config={"trans": "Total Number of Transactions"}, hide_index=True)
            with col2:
                query2 = f'''select concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as value from agg_trans 
                where years=years and quarter=quarter;'''
                trans_val = pd.read_sql_query(query2, mydb)
                st.dataframe(trans_val, column_config={"value": "Total Payment Value"}, hide_index=True)
            with col3:
                query3 = f'''select concat('₹ ',sum(Transaction_Amount)/sum(Transaction_Count)) as avg from agg_trans 
                where years=years and quarter=quarter;'''
                avg_val = pd.read_sql_query(query3, mydb)
                st.dataframe(avg_val, column_config={"avg": "Average Payment Value"}, hide_index=True)
             # Transactions Category Tab
        with tab2:
                st.markdown(f"### :grey[Tables on Transaction Count and Payment Value based on the category]")
                col1, col2 = st.columns([4, 4])
                with col1:
                    query4 = f'''select transaction_type as mode , concat(sum(transaction_count)/100000,' lakh') as tc from agg_trans 
                    where years=years and quarter=quarter group by transaction_type;'''
                    cat_count = pd.read_sql_query(query4, mydb)
                    st.dataframe(cat_count, column_config={"mode": "Type of Transaction", "tc": "No Of Transactions"},
                                hide_index=True)
                with col2:
                    query5 = f'''select transaction_type as mode , concat('₹',sum(transaction_amount)/10000000,' Cr') as amt from agg_trans 
                    where years=years and quarter=quarter group by transaction_type;'''
                    cat_val = pd.read_sql_query(query5, mydb)
                    st.dataframe(cat_val, column_config={"mode": "Type of Transaction", "amt": "Transaction Value"},
                                hide_index=True)
        # Transaction Top-10 Tab
        with tab3:
            # Creating select biox for top 10 based on transaction count and amount transferred
            select = st.selectbox('Select Option To Get TOP 10 :', options=['Number Of Transactions', 'Amount'])
            # Based on Transactions
            if select == "Number Of Transactions":
                # Top 10 States based on transaction
                if st.button("Top 10 States"):
                    st.markdown(
                        f"Top 10 States Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Count) desc) as rnk,states as State,concat(sum(Transaction_Count)/10000000,' Cr') as tc from agg_trans 
                    where years=years and quarter=quarter group by state order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Districts based on transaction
                if st.button("Top 10 Districts"):
                    st.markdown(
                        f"Top 10 Districts Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by transaction_count desc) as rnk, concat(transaction_count/100000, ' lakh') as tc from top_trans 
                    where year=year and quarter=quarter  order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Postal based on transaction
                if st.button("Top 10 Postal"):
                    st.markdown(
                        f"Top 10 Postal Based On :blue[Number Of Transactions] Made by :red[{year} - Q{quarter}]:")
                    query8 = f'''select dense_rank()over(order by transaction_count desc) as rnk, concat(transaction_count/100000,' lakh') as tc from top_trans 
                    where year=year and quarter=quarter order by rnk asc limit 10;'''
                    top_post = pd.read_sql_query(query8, mydb)
                    st.dataframe(top_post, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                 # Based on Amount
            elif select == "Amount":
                # Top 10 states based on Amount
                if st.button("Top 10 States"):
                    st.markdown(f"Top 10 States Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query6 = f'''select dense_rank()over(order by sum(Transaction_Amount) desc) as rnk,states as State,concat('₹ ',sum(Transaction_Amount)/10000000,' Cr') as amt from agg_trans 
                    where years=years and quarter=quarter group by state order by rnk asc limit 10;'''
                    top_state = pd.read_sql_query(query6, mydb)
                    st.dataframe(top_state, column_config={"rnk": "Rank", "amt": "Payment Value"}, hide_index=True)    

                 # Top 10 Districts based on Amount
                if st.button("Top 10 Districts"):
                    st.markdown(f"Top 10 Districts Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query7 = f'''select dense_rank()over(order by transaction_amount desc) as rnk, concat('₹ ',transaction_amount/10000000, ' Cr') as tc from top_trans 
                    where year=year and quarter=quarter  order by rnk asc limit 10;'''
                    top_district = pd.read_sql_query(query7, mydb)
                    st.dataframe(top_district, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
                # Top 10 Postal based on Amount
                if st.button("Top 10 Postal"):
                    st.markdown(f"Top 10 Postal Based On :blue[Transaction Amount] :red[{year} - Q{quarter}]:")
                    query8 = f'''select dense_rank()over(order by transaction_amount desc) as rnk, concat('₹ ',transaction_amount/10000000,' Cr') as tc from top_trans 
                    where year=year and quarter=quarter order by rnk asc limit 10;'''
                    top_post = pd.read_sql_query(query8, mydb)
                    st.dataframe(top_post, column_config={"rnk": "Rank", "tc": " Number of Transaction"},
                                 hide_index=True)
# When the transaction type is Users
    elif trans == 'Users':
        tab1, tab2 = st.tabs(['Details', 'TOP 10'])
        # User Details
        with tab1:
            st.markdown(f'#### :grey[PhonePe Users Data In INDIA by Q{quarter} - {year}]')
            query9 = f'''select concat(sum(RegisteredUser)/10000000,' Cr') as users from map_user 
            where year=year and quarter=quarter group by year,quarter;'''
            usercount = pd.read_sql_query(query9, mydb)
            st.dataframe(usercount, column_config={"users": f"PhonePe users"}, hide_index=True)
            st.markdown("#### Total no of app opens in the selected period of time")
            query10 = f'''select case when sum(appopens)=0 then 'N/A' else concat(sum(appopens)/10000000, ' Cr') end as ao from map_user
            where year=year and quarter =quarter group by year, quarter;'''
            app_opens = pd.read_sql_query(query10, mydb)
            st.dataframe(app_opens, column_config={"ao": f"App Opens"}, hide_index=True)   

    # User Top 10
        with tab2:
            # Top 10 User States
            if st.button("Top 10 States"):
                st.markdown(f'#### Top 10 States Based on Registered Users Q{quarter} - {year}:')
                query11 = (f'''select dense_rank()over(order by sum(registeredusers) desc)as rnk,state,concat(sum(registeredusers)/100000,' lakh') as reguser from top_user
                where year=year and quarter=quarter group by state order by rnk asc limit 10;''')
                state = pd.read_sql_query(query11, mydb)
                st.dataframe(state, column_config={"reguser": f"Registered Users"}, hide_index=True)
            # Top 10 User Districts
            if st.button("Top 10 Districts"):
                st.markdown(f'#### Top 10 District Based on Registered Users Q{quarter} - {year}:')
                query12 = f'''select dense_rank()over(order by registeredusers desc) as rnk,
                concat(registeredusers/100000,' lakh') as reguser from top_user
                where year=2019 and quarter=1 order by rnk asc limit 10;'''
                dist = pd.read_sql_query(query12, mydb)
                st.dataframe(dist, column_config={"reguser": f"Registered Users"}, hide_index=True)
             # Top 10 User Postal
            if st.button("Top 10 Postal"):
                st.markdown(f'#### Top 10 Postal Based on Registered Users Q{quarter} - {year}:')
                query13 = f'''select dense_rank()over(order by registeredusers desc) as rnk,
                concat(registeredusers/100000,' lakh') as reguser from top_user
                where year=2019 and quarter=1 order by rnk asc limit 10;'''
                dist = pd.read_sql_query(query13, mydb)
                st.dataframe(dist, column_config={"reguser": f"Registered Users"}, hide_index=True)    

#option menu for visualization                  
option = option_menu(menu_title=None,
                options=['Visualization'],
                icons=['file-bar-graph'],
                orientation='horizontal',
                menu_icon="app-indicator",
                styles={"nav-link": {"font-size": "25px", "text-align": "center", "margin": "-1px",
                                    "--hover-color": ""},
                        "nav-link-selected": {"background-color": "#9370DB"}})
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
query1 = f'''select years,sum(transaction_amount) trans from agg_trans
group by years;'''
data = pd.read_sql_query(query1, mydb)
fig = px.pie(data,names='years', values='trans',width=500, height=1000, title='Total  Transaction Year Wise')
st.plotly_chart(fig)

st.markdown('#### Animated chart ')
col1, col2 = st.columns([3, 2])
with col1:
    query2 = f'''select transaction_type,years,sum(transaction_count) as tc,
                concat('₹',sum(Transaction_Amount)/10000000,' Cr') as amount from agg_trans
                group by transaction_type,years;'''
df = pd.read_sql_query(query2, mydb)
fig = px.bar(df, x='years', y='tc', color='transaction_type', hover_name='amount',
                color_discrete_sequence=px.colors.sequential.Turbo, animation_frame='years', range_x=[2018, 2023],
                range_y=[0, 50000000000], title='Transaction Count Vs Year')
st.plotly_chart(fig)

with col2:
    query3 = f'''select  distinct transaction_type categories,sum(transaction_amount) Amount from agg_trans
group by categories ;'''
data = pd.read_sql_query(query3, mydb)
fig = px.scatter(data, x='categories', y='Amount',
                title='Categories Of Transaction Amounts')
st.plotly_chart(fig)

with col3:
    query4 = f'''select distinct state states,sum(registereduser) Registereduser from map_user
    group by states;'''
    data = pd.read_sql_query(query4, mydb)
fig = px.line(data, x='states', y='Registereduser',width=800, height=400,
title='State Wise Registered User')
st.plotly_chart(fig)

with col4:
    query5 = f'''select years year,avg(transaction_count) avgtransaction from agg_trans
    group by year;'''
    data = pd.read_sql_query(query5, mydb)
fig = px.histogram(data,x='year',y='avgtransaction', nbins=30, title='Histogram Example')  
st.plotly_chart(fig)