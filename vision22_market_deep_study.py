import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Market Deep Study', page_icon='🌎', layout='wide')

st.title('🌎 Vision22 | USA & Canada B2B Market Deep Study')
st.caption('Detailed Market Entry Analysis | Services Strategy | Sales Opportunity Model')

menu = st.sidebar.radio('الأقسام', [
    'Executive Summary',
    'Market Entry Strategy',
    'Target Industries',
    'Package Ranking',
    'Email Campaign Strategy',
    'SWOT Analysis',
    'Risks & Solutions'
])

packages = pd.DataFrame({
    'Package': [
        'Lead Generation Engine',
        'Website & Conversion System',
        'Performance Growth System',
        'Growth Foundation',
        'Digital Authority System',
        'Complete B2B Marketing Department',
        'International B2B Expansion'
    ],
    'Success %':[92,86,84,80,76,72,68],
    'Opportunity %':[96,93,91,87,82,85,70],
    'Price':['$10K-$20K/mo','$7K-$15K/mo','$10K-$25K/mo','$5K-$10K/mo','$7K-$15K/mo','$15K-$50K/mo','$20K+']
})

if menu == 'Executive Summary':
    a,b,c,d=st.columns(4)
    a.metric('أفضل نقطة دخول','B2B Lead Generation')
    b.metric('أفضل قطاعات','Manufacturing + SaaS')
    c.metric('Retainer Potential','$7K-$50K')
    d.metric('90 Day Success','High')
    st.dataframe(packages, use_container_width=True)

elif menu == 'Market Entry Strategy':
    st.header('أقوى استراتيجية دخول')
    st.write('1- Start with B2B companies needing predictable leads.')
    st.write('2- Target companies with high customer lifetime value.')
    st.write('3- Use Audit + Growth Opportunity approach.')

elif menu == 'Target Industries':
    df=pd.DataFrame({'Industry':['Manufacturing','Construction','B2B SaaS','Distribution','Professional Services'],'Opportunity':[96,91,90,84,78]})
    st.plotly_chart(px.bar(df,x='Industry',y='Opportunity'),use_container_width=True)

elif menu == 'Package Ranking':
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)
    st.dataframe(packages.sort_values('Success %',ascending=False))

elif menu == 'Email Campaign Strategy':
    emails=[
    'Growth Opportunity Audit For Your Company',
    'How To Increase Qualified B2B Leads',
    'Your Digital Growth Gap Analysis',
    '90 Day Pipeline Growth Opportunity',
    'Competitive Advantage Review',
    'B2B Revenue Growth Strategy',
    'Free Marketing Performance Review',
    'Improve Your Customer Acquisition System',
    'Website Conversion Opportunity',
    'Strategic Growth Partnership'
    ]
    st.table(pd.DataFrame({'Email Subject':emails}))

elif menu == 'SWOT Analysis':
    st.write('Strengths: Complete digital marketing capability and international delivery.')
    st.write('Weaknesses: Need trust building and local proof.')
    st.write('Opportunities: Strong B2B demand in USA and Canada.')
    st.write('Threats: Competition and longer sales cycles.')

else:
    st.table(pd.DataFrame({
        'Problem':['Low Trust','Long Sales Cycle','High Competition'],
        'Solution':['Case Studies + Proof','Nurturing + Follow Up','Niche Positioning']
    }))
