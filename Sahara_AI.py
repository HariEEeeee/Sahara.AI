import mysql.connector
from PIL import Image


def intro():
    return '''\n
    🏜️Sahara.ai — Where Ideas Bloom Into Pixel Art!
    
    ✨ Introduction
    In the endless sands of imagination, Sahara.ai stands tall like an oasis of creativity!
    Type a word, cast a spell — and Sahara.ai brings it to life with beautiful pixel art. 🎨🌟
    Our Python-powered AI project captures the magic of turning simple prompts into colorful, pixel-perfect images —
        
        💡What Can Sahara.ai Do?
        ✍️ Turn Any Text Prompt into Pixel Art
           Type a word like "spider" or "castle," and Sahara.ai instantly creates colorful pixel art from your 
           imagination!
        
        🖼️ Save Generated Pixel Art Automatically
           Every pixel masterpiece created by Sahara.ai is automatically saved so you never lose your creations.
        
        🗄️ Connect to a Real MySQL Database
           Sahara.ai securely stores your prompts, timestamps, and generated artwork information in a powerful MySQL 
           database.
        
        🔎 Track and View Your Past Creations
           Sahara.ai remembers everything you've created — making it easy to view and treasure your old pixel artworks 
           anytime.
        
        🗂️ Choose Existing Images and Convert Them to Pixel Art
           Upload your favorite photos or drawings — Sahara.ai will pixel-ify them in seconds!
        
        🎨 Create a Custom Color Palette
           Design your own color palette to give your pixel art a unique style and flavor.
        
        📏 Customize Pixel Art Dimensions and Size
           Want bigger or tiny pixel artworks? Sahara.ai lets you choose the width, height, and resolution for your 
           creations!'''


def image_to_pixelart():
    # block size

    block = int(input("Select the level of details:"))
    print("Choose between 2 - 25, remember the more number you select the detailed your image :")
    # height and width

    height = int(input("Choose the height of the image:"))
    width = int(input("Choose the width of the image:"))

    # here's the code
    image_from_user = input("Enter the path of the file you want to make pixel art:")
    img = Image.open(image_from_user)

    pixel_size = img.resize((height, width), resample=Image.BILINEAR)

    resizing = pixel_size.resize(img.size, Image.NEAREST)
    resizing.show()


# log in ??
secret_code = input("Set your Secret code( press any key to know more ):")
length_of_SC = len(secret_code)
if length_of_SC >= 0:
    intructions = """
    🔐 Secret Code Instructions
Enter a secret code using letters, numbers & symbols.

Keep it safe — you'll need it to log in next time.

⚠️ If you forget it, your data cannot be recovered.
"""
else:
    print("Secret code created Successfully :) and remember not to forget it!!")
    email_id = input("Enter your Secret code:")
    print(email_id)

#options
Query = input("What would you like to do? :")
option1 = "Turn image into Pixel Art"
option2 ="Create a color palette"
option3 ="Save a color palette"

if Query == option1:
    print(image_to_pixelart())
elif Query == option2:



#Image to pixel art


color_list = []
# def custom_color():

while True:
    clr = input("Enter the the colours you want (eg:#00000,#:")
    if clr == 'done':
        break
    else:
        color_list.append(clr)
        print(color_list)

# Saved color palettes
clr_palette1 = []


# prompt to pixel art
prompt = input("Describe your image:")

# Database Connectivity
database = mysql.connector.connect(
    host="localhost",
    user="hippo",
    password="Sahara123/"
)
Db_cursor = database.cursor()
Db_cursor.execute("Create Database Sahara_AI")
