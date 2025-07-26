import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("BMW_Car_Sales_Classification.csv")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Create new feature: Car Age
df["Car_Age"] = 2025 - df["Year"]

# Export cleaned dataset for Power BI
df.to_csv("BMW_Car_Sales_Cleaned.csv", index=False)
print("✅ Cleaned CSV saved as: BMW_Car_Sales_Cleaned.csv")

# --- Exploratory Analysis ---

# Top 10 Selling Models
top_models = df.groupby("Model")["Sales_Volume"].sum().sort_values(ascending=False).head(10)
print("\n🔝 Top 10 Models by Sales:\n", top_models)

# Sales by Region
region_sales = df.groupby("Region")["Sales_Volume"].sum().sort_values(ascending=False)
print("\n🌍 Region-wise Sales:\n", region_sales)

# Fuel Type Distribution
fuel_dist = df["Fuel_Type"].value_counts(normalize=True) * 100
print("\n⛽ Fuel Type Distribution (%):\n", fuel_dist)

# Transmission-wise Average Sales
trans_sales = df.groupby("Transmission")["Sales_Volume"].mean()
print("\n🔁 Transmission vs Avg Sales:\n", trans_sales)

# Sales Classification Analysis
sales_stats = df.groupby("Sales_Classification")[["Price_USD", "Mileage_KM", "Engine_Size_L"]].mean()
print("\n📊 Avg Stats by Sales Classification:\n", sales_stats)

# Optional: Plot bar chart (save as image)
plt.figure(figsize=(10,5))
top_models.plot(kind='bar', color='skyblue')
plt.title("Top 10 BMW Models by Sales Volume")
plt.ylabel("Sales Volume")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_models_sales.png")
plt.show()
