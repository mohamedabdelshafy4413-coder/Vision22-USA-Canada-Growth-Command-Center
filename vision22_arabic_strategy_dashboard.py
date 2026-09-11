import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 تحليل السوق الأمريكي والكندي', layout='wide')

st.title('Vision22 | دراسة وتحليل دخول السوق الأمريكي والكندي')
st.caption('B2B Digital Marketing Market Analysis Dashboard')

section = st.sidebar.selectbox('القائمة',[
'الرئيسية','تحليل السوق','تحليل الباقات','SWOT Analysis','المخاطر والحلول','خطة 90 يوم'
])

if section=='الرئيسية':
    c1,c2,c3,c4=st.columns(4)
    c1.metric('أفضل نقطة دخول','Lead Generation Engine')
    c2.metric('أفضل سوق','USA + Canada')
    c3.metric('Retainer المتوقع','$7K - $50K')
    c4.metric('هدف 90 يوم','5-10 عملاء')

elif section=='تحليل السوق':
    st.header('تحليل القطاعات المستهدفة')
    df=pd.DataFrame({'القطاع':['Manufacturing','Construction','B2B SaaS','Distribution','Professional Services'],'الفرصة':[95,90,88,82,75]})
    st.plotly_chart(px.bar(df,x='القطاع',y='الفرصة'),use_container_width=True)

elif section=='تحليل الباقات':
    st.header('ترتيب الباقات حسب فرصة النجاح')
    df=pd.DataFrame({'Package':['Lead Generation Engine','Website & Conversion System','Performance Growth System','Growth Foundation','Digital Authority System','Complete B2B Marketing Department','International B2B Expansion'],'Success %':[92,88,85,78,72,68,60],'Price Level':['High','High','High','Medium','Medium','Premium','Premium']})
    st.dataframe(df,use_container_width=True)

elif section=='SWOT Analysis':
    st.header('SWOT Analysis')
    st.write('Strengths: فريق متكامل وقدرة على تقديم حلول B2B كاملة')
    st.write('Weaknesses: الحاجة لبناء Proof محلي في أمريكا وكندا')
    st.write('Opportunities: طلب قوي على Lead Generation والنمو الرقمي')
    st.write('Threats: المنافسة وطول دورة البيع')

elif section=='المخاطر والحلول':
    st.table(pd.DataFrame({'المشكلة':['الثقة','طول دورة البيع','المنافسة'],'الحل':['Case Studies و Proof','Nurturing و Follow Up','Niche Positioning']}))

elif section=='خطة 90 يوم':
    st.write('الشهر الأول: ICP + Database + Campaign Setup')
    st.write('الشهر الثاني: Outreach + Meetings + Optimization')
    st.write('الشهر الثالث: Closing + Scaling')
