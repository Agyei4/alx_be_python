# this code provides a recommendation for 
# various weather condotions
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

#choosing the flow condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")


#Displaying the recommendation

# /tmp/correction/1362158841532185586254326663668238768853_5/100740/780490
# /control-flow/weather_advice.py doesn't contain 
# if\s+weather\s*==\s*['\"]sunny['\"]\s*:\s*print\s*\(\s*['\"]Wear a t-shirt and sunglasses\.['\"]\s*\)