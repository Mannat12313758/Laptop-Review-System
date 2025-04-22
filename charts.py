import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('cleaned_laptop_reviews.xlsx')

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Distribution of Overall Ratings
# sns.histplot(df['overall_rating'], bins=20, kde=True, color='skyblue')
# plt.title('Distribution of Overall Ratings')
# plt.xlabel('Overall Rating')
# plt.ylabel('Frequency')
# plt.show()
# 2. Count of Review Ratings (1 to 5 stars)
# sns.countplot(data=df, x='rating', palette='viridis')
# plt.title('Count of Review Ratings')
# plt.xlabel('Review Rating')
# plt.ylabel('Number of Reviews')
# plt.show()
# 3. Top 10 Most Rated Products
# top_rated = df.groupby('product_name')['no_ratings'].max().sort_values(ascending=False).head(10)
# top_rated.plot(kind='bar', color='coral')
# plt.title('Top 10 Most Rated Products')
# plt.xlabel('Product Name')
# plt.ylabel('Number of Ratings')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# # 4. Average Overall Rating of Top 10 Reviewed Products
# top_reviewed = df.groupby('product_name').agg({
#     'no_reviews': 'max',
#     'overall_rating': 'mean'
# }).sort_values(by='no_reviews', ascending=False).head(10)

# sns.barplot(x=top_reviewed['overall_rating'], y=top_reviewed.index, palette='mako')
# plt.title('Average Rating of Top 10 Reviewed Products')
# plt.xlabel('Average Overall Rating')
# plt.ylabel('Product Name')
# plt.show()

# 5. Correlation Heatmap
# corr = df[['overall_rating', 'no_ratings', 'no_reviews', 'rating']].corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Between Numerical Features')
# plt.show()

# 6. Boxplot of Review Ratings vs Overall Rating
sns.boxplot(data=df, x='rating', y='overall_rating', palette='Set3')
plt.title('Boxplot: Overall Rating by Review Rating')
plt.xlabel('Review Rating')
plt.ylabel('Overall Rating')
plt.show()
