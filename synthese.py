import numpy as np

print(" 1. OPÉRATIONS VECTORISÉES ")
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2 + 5
print("arr * 2 + 5 =", result)
print("arr ** 2 =", arr ** 2)
print("normalized =", (arr - np.mean(arr)) / np.std(arr))

print("\n 2. UFUNCS ")
print("sin(arr) =", np.sin(arr))
print("exp(arr) =", np.exp(arr))
print("log(arr + 1) =", np.log(arr + 1))
print("sum =", np.sum(arr), "mean =", np.mean(arr))

print("\n 3. MASQUES BOOLÉENS ")
data = np.array([-2, -1, 0, 1, 2, 3, 4])
print("data > 0 =", data[data > 0])
print("data pairs =", data[data % 2 == 0])
data[data < 0] = 0
print("négatifs → 0 =", data)
print("nombre > 1 =", np.sum(data > 1))

print("\n 4. BROADCASTING ")
matrix = np.ones((3, 4))
print("matrix + 5 =\n", matrix + 5)

col = np.array([1, 2, 3]).reshape(3, 1)
print("\ncol vector shape:", col.shape)
print("matrix + col =\n", matrix + col)

row = np.array([10, 20, 30, 40])
print("\nrow vector shape:", row.shape)
print("matrix + row =\n", matrix + row)

print("\n 5. APPLICATION COMBINÉE ")
temps = np.array([22.5, 18.3, 25.1, 16.8, 30.2, 19.5])
fahrenheit = temps * 9/5 + 32
z_scores = (temps - np.mean(temps)) / np.std(temps)
jours_chauds = temps[temps > 25]
ajustement = np.array([-2, -2, 0, 0, 2, 2])
ajuste = temps + ajustement

print("°C:", temps)
print("°F:", fahrenheit)
print("z-scores:", z_scores)
print("jours > 25°C:", jours_chauds)
print("ajusté:", ajuste)