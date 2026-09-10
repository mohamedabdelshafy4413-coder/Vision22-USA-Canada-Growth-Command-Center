import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Growth Command Center',page_icon='🌎',layout='wide')

st.markdown('''<style>
[data-testid="stMetric"]{background:#f5f5f5;padding:18px;border-radius:15px}
</style>''',unsafe_allow_html=True)

st.title('🌎 مركز قيادة نمو Vision22')
st.caption('USA & Canada B2B Growth Intelligence | Sales Command Center | Revenue Strategy')

menu=st.sidebar.radio('القائمة الرئيسية',[
'الرئيسية','تحليل السوق','Buyer Intelligence','الخدمات والباقات','Sales Pipeline','Revenue Forecast','خطة 90 يوم'])

if menu=='الرئيسية':
    st.header('Executive Dashboard')
    a,b,c,d=st.columns(4)
    a.metric('الأسواق','USA + Canada')
    b.metric('القطاعات','5 Priority Industries')
    c.metric('Retainer','$7K - $50K')
    d.metric('هدف 90 يوم','5-10 Clients')
    df=pd.DataFrame({'Industry':['Manufacturing','Construction','B2B SaaS','Distribution','Professional Services'],'Opportunity':[95,90,88,82,75]})
    st.plotly_chart(px.bar(df,x='Industry',y='Opportunity'),use_container_width=True)

elif menu=='تحليل السوق':
    st.header('تحليل السوق الأمريكي والكندي')
    st.subheader('USA')
    st.write('Texas | Florida | California | Illinois | North Carolina')
    st.subheader('Canada')
    st.write('Ontario | Alberta | British Columbia')

elif menu=='Buyer Intelligence':
    st.header('ICP & Buyer Intelligence')
    st.write('Decision Makers: CEO | Founder | VP Sales | Marketing Director | Business Development')
    score=st.slider('Company Opportunity Score',0,100,85)
    st.metric('Opportunity Score',f'{score}/100')

elif menu=='الخدمات والباقات':
    st.header('Vision22 Service Packages')
    packages=['Complete B2B Marketing Department','Performance Growth System','Lead Generation Engine','International B2B Expansion','Digital Authority System','Website & Conversion System','Growth Foundation']
    st.table(pd.DataFrame({'Packages':packages}))

elif menu=='Sales Pipeline':
    st.header('Sales Command Center')
    df=pd.DataFrame({'Stage':['Prospects','Contacted','Replies','Meetings','Proposals','Won'],'Count':[5000,800,150,40,15,5]})
    st.plotly_chart(px.funnel(df,x='Count',y='Stage'),use_container_width=True)

elif menu=='Revenue Forecast':
    st.header('Revenue Forecast')
    accounts=st.number_input('Target Accounts',100,100000,5000)
    reply=st.slider('Reply Rate %',1,20,5)
    close=st.slider('Close Rate %',1,50,15)
    retainer=st.number_input('Monthly Retainer',5000,100000,15000)
    clients=accounts*reply/100*close/100
    a,b=st.columns(2)
    a.metric('Expected Clients',round(clients))
    b.metric('Expected MRR',f'${clients*retainer:,.0f}')

else:
    st.header('خطة 90 يوم GTM')
    st.write('الشهر الأول: ICP + Database + Campaign Setup')
    st.write('الشهر الثاني: Outreach + Meetings + Optimization')
    st.write('الشهر الثالث: Closing + Scaling + Partnerships')
