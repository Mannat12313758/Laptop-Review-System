import pandas as pd

# Load the dataset
df = pd.read_csv("laptops_dataset_final_600.csv")

# Clean the data
df['no_ratings'] = df['no_ratings'].str.replace(',', '').astype(int)
df['no_reviews'] = df['no_reviews'].str.replace(',', '').astype(int)
df_cleaned = df.drop_duplicates()

# Export to Excel
df_cleaned.to_excel("cleaned_laptop_reviews.xlsx", index=False)

print(" Cleaned dataset saved as 'cleaned_laptop_reviews.xlsx'")

