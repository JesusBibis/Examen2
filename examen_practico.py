import smbus
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used


# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()


# Draw a black filled box to clear the image. 
draw.rectangle((0,0,width,height), outline=0, fill=0)
            
bus = smbus.SMBus(1)
address = 0x50
regmsbyte = 0x00
reglsbyte = 0x00

nArr= ['0','2','3','1','5','6','7','8','9', '3', '6','4','5','7','8','2','8','4','9','2','8']
arre = []
def StoB(val):
    Val = []
    Val.append(reglsbyte)
    for c in val:
        Val.append(ord(c))
    Val.append(64)
    return Val

def addition():
    i=1 
    suma_pares = 0
    while i < 21 :
        suma_pares = suma_pares + int(nArr[i])
        i = i + 2
    return suma_pares

def subtract():
    i=2 
    resta_nones = 0
    while i < 21 :
        resta_nones = resta_nones - int(nArr[i])
        i = i + 2
    return resta_nones

def nPrimos():
    multi = 1
    primos = [2,3,5,7,11,13,17,19]
    for i in primos:
        multi = multi* int(nArr[i]) 
    return multi

def multitres():
    cuadrado = 0
    mtres = [3,6,9,12,15,18]
    for i in mtres:
        cuadrado = cuadrado+(int(nArr[i])*int(nArr[i])) 
    return cuadrado

#Almacenamos los datos
xx = StoB(nArr)
print (xx)
bus.write_i2c_block_data(address,regmsbyte,xx) 
time.sleep(0.5)
bus.write_i2c_block_data(address,regmsbyte,[reglsbyte])

print(addition())
# Write two lines of text.
draw.text((x, top),       "Suma pares: "+ str(addition()),  font=font, fill=255)
draw.text((x, top+8),str(nArr[1])+"+"+str(nArr[3])+"+"+str(nArr[5])+"+"+str(nArr[7])+"+"+str(nArr[9])+"+"+str(nArr[11])+"+"+str(nArr[13])+"+"+str(nArr[15])+"+"+str(nArr[17])+"+"+str(nArr[19]), font=font, fill=255)



print(subtract())
# Write two lines of text.
draw.text((x, top+16),       "Resta nones: "+ str(subtract()),  font=font, fill=255)
draw.text((x, top+24),str(nArr[2])+"+"+str(nArr[4])+"+"+str(nArr[6])+"+"+str(nArr[8])+"+"+str(nArr[10])+"+"+str(nArr[12])+"+"+str(nArr[14])+"+"+str(nArr[16])+"+"+str(nArr[18])+"+"+str(nArr[20]), font=font, fill=255)

print(nPrimos())
# Write two lines of text.
draw.text((x, top+32),       "Multi primos: "+ str(nPrimos()),  font=font, fill=255)
draw.text((x, top+40),str(nArr[2])+"+"+str(nArr[3])+"+"+str(nArr[5])+"+"+str(nArr[7])+"+"+str(nArr[11])+"+"+str(nArr[13])+"+"+str(nArr[17])+"+"+str(nArr[19]), font=font, fill=255)


print(multitres())
# Write two lines of text.
draw.text((x, top+48),       "Multi tres: "+ str(multitres()),  font=font, fill=255)
draw.text((x, top+56),str(nArr[3])+"+"+str(nArr[6])+"+"+str(nArr[9])+"+"+str(nArr[12])+"+"+str(nArr[15])+"+"+str(nArr[18]), font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
time.sleep(.1)

for i  in range(21,25):
    mensaje = input('Valor '+ str(i)+': ')
    arre.append(str(mensaje))
# Draw a black filled box to clear the image. 
disp.clear()
disp.display()

image2 = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw2 = ImageDraw.Draw(image2)

# Draw a black filled box to clear the image.
draw2.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()


# Draw a black filled box to clear the image. 
draw2.rectangle((0,0,width,height), outline=0, fill=0)

# Write two lines of text.
draw2.text((x, top),       "Suma final",  font=font, fill=255)
draw2.text((x, top+8),     str(addition())+ "+" + str(arre[0])+"+" + str(arre[1])+"+" + str(arre[2])+"+" + str(arre[3]), font=font, fill=255)




def additionf():
    res = addition()
    for i in range(4):
        res = res+int(arre[i])
    return res
print(additionf())
draw2.text((x, top+16),     str(additionf()), font=font, fill=255)
# Display image.
disp.image(image2)
disp.display()
time.sleep(.1)
