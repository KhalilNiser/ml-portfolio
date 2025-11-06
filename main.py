import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PANDAS/NUMPY TEST
print("TESt PANDAS/NUMPY")
print("Pandas Version: ", pd.__version__)
print("Numpy Version: ", np.__version__)


# Tiny Dataframe test
df_Test = pd.DataFrame ({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78],
    "Passed": [True, True, False]
})

print("\nDataFrame")
print(df_Test)

print("\nSummary Stats:")
print(df_Test.describe(include="all"))
# END PANDAS/NUMPY TEST


# MATPLOTLIB TEST
# Object-Oriented Plotting
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 8])
ax.set_title("Test Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
plt.show()

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x,y)
plt.title("Test Matrix Plot: y = x^2")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# print("MATPLOTLIB TEST")
# plt.plot([1, 2, 3], [2, 4, 8])
# plt.title("Test Plot")
# plt.show()
