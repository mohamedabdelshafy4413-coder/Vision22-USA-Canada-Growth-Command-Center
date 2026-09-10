import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 Growth Command Center', page_icon='🌎', layout='wide')

st.title('🌎 Vision22 USA & Canada Growth Command Center')
st.caption('B2B Market Expansion | Sales Intelligence | Revenue Planning')

menu = st.sidebar.selectbox('Modules', [
    'Executive Dashboard',
    'Market Intelligence',
    'Buyer Intelligence',
    'Package Intelligence',
    'Sales Pipeline',
    'Revenue Forecast',
    '90 Day GTM Plan'
])

if menu == 'Executive Dashboard':
    st.header('Executive Dashboard')
    a,b,c,d = st.columns(4)
    a.metric('Markets','USA + Canada')
    b.metric('Target Industries','5')
    c.metric('Retainer Range','$7K-$50K')
    d.metric('90 Day Goal','5-10 Clients')

elif menu == 'Market Intelligence':
    st.header('Market Intelligence')
    st.write('USA: Manufacturing, Construction, SaaS, Distribution, Professional Services')
    st.write('Canada: Ontario, Alberta, British Columbia priority markets')

elif menu == 'Buyer Intelligence':
    st.header('ICP & Buyer Intelligence')
    st.write('Target decision makers: CEO, Founder, VP Sales, Marketing Director, Business Development')

elif menu == 'Package Intelligence':
    st.header('Vision22 Service Packages')
    st.write('- Complete B2B Marketing Department')
    st.write('- B2B Lead Generation Engine')
    st.write('- International B2B Expansion')
    st.write('- Digital Authority System')
    st.write('- Website & Conversion System')

elif menu == 'Sales Pipeline':
    st.header('Sales Command Center')
    df = pd.DataFrame({'Stage':['Prospects','Replies','Meetings','Proposals','Won'],'Count':[5000,150,40,15,5]})
    st.dataframe(df,use_container_width=True)

elif menu == 'Revenue Forecast':
    st.header('Revenue Forecast')
    accounts = st.number_input('Target Accounts',100,100000,5000)
    reply = st.slider('Reply Rate %',1,20,5)
    close = st.slider('Close Rate %',1,50,15)
    retainer = st.number_input('Monthly Retainer',5000,100000,15000)
    clients = accounts*reply/100*close/100
    st.metric('Expected Clients',round(clients))
    st.metric('Expected MRR',f'${clients*retainer:,.0f}')

elif menu == '90 Day GTM Plan':
    st.header('90 Day Go To Market Plan')
    st.write('Month 1: Research, ICP, Database, Campaign Setup')
    st.write('Month 2: Outreach, Meetings, Optimization')
    st.write('Month 3: Closing, Scaling, Partnerships')
