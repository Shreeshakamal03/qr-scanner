import qrcode
from pyzbar.pyzbar import decode
from PIL import Image



myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo")
myqr1 = qrcode.make("https://www.youtube.com/watch?v=rz6voM8mQj0&list=RDCMUCk2OqgNGi5_dZ5LTUOk9JZw&start_radio=1")

myqr.save("myqr.png",scale =8)
myqr1.save("myqr1.png",scale =8)

b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))

