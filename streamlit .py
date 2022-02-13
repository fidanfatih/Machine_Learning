# streamlit run app.py

import streamlit as st
#text/title
st.title("Streamlit Tutorials")
st.text('Hello Streamlit !')

# header/subheader
st.header('This is header...')
st.subheader('This is subheader...')

# markdown
st.markdown('### This is a markdown')
st.markdown('## This is a markdown')
st.markdown('# This is a markdown')

# bold
st.markdown('**This is a markdown**')

# yazi yesil
st.markdown('`This is a markdown`')

# italik
st.markdown("_This is a Markdown_")


# arka fon yesil
st.success("Succesful")

# arka fon mavi
st.info("This is an information...")

# arka fon sari
st.warning("This is an yellow information...")

# arka fon red
st.error("This is an error...")

# st.help(st.info)

# st.help(range)
    
# writing text
st.write('This is write function')

# images
from PIL import Image
im = Image.open("esra.png")
st.image(im, width=300, caption="**ESRA**")

im = Image.open("azra.png")
st.image(im, width=300, caption="**AZRA**")

# video File
vid_file=open('video.mp4','rb')
st.video(vid_file)


# checkbox olusturur, tik koymaniza gore sart olusturup kod ona gore aksiyon alir.
if st.checkbox('Show/Hide'):
    st.text("I'am showing because you checked the box.")
else:
    st.text("I do not show")
    
# radio buttons
status = st.radio("What is your status?",("Active", "Inactive"))

# st.help(st.radio)

if status=='Active':
    st.success("Yor are ACTIVE...")

else:
    st.warning("You are INACTIVE...")
    
# selectbox
occupations=st.selectbox("Your Occupation", ["Programmer","Data_Scientist","Doctor"])

options=st.selectbox("Your Occupation", list(range(1,5)))

st.write("You selected this option:",occupations)

# multiselect
location=st.multiselect("Where do you work?", ("London","Istanbul","Moscow","Berlin"))

st.text(f"You have selected {len(location)} location(s)")

# slider
level=st.slider('What is your level',0,40)

# inputlari 5 er 5er alir
level=st.slider('What is your level',0,40,step=5)

# slider icinde ilk secilen default olarak 10 secer
level=st.slider('What is your level',0,40,10,step=5)
st.write("You selected",level)


# Button
st.button("Simple Button")
# Tum deger ve degiskenleri aldiktan sonra ML Modeli calistirmadan once button koyularak daha sik olur.

import webbrowser
url ='https://www.youtube.com/watch?v=SvWrEnfzIZo'
if st.button('Play Video'):
    webbrowser.open_new_tab(url)
    
if st.button('Run'):
    st.write("ML Model is running...")
    
# text input
firstname=st.text_input("Enter your Firstname")

if st.button('Submit'):
    st.success(firstname.capitalize())
    
#text area, default degeri var (Type Here...)
message=st.text_area('Enter your text',"Type Here...")

if st.button('load'):
    result=message.capitalize()
    st.success(result)
    
#date input
import datetime
today=st.date_input("Today is",datetime.datetime.now())

d = st.date_input("When's your birthday", datetime.date(1984, 3, 1))
st.write('Your birthday is:', d)

# time input
the_time=st.time_input("The time is", datetime.time(8,37))

# Raw data
st.text("Display Text")
#single code
st.code('import numpy as np') # metnin sonuna kopyala ozelligi eklenir.

#multiple codes
with st.echo(): # alttaki lines hepsi st.code() icinde gibi yazdirir.
    import numpy as np
    import pandas as pd
    
# #progress bar
# # Program loading deki gibi yukleme simulasyonu olusturur.
# import time
# my_bar=st.progress(0)
# for p in range(70):
#     my_bar.progress(p+1)
#     time.sleep(0.1)


# # spinner
# # yazilan mesaj belirlenen sure kadar ekranda gorunur. SOnunda yine istenilen baska mesaj gosterilir ve balon gosterisi yapar.
# import time
# with st.spinner("Waiting....."):
#     time.sleep(3)
# st.success("Finished")
# st.balloons()

# sayfanin sol tarafina tiklayinca cikan pencerede text yazdirilir.
st.sidebar.title("Churn probability of a Single Customer")
# st.markdown(html_temp,unsafe_allow_html=True)
# st.markdown(
#     f'''
#         <style>
#             .sidebar.sidebar-content {{
#                 width: 500px;
#             }}
#         </style>
#     ''',
#     unsafe_allow_html=True)

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Richard Title </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

import pickle
import pandas as pd
df=pickle.load(open('df_saved.pkl',"rb"))
st.write(df.head())

st.table(df.head())
st.dataframe(df.head())


tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))

def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample

df = single_customer()

st.table(df)


    