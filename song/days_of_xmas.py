
def get_gifts(day):
    
    gifts = ["a partridge in a pear tree 🌳", 
             "two turtle doves 🕊", 
             "three french hens 🐓", 
             "four calling birds 🦜", 
             "five gold rings 💍", 
             "six geese a laying 🥚", 
             "seven swans a swimming 🦢",
             "eight maids a milking 🥛",
             "nine ladies dancing 💃",
             "ten lords a leaping 🤾",
             "eleven pipers piping 🎺",
             "twelve drummers drumming 🥁"]
    
    if day == 0:
        return []

    return [gifts[day - 1]] + get_gifts(day - 1)

def build_gift_message(gift_list):
    
    if len(gift_list) == 1:
        gift_message = gift_list[0]
    else:
        last_item = gift_list[-1:]
        other_items = gift_list[:-1]
        gift_message = "\n\t".join(other_items)
        gift_message += "\n\tand " + last_item[0]
        
    return gift_message

def build_day_description(day_number):
    
    if day_number == 1:
        suffix = "st"
    elif day_number == 2:
        suffix = "nd"
    elif day_number == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    return f"{day_number}{suffix}"
        

def sing_the_song():

    for current_day in range(1,13):

        gift_list = get_gifts(current_day)     
        gift_message = build_gift_message(gift_list)
        day_description = build_day_description(current_day)
            
        print(f"On day {day_description} day of Christmas my true love gave to me:\n\t{gift_message}")
        print()


if __name__ == "__main__":
    sing_the_song()