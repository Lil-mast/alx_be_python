# Ask the user about the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses. ")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather ==  "cold":
    print("Make sure to wear a warm caot and a scarf.")
else:
    print("Sorry, I dont have advice for that weather condition. Please enter sunny, rainy, or cold.")