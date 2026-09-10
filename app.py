import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 مركز قيادة النمو',page_icon='🌎',layout='wide')

st.title('🌎 Vision22 USA & Canada Growth Command Center')
st.caption('مركز ذكاء السوق | تطوير الأعمال | تخطيط الإيرادات')

industries=pd.DataFrame([
['Manufacturing','$8K-$30K/mo','Lead Generation + SEO'],
['Construction','$7K-$25K/mo','Pipeline Growth'],
['B2B SaaS','$10K-$40K/mo','Demand Generation'],
['Distribution','$8K-$25K/mo','Buyer Acquisition'],
['Professional Services','$5K-$15K/mo','Authority Building']],columns=['Industry','Retainer','Solution'])

menu=st.sidebar.selectbox('القائمة الرئيسية',['الرئيسية','تحليل السوق','تحليل العملاء','الباقات والخدمات','خط المبيعات','توقع الإيرادات','خطة 90 يوم'])

if menu=='الرئيسية':
    a,b,c,d=st.columns(4)
    a.metric('الأسواق','USA + Canada')
    b.metric('القطاعات','5')
    c.metric('قيمة التعاقد','$5K-$50K')
    d.metric('هدف 90 يوم','5-10 عملاء')
    st.dataframe(industries,use_container_width=True)

elif menu=='تحليل السوق':
    st.header('تحليل السوق')
    st.write('🇺🇸 USA: Manufacturing - Construction - B2B SaaS - Distribution')
    st.write('🇨🇦 Canada: Ontario - Alberta - British Columbia')
    st.plotly_chart(px.bar(industries,x='Industry',y='Retainer'),use_container_width=True)

elif menu=='تحليل العملاء':
    st.header('ICP & Buyer Intelligence')
    st.write('صناع القرار: CEO - Founder - VP Sales - Marketing Director - Business Development')

elif menu=='الباقات والخدمات':
    st.header('Vision22 Services Packages')
    packages=['Complete B2B Marketing Department','Performance Growth System','Lead Generation Engine','International B2B Expansion','Digital Authority System','Website & Conversion System','Growth Foundation']
    st.table(pd.DataFrame({'Services & Packages':packages}))

elif menu=='خط المبيعات':
    st.header('Sales Pipeline Command Center')
    df=pd.DataFrame({'المرحلة':['Prospects','Replies','Meetings','Proposals','Won'],'العدد':[5000,150,40,15,5]})
    st.plotly_chart(px.funnel(df,x='العدد',y='المرحلة'),use_container_width=True)

elif menu=='توقع الإيرادات':
    st.header('Revenue Forecast')
    accounts=st.number_input('عدد الشركات المستهدفة',100,100000,5000)
    reply=st.slider('نسبة الرد %',1,20,5)
    close=st.slider('نسبة الإغلاق %',1,50,15)
    retainer=st.number_input('Monthly Retainer USD',5000,100000,15000)
    clients=accounts*reply/100*close/100
    st.metric('العملاء المتوقعون',round(clients))
    st.metric('MRR',f'${clients*retainer:,.0f}')

elif menu=='خطة 90 يوم':
    st.header('خطة دخول السوق')
    st.write('الشهر الأول: ICP + Database + Campaign Setup')
    st.write('الشهر الثاني: Outreach + Meetings + Optimization')
    st.write('الشهر الثالث: Closing + Scaling')
