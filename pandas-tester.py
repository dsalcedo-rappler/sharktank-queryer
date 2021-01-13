import pandas as pd

data = [
    {
        "name": "a",
        "age": 5
    },
    {
        "name": "b",
        "age": 3
    }
]

df = pd.DataFrame(data)
df.to_csv("pandas-test.csv", index=False)