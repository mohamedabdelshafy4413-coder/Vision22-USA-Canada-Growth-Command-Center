import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 USA Canada Market Strategy',page_icon='🌎',layout='wide')

st.title('🌎 Vision22 | دراسة دخول سوق أمريكا وكندا')
st.caption('B2B Digital Marketing Market Entry Strategy | Services | Growth Plan')

menu=st.sidebar.radio('القائمة',['الرئيسية','أقوى نقطة دخول','الباقات والخدمات','نسب النجاح والانتشار','Email Campaign','SWOT Analysis','المخاطر والحلول'])

packages=pd.DataFrame({
'Package':['Lead Generation Engine','Website & Conversion System','Performance Growth System','Growth Foundation','Digital Authority System','Complete B2B Marketing Department','International B2B Expansion'],
'Success %':[90,85,82,78,75,70,65],
'Opportunity %':[95,92,90,86,80,85,70],
'Price':['$10K-$20K/mo','$7K-$15K/mo','$10K-$25K/mo','$5K-$10K/mo','$7K-$15K/mo','$15K-$50K/mo','$20K+']
})

if menu=='الرئيسية':
    a,b,c,d=st.columns(4)
    a.metric('أفضل نقطة دخول','Lead Generation Engine')
    b.metric('أقوى قطاعات','Manufacturing + B2B SaaS')
    c.metric('قيمة العميل','$7K-$50K/mo')
    d.metric('فرصة أول 90 يوم','High')
    st.dataframe(packages,use_container_width=True)

elif menu=='أقوى نقطة دخول':
    st.header('أقوى نقطة دخول للسوق')
    st.write('1- Manufacturing Companies')
    st.write('2- Construction & Engineering')
    st.write('3- B2B SaaS Companies')
    st.write('4- Distribution Companies')

elif menu=='الباقات والخدمات':
    st.header('Vision22 Service Packages')
    st.dataframe(packages,use_container_width=True)

elif menu=='نسب النجاح والانتشار':
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)
    st.dataframe(packages.sort_values('Success %',ascending=False))

elif menu=='Email Campaign':
    emails=['Growth Opportunity Audit','Increase Qualified B2B Leads','Your Digital Growth Gap','90 Day Pipeline Growth Plan','Market Expansion Opportunity','Free B2B Marketing Review','Revenue Growth Strategy','Improve Your Lead Generation','Website Conversion Analysis','Strategic Growth Partnership']
    st.table(pd.DataFrame({'Email Hooks':emails}))

elif menu=='SWOT Analysis':
    st.write('Strengths: فريق متكامل وقدرة تقديم خدمات B2B كاملة')
    st.write('Weaknesses: بناء الثقة والعلامة في سوق جديد')
    st.write('Opportunities: طلب مرتفع على Lead Generation وGrowth')
    st.write('Threats: المنافسة وطول دورة البيع')

else:
    st.table(pd.DataFrame({'المشكلة':['Trust','Long Sales Cycle','Competition'],'الحل':['Case Studies + Proof','Follow Up + Nurturing','Niche Positioning']}))
