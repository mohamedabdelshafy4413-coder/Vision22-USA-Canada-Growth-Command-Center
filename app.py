import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Growth Command Center',page_icon='🌎',layout='wide')

st.title('🌎 Vision22 USA & Canada Growth Command Center')
st.caption('B2B Market Intelligence | Sales Engine | Revenue Planning')

industries=pd.DataFrame([
['Manufacturing','$8K-$30K/mo','Lead Generation + SEO'],
['Construction','$7K-$25K/mo','Pipeline Growth'],
['B2B SaaS','$10K-$40K/mo','Demand Generation'],
['Distribution','$8K-$25K/mo','Buyer Acquisition'],
['Professional Services','$5K-$15K/mo','Authority Building']],columns=['Industry','Retainer','Solution'])

menu=st.sidebar.selectbox('Command Center',['Executive Dashboard','Market Intelligence','ICP Builder','Package Strategy','Sales Pipeline','Revenue Forecast','90 Day GTM'])

if menu=='Executive Dashboard':
    a,b,c,d=st.columns(4)
    a.metric('Markets','USA + Canada')
    b.metric('Industries','5')
    c.metric('Retainer','$5K-$50K')
    d.metric('Goal','5-10 Clients')
    st.dataframe(industries,use_container_width=True)

elif menu=='Market Intelligence':
    st.subheader('Priority Markets')
    st.write('USA: Texas, Florida, California, Illinois, North Carolina')
    st.write('Canada: Ontario, Alberta, British Columbia')
    st.plotly_chart(px.bar(industries,x='Industry',y='Retainer'),use_container_width=True)

elif menu=='ICP Builder':
    industry=st.selectbox('Industry',industries['Industry'])
    st.success(industry)
    st.write('Decision Makers: CEO, Founder, VP Sales, Marketing Director, Business Development')

elif menu=='Package Strategy':
    packages=['Complete B2B Marketing Department','Performance Growth System','Lead Generation Engine','International B2B Expansion','Digital Authority System','Website & Conversion System','Growth Foundation']
    st.table(pd.DataFrame({'Packages':packages}))

elif menu=='Sales Pipeline':
    df=pd.DataFrame({'Stage':['Prospects','Replies','Meetings','Proposals','Won'],'Count':[5000,150,40,15,5]})
    st.plotly_chart(px.funnel(df,x='Count',y='Stage'),use_container_width=True)

elif menu=='Revenue Forecast':
    accounts=st.number_input('Target Accounts',100,100000,5000)
    reply=st.slider('Reply Rate %',1,20,5)
    close=st.slider('Close Rate %',1,50,15)
    retainer=st.number_input('Monthly Retainer',5000,100000,15000)
    clients=accounts*reply/100*close/100
    st.metric('Clients',round(clients))
    st.metric('MRR',f'${clients*retainer:,.0f}')

elif menu=='90 Day GTM':
    st.write('Month 1: ICP + Database + Campaign Setup')
    st.write('Month 2: Outreach + Meetings + Optimization')
    st.write('Month 3: Closing + Scaling')
