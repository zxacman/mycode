heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}


print("Flash is " + heroes['flash']['speed'] + "!")

print("Superman is " + heroes['superman']['strength'] + "!")
print("Batman has the ultimate super power : " + heroes['batman']['strength'] + "!")









char_name= input("Which character do you want to know about? (Flash, Batman, Superman)\n>")
char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence)\n>")

print(f"{char_name}'s {char_stat} is: {heroes[char_name][char_stat]}")
exit
# ANSWER TO BONUS
# this includes the .capitalize(), .lower(), and .upper() methods to "normalize" the input
print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name.lower()][char_stat.lower()].upper()}")
