import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Constants
DATA_FOLDER = "data"
HISTORY_FOLDER = "history"
TECH_LEADS = [
    "nikhil", "Edla Divyansh Teja", "GANNARAM DHRUV",
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

# Sidebar Cohort Filter
cohort_filter = st.sidebar.selectbox("Select Cohort", ["All", "Cohort 1", "Cohort 2"])

# File paths
data_file = os.path.join(DATA_FOLDER, f"{tech_lead.replace(' ', '_')}.csv")
history_file = os.path.join(HISTORY_FOLDER, f"{tech_lead.replace(' ', '_')}_history.csv")

# Load data
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=[
        "Name", "Cohort", "GitLab User Name", "Year", "Received Offer letter", "College",
        "GitLab Acc (README.md)", "GitLab Acc Link",
        "Innings Courses (Python & AI)", "Huggingchat/Dify", "Huggingchat Link",
        "Streamlit app and Deployment", "Streamlit Link",
        "Huggingface+streamlit integration", "HF+Streamlit Link",
        "Pushed Apps onto GitLab", "Data Collection (started?)", "Size of Data",
        "Can go to any other places", "Blockers?", "Remarks"
    ])

# Add new intern
st.title("Intern Management")
st.subheader("Add or Update Intern")
with st.form("intern_form"):
    name = st.text_input("Name")
    cohort = st.selectbox("Cohort", ["Cohort 1", "Cohort 2"])
    values = {
        "GitLab User Name": st.text_input("GitLab User Name"),
        "Year": st.selectbox("Year", ["1", "2", "3", "4"]),
        "Received Offer letter": st.selectbox("Received Offer letter", ["Yes", "No"]),
        "College": st.text_input("College"),
        "GitLab Acc (README.md)": st.text_input("GitLab Acc (README.md)"),
        "GitLab Acc Link": st.text_input("GitLab Acc Link"),
        "Innings Courses (Python & AI)": st.text_input("Innings Courses (Python & AI)"),
        "Huggingchat/Dify": st.text_input("Huggingchat/Dify"),
        "Huggingchat Link": st.text_input("Huggingchat Link"),
        "Streamlit app and Deployment": st.text_input("Streamlit app and Deployment"),
        "Streamlit Link": st.text_input("Streamlit Link"),
        "Huggingface+streamlit integration": st.text_input("Huggingface+streamlit integration"),
        "HF+Streamlit Link": st.text_input("HF+Streamlit Link"),
        "Pushed Apps onto GitLab": st.selectbox("Pushed Apps onto GitLab", ["Yes", "No"]),
        "Data Collection (started?)": st.selectbox("Data Collection (started?)", ["Yes", "No"]),
        "Size of Data": st.text_input("Size of Data"),
        "Can go to any other places": st.text_input("Can go to any other places"),
        "Blockers?": st.text_area("Blockers?"),
        "Remarks": st.text_area("Remarks")
    }
    submitted = st.form_submit_button("Save")
    if submitted:
        new_row = {"Name": name, "Cohort": cohort}
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

# Show table of interns with cohort filtering
st.subheader("Interns List")
if cohort_filter != "All":
    filtered_df = df[df["Cohort"] == cohort_filter]
else:
    filtered_df = df
st.dataframe(filtered_df, use_container_width=True)

# Download data
st.download_button("Download CSV", filtered_df.to_csv(index=False), file_name=f"{tech_lead.replace(' ', '_')}_interns.csv")

# History View
st.sidebar.subheader("Change History")
if os.path.exists(history_file):
    hist_df = pd.read_csv(history_file)
    st.sidebar.dataframe(hist_df.tail(10), use_container_width=True)
else:
    st.sidebar.write("No history yet.")

# Edit Intern Record
st.subheader("Edit Existing Intern")
with st.expander("Edit an Intern"):
    intern_names = df["Name"].tolist()
    selected_intern = st.selectbox("Select Intern to Edit", ["None"] + intern_names)
    if selected_intern != "None":
        intern_data = df[df["Name"] == selected_intern].iloc[0].to_dict()
        st.write("Now edit via the form above or re-enter details.")
