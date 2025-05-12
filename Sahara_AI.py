# User inputs
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


# prompt to pixel art generator

# block size
def detail_Level():
    block = int(input("Select the level of details:"))
    instruct = "Choose between 2 - 25, remember the more number you select the detailed your image :"


# height and width
def heigt_width():
    height = int(input("Choose the height of the image:"))
    width = int(input("Choose the width of the image:"))


#def custom_color():
color_list = []
while True:
    clr = input("Enter the the colours you want (eg:#00000,#:")
    if clr == 'done':
        break
    else:
        color_list.append(clr)
        print(color_list)

# Wanna save the palette for future use?
collr_enquiry = "Would you like to save your colour palette?"
if collr_enquiry in ["yes","Yes","No","no"]:
    lst_of_col_tobesaved = color_list

# view_image
