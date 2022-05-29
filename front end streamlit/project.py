import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import io
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
sns.set(style="darkgrid", color_codes=True)




st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    choose = option_menu("Dashboard", ["About Project","Problem Statement","Brief Description","Project Process","YouTube Analtyics", "Send an email"],
                         icons=['journal-richtext','', 'signpost','reception-4','columns-gap', 'envelope'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#faf5f7"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#f1c9ff"},
        "nav-link-selected": {"background-color": "#ffbf1f"},
    }
    )
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#-------navigation bar---------------------

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #fc0341;">
   <a class="nav-link disabled" href="#"><span class="sr-only">(current)</span></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
       <a class="navbar-brand" href="https://github.com/Druti0509/Youtube_Analysis" target="_blank">My Git Hub Code</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#--------------------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:/Users/druti/OneDrive/Desktop/Project/front end streamlit/style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_coding1= load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_li9krdlx.json")
lottie_coding2= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_6ywhhblw.json")
lottie_coding3= load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_57yvxdqx.json")
lottie_coding4= load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_7zjif55a.json")

img1 = Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/ted-logo.png")
img2 = Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/nasa-logo.png")
img3 = Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/bbc-logo.png")
img4 = Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/tg-logo.jpg")
img5 = Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/t-logo.webp")


#------------------------------------------------------------------------------------------------------------------------------------------------

#-----About Project------


if choose == "About Project":
    col1, = st.columns([0.8])
    with col1:              
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    st.subheader("Hi, I am Druti Negi:wave:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("I am from Jodhpur (Rajasthan). ")
        st.write("I am currently enrolled in B.Tech 2nd year undergraduate degree program ")
        st.write("from Jodhpur Institute of Engineering in Design and Technology, Jodhpur.")
        st.write("This is my first Microsoft Intern Engage 2022 program ")
        st.write("Here I have done a Data Analysis of YouTube Channels and")
        st.write("Click on the GitHub Link to view my Project code on YouTube Analytics there.")
    with right_column:
        st_lottie(lottie_coding1, height=300, key="coding1")

#-------------------------------------------------------------------------------------------------------------------------------------------------

 # ---- Problem Statement ----
    with st.container():
        st.title("Problem Statement: Data Analysis ")
        st.write(".......As Stated by Microsoft.......")
        st.write("Develop an application to demonstrate how the Information Technology Industry could harness data to take informed decisions.")
        st.write("You could choose to use the data set provided, or use any open-source data set available you might have access to, or create your own.")
        st.write("Demonstrate the use of data analytics in identifying:Customer segments, Most popular product specifications , Right time to launch a new product, etc Any other queries you can think of it.")
   
  #----------------------------- 
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding2, height=300, key="coding2")
        st.header("YouTube Analysis -> To demonstrate how YouTube analyse data.")

        st.write("")
        st.write(
            """
            Insights About YouTube :
              
              - YouTube is one of the most popular and premier video-sharing platforms by Google.
              - It is also World’s second largest Search Engine.
              - It provides numerous functionalities to optimize, refine content, promotion, viewer engagement strategies.
              - It has well-designed recommendation system till date.

            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------

    with st.container():      
        st.subheader("Discovering Data ")
        left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """ 
            1. Import Libraries/Packages &
               Set configurations for Data Visualization Plots

                      ->Import Data
            
            2.Explore Data

                      ->Identifying type/category of data 

                      ->Data cleaning -missing values + Data Wrangling

                      ->Data Filtering

                      ->Data Preparation (Tabular form)

                      ->Feature Generation + Feature Selection

            3.Visualize Data

                      ->Types of visualizations

            4.Extract Preliminary Insights

            5.Evaluation Metrics
            
            """)
    with right_column:
        st_lottie(lottie_coding4, height=300, key="coding4")
#-----------------------------------------------------------------------------------------------------------------------

if choose == "Send an email":
    col4, = st.columns([2.0])
    with col4:              
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> Contact </p>', unsafe_allow_html=True)    
                 
    

    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------Brief Description---------------------
# ---- YouTube Analysis ----
# ------TED-------------------------------------------------
with st.container():
    st.write("---")
    st.header(" Brief Description about YouTube Channels that i have analysed ")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("TED YouTube Channel")
        st.write(
            """
            The TED Talks channel features the best talks and performances from the TED Conference,
            where the world's leading thinkers and doers give the talk of their lives in 18 minutes (or less). 
            Look for talks on Technology, Entertainment and Design -- plus science, business, global issues, the arts and more.
           
            """
        )
        st.write("21.3M subscribers")
        st.write("Joined 7 Dec 2006")
        st.write("2,327,150,579 views")

#--------NASA----------------------------------------------------        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("NASA YouTube Channel")
        st.write(
            """
           NASA's mission is to pioneer the future in space exploration, scientific discovery and aeronautics research.
           To do that,  we have worked around the world -- and off it -- for more than 50 years, 
           searching for answers to fundamental questions about our place in the universe. 
           We're exploring space and discovering Earth. 
           
            """
        )
        st.write("10M subscribers")
        st.write("Joined 4 Jun 2008")
        st.write("797,920,149 views")
        
#----------------BBC EARTH--------------------------------------
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("BBC Earth YouTube Channel")
        st.write(
            """
            Celebrating nature, science, space and the human race, BBC Earth brings you face to face with heart-pounding action,
            mind-blowing ideas and the sheer wonder of being part of this amazing planet we call home. 

           BBC Earth is the official channel of well-known Sir David Attenborough series such as Planet Earth, Frozen Planet and Blue Planet II. 
           It is also where you can find fantastic nature and wildlife documentaries such as Life of Mammals and classics like Planet Dinosaur.

            """
        )
        st.write("11.2M subscribers")
        st.write("Joined 25 Feb 2009")
        st.write("3,983,762,955 views")
        
#--------------TECHNICAL GURUJI-----------------------------------
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img4)
    with text_column:
        st.subheader("Technical Guruji YouTube Channel")
        st.write(
            """
            Hello friends, Welcome to "Technical Guruji", I created this channel on 18th October 2015, 
            my motive behind creating this channel is to make easy to understand, Tech Videos in Hindi, and 
            I want each and every individual whoever is interested in technology to be able to understand it in the easiest possible way.
            I post two videos daily, on topics that cover latest technology and tech news. Please SUBSCRIBE to Technical Guruji, 
            Thanks.जय हिन्द, वन्दे मातरम|
             
            """
        )
        st.write("22.1M subscribers")
        st.write("Joined 19 Oct 2015")
        st.write("3,004,753,279 views")
        

#--------------tseries-------------------------------------------
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img5)
    with text_column:
        st.subheader("TSeries YouTube Channel")
        st.write(
            """
            "Music can change the world". T-Series is India's largest Music Label & Movie Studio, believes in bringing world close together through its music.
            T-Series is associated with music industry from past three decades, having ample catalogue of music comprising plenty of languages that covers the length & breadth of India. 
            We believe after silence, nearest to expressing the inexpressible is Music.
            So, all the music lovers who believe in magic of music come join us and live the magic of music with T-Series.
             
            """
        )
        st.write("217M subscribers")
        st.write("Joined 13 Mar 2006")
        st.write("192,039,833,258 views")
        
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
# ---- Visualization ----


st.title('Data Visualizations ')

with st.expander('Plots :'):
     st.write('Bar plot')
     st.write('Scatter plot')
     st.write('Pie plot')
     st.write('Dis plot')
     st.write('Violin plot')
     st.write('Donut plot')
     st.write('Hist plot')
      

video_stats=pd.read_csv("C:/Users/druti/OneDrive/Desktop/Project/Youtube-Analysis/TED.csv")
comments_stats=pd.read_csv("C:/Users/druti/OneDrive/Desktop/Project/Youtube-Analysis/TED_comments.csv")
channel_stats=pd.read_csv("C:/Users/druti/OneDrive/Desktop/Project/Youtube-Analysis/channels.csv")

st.title("Channel Statistics")
st.write(channel_stats)

st.title("Video Details")
st.write(video_stats)

st.title("Comments Info")
st.write(comments_stats)


st.title("Does Views and Like correlate?")
h_labels = [x.replace('_', ' ').title() for x in 
            list(video_stats.select_dtypes(include=['number', 'bool']).columns.values)]

fig, ax = plt.subplots(figsize=(10,6))
_ = sns.heatmap(video_stats.corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax)
st.write(fig)

st.title("Relation of views and like with new uploads on a day of week")
im1= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/1.png")
st.image(im1)

st.title("video definition")
im2= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/2.png")
st.image(im2)

st.title("publish time v/s year")
im3= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/3.png")
st.image(im3)

st.title("Video Duration")
im4= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/4.png")
st.image(im4)

st.title("Comments and Likes V/S Views")
im5= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/5.png")
st.image(im5)

st.title("Comment and Like Ratio per Views")
im6= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/6.png")
st.image(im6)


st.title("Number of videos which are having Less watch time duration")
im7= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/7.png")
st.image(im7)

st.title("Comments and Likes V/S Watch Time Duration")
im8= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/8.png")
st.image(im8)

st.title("Title Length V/S Views")
im9= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/9.png")
st.image(im9)

st.title("Channel Name with number of subscribers")
im10= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/10.png")
st.image(im10)

st.title("Channel Name with number of views")
im11= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/11.png")
st.image(im11)

st.title("Number of Tags per View")
im12= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/12.png")
st.image(im12)

st.title("Most Uploads on a Day of WeekPercentage of Subscribers Per Youtube Channel")
im13= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/13.png")
st.image(im13)

st.title("Percentage of Subscribers Per Youtube Channel")
im14= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/14.png")
st.image(im14)

st.title("Percentage of Total Videos posted on Different Channels")
im15= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/15.png")
st.image(im15)

st.title("Best Video critics on this Channel")
im16= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/16.png")
st.image(im16)

st.title("Worst Video critics on this Channel")
im17= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/17.png")
st.image(im17)

st.title("Number of Videos per Title Length")
im18= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/18.png")
st.image(im18)

st.title("Number of likes per Title length")
im19= Image.open("C:/Users/druti/OneDrive/Desktop/Project/images/19.png")
st.image(im19)











# ---- Send an ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your Email address" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
       
