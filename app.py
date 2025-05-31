import streamlit as st

st.title('Good Foodz')

col1, col2 = st.columns(2)

with col1:
    st.image('fooodz.jpg')
with col2: 
    st.write("""When writing a description for a food website, you should include information such as your location, cuisine type, and restaurant name. If you are known for a specific dish, it can also be helpful to include the name of that dish. To make a food website effective, it should be visually appealing with high-quality photos and a clean, visually cohesive design. It should also be easy to navigate with a clear hierarchy of information and a logical layout.
""")
    
st.header("All Foods Catogery")
st.subheader("Paneer")
st.subheader("Burger & momos")
st.subheader("Chinese")
st.subheader("Rolls")
st.subheader("Pizza")
st.subheader("Paratha")
st.subheader("Lassi")

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- log in 
- Careers
- Near Restaurent 
- Locations                                       
""")

option = st.sidebar.selectbox('Select one',['Veg','Non-Veg'])
btn = st.sidebar.button('Select')

if btn:
    st.title(option + "food lists")