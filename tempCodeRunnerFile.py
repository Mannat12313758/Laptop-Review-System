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