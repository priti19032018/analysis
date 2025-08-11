# analysis
# Sales Data Analysis

## 📌 Overview
This project performs **data analysis** on sales records stored in a CSV file using **Python** and **Pandas**.  
It demonstrates data cleaning, aggregation, visualization, and exporting results.

---

## 📂 Dataset
The dataset contains the following columns:

| Column    | Description |
|-----------|-------------|
| Date      | Transaction date (YYYY-MM-DD) |
| Product   | Name of the product sold |
| Category  | Product category (Electronics, Furniture, Stationery, etc.) |
| Region    | Sales region (North, South, East, West) |
| Quantity  | Number of units sold |
| Sales     | Total sales amount in USD |

---

## ⚙️ Steps Performed
1. **Load CSV data** using Pandas.
2. **Inspect** the dataset (`head()`, `info()`, `shape`).
3. **Clean data**:
   - Convert columns to correct data types.
   - Remove duplicates and missing values.
4. **Feature engineering**: Extract `YearMonth` for time-series analysis.
5. **Aggregate data** using `groupby()`:
   - Sales by product, category, and region.
   - Monthly sales trends.
6. **Visualizations**:
   - Top 10 products by sales (bar chart).
   - Monthly sales trend (line chart).
   - Sales by category (horizontal bar chart).
7. **Export results** to new CSV files.

---

## 📊 Visualizations
The script generates:
- `top10_products.png` – Top 10 products by sales.
- `monthly_sales.png` – Monthly sales trend.
- `sales_by_category.png` – Sales by category.

---

## 📁 Project Structure
```
├── analysis.py           # Main Python script
├── sales.csv             # Sales dataset
├── cleaned_sales.csv     # Cleaned dataset
├── sales_by_product.csv  # Aggregated sales by product
├── top10_products.png    # Bar chart image
├── monthly_sales.png     # Line chart image
├── sales_by_category.png # Horizontal bar chart image
└── README.md             # Project documentation
```

---

## 🚀 How to Run
1. Clone this repository or copy files into a folder.
2. Ensure **Python 3.x** is installed.
3. Install required packages:
   ```bash
   pip install pandas matplotlib
   ```
4. Place `sales.csv` in the project folder.
5. Run the script:
   ```bash
   python analysis.py
   ```
6. View the output CSV and PNG files in the same directory.

---

## 📝 Requirements
- Python 3.x
- Pandas
- Matplotlib

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## 📌 Example Insights
- Best-selling product by revenue.
- Top-performing category.
- Region with highest sales.
- Monthly sales growth trends.

---

## ✨ Author
**Priyam Yadav** – Internship Project
