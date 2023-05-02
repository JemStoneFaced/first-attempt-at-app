import streamlit as st
import pandas as pd
import numpy as np

def foo():
    print("bar")
   
st.set_page_config(layout='wide')
st.title("First attempt at a GUI")
tab1, tab2, tab3, tab4, tab5=st.tabs(["clickers",'dropdowns', 'sliders',"graphs",'attachments'])

with tab1:
    st.header('terms of service')
    col1_t1,col2_t1=st.columns(["button","check_box"])
    with col1_t1:
        st.subheader('button')
        st.button('agree')
        st.button('disagree')
    with col2_t1:
        st.subheader('checkbox')
        st.checkbox('I agree')
with tab2:
    st.header("decisions, decisions")
        col1_t2,col2_t2,col3_t2=st.columns([1,1,1])
        with col1_t2:
            st.radio('platform', ["mobile", 'PC', 'console'])
        with col2_t2:
            st.selectbox('pet', ['doggo', 'kitr', 'hampter'])
        with col3_t2:
            st.multiselect('make a smoothie:', ['banana', 'apple', 'orange','mango','kiwi']
with tab3:
    st.header("sliders")
    col1_t3,col2_t3,col3_t3=st.columns([1,1,1])
    with col1_t3:
        st.slider('rate your mood',[1,2,3,4,5,6,7,8,9,10])
    with col2_t3:
        st.select_slider('how much cheese slices on your burger?',[0,1,2,3]
    with col3_t3:
        st.text_input('compose some top tier literature')
with tab4:
    col1_t4,col2_t4=st.columns([5,2])
    data=np.random.randint(10,1)
    with col1_t4:
        st.subheader("hours of sleep for the average college student")
        st.linechart(data)
with tab5:
    st.image(https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fe6%2F44%2F25%2Fe64425a44b748cb9426a1df927ac49c5.jpg&f=1&nofb=1&ipt=784e1cc6c2602cf433ad2be569ee7484da835148a0157dde6674d8d3f44b8dc2&ipo=images,width=100)
