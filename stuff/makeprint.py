from PIL import ImageGrab,Image
import win32api
import time
from datetime import datetime 

CRTL = 0x11
X = 0x58
ALT = 0x12
SHIFT = 0x10

def save(img):
    n = datetime.now()
    name="image_{}_{}.jpg".format(n.strftime('%Y-%m-%d-%H%M%S'),time.time())
    img.save(name,'JPEG')
    print('saved as:',name)
def cutedimage(cord1,cord2):
    img = ImageGrab.grab()
    size = (abs(cord1[0]-cord2[0]),abs(cord1[1]-cord2[1]))
    new = Image.new('RGB',size)
    a = cord1 if cord1<cord2 else cord2
    b = cord1 if a==cord2 else cord2
    for x in range(a[0],b[0]):
        for y in range(a[1],b[1]):
            xy = (x-a[0],y-a[1])
            #print(xy,new.size)
            pixel = img.getpixel((x,y))
            new.putpixel(xy,pixel)
    return new
    
h = 0 if win32api.GetKeyState(0x01)==1 else 1
f = 1

while True:
    if win32api.GetKeyState(ALT) in (-0x7f,-0x80):
        x = win32api.GetKeyState(0x01)
        if x not in (0,1): continue
        if x==h:
            #makeprint()
            h = 0 if x==1 else 1
            if f%2:
                cord1 = win32api.GetCursorPos()
            if not f%2 and f!=0:
                cord2 = win32api.GetCursorPos()
                print('taking print...')
                save(cutedimage(cord1,cord2))
                
            if f==10: f = 0
            f+=1

    else:
        h = 0 if win32api.GetKeyState(0x01)==1 else 1
        f = 1
