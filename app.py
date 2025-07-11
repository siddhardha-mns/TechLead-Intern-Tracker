import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Constants
DATA_FOLDER = "data"
HISTORY_FOLDER = "history"
TECH_LEADS = [
    "MADAGALA NIKHIL SAI SIDDHARDHA", "Edla Divyansh Teja", "GANNARAM DHRUV",
    "Satwik Rakhelkar", "Gadagoju Srikar", "Hasini Parre", "Shiva Kumar ambotu",
    "Puneeth Peela", "Ch.Bhuvana Sri", "Guni Sreepranav", "Sai Kartikeyan Koduri",
    "Sudheer Kumar"
]

# Ensure folders exist
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(HISTORY_FOLDER, exist_ok=True)

# Auth system using Streamlit secrets
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.tech_lead = None

if not st.session_state.logged_in:
    st.title("Tech Lead Login")
    username = st.text_input("Enter your full name")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in TECH_LEADS and password == st.secrets.get(username, ""):
            st.session_state.logged_in = True
            st.session_state.tech_lead = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
    st.stop()

tech_lead = st.session_state.tech_lead
st.sidebar.title(f"Welcome, {tech_lead}")

# File paths
data_file = os.path.join(DATA_FOLDER, f"{tech_lead.replace(' ', '_')}.csv")
history_file = os.path.join(HISTORY_FOLDER, f"{tech_lead.replace(' ', '_')}_history.csv")

# Load data
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=[
        "Name", "GitLab User Name", "Year", "Received Offer letter", "College",
        "GitLab Acc (README.md)", "Innings Courses (Python & AI)", "Huggingchat/Dify",
        "Streamlit app and Deployment", "Huggingface+streamlit integration", "Pushed Apps onto GitLab",
        "Data Collection (started?)", "Size of Data", "Can go to any other places", "Blockers?", "Remarks"
    ])

# Add new intern
st.title("Intern Management")
st.subheader("Add or Update Intern")
with st.form("intern_form"):
    name = st.text_input("Name")
    values = {
        "GitLab User Name": st.text_input("GitLab User Name"),
        "Year": st.text_input("Year"),
        "Received Offer letter": st.selectbox("Received Offer letter", ["Yes", "No"]),
        "College": st.text_input("College"),
        "GitLab Acc (README.md)": st.text_input("GitLab Acc (README.md)"),
        "Innings Courses (Python & AI)": st.text_input("Innings Courses (Python & AI)"),
        "Huggingchat/Dify": st.text_input("Huggingchat/Dify"),
        "Streamlit app and Deployment": st.text_input("Streamlit app and Deployment"),
        "Huggingface+streamlit integration": st.text_input("Huggingface+streamlit integration"),
        "Pushed Apps onto GitLab": st.selectbox("Pushed Apps onto GitLab", ["Yes", "No"]),
        "Data Collection (started?)": st.selectbox("Data Collection (started?)", ["Yes", "No"]),
        "Size of Data": st.text_input("Size of Data"),
        "Can go to any other places": st.selectbox("Can go to any other places", ["Yes", "No"]),
        "Blockers?": st.text_area("Blockers?"),
        "Remarks": st.text_area("Remarks")
    }
    submitted = st.form_submit_button("Save")
    if submitted:
        new_row = {"Name": name}
        new_row.update(values)
        # Check if intern exists
        if name in df["Name"].values:
            old_row = df[df["Name"] == name].iloc[0].to_dict()
            df.loc[df["Name"] == name] = new_row
            change_time = datetime.now().isoformat()
            history_entry = {"Time": change_time, "Intern": name, "Action": "Updated", "Old": str(old_row), "New": str(new_row)}
        else:
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            change_time = datetime.now().isoformat()
            history_entry = {"Time": change_time, "Intern": name, "Action": "Added", "Old": "", "New": str(new_row)}
        df.to_csv(data_file, index=False)
        pd.DataFrame([history_entry]).to_csv(history_file, mode='a', header=not os.path.exists(history_file), index=False)
        st.success("Intern data saved successfully.")

# Show table of interns
st.subheader("Interns List")
st.dataframe(df, use_container_width=True)

# Download data
st.download_button("Download CSV", df.to_csv(index=False), file_name=f"{tech_lead.replace(' ', '_')}_interns.csv")

# History View
st.sidebar.subheader("Change History")
if os.path.exists(history_file):
    hist_df = pd.read_csv(history_file)
    st.sidebar.dataframe(hist_df.tail(10), use_container_width=True)
else:
    st.sidebar.write("No history yet.")
