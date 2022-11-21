from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = [255, 0, 0]
b = [0, 0, 0]

heartImage = [
b,b,b,b,b,b,b,b,
b,r,r,b,b,r,r,b,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
b,r,r,r,r,r,r,b,
b,b,r,r,r,r,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b
]

sense.set_pixels(heartImage)
