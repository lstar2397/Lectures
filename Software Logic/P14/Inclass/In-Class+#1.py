from sense_hat import SenseHat

sense = SenseHat()

class SenseData(object):
    sense_data = []
    def __init__(self):
        self.get_sense_data()

    def get_sense_data(self):
        self.sense_data.append(sense.get_temperature_from_humidity())
        self.sense_data.append(sense.get_temperature_from_pressure())
        self.sense_data.append(sense.get_humidity())
        self.sense_data.append(sense.get_pressure())

    def write_sense_data(self):
        f = open("output.txt", "w")
        f.write("temp from humidity: %.2f\n" % self.sense_data[0])
        f.write("temp from pressure: %.2f\n" % self.sense_data[1])
        f.write("humidity: %.2f\n" % self.sense_data[2])
        f.write("pressure: %.2f\n" % self.sense_data[3])
        f.close()

    def show_message_sense_data(self):
        sense.show_message("temp from humidity: %.2f" % self.sense_data[0])
        sense.show_message("temp from pressure: %.2f" % self.sense_data[1])
        sense.show_message("humidity: %.2f" % self.sense_data[2])
        sense.show_message("pressure: %.2f" % self.sense_data[3])

senseData = SenseData()
senseData.show_message_sense_data()
senseData.write_sense_data()
