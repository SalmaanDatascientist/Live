import streamlit as st
import json
import os
import time

# --- CONFIGURATION ---
DATA_FILE = "class_data.json"
st.set_page_config(page_title="Molecular Man Portal", page_icon="🧪")

# --- DATABASE FUNCTIONS (To sync Admin and Student) ---
def load_data():
    if not os.path.exists(DATA_FILE):
        # Default state
        return {"is_live": False, "discord_link": "", "topic": "General Session"}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(is_live, link, topic):
    data = {"is_live": is_live, "discord_link": link, "topic": topic}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# --- AUTHENTICATION ---
def login_user(username, password):
    if username == "admin" and password == "admin":
        return "admin"
    elif username == "demo" and password == "demo":
        return "student"
    else:
        return None

# --- INITIALIZE SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.username = None

# --- UI: LOGIN PAGE ---
def show_login_page():
    st.markdown("<h1 style='text-align: center;'>🧪 Molecular Man Login</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                user_role = login_user(username, password)
                if user_role:
                    st.session_state.logged_in = True
                    st.session_state.user_type = user_role
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")

# --- UI: ADMIN DASHBOARD ---
def show_admin_dashboard():
    st.title("🛠️ Admin Control Panel")
    st.success(f"Welcome back, {st.session_state.username}")
    
    # Load current status
    current_data = load_data()
    
    st.divider()
    
    st.subheader("📢 Live Class Controls")
    
    with st.form("admin_controls"):
        topic_input = st.text_input("Class Topic", value=current_data['topic'])
        # Admin pastes the specific Discord Voice Channel link here
        link_input = st.text_input("Discord Invite/Channel Link", value=current_data['discord_link'])
        
        status_radio = st.radio("Class Status", ["Offline", "Live"], index=1 if current_data['is_live'] else 0)
        
        update_btn = st.form_submit_button("Update Status")
        
        if update_btn:
            is_live = True if status_radio == "Live" else False
            save_data(is_live, link_input, topic_input)
            st.success("✅ Class status updated successfully! Students can now see the changes.")
            time.sleep(1)
            st.rerun()

    st.info("💡 Tip: Copy the Discord Voice Channel link (Right Click Channel -> Copy Link) and paste it above.")

# --- UI: STUDENT DASHBOARD ---
def show_student_dashboard():
    st.title("🎓 Student Portal")
    st.write(f"Logged in as: {st.session_state.username}")
    
    st.divider()
    
    # Read live data
    data = load_data()
    
    st.subheader("Live Class Status")
    
    if data['is_live']:
        st.success("🔴 CLASS IS LIVE NOW")
        st.markdown(f"### Topic: {data['topic']}")
        
        # Big Join Button
        st.markdown(f"""
            <a href="{data['discord_link']}" target="_blank">
                <button style="
                    background-color: #5865F2; 
                    color: white; 
                    padding: 15px 32px; 
                    text-align: center; 
                    text-decoration: none; 
                    display: inline-block; 
                    font-size: 20px; 
                    border-radius: 8px; 
                    border: none; 
                    cursor: pointer; 
                    width: 100%;">
                    🚀 JOIN DISCORD CLASS
                </button>
            </a>
            """, unsafe_allow_html=True)
        st.caption("Clicking this will open Discord directly to the class.")
    else:
        st.error("⚫ Class is currently OFFLINE")
        st.write("Please wait for the tutor to start the session.")
        
    if st.button("🔄 Refresh Status"):
        st.rerun()

# --- MAIN APP LOGIC ---
if not st.session_state.logged_in:
    show_login_page()
else:
    # Sidebar logout for everyone
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_type = None
        st.rerun()
        
    # Router
    if st.session_state.user_type == "admin":
        show_admin_dashboard()
    elif st.session_state.user_type == "student":
        show_student_dashboard()
