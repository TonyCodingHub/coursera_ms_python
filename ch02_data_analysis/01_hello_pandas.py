import pandas as pd

"""
在該程式碼段中，我們建立了一個DataFrame，其中包含年齡（數值型）、性別（分類型）和收入（數值型）變數。
我們將性別轉換為分類類型，然後計算平均收入並統計每個性別的出現次數。
"""

# Sample data
data = {
    "age": [25, 30, 35, 40],
    "gender": ["male", "female", "male", "female"],
    "income": [50000, 60000, 75000, 55000],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'gender' to a categorical variable
df["gender"] = df["gender"].astype("category")

# Calculate average income
average_income = df["income"].mean()

# Count the number of males and females
gender_counts = df["gender"].value_counts()

print(average_income)
print(gender_counts)
