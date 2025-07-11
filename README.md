# 🚀 Intern Management System

<div align="center">

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A comprehensive web-based application for managing intern data, tracking progress, and maintaining change history.*

</div>

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🛠️ Installation](#️-installation)
- [⚙️ Configuration](#️-configuration)
- [🚀 Usage](#-usage)
- [💾 Data Management](#-data-management)
- [🔧 Troubleshooting](#-troubleshooting)
- [📝 License](#-license)

---

## 🌟 Features

### 🔐 **Authentication & Security**
- ✅ Secure login for authorized Tech Leads
- ✅ Role-based access control
- ✅ Session management with auto-logout
- ✅ Individual data isolation per tech lead

### 📊 **Core Management**
| Feature | Description | Status |
|---------|-------------|--------|
| 🆕 **Add/Update Interns** | Complete intern information management | ✅ Active |
| 👥 **View All Interns** | Display all interns with cohort filtering | ✅ Active |
| ✏️ **Edit Intern** | Selective field editing with checkbox selection | ✅ Active |
| 🗑️ **Delete Intern** | Safe deletion with confirmation dialogs | ✅ Active |
| 📈 **Change History** | Complete audit trail of all modifications | ✅ Active |

### 📥 **Data Export & Downloads**
- 📊 **CSV Export**: Download complete or filtered data
- 🎯 **Cohort-based Downloads**: Separate downloads for Cohort 1 and Cohort 2
- 📋 **History Tracking**: Detailed change logs with timestamps
- 💾 **Auto-backup**: Automatic data persistence

---

## 🛠️ Installation

### 📋 Prerequisites
```bash
Python 3.7+
pip package manager
```

### 📦 Dependencies
```bash
pip install streamlit pandas
```

### 🚀 Quick Setup
```bash
# 1. Clone the repository
git clone <repository-url>
cd intern-management-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create directory structure
mkdir -p data history .streamlit

# 4. Configure secrets (see configuration section)
touch .streamlit/secrets.toml

# 5. Run the application
streamlit run app.py
```

---

## ⚙️ Configuration

### 🔑 Authentication Setup

Create `.streamlit/secrets.toml`:

```toml
[secrets]
"nikhil" = "your_secure_password_here"
"Edla Divyansh Teja" = "another_secure_password"
"GANNARAM DHRUV" = "yet_another_password"
# Add more tech leads as needed
```

### 👥 Tech Leads Configuration

Update the `TECH_LEADS` list in `app.py`:

```python
TECH_LEADS = [
    "nikhil", 
    "Edla Divyansh Teja", 
    "GANNARAM DHRUV",
    "Satwik Rakhelkar", 
    "Gadagoju Srikar", 
    "Hasini Parre",
    # Add more tech leads here
]
```

---

## 🚀 Usage

### 🌐 Starting the Application

```bash
streamlit run app.py
```

Your application will be available at: `http://localhost:8501`

### 🧭 Navigation Guide

<div align="center">

| 🏠 Page | 🎯 Purpose | 🔧 Actions |
|---------|------------|------------|
| 🆕 **Add/Update Intern** | Create new records | ➕ Add, 🔄 Update |
| 👥 **View All Interns** | Browse all records | 👀 View, 📊 Filter, 📥 Download |
| ✏️ **Edit Intern** | Modify existing data | ✅ Select fields, 🔄 Update |
| 🗑️ **Delete Intern** | Remove records | ⚠️ Confirm, 🗑️ Delete |
| 📈 **Change History** | View audit trail | 👤 Filter by intern, 📅 View changes |

</div>

### 📝 Data Fields Overview

<details>
<summary>📋 Click to view all data fields</summary>

#### 👤 **Basic Information**
- 📛 Name
- 🎓 Cohort (1 or 2)
- 📅 Year (1-4)
- 🏫 College

#### 🔧 **GitLab & Development**
- 👨‍💻 GitLab Username
- 📄 README.md Status
- 🔗 GitLab Account Link

#### 📚 **Courses & Learning**
- 🐍 Python & AI Courses
- 🤖 Huggingchat/Dify Usage
- 🔗 Huggingchat Link

#### 🚀 **Projects & Deployment**
- 🌐 Streamlit App Status
- 🔗 Streamlit Link
- 🤗 Huggingface Integration
- 🔗 HF+Streamlit Link

#### 📊 **Progress Tracking**
- 📤 Apps Pushed to GitLab
- 📊 Data Collection Status
- 📏 Size of Data
- 🚶 Mobility Options

#### 📝 **Notes & Issues**
- 🚧 Blockers
- 💬 Remarks

</details>

---

## 💾 Data Management

### 📁 File Structure
```
📦 intern-management-system/
├── 📄 app.py                    # Main application
├── 📂 data/                     # Intern data storage
│   ├── 📊 nikhil.csv           # Individual tech lead data
│   └── 📊 other_leads.csv      # Other tech leads' data
├── 📂 history/                  # Change history
│   ├── 📈 nikhil_history.csv   # Change logs
│   └── 📈 other_history.csv    # Other change logs
└── 📂 .streamlit/
    └── 🔐 secrets.toml          # Authentication config
```

### 🔒 Data Security Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🔐 **Isolation** | Each tech lead accesses only their data | ✅ |
| 📝 **Audit Trail** | Complete history of all changes | ✅ |
| 🔄 **Backup** | Auto-save to CSV files | ✅ |
| 🛡️ **Session Security** | Automatic logout on browser close | ✅ |

### 📥 Export Options

<div align="center">

| 📊 Export Type | 📋 Description | 🎯 Use Case |
|----------------|----------------|-------------|
| 📥 **All Data** | Complete dataset | 📊 Full reports |
| 🎯 **Cohort 1** | Filtered by Cohort 1 | 📈 Cohort analysis |
| 🎯 **Cohort 2** | Filtered by Cohort 2 | 📈 Cohort analysis |

</div>

---

## 🔧 Troubleshooting

### ❌ Common Issues & Solutions

<details>
<summary>🔑 Login Problems</summary>

#### Symptoms:
- ❌ "Invalid credentials" error
- ❌ Cannot access dashboard

#### Solutions:
1. ✅ Verify tech lead name matches exactly (case-sensitive)
2. ✅ Check `.streamlit/secrets.toml` file exists
3. ✅ Ensure user is in `TECH_LEADS` list
4. ✅ Restart the application

</details>

<details>
<summary>💾 Data Not Saving</summary>

#### Symptoms:
- ❌ Changes not persisting
- ❌ CSV files not updating

#### Solutions:
1. ✅ Check folder permissions for `data/` and `history/`
2. ✅ Verify CSV file isn't locked by another application
3. ✅ Ensure sufficient disk space
4. ✅ Restart the application

</details>

<details>
<summary>📈 History Not Displaying</summary>

#### Symptoms:
- ❌ Empty history page
- ❌ History data missing

#### Solutions:
1. ✅ Ensure history file exists and is readable
2. ✅ Check JSON format in changed_fields column
3. ✅ Verify file permissions
4. ✅ Check for corrupted history files

</details>

### 🛠️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| 🖥️ **RAM** | 512MB | 1GB+ |
| 💾 **Storage** | 100MB | 500MB+ |
| 🌐 **Browser** | Chrome 60+ | Chrome/Firefox Latest |
| 🐍 **Python** | 3.7+ | 3.9+ |

---

## 📊 Version History

<div align="center">

| Version | Date | Features Added | Status |
|---------|------|----------------|--------|
| 🎯 **v1.0** | Initial | Basic CRUD operations | ✅ Released |
| 🚀 **v2.0** | Update | Navigation, history tracking | ✅ Released |
| 📥 **v2.1** | Latest | Sidebar downloads, enhanced UI | ✅ Current |

</div>

---

## 🤝 Support & Contact

<div align="center">

### 📞 Need Help?

| Issue Type | Contact Method | Response Time |
|------------|----------------|---------------|
| 🐛 **Bug Reports** | GitHub Issues | 24-48 hours |
| 💡 **Feature Requests** | GitHub Issues | 1-2 weeks |
| ❓ **General Questions** | Email/Slack | Same day |

### 📚 Additional Resources

[![Documentation](https://img.shields.io/badge/docs-streamlit-blue)](https://docs.streamlit.io)
[![Python](https://img.shields.io/badge/docs-python-yellow)](https://docs.python.org)
[![Pandas](https://img.shields.io/badge/docs-pandas-purple)](https://pandas.pydata.org/docs/)

</div>

---

## 📝 License

<div align="center">

```
MIT License

Copyright (c) 2024 Intern Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

</div>

---

<div align="center">

### 🌟 Made with ❤️ for efficient intern management

[![⭐ Star this repo](https://img.shields.io/github/stars/yourusername/intern-management-system?style=social)](https://github.com/yourusername/intern-management-system)
[![🍴 Fork this repo](https://img.shields.io/github/forks/yourusername/intern-management-system?style=social)](https://github.com/yourusername/intern-management-system/fork)

</div>
