import streamlit as st

# Set the background image using HTML and CSS
background_image = """
<style>

[data-testid="stSidebarContent"] {
    background-image: linear-gradient(to bottom right, #290e47, #341c5c);
}

[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnJ1bm52Z3FoYXF6bHphZHM3NHMzMzV0a2l6bHd4Z2lsaTNnc3NtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TxVVB6PfWMjE4/giphy.gif");
    background-size: cover;
    background-position: center;  
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

st.title("About AI-Powered Data Science Dashboard")

st.write("""
Welcome to the **AI-Powered Data Science Dashboard**!

This tool was designed by **Lee Henriques** as part of the **Datazen Trek Project**, with the goal of making data science more accessible to everyone. Whether you're a data scientist, analyst, or just someone curious about data, this dashboard provides powerful visualization and machine learning capabilities.

### Why Use This Dashboard?
- **Real-time Analysis**: Upload your data and get insights instantly.
- **Machine Learning on the Fly**: Perform linear and multiple linear regression with ease.
- **Data Visualization**: Understand your data with intuitive and interactive charts.
- **User-Friendly**: No need to code! Just upload a CSV and the tool takes care of the rest.

### Who is it for?
This tool is perfect for:
- **Data Enthusiasts**: Looking to explore their datasets.
- **Students**: Learning about data science and wanting hands-on experience.
- **Business Analysts**: Needing quick insights without complicated processes.
- **Developers**: Wanting a simple yet powerful dashboard for quick data analysis.

Enjoy exploring your data with AI-powered insights!
""")
