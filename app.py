import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Market Study',page_icon='🌎',layout='wide')

st.markdown('''<style>[data-testid="stMetric"]{background:#f5f5f5;padding:18px;border-radius:15px}</style>''',unsafe_allow_html=True)

st.title('🌎 دراسة دخول سوق أمريكا وكندا - Vision22')
st.caption('B2B Digital Marketing Market Analysis | Services Strategy | Growth Plan')

menu=st.sidebar.radio('الأقسام',['الرئيسية','أقوى نقطة دخول','الباقات والخدمات','نسب النجاح','Email Campaign','SWOT Analysis','المخاطر والحلول'])

packages=pd.DataFrame({
'Package':['Complete B2B Marketing Department','Performance Growth System','Lead Generation Engine','International B2B Expansion','Digital Authority System','Website & Conversion System','Growth Foundation'],
'Success %':[70,82,90,65,75,85,88],
'Opportunity %':[85,90,95,70,80,92,86],
'Price Level':['Premium','High','High','Premium','Medium','Premium','Medium']
})

if menu=='الرئيسية':
    a,b,c,d=st.columns(4)
    a.metric('أفضل دخول','B2B Lead Generation')
    b.metric('أقوى قطاعات','Manufacturing + SaaS')
    c.metric('أفضل Retainer','$7K-$30K/mo')
    d.metric('فرصة 90 يوم','High')
    st.dataframe(packages,use_container_width=True)

elif menu=='أقوى نقطة دخول':
    st.header('استراتيجية الدخول الأقوى')
    st.write('1- Manufacturing Companies')
    st.write('2- Construction & Engineering')
    st.write('3- B2B SaaS Companies')
    st.write('4- Distribution Companies')
    st.write('سبب الاختيار: قيمة عميل عالية + احتياج مستمر للـ Leads + قدرة دفع قوية')

elif menu=='الباقات والخدمات':
    st.header('Vision22 Service Packages')
    st.table(packages[['Package','Price Level']])

elif menu=='نسب النجاح':
    st.header('ترتيب الباقات من الأعلى فرصة للأقل')
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)
    st.dataframe(packages.sort_values('Success %',ascending=False))

elif menu=='Email Campaign':
    st.header('أفضل 10 رسائل Email Hooks')
    emails=['Growth Opportunity Audit','Increase Qualified B2B Leads','Your Competitor Digital Gap','90 Day Pipeline Growth Plan','Market Expansion Strategy','Free Digital Growth Review','Revenue Growth Opportunity','B2B Acquisition Improvement','Website Conversion Analysis','Strategic Growth Partnership']
    st.table(pd.DataFrame({'Email Subject':emails}))

elif menu=='SWOT Analysis':
    st.write('Strengths: Full marketing team capability, international delivery')
    st.write('Weaknesses: New market trust building')
    st.write('Opportunities: High B2B demand in USA/Canada')
    st.write('Threats: Competition, long sales cycles')

else:
    st.header('المشاكل والحلول')
    data=pd.DataFrame({'Problem':['عدم الثقة','طول دورة البيع','منافسة عالية'],'Solution':['Case Studies + Proof','Nurturing + Follow Up','Niche Positioning']})
    st.table(data)
