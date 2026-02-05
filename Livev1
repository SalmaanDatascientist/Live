import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Molecular Man Tuition",
    page_icon="🧪",
    layout="wide"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #4B4B4B;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .live-banner {
        padding: 20px;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/123/123392.png", width=100) # Placeholder atom icon
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Live Classroom", "Class Schedule", "Notes & Resources"])

st.sidebar.divider()
st.sidebar.info("📞 Contact: +91 98765 43210\n\n📧 contact@molecularman.com")

# --- GLOBAL VARIABLES (Edit these) ---
DISCORD_INVITE_LINK = "https://discord.gg/YOUR_INVITE_CODE" # General Server Invite
# Specific link to the Voice Channel (Right click channel -> Copy Link)
DISCORD_CLASSROOM_LINK = "https://discord.com/channels/YOUR_SERVER_ID/YOUR_CHANNEL_ID" 

# --- PAGE: HOME ---
if page == "Home":
    st.markdown('<h1 class="main-header">The Molecular Man</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="sub-header">Expert Tuition Solutions for Science & Math</h3>', unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=1000", use_column_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("🧪 Chemistry")
        st.write("Master organic and inorganic chemistry with deep conceptual clarity.")
    with col2:
        st.header("📐 Mathematics")
        st.write("Solving complex problems with simple, step-by-step logic.")
    with col3:
        st.header("🧬 Biology")
        st.write("Comprehensive notes and diagrams for CBSE & ICSE curriculums.")

# --- PAGE: LIVE CLASSROOM ---
elif page == "Live Classroom":
    st.title("🔴 Live Classroom Hub")
    
    st.markdown("""
    ### How to Join
    Classes are hosted live on our private Discord server to ensure high-quality audio and video with zero lag.
    """)
    
    # Status Indicator (You can toggle this manually or automate it later)
    is_class_live = True 
    
    if is_class_live:
        st.markdown('<div class="live-banner"><h2>🎥 CLASS IS CURRENTLY LIVE!</h2></div>', unsafe_allow_html=True)
        st.write("### Topic: Thermodynamics & Heat Transfer")
        st.write("**Target Audience:** Class 10 CBSE")
        
        st.markdown("---")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.link_button("🚀 JOIN LIVE CLASS ON DISCORD", DISCORD_CLASSROOM_LINK, type="primary", use_container_width=True)
            st.caption("*Clicking this will open Discord and drop you directly into the classroom voice channel.*")
    else:
        st.warning("No classes are live right now. Check the schedule tab!")

# --- PAGE: CLASS SCHEDULE ---
elif page == "Class Schedule":
    st.title("📅 Weekly Schedule")
    
    # Example Data - Replace with your real schedule
    schedule_data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Time (IST)": ["6:00 PM", "6:00 PM", "7:30 PM", "6:00 PM", "7:00 PM"],
        "Subject": ["Chemistry (Class 10)", "Math (Class 10)", "Physics (Class 9)", "Chemistry (Class 12)", "Doubt Clearing"],
        "Topic": ["Carbon Compounds", "Quadratic Equations", "Motion", "Solutions", "Open Session"]
    }
    
    df = pd.DataFrame(schedule_data)
    st.table(df)
    
    st.info("Note: Extra classes for exam prep will be announced 24 hours in advance.")

# --- PAGE: NOTES & RESOURCES ---
elif page == "Notes & Resources":
    st.title("📚 Study Materials")
    
    tab1, tab2 = st.tabs(["Class 10 Notes", "Previous Year Qs"])
    
    with tab1:
        st.subheader("Chemistry")
        # You would replace data= with your actual PDF file bytes
        st.download_button("Download: Acid Bases and Salts.pdf", data="dummy data", file_name="Acids_Bases.pdf")
        st.download_button("Download: Carbon and its Compounds.pdf", data="dummy data", file_name="Carbon.pdf")
        
        st.divider()
        st.subheader("Math")
        st.download_button("Download: Trigonometry Formulas.pdf", data="dummy data", file_name="Trig_Formulas.pdf")

    with tab2:
        st.write("Previous Year Questions (PYQs) for CBSE & ICSE")
        st.download_button("Download: 2024 Science Paper.pdf", data="dummy data", file_name="2024_Science.pdf")
