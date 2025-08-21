# 📊 Pharma Patient Analysis

A data analysis project focused on **patient insurance & churn behavior** in the pharmaceutical domain.
This project demonstrates **data cleaning, SQL-based analytics, and interactive dashboards** to derive insights into patient behavior.

---

## 🛠️ 📝 Tech Stack and Tools

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **SQL (SQLite)** (SQLite for querying)
- **Tableau** (for dashboards)
- **Jupyter Notebooks**

---

## 📂 Project Structure

```
pharma-patient-analysis/
│
├── data/
│   └── insurance.csv          # Raw dataset
│   └── cleaned_insurance.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb    # Jupyter: data cleaning & preprocessing
│   ├── sql_analysis.ipynb     # Jupyter: SQL queries on cleaned data
│   └── visualise.ipynb    # Jupyter: charts & plots
│
├── scripts/
│   ├── clean_data.py          # Python automation of data cleaning
│   ├── run_sql.py             # Runs SQL queries on SQLite DB
│   └── visualize.py           # Generates plots & graphs
│
├── visualizations/
│    ├── churn_dashboard.png       # Static screenshot/image for quick viewing
│    └── churn_dashboard.twbx      # Interactive Tableau workbook (requires Tableau Desktop)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📑 Dataset

- **File:** `insurance.csv`
- **Attributes:**

  - `age` → Age of the patient
  - `sex` → Male/Female
  - `bmi` → Body Mass Index
  - `children` → Number of dependents
  - `smoker` → Yes/No
  - `region` → Patient’s residential region
  - `charges` → Insurance claim charges

---

## 🔄 Workflow

1. **Data Cleaning** (`cleaned_insurance.ipynb`)

   - Handled missing values
   - Removed duplicates
   - Standardized column names

2. **SQL Analysis** (`sql_analysis.ipynb`)

   - Stored cleaned data in SQLite
   - Ran queries for insights:

     - Average charges by region
     - Impact of smoking on insurance cost
     - High-risk patient segments

3. **Visualization** (`visualise.ipynb`)

   - Created charts with **Matplotlib & Seaborn**
   - Built **Tableau dashboard** (see `visualizations/churn_dashboard.png`)

4. **Final Insights**

   - Patients who smoke have **2x higher charges** on average
   - BMI is a strong predictor of high insurance claims
   - Southeast region patients show higher average costs

---

## ⚡ Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/shalininukella/pharma-patient-analysis.git
cd pharma-patient-analysis
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run scripts

```bash
# Clean dataset
python scripts/clean_data.py

# Run SQL analysis
python scripts/run_sql.py

# Generate visualizations
python scripts/visualize.py
```

---

## 📊 Dashboard

The final interactive dashboard is created using **Tableau** and included as:

- `visualizations/churn_dashboard.twbx` — Tableau workbook (open with Tableau Desktop)
- `visualizations/churn_dashboard.png` — Static screenshot preview

If you do not have Tableau installed, you can view the dashboard screenshot above.

---

## ✅ Business Insights

- Smoking is the **biggest cost driver** in patient insurance.
- Higher BMI correlates with significantly higher claim amounts.
- Patients with multiple children are more likely to have higher charges.
- Southeast region shows **highest average insurance charges** compared to other regions.

---
