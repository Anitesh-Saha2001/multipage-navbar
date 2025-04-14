import streamlit as st
from streamlit_navigation_bar import st_navbar
original_title ='''<p style="font-size: 50px; font-weight: bold;color: #333; 
    text-shadow: 
        1px 1px 0px #eab,  /* Top-left shadow (light) */
        2px 2px 0px #ccc,  /* Middle-left shadow */
        3px 3px 0px #999;  /* Bottom-left shadow (dark) */
    font-family: Times new roman;"><b>SMART HIRING SYSTEM</b></p>'''
st.markdown(original_title, unsafe_allow_html=True)

# Initialize session state
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Dummy authentication
def sign_in(username, password):
    if username in st.session_state.users and st.session_state.users[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
    else:
        st.error("Invalid credentials")

def sign_up(username, password):
    if username in st.session_state.users:
        st.warning("Username exists!")
    else:
        st.session_state.users[username] = password
        st.success("Registered! Please log in.")

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# Login or Sign-up
if not st.session_state.logged_in:
    st.title("🔐 Login Portal")
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
    
    with login_tab:
        user = st.text_input("Username", key="login_user")
        pwd = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            sign_in(user, pwd)

    with signup_tab:
        new_user = st.text_input("New Username", key="signup_user")
        new_pass = st.text_input("New Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            sign_up(new_user, new_pass)

# Top Nav UI
else:
    option = st_navbar(
        ["Home", "Interview Section", "Logout"],
        selected="Home"
    )

    st.title(f"👋 Welcome, {st.session_state.username}!")

    if option == "Home":
        from pages.Home import show_home
        show_home()
    elif option == "Interview Section":
        from pages.Interview import show_interview
        show_interview()
    elif option == "Logout":
        logout()
        st.rerun()
