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

data = get_rpi_data()
st.line_chart(data)
st.header("Select RPI")
get_rpi = st.selectbox('',list(data.keys())[::-1])
if(get_rpi):
    rate = data[get_rpi]
    st.text("rpi is : "+str(rate))
