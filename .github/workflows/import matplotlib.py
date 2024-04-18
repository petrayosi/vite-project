import matplotlib.pyplot as plt

# Nilai X1
x1_values = [10, 15, 20]

# Koefisien regresi
intercept = 8.743053
slope_x1 = 3221
slope_x2 = 0.001456

# Menghitung nilai Y
y_values = [intercept + slope_x1 * x1 + slope_x2 * x2 for x1, x2 in zip(x1_values, x2_values)]

# Plot grafik
plt.plot(x1_values, y_values, marker='o', linestyle='-')
plt.title('Prediksi Berdasarkan Model Regresi Linier Berganda')
plt.xlabel('Nilai X1')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.show()
