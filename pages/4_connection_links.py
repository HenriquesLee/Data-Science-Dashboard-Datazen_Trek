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

st.title("Connection Links")

st.write("""
Feel free to connect with me,**Lee Henriques** on the following platforms. Whether you have questions about the project, ideas for improvements, or just want to connect, these platforms are the best way to reach me!
""")

# Example dummy paths for logos
linkedin_logo = "img/LinkedIn.png"
github_logo = "img/Github.png"
leetcode_logo = "img/Leetcode.png"
gfg_logo = "img/gfg.png"

col1, col2, col3, col4 = st.columns(4)

# Display logos with links
with col1:
    st.image(linkedin_logo, width=50)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/lee-henriques/)")

with col2:
    st.image(github_logo, width=50)
    st.markdown("[GitHub](https://github.com/HenriquesLee)")

with col3:
    st.image(leetcode_logo, width=50)
    st.markdown("[LeetCode](https://leetcode.com/u/lee_henriques/)")

with col4:
    st.image(gfg_logo, width=50)
    st.markdown("[GeeksforGeeks](https://www.geeksforgeeks.org/user/2401henriques/)")

st.write("""
If you're interested in knowing more about the **AI-Powered Data Science Dashboard** or other projects, check out the my GitHub profile. I'm always open to feedback and collaboration!
""")
