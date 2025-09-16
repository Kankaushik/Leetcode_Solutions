import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Unique salaries in DESC order
    unique_salaries = (
        employee['salary']
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )

    # Guard against invalid N (<= 0) and too-large N
    if N <= 0 or N > len(unique_salaries):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    # 1-based N -> 0-based index
    return pd.DataFrame({f"getNthHighestSalary({N})": [unique_salaries.iloc[N-1]]})
