# 🧠 Generative AI Powered: Natural Language to SQL Prototype Application

A prototype application which is deployed on Streamlit Community Cloud that transforms **natural language** into **SQL queries**, allowing users to explore a company's database using everyday English.

---
## App Login Screenshot
![App Login-Demo](assests/login.png)

## App Dashboard Screenshot
![App Dashboard-Demo](assests/dashboard.png)

---

## 🚀 Features

- 🔐 User registration & login system (PostgreSQL + bcrypt)
- 📋 Consent form signing with auto-generated PDF
- ☁️ PDF storage to AWS S3
- 🧪 Questionnaire feedback module
- 🗃️ Query interface for company data (using SQLite)
- 🖥️ CI/CD support with Streamlit Cloud

---


## 📂 Project Structure

```bash
.
├── backend/           # Auth, registration, database logic
├── database/          # Local SQLite files (e.g., company.db)
├── utils/             # Utility functions (PDF generation, S3 upload, Handle pages etc.)
├── views/             # Streamlit UI pages: login, register, consent, etc.
├── main.py            # App entry point
├── requirements.txt   # Python dependencies
└── README.md