import pandas as pd

# Example DataFrame
df = pd.DataFrame({'Column1': [1, 2], 'Column2': [3, 4]})
latex_code = df.to_latex(index=False)
print(latex_code)

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_tuples([
    ('Group 1', 'Sub 1'),
    ('Group 1', 'Sub 2'),
    ('Group 2', 'Sub 1'),
    ('Group 2', 'Sub 2')
])
df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=columns)
latex_code = df.to_latex(index=False, multirow=True)
print(latex_code)