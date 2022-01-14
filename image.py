import psutil, time, datetime, pytz
import urllib.request

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime




def start(username, url):
      platforms = psutil.cpu_count()
      platforms2 = psutil.cpu_percent()
      ramto = round(psutil.virtual_memory().total / (10**6))
      ramuse = round(psutil.virtual_memory().used / (10**6))
      ramfree = round(psutil.virtual_memory().available / (10**6))
      now = datetime.now(pytz.timezone('Asia/Jakarta'))

      image = Image.open("keqing.png")
      print('size:', image.size)

      response = urllib.request.urlopen(url)
      images = Image.open(response)
      IMAGE_WIDTH2, IMAGE_HEIGHT2 = images.size
      x = ((IMAGE_WIDTH2)//6)-5
      y = ((IMAGE_HEIGHT2)//6)-5
      imagee = images.resize([x,y])

      IMAGE_WIDTH, IMAGE_HEIGHT = image.size

      draw = ImageDraw.Draw(image)

      status = "status"
      sys = f"cpu count : {platforms}"
      mch = f"cpu : {platforms2} %"
      text = f"ram : {ramto} mb"
      text2 = f"used : {ramuse} mb"
      text3 = f"free : {ramfree} mb"
      user = username
      uptime = now.strftime("%m/%d/%Y, %H:%M:%S")


      font = ImageFont.truetype('Staatliches-Regular.ttf', 30)
      font2 = ImageFont.truetype('Staatliches-Regular.ttf', 20)


      text_width, text_height = draw.textsize(text, font=font)
      x = ((IMAGE_WIDTH - text_width)//2)-180
      y = ((IMAGE_HEIGHT - text_height)//2)+30
      z = 30
      
      draw.text( (x-z-9, y-(z*5)-16), status, font=font, fill="#4d39cc")
      draw.text( (x, y-(z*4)+16), sys, font=font, fill="#574c9c")
      draw.text( (x, y-(z*3)+16), mch, font=font, fill="#574c9c")
      draw.text( (x, y), text, font=font, fill="#574c9c")
      draw.text( (x, y+z), text2, font=font, fill="#574c9c")
      draw.text( (x, y+(z*2)), text3, font=font, fill="#574c9c")
      draw.text( (x+(z*6)-14.5, y+(z*4)-12), user, font=font2, fill="#4d39cc")
      draw.text( (x+(z*15), y+(z*5)+7), uptime, font=font2, fill="#4d39cc")
      
      image.paste(imagee, (x+(z*18)+5, y-(z*7)+4))

      image.save("neko.png", format='PNG')

while True:
      start("@nekomatanee", "https://pbs.twimg.com/profile_images/1468356893034696704/MooFViNh_400x400.jpg")
      time.sleep(1800)

      









