from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

interval = 20
thresholdValue = sense.temp

while True:
    currentTemp = sense.temp - thresholdValue

    if currentTemp > 0:
        sense.clear(48 + round(207 * currentTemp / interval), 0, 0)
    elif currentTemp < 0:
       sense.clear(0, 0, 48 + round(207 * (-currentTemp) / interval))
    else:
        sense.clear(0, 0, 0)

    print("Current Temp: %s" % currentTemp)