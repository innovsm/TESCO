import streamlit as st
import requests
from bs4 import BeautifulSoup
st.title("Rent calculator")

@st.cache_data
def get_rpi_data():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.google.com/",
    "Accept-Language": "en-US,en;q=0.9",
    }
    url = "https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l55o/mm23"
    response = requests.get(url, headers=headers)
    bsObj = BeautifulSoup(response.text, "html.parser")
    final_dict = {}
    x_1 = bsObj.find_all("td")
    while(len(x_1) != 0):
        pop_1 = x_1.pop(0).text
        pop_2 = x_1.pop(0).text
        final_dict[pop_1] = float(pop_2)
    return final_dict


# assembly line
with st.sidebar:
    st.image('https://imgs.search.brave.com/ZMF69n3XrMrrpVv0fRPRkl2RT53YMjd6MvPN5wCjhzw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi8yLzIzL1Rl/c2NvX2xvZ28ucG5n/LzIyMHB4LVRlc2Nv/X2xvZ28ucG5n')

data = get_rpi_data()
st.line_chart(data)
st.header("Select RPI")
base_rent = st.slider("Select Baserent",0,100000,step = 1)
get_rpi = st.selectbox('',list(data.keys())[::-1])
if(get_rpi):
    # rent calculation 
    rate = data[get_rpi]
    st.text("rpi is : "+str(rate))
    adjusted_rent = base_rent * (1 + rate/100)
    st.text("Adjusted rent :" + str(round(adjusted_rent)))