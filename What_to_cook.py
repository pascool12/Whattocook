import requests as rq
import json
from tkinter import *
import tkinter
import tkinter.scrolledtext as scrolledtext

from PIL import ImageTk, Image

class food:
    def __init__(self):
        self.title = None
        self.origin = None
        self.reciepe = None
        self.pic = None
        self.category = None
        self.mealdict = {'idMeal': '52797', 'strMeal': 'Spicy North African Potato Salad', 'strDrinkAlternate': None,
                    'strCategory': 'Vegetarian', 'strArea': 'Moroccan',
                    'strInstructions': 'Cook potatoes - place potatoes in a pot of cold water, and bring to the boil. Boil 20 minutes, or until potatoes are tender. You know they are cooked when you can stick a knife in them and the knife goes straight through.\r\nCombine harissa spice, olive oil, salt and pepper and lemon juice in a small bowl and whisk until combined.\r\nOnce potatoes are cooked, drain water and roughly chop potatoes in half.\r\nAdd harissa mix and spring onions/green onions to potatoes and stir.\r\nIn a large salad bowl, lay out arugula/rocket.\r\nTop with potato mix and toss.\r\nAdd fetta, mint and sprinkle over pine nuts.\r\nAdjust salt and pepper to taste.',
                    'strMealThumb': 'https://www.themealdb.com/images/media/meals/urtwux1486983078.jpg',
                    'strTags': 'Vegetarian,Spicy', 'strYoutube': 'https://www.youtube.com/watch?v=zxBzwJvTK4g',
                    'strIngredient1': 'Small Potatoes', 'strIngredient2': 'Harissa Spice',
                    'strIngredient3': 'olive oil', 'strIngredient4': 'Lemon', 'strIngredient5': 'Spring onions',
                    'strIngredient6': 'Rocket', 'strIngredient7': 'Feta', 'strIngredient8': 'Mint',
                    'strIngredient9': 'Pine nuts', 'strIngredient10': 'Salt', 'strIngredient11': 'Pepper',
                    'strIngredient12': '', 'strIngredient13': '', 'strIngredient14': '', 'strIngredient15': '',
                    'strIngredient16': '', 'strIngredient17': '', 'strIngredient18': '', 'strIngredient19': '',
                    'strIngredient20': '', 'strMeasure1': '650g/1lb 8 oz', 'strMeasure2': '1 tsp',
                    'strMeasure3': '2 tsp', 'strMeasure4': 'juice of half', 'strMeasure5': '4',
                    'strMeasure6': '150g/6oz', 'strMeasure7': '80g/3oz', 'strMeasure8': '20 chopped',
                    'strMeasure9': '2 tablespoons', 'strMeasure10': 'Pinch', 'strMeasure11': 'Pinch',
                    'strMeasure12': '', 'strMeasure13': '', 'strMeasure14': '', 'strMeasure15': '', 'strMeasure16': '',
                    'strMeasure17': '', 'strMeasure18': '', 'strMeasure19': '', 'strMeasure20': '', 'strSource': '',
                    'strImageSource': None, 'strCreativeCommonsConfirmed': None, 'dateModified': None}
        self.Shoppiglist = None

    def testveg(self):
        food = self.mealdict
        reciepeclean1 = None
        f = food["strInstructions"].replace("\r", "")
        f = f.replace("\n", "")
        f = f.replace(".", ".\n")
        self.reciepe = f
        self.title = food["strMeal"]
        self.category = food["strCategory"]
        self.origin = food["strArea"]
        print(self.reciepe)
        self.pic = food['strMealThumb']

    def vegetarian(self):
        url = "http://www.themealdb.com/api/json/v1/1/random.php"
        x = 0
        vegetarian = False
        food = None
        while vegetarian == False:
            if x == 30:
                vegetarian = True
                print("iterationlimit reached, try again")
                break
            r = rq.get(url=url)
            data = json.loads(r.text)
            data1 = data["meals"]
            mealdict = None
            for item in data1:
                mealdict = item
            print(mealdict["strCategory"])
            if mealdict["strCategory"] == "Vegetarian":
                vegetarian = True
                food = mealdict
                print(mealdict)
                print("found vegetarian food for u <3")
            if mealdict["strCategory"] == "Vegan":
                vegetarian = True
                food = mealdict
                print(mealdict)
                print("found vegan food for u <3")
            else:
                x += 1
                print("iterate further")
        self.title = food["strMeal"]
        self.category = food["strCategory"]
        self.origin = food["strArea"]
        self.reciepe = food["strInstructions"].replace(".", ".\n")
        self.pic = food['strMealThumb']
        self.mealdict = mealdict
        return self.title, self.category, self.origin, self.reciepe, self.pic, mealdict


    def reciepe_getter(self):
        #for real process
        #a = vegetarian()
        #print(a.mealdict["strIngredient1"])
        #for testing
        Shoppinglist = ""
        number = 0
        while number < 20:
            number += 1
            i = str(number)
            Shoppinglist = Shoppinglist + str(self.mealdict['strIngredient'+i]) + ":\t" + str(self.mealdict['strMeasure'+i]) + "\n"
            if str(self.mealdict['strIngredient'+i]) == "":
                number = 20
            else:
                pass
            self.Shoppiglist = Shoppinglist
        return self.Shoppiglist

a = food()
a.vegetarian()
a.reciepe_getter()

infotext = str(a.title+"\n\n"+a.origin)


win = tkinter.Tk()
win.geometry('1200x550+50+50')
win.title(str(a.title))
win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)

frame = Frame(win, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.85, rely=0.25)
url=a.pic
img = ImageTk.PhotoImage(Image.open(rq.get(url, stream=True).raw).resize((250,250)))
label = Label(frame, image = img)
label.pack()

textbox = scrolledtext.ScrolledText(win, width=100, height=20, wrap="word", undo=True)
textbox['font'] = ('consolas', '10')
textbox.pack(expand=True, fill='both')
#textbox = Text(win, width=30, height=30, wrap="word", yscrollcommand=scroller.set)
#textbox.pack()
textbox.place(anchor='center', relx=0.35, rely=0.70)
textbox.insert(0.3, a.reciepe)
#textlabel = Label(textbox, text=a.reciepe)
#textlabel.pack()

textbox1 = Text(win, width=30, height=30, wrap="word")
textbox1.pack()
textbox1.place(anchor='center', relx=0.85, rely=0.75)
textbox1.insert(0.3, a.reciepe)
textlabel1 = Label(textbox1, text=a.Shoppiglist)
textlabel1.pack()

textbox2 = Text(win, width=30, height=30, wrap="word")
textbox2.pack()
textbox2.place(anchor='center', relx=0.32, rely=0.15)
textbox2.insert(0.3, a.reciepe)
textlabel2 = Label(textbox2, text=infotext, font=("Arial", 20))
textlabel2.pack()


win.mainloop()

