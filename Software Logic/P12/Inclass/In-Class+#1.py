from sense_hat import SenseHat

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
    return sense_data

sense_data = get_sense_data()
sense.show_message("temp from humidity: %.2f" % sense_data[0])
sense.show_message("temp from pressure: %.2f" % sense_data[1])
sense.show_message("humidity: %.2f" % sense_data[2])
sense.show_message("pressure: %.2f" % sense_data[3])
