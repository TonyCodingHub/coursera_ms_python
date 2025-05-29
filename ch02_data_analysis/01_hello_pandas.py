import pandas as pd

"""
在該程式碼段中，我們建立了一個DataFrame，其中包含年齡（數值型）、性別（分類型）和收入（數值型）變數。
然後，我們添加了一個新的列（城市）和一個新的行，並在每個步驟後都打印出結果，以更好地理解DataFrame的變化。
接著，我們將性別轉換為分類類型，並計算平均收入和每個性別的出現次數。
"""

# Sample data
data = {
    "age": [25, 30, 35, 40],
    "gender": ["male", "female", "male", "female"],
    "income": [50000, 60000, 75000, 55000],
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df)
print("----------")

# Add a new column 'city' to the DataFrame
df["city"] = ["Taipei", "Kaohsiung", "Taichung", "Tainan"]
print(df)
print("----------")

# Add a new row to the DataFrame
new_row = {"age": 28, "gender": "female", "income": 65000, "city":"Taipei"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df)
print("----------")

# Convert 'gender' to a categorical variable
df["gender"] = df["gender"].astype("category")

# Calculate average income
average_income = df["income"].mean()

# Count the number of males and females
gender_counts = df["gender"].value_counts()

print(average_income)
print(gender_counts)
