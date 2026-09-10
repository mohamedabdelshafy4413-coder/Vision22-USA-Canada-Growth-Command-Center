import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 USA Canada Deep Market Strategy', page_icon='🌎', layout='wide')

st.title('🌎 Vision22 | USA & Canada Deep Market Strategy')
st.caption('B2B Digital Marketing Entry Analysis | Package Intelligence | Sales Strategy')

menu = st.sidebar.radio('الأقسام',[
    'Executive Summary','Market Entry Analysis','Target Industries','Package Analysis','Email Strategy','SWOT','Risks & Solutions'
])

packages=pd.DataFrame({
'Package':['Lead Generation Engine','Website & Conversion System','Performance Growth System','Growth Foundation','Digital Authority System','Complete B2B Marketing Department','International B2B Expansion'],
'Success %':[92,86,84,80,76,72,68],
'Sales Opportunity %':[96,93,91,87,82,85,70],
'Price':['$10K-$20K/mo','$7K-$15K/mo','$10K-$25K/mo','$5K-$10K/mo','$7K-$15K/mo','$15K-$50K/mo','$20K+']
})

if menu=='Executive Summary':
    a,b,c,d=st.columns(4)
    a.metric('أقوى نقطة دخول','Lead Generation Engine')
    b.metric('أفضل سوق','USA B2B')
    c.metric('أفضل قطاعات','Manufacturing + SaaS')
    d.metric('فرصة 90 يوم','High')
    st.dataframe(packages,use_container_width=True)

elif menu=='Market Entry Analysis':
    st.header('تحليل الدخول للسوق')
    st.write('الاستراتيجية: الدخول عبر حل مشكلة واضحة وهي زيادة العملاء المحتملين وتحسين نظام اكتساب العملاء.')
    st.write('أفضل نموذج بيع: Audit → Strategy → Monthly Retainer')
    st.write('Target Buyer: CEO, Founder, VP Sales, Marketing Director')

elif menu=='Target Industries':
    df=pd.DataFrame({'Industry':['Manufacturing','Construction & Engineering','B2B SaaS','Distribution','Professional Services'],'Opportunity':[96,92,90,84,78]})
    st.plotly_chart(px.bar(df,x='Industry',y='Opportunity'),use_container_width=True)

elif menu=='Package Analysis':
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)
    st.dataframe(packages.sort_values('Success %',ascending=False),use_container_width=True)

elif menu=='Email Strategy':
    emails=['Growth Opportunity Audit','Increase Qualified B2B Leads','Your Competitor Digital Gap','90 Day Pipeline Growth Plan','Market Expansion Opportunity','Free Growth Assessment','Revenue Growth Strategy','Improve Customer Acquisition','Website Conversion Review','Strategic Growth Partnership']
    st.table(pd.DataFrame({'Email Hook':emails}))

elif menu=='SWOT':
    st.write('Strengths: Full-service digital marketing capability and strategic execution.')
    st.write('Weaknesses: Need local market proof and references.')
    st.write('Opportunities: Strong B2B demand for lead generation and growth systems.')
    st.write('Threats: Strong agencies, trust barrier, long buying cycles.')

else:
    st.table(pd.DataFrame({'Problem':['Trust Barrier','Long Sales Cycle','Competition'],'Solution':['Case Studies + Proof','Nurturing Sequence','Vertical Positioning']}))
