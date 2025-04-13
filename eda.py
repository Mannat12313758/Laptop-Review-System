import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("cleaned_laptop_reviews.xlsx")

# Set visual style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (8, 5)

# Select relevant numerical columns
numeric_cols = ['overall_rating', 'no_ratings', 'no_reviews', 'rating']

# # ----------------------------------------
# # 📌 1. Correlation Heatmap
# # ----------------------------------------
# corr = df[numeric_cols].corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Correlation Heatmap")
# plt.show()

# ----------------------------------------
# # 📌 2. Boxplots for Outlier Detection
# for col in numeric_cols:
#     plt.figure()
#     sns.boxplot(y=df[col], color='lightgreen')
#     plt.title(f"Boxplot of {col}")
#     plt.show()

# # ----------------------------------------
# 📌 3. IQR-Based Outlier Detection
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

# Detect and print number of outliers per column
for col in numeric_cols:
    outlier_rows = detect_outliers_iqr(df, col)
    print(f"{col}: {len(outlier_rows)} outliers found")

# # ----------------------------------------
# # 📌 4. Optional: Remove Outliers
# # ----------------------------------------
# def remove_outliers_iqr(data, column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# # Remove outliers from all numeric columns
# df_cleaned = df.copy()
# for col in numeric_cols:
#     df_cleaned = remove_outliers_iqr(df_cleaned, col)

# # Save cleaned version without outliers (optional)
# df_cleaned.to_excel("cleaned_laptop_reviews_no_outliers.xlsx", index=False)
# print("✅ Cleaned dataset saved as 'cleaned_laptop_reviews_no_outliers.xlsx'")
