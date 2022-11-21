from sense_hat import SenseHat

sense = SenseHat()

print("Humidity: %.2f%%" % sense.humidity)
print("Temperature: %.2fC" % sense.temp)
print("Pressure: %.2f bars" % (sense.pressure / 1000))

printFormat = "Humidity: %.2f%%, Temp: %.2fC, Pressure: %.2f bars" % (sense.humidity, sense.temp, (sense.pressure / 1000))

sense.show_message(printFormat)
