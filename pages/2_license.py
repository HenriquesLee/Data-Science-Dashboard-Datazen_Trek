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

st.title("License")

st.write("""
This project is open source and licensed under the **GNU General Public License (GPL) v3.0**. Here's a brief overview of what that means:

- **Freedom to Use**: You are free to use this software for any purpose, whether it's personal, educational, or commercial.
- **Freedom to Modify**: You're allowed to modify or improve the code, adapting it to your needs.
- **Freedom to Share**: You can redistribute both the original and modified versions, as long as the same GPL license is applied.
- **Source Code Must Stay Open**: If you share your modifications, you must also make your source code available under the same terms.

I kindly ask that you credit me, **Lee Henriques**, as the original creator when distributing or sharing this project.

The full GNU GPL v3.0 License can be found [here](https://www.gnu.org/licenses/gpl-3.0.en.html).

