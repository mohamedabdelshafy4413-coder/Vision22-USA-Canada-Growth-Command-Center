import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Growth Command Center',page_icon='🌎',layout='wide')

st.title('🌎 مركز قيادة نمو Vision22')
st.caption('USA & Canada B2B Growth Intelligence | Sales | Revenue Planning')

menu=st.sidebar.selectbox('القائمة الرئيسية',[
'لوحة القيادة','تحليل السوق','تحليل العملاء','الخدمات والباقات','Sales Pipeline','Revenue Forecast','خطة 90 يوم'])

if menu=='لوحة القيادة':
    a,b,c,d=st.columns(4)
    a.metric('الأسواق','USA + Canada')
    b.metric('القطاعات المستهدفة','5')
    c.metric('قيمة العميل','$7K-$50K')
    d.metric('هدف 90 يوم','5-10 Clients')
    df=pd.DataFrame({'القطاع':['Manufacturing','Construction','B2B SaaS','Distribution','Professional Services'],'الفرصة':[95,90,88,82,75]})
    st.plotly_chart(px.bar(df,x='القطاع',y='الفرصة'),use_container_width=True)

elif menu=='تحليل السوق':
    st.header('تحليل السوق الأمريكي والكندي')
    st.write('🇺🇸 USA: Texas - Florida - California - Illinois - North Carolina')
    st.write('🇨🇦 Canada: Ontario - Alberta - British Columbia')

elif menu=='تحليل العملاء':
    st.header('ICP & Buyer Intelligence')
    st.write('Decision Makers: CEO | Founder | VP Sales | Marketing Director')
    st.metric('Opportunity Score','85/100')

elif menu=='الخدمات والباقات':
    st.header('Vision22 Service Packages')
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
    st.metric('Expected Clients',round(clients))
    st.metric('Expected MRR',f'${clients*retainer:,.0f}')

else:
    st.header('خطة 90 يوم')
    st.write('الشهر الأول: ICP + Database + Campaign Setup')
    st.write('الشهر الثاني: Outreach + Meetings + Optimization')
    st.write('الشهر الثالث: Closing + Scaling + Partnerships')
