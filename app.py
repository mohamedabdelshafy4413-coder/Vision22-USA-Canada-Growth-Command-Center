import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 USA Canada Market Strategy',page_icon='🌎',layout='wide')

st.title('🌎 Vision22 | دراسة دخول سوق أمريكا وكندا')
st.caption('B2B Digital Marketing Market Entry Strategy')

menu=st.sidebar.radio('القائمة',[
'الرئيسية','تحليل السوق','الباقات والخدمات','ترتيب فرص النجاح','Email Campaign','SWOT Analysis','المخاطر والحلول'])

packages=pd.DataFrame({
'Package':['Lead Generation Engine','Website & Conversion System','Performance Growth System','Growth Foundation','Digital Authority System','Complete B2B Marketing Department','International B2B Expansion'],
'Success %':[90,85,82,78,75,70,65],
'Market Opportunity %':[95,92,90,86,80,85,70],
'Price':['$10K-$20K/mo','$7K-$15K/mo','$10K-$25K/mo','$5K-$10K/mo','$7K-$15K/mo','$15K-$50K/mo','$20K+']
})

if menu=='الرئيسية':
    a,b,c,d=st.columns(4)
    a.metric('أفضل نقطة دخول','B2B Lead Generation')
    b.metric('أفضل قطاعات','Manufacturing + SaaS')
    c.metric('متوسط العميل','$7K-$50K')
    d.metric('فرصة 90 يوم','High')
    st.dataframe(packages,use_container_width=True)

elif menu=='تحليل السوق':
    st.header('أقوى نقطة دخول للسوق')
    st.write('🇺🇸 USA: Manufacturing - Construction - B2B SaaS - Distribution')
    st.write('🇨🇦 Canada: Ontario - Alberta - British Columbia')
    chart=pd.DataFrame({'Industry':['Manufacturing','Construction','B2B SaaS','Distribution'],'Opportunity':[95,90,88,82]})
    st.plotly_chart(px.bar(chart,x='Industry',y='Opportunity'),use_container_width=True)

elif menu=='الباقات والخدمات':
    st.header('Vision22 Services & Packages')
    st.dataframe(packages,use_container_width=True)

elif menu=='ترتيب فرص النجاح':
    st.header('ترتيب الباقات من الأعلى فرصة للأقل')
    st.plotly_chart(px.bar(packages,x='Package',y='Success %'),use_container_width=True)

elif menu=='Email Campaign':
    emails=['Growth Opportunity Audit','Increase Qualified B2B Leads','Your Digital Growth Gap','90 Day Pipeline Growth Plan','Market Expansion Opportunity','Free B2B Marketing Review','Revenue Growth Strategy','Improve Your Lead Generation','Website Conversion Analysis','Strategic Growth Partnership']
    st.header('أفضل 10 Email Hooks')
    st.table(pd.DataFrame({'Email':emails}))

elif menu=='SWOT Analysis':
    st.write('Strengths: فريق متكامل وخبرة تنفيذية متعددة الخدمات')
    st.write('Weaknesses: بناء الثقة في سوق جديد')
    st.write('Opportunities: طلب مرتفع على B2B Growth')
    st.write('Threats: منافسة قوية وطول دورة البيع')

else:
    st.header('المشاكل والحلول')
    st.table(pd.DataFrame({'Problem':['Trust','Long Sales Cycle','Competition'],'Solution':['Case Studies + Proof','Nurturing + Follow Up','Strong Positioning']}))
