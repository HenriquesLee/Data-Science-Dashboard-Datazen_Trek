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

st.title("Cool Features")

st.write("""
The **AI-Powered Data Science Dashboard** is packed with some really cool features designed to make data exploration and machine learning fun and easy!

### 1. **Live CSV Upload**:
- You can upload your dataset in CSV format and see the results instantly! The tool processes your data in real-time, no delays, no waiting around. Just upload, and boom — your data is ready for exploration.

### 2. **Interactive Correlation Matrix**:
- With a simple click, you can visualize the correlation between different numeric columns. This helps you quickly identify which features are most related to each other, which can be especially useful when building predictive models.

### 3. **Pair Plot Magic**:
- Visualize the relationships between all your variables with the interactive **pair plot**. It helps you spot patterns, relationships, or even outliers in your data.

### 4. **Linear Regression at Your Fingertips**:
- Ever wanted to see how one feature affects another? With just a couple of clicks, you can run a linear regression model. It even calculates key metrics like **R²**, **MAE**, and **RMSE** — all without writing a single line of code!

### 5. **Responsive and Mobile-Ready**:
- This dashboard isn't just desktop-friendly — it's fully responsive, meaning you can use it on your phone or tablet too! Perfect for when you're on the go but still want to analyze data.

### 6. **Sleek Design**:
- Who said data dashboards have to be boring? With the stunning design and smooth UI, this dashboard is a joy to use.

Whether you're a pro or a beginner, this tool has everything you need to explore, visualize, and model your data in an engaging way!
""")
