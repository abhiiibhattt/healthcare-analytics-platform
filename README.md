# Healthcare Operations Analytics Platform

## 🔍 Project Overview
This project demonstrates an end-to-end **data engineering and analytics pipeline** built on healthcare operational data. The objective is to transform raw data into clean, analytics-ready datasets and deliver actionable insights through SQL and Power BI dashboards.

The project mirrors real-world healthcare analytics workflows used in enterprise environments.

---

## 🏥 Problem Statement
Healthcare organizations generate large volumes of operational data across appointments, diagnostics, and billing systems. This data is often inconsistent and siloed, making it difficult to monitor efficiency, revenue, and patient distribution.

This project addresses the problem by:
- Designing a structured ETL pipeline
- Ensuring data quality and validation
- Building a relational analytics database
- Creating business-focused dashboards

---

## 🛠️ Tech Stack
- **Programming:** Python  
- **Data Engineering:** Pandas, SQLite  
- **Database:** SQL (Relational schema design)  
- **Analytics & Visualization:** Power BI  
- **Version Control:** Git, GitHub  

---

## 🧱 Data Pipeline Architecture
```text
Raw CSV Data
↓
Python ETL (Extract, Transform, Validate)
↓
Cleaned Analytics Datasets
↓
SQLite Relational Database
↓
SQL Analytics Queries
↓
Power BI Dashboards
```

---

## 🧹 Data Processing & Validation
- Standardized column naming conventions
- Removed duplicate records
- Validated patient-level relationships across datasets
- Converted date fields to appropriate formats
- Ensured referential integrity before loading data into the database

---

## 📊 Analytics & Insights
The analytics layer focuses on key healthcare operational metrics, including:
- Appointment completion, cancellation, and no-show rates
- Diagnostic test turnaround time analysis
- Department-wise revenue distribution
- Billing payment status monitoring
- Patient distribution across cities

---

## 📁 Project Structure
```text
healthcare-analytics-platform/
├── data/
│ ├── raw/
│ └── processed/
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── sql/
│ ├── schema.sql
│ └── analytics_queries.sql
├── dashboard/
│ ├── healthcare_dashboard.pbix
│ └── screenshots/
├── healthcare.db
└── README.md
```

---

## 📈 Dashboard
The Power BI dashboard provides an interactive view of healthcare KPIs such as appointment efficiency, diagnostic bottlenecks, revenue contribution by department, billing health, and patient distribution.

Dashboard screenshots are available in the `dashboard/` directory.

---

## 🎯 Outcome
This project demonstrates practical experience in:
- Building production-style ETL pipelines
- Designing relational data models
- Writing analytics-driven SQL queries
- Delivering business-focused dashboards

It reflects real-world data engineering and analytics practices commonly used in enterprise healthcare environments.

---

## 👨‍💻 Author

Abhinava Bhat

* GitHub: https://github.com/abhiiibhattt
* Portfolio: https://abhiiibhattt.github.io/portfolio/

---

## 📌 License

This project is intended for educational, research, and portfolio purposes.

© 2026 Abhinava Bhat P V. All rights reserved.
