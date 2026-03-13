import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 33, 31, 29, 28, 27]

plt.plot(days, temperature, marker='o')

plt.title("Temperature Trend Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.show()
