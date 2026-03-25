
from PIL import Image

#pic = Image.new(mode="RGB", size=(256, 256), color="white")
#pixels = pic.load()
#for y in range (pic.size[1]):
#    for x in range (pic.size[0]):
#        pixels[x, y] = ((x + y) % 256, (x + y) % 256,125)
#pic.show()
#pic.save('moj prvy bycikel.png')

#pic = Image.open("C:\\Users\\annak\\Desktop\\skola2\\4.3\\schmackeen.png")
#pixels = pic.load()
#for y in range (pic.size[1]):
   # for x in range (pic.size[0]):
    #    temp = pixels[x, y] #urobit priemer z RGB hodnot
        #seda = sum(temp) // 3
       # pixels[x, y] = (seda, seda, seda) #nastavit RGB hodnotu na sivu
     #   if temp[0] > 128: #ak je cervena zlozka vacsia ako 128, nastavime ju na 255, inak na 0
      #      pixels[x, y] = (255,255,255)
       # else:
        #    pixels[x, y] = (0,0,0)
#pic.show()

pic = Image.open("C:\\Users\\annak\\Desktop\\skola2\\4.3\\schmackeen.png")  
pic2 = Image.new(mode="RGB", size=pic.size, color="white")
pixels = pic.load()
pixels2 = pic2.load()
for y in range (pic.size[1]):
    for x in range (pic.size[0]):
       # pixels2[x,y] = pixels[x,pic.size[1] - 1 - y]#prevratenie obrazka
        pixels2[x,y] = pixels[pic.size[0] - 1 - x, y]
pic2.show()