import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Aina's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - February 2025***")
    st.write("**Author:** Aina Lluis Huelmo")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Aina</h1></div>""", unsafe_allow_html=True)


# ----- Profile image file -----
profile_image_file_path = "data/profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Data Scientist"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am currently working as a Data Scientist in Xvolv.

- 🛩️ Student of the master in Big Data & Business Analytics. Previously graduated in Applied Statistics.

- ❤️ High interest in data modelling, Data Science and Big Data

- 🏂 I love travelling and skiing 

- 📫 How to reach me: ainalluis3@gmail.com

- 🏠 L'Ametlla del Vallès, Barcelona

- Linkedin: www.linkedin.com/in/aina-lluis

- Github: https://github.com/ainalluis1/eae_ipld_project.git



""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
