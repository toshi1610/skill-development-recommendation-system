import streamlit as st
from streamlit_option_menu import option_menu
# Set page title and icon
st.set_page_config(page_title="Home", page_icon="📄",initial_sidebar_state="collapsed")
page = option_menu(
        menu_title = None,
        options=["Home","About","Services","Contact"],
        icons=["house","book","body-text","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

# Navigation bar
st.markdown("""
<style>
.navbar {
  overflow: hidden;
  background-color: #333;
  width: 100%;
}

.navbar a {
  float: left;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 20px;
  text-decoration: none;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
  <a href="#">Home</a>
  <a href="resume">Resume Anylazer</a>
  <a href="sde">SDE</a>
  <a href="web_dev">Web Devlopment</a>
  <a href="ml">Machine Learning</a>
</div>
""", unsafe_allow_html=True)

# Main title
st.title("SKILL DEVELOPMENT RECOMMENDATION SYSTEM")

# Create a container for the main content
main_container = st.container()

# About Us section
with main_container:
    st.markdown("<h2 id='about'>About Us</h2>", unsafe_allow_html=True)
    st.write("Welcome to Skill Development Recommendation System, your personalized guide to acquiring new skills and advancing your career. Our platform is designed to help you discover relevant and in-demand skills based on your interests, experience, and career goals.")
    st.write("At Skill Development Recommendation System, we understand that continuous learning is key to success in today's fast-paced world. Whether you're looking to upskill for a new job, enhance your current skills, or explore new career paths, our platform provides personalized recommendations to help you achieve your goals.")

# Services section
with main_container:
    st.markdown("<h2 id='services'>Services</h2>", unsafe_allow_html=True)
    st.write("- Skill Assigment\n- Resume Anylasis\n- Skill Recommendation")

# Contact Us section
with main_container:
    st.markdown("<h2 id='contact'>Contact Us</h2>", unsafe_allow_html=True)
    st.write("Email: example@example.com\nPhone: 123-456-7890")

# Add some spacing
st.write("")
st.write("")
st.markdown("<h3>Feedback Form</h3>", unsafe_allow_html=True)
st.markdown("[Click here to provide feedback](feedback)")
# Footer
st.markdown("---")
st.write("Copyright © 2024 My Website")
