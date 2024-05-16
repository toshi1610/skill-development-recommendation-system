import streamlit as st
import os
st.set_page_config(page_title="Feedback", page_icon="📄",initial_sidebar_state="collapsed")
import streamlit as st
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
def main():
    st.title("Feedback Form")

    # Input fields for name, email, feedback category, and feedback message
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback_category = st.selectbox("Feedback Category", ["General", "Bug Report", "Feature Request"])
    feedback_message = st.text_area("Feedback Message")

    # Submit button
    if st.button("Submit"):
        if not name or not email or not feedback_message:
            st.error("Please fill in all required fields.")
        elif not "@" in email or not "." in email:
            st.error("Please enter a valid email address.")
        else:
            # Store the feedback data in a dictionary
            feedback = {
                "Name": name,
                "Email": email,
                "Category": feedback_category,
                "Message": feedback_message
            }
            # Save the feedback to a text file
            save_feedback(feedback)

            # Display confirmation message
            st.success("Thank you for your feedback! We have received your submission.")
            st.markdown("### Submitted Details")
            st.markdown(f"**Name:** {name}")
            st.markdown(f"**Email:** {email}")
            st.markdown(f"**Category:** {feedback_category}")
            st.markdown(f"**Message:** {feedback_message}")

def save_feedback(feedback):
    current_dir = os.getcwd()

    # Specify the file path in the current directory
    file_path = os.path.join(current_dir, "feedback_data.txt")

    # Use file_path in the save_feedback function
    with open(file_path, "a") as file:
        file.write(f"Name: {feedback['Name']}\n")
        file.write(f"Email: {feedback['Email']}\n")
        file.write(f"Category: {feedback['Category']}\n")
        file.write(f"Message: {feedback['Message']}\n\n")

if __name__ == "__main__":
    main()
