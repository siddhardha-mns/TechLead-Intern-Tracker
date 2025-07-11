import streamlit as st
import pandas as pd
import os
from datetime import datetime
import json

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
            st.rerun()
        else:
            st.error("Invalid credentials")
    st.stop()

tech_lead = st.session_state.tech_lead

# File paths
data_file = os.path.join(DATA_FOLDER, f"{tech_lead.replace(' ', '_')}.csv")
history_file = os.path.join(HISTORY_FOLDER, f"{tech_lead.replace(' ', '_')}_history.csv")

# Load data
def load_data():
    if os.path.exists(data_file):
        return pd.read_csv(data_file)
    else:
        return pd.DataFrame(columns=[
            "Name", "Cohort", "GitLab User Name", "Year", "Received Offer letter", "College",
            "GitLab Acc (README.md)", "GitLab Acc Link",
            "Innings Courses (Python & AI)", "Huggingchat/Dify", "Huggingchat Link",
            "Streamlit app and Deployment", "Streamlit Link",
            "Huggingface+streamlit integration", "HF+Streamlit Link",
            "Pushed Apps onto GitLab", "Data Collection (started?)", "Size of Data",
            "Can go to any other places", "Blockers?", "Remarks"
        ])

# Save history function
def save_history(intern_name, action, old_data="", new_data="", changed_fields=None):
    change_time = datetime.now().isoformat()
    history_entry = {
        "Time": change_time, 
        "Intern": intern_name, 
        "Action": action, 
        "Old": str(old_data), 
        "New": str(new_data),
        "Changed_Fields": json.dumps(changed_fields) if changed_fields else ""
    }
    
    # Load existing history or create new
    if os.path.exists(history_file):
        hist_df = pd.read_csv(history_file)
        hist_df = pd.concat([hist_df, pd.DataFrame([history_entry])], ignore_index=True)
    else:
        hist_df = pd.DataFrame([history_entry])
    
    hist_df.to_csv(history_file, index=False)

# Navigation sidebar
st.sidebar.title(f"Welcome, {tech_lead}")
page = st.sidebar.selectbox("Navigate to:", [
    "Add/Update Intern", 
    "View All Interns", 
    "Edit Intern", 
    "Delete Intern", 
    "Change History"
])

df = load_data()

# Page 1: Add/Update Intern (Original functionality)
if page == "Add/Update Intern":
    st.title("Add or Update Intern")
    
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
        
        if submitted and name:
            new_row = {"Name": name, "Cohort": cohort}
            new_row.update(values)
            
            # Check if intern exists
            if name in df["Name"].values:
                old_row = df[df["Name"] == name].iloc[0].to_dict()
                df.loc[df["Name"] == name] = new_row
                save_history(name, "Updated", old_row, new_row)
                st.success("Intern data updated successfully.")
            else:
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                save_history(name, "Added", "", new_row)
                st.success("Intern added successfully.")
            
            df.to_csv(data_file, index=False)

# Page 2: View All Interns
elif page == "View All Interns":
    st.title("All Interns")
    
    # Cohort filter
    cohort_filter = st.selectbox("Select Cohort", ["All", "Cohort 1", "Cohort 2"])
    
    if cohort_filter != "All":
        filtered_df = df[df["Cohort"] == cohort_filter]
    else:
        filtered_df = df
    
    if not filtered_df.empty:
        st.dataframe(filtered_df, use_container_width=True)
        
        # Download button
        st.download_button(
            "Download CSV", 
            filtered_df.to_csv(index=False), 
            file_name=f"{tech_lead.replace(' ', '_')}_interns.csv"
        )
    else:
        st.info("No interns found.")

# Page 3: Edit Intern
elif page == "Edit Intern":
    st.title("Edit Intern")
    
    if df.empty:
        st.info("No interns to edit.")
    else:
        intern_names = df["Name"].tolist()
        selected_intern = st.selectbox("Select Intern to Edit", ["None"] + intern_names)
        
        if selected_intern != "None":
            intern_data = df[df["Name"] == selected_intern].iloc[0].to_dict()
            
            st.subheader(f"Editing: {selected_intern}")
            
            with st.form("edit_intern_form"):
                # Fields to edit selection
                st.write("Select fields to edit:")
                fields_to_edit = {}
                
                # Basic info
                edit_cohort = st.checkbox("Edit Cohort")
                if edit_cohort:
                    fields_to_edit["Cohort"] = st.selectbox("Cohort", ["Cohort 1", "Cohort 2"], 
                                                           index=0 if intern_data["Cohort"] == "Cohort 1" else 1)
                
                # Other fields
                field_mapping = {
                    "GitLab User Name": "text",
                    "Year": "selectbox",
                    "Received Offer letter": "selectbox",
                    "College": "text",
                    "GitLab Acc (README.md)": "text",
                    "GitLab Acc Link": "text",
                    "Innings Courses (Python & AI)": "text",
                    "Huggingchat/Dify": "text",
                    "Huggingchat Link": "text",
                    "Streamlit app and Deployment": "text",
                    "Streamlit Link": "text",
                    "Huggingface+streamlit integration": "text",
                    "HF+Streamlit Link": "text",
                    "Pushed Apps onto GitLab": "selectbox",
                    "Data Collection (started?)": "selectbox",
                    "Size of Data": "text",
                    "Can go to any other places": "text",
                    "Blockers?": "textarea",
                    "Remarks": "textarea"
                }
                
                for field, input_type in field_mapping.items():
                    edit_field = st.checkbox(f"Edit {field}")
                    if edit_field:
                        current_value = intern_data.get(field, "")
                        if input_type == "text":
                            fields_to_edit[field] = st.text_input(f"{field}", value=current_value)
                        elif input_type == "textarea":
                            fields_to_edit[field] = st.text_area(f"{field}", value=current_value)
                        elif input_type == "selectbox":
                            if field == "Year":
                                options = ["1", "2", "3", "4"]
                                index = options.index(current_value) if current_value in options else 0
                                fields_to_edit[field] = st.selectbox(f"{field}", options, index=index)
                            elif field in ["Received Offer letter", "Pushed Apps onto GitLab", "Data Collection (started?)"]:
                                options = ["Yes", "No"]
                                index = options.index(current_value) if current_value in options else 0
                                fields_to_edit[field] = st.selectbox(f"{field}", options, index=index)
                
                update_submitted = st.form_submit_button("Update Intern")
                
                if update_submitted and fields_to_edit:
                    old_data = intern_data.copy()
                    
                    # Update only the selected fields
                    for field, value in fields_to_edit.items():
                        df.loc[df["Name"] == selected_intern, field] = value
                    
                    # Save changes
                    df.to_csv(data_file, index=False)
                    
                    # Save history with changed fields
                    changed_fields = list(fields_to_edit.keys())
                    new_data = df[df["Name"] == selected_intern].iloc[0].to_dict()
                    save_history(selected_intern, "Updated", old_data, new_data, changed_fields)
                    
                    st.success(f"Updated {len(fields_to_edit)} field(s) for {selected_intern}")
                    st.rerun()

# Page 4: Delete Intern
elif page == "Delete Intern":
    st.title("Delete Intern")
    
    if df.empty:
        st.info("No interns to delete.")
    else:
        intern_names = df["Name"].tolist()
        selected_intern = st.selectbox("Select Intern to Delete", ["None"] + intern_names)
        
        if selected_intern != "None":
            intern_data = df[df["Name"] == selected_intern].iloc[0].to_dict()
            
            st.subheader(f"Intern Details:")
            st.write(f"**Name:** {intern_data['Name']}")
            st.write(f"**Cohort:** {intern_data['Cohort']}")
            st.write(f"**College:** {intern_data.get('College', 'N/A')}")
            st.write(f"**Year:** {intern_data.get('Year', 'N/A')}")
            
            st.warning("⚠️ This action cannot be undone!")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Delete Intern", type="secondary"):
                    # Remove from dataframe
                    df = df[df["Name"] != selected_intern]
                    df.to_csv(data_file, index=False)
                    
                    # Save history
                    save_history(selected_intern, "Deleted", intern_data, "")
                    
                    st.success(f"Intern {selected_intern} has been deleted.")
                    st.rerun()
            
            with col2:
                if st.button("Cancel"):
                    st.rerun()

# Page 5: Change History
elif page == "Change History":
    st.title("Change History")
    
    if os.path.exists(history_file):
        hist_df = pd.read_csv(history_file)
        
        if not hist_df.empty:
            # Get unique intern names from history
            intern_names = hist_df["Intern"].unique().tolist()
            selected_intern = st.selectbox("Select Intern to View History", ["All"] + intern_names)
            
            if selected_intern != "All":
                filtered_hist = hist_df[hist_df["Intern"] == selected_intern]
                st.subheader(f"History for: {selected_intern}")
            else:
                filtered_hist = hist_df
                st.subheader("All Changes")
            
            # Display history
            for index, row in filtered_hist.iterrows():
                with st.expander(f"{row['Time']} - {row['Action']} - {row['Intern']}"):
                    st.write(f"**Action:** {row['Action']}")
                    st.write(f"**Time:** {row['Time']}")
                    st.write(f"**Intern:** {row['Intern']}")
                    
                    # Show changed fields if available
                    if pd.notna(row.get('Changed_Fields', '')) and row['Changed_Fields']:
                        try:
                            changed_fields = json.loads(row['Changed_Fields'])
                            st.write(f"**Changed Fields:** {', '.join(changed_fields)}")
                        except:
                            pass
                    
                    if row['Action'] == "Updated":
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("**Before:**")
                            st.code(row['Old'])
                        with col2:
                            st.write("**After:**")
                            st.code(row['New'])
                    elif row['Action'] == "Added":
                        st.write("**Added Data:**")
                        st.code(row['New'])
                    elif row['Action'] == "Deleted":
                        st.write("**Deleted Data:**")
                        st.code(row['Old'])
        else:
            st.info("No history available.")
    else:
        st.info("No history file found.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write(f"Total Interns: {len(df)}")
if not df.empty:
    cohort_counts = df["Cohort"].value_counts()
    for cohort, count in cohort_counts.items():
        st.sidebar.write(f"{cohort}: {count}")
