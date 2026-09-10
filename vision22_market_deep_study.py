import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Deep Market Strategy',page_icon='🌎',layout='wide')

st.title('🌎 Vision22 | USA & Canada Deep Market Strategy')
st.caption('B2B Digital Marketing Entry Analysis | Packages | Sales Opportunity | Growth Plan')

menu=st.sidebar.radio('الأقسام',[
'الرؤية التنفيذية','تحليل السوق','القطاعات المستهدفة','تحليل الباقات','Email Campaigns','SWOT','المخاطر وخطة الحل'
])

packages=pd.DataFrame({
'Package':['Lead Generation Engine','Website & Conversion System','Performance Growth System','Growth Foundation','Digital Authority System','Complete B2B Marketing Department','International B2B Expansion'],
'Success %':[92,86,84,80,76,72,68],
'Opportunity %':[96,93,91,87,82,85,70],
'Price':['$10K-$20K/mo','$7K-$15K/mo','$10K-$25K/mo','$5K-$10K/mo','$7K-$15K/mo','$15K-$50K/mo','$20K+']
})

if menu=='الرؤية التنفيذية':
    a,b,c,d=st.columns(4)
    a.metric('أفضل نقطة دخول','Lead Generation Engine')
    b.metric('أفضل قطاعات','Manufacturing + SaaS')
    c.metric('Retainer','$7K-$50K')
    d.metric('90 Day Chance','High')
    st.dataframe(packages,use_container_width=True)

elif menu=='تحليل السوق':
    st.header('Market Entry Strategy')
    st.write('USA Priority: Texas, Florida, California, Illinois, North Carolina')
    st.write('Canada Priority: Ontario, Alberta, British Columbia')
    st.write('Strategy: Start with high-value B2B companies needing predictable leads.')

elif menu=='القطاعات المستهدفة':
    df=pd.DataFrame({'Industry':['Manufacturing','Construction','B2B SaaS','Distribution','Professional Services'],'Opportunity':[96,91,90,84,78]})
    st.plotly_chart(px.bar(df,x='Industry',y='Opportunity'),use_container_width=True)

elif menu=='تحليل الباقات':
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)
    st.dataframe(packages.sort_values('Success %',ascending=False),use_container_width=True)

elif menu=='Email Campaigns':
    emails=['Growth Opportunity Audit','Increase Qualified B2B Leads','Digital Growth Gap Analysis','90 Day Pipeline Growth Plan','Competitive Advantage Review','B2B Revenue Growth Strategy','Free Marketing Performance Review','Customer Acquisition Improvement','Website Conversion Opportunity','Strategic Growth Partnership']
    st.table(pd.DataFrame({'Email Subject':emails}))

elif menu=='SWOT':
    st.write('Strengths: Full digital marketing capabilities and international delivery.')
    st.write('Weaknesses: Need local trust and references.')
    st.write('Opportunities: High demand for B2B growth systems.')
    st.write('Threats: Strong agencies and long sales cycles.')

else:
    st.table(pd.DataFrame({'Problem':['Trust Building','Long Sales Cycle','Competition'],'Solution':['Case Studies + Proof','Nurturing + Follow Up','Niche Positioning + Strong Offer']}))
