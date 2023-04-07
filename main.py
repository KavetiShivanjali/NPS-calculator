import streamlit as st
import numpy as np
from PIL import Image

st.markdown("<h1 style='text-align: center; color: white;'>NPS Calculator😉</h1>", unsafe_allow_html=True)
image = Image.open('net-promoter-score-1.jpg')
st.image(image, caption='NPS',width = 650)
score = float('inf')
with st.sidebar:
    uploaded_file = st.file_uploader("Choose ratings file")

    if uploaded_file is not None:
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
             if st.button('Calculate'):
                data = np.loadtxt(uploaded_file,dtype = 'int')
                total = data.shape[0]
                promoters = (data[data>8].shape[0])*100/total
                demoters = (data[data<7].shape[0])*100/total
                score = promoters-demoters
        with col3:
            st.write(' ')
        #st.write(dataframe)
if(score != float('inf')):
    st.write('NPS Score: ',score)
    if(score < 30):
        st.write('Your Business is not doing well, Please improve your services')
    elif(score == 50):
        st.write('Your Business is doing excellent!!')
    else:
        st.write('Customers are very much satisfied by your business!!')


    
