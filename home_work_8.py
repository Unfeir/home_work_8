from datetime import datetime


def get_birthdays_per_week(users):
    current_date = datetime.now() 
    users_for_congratulate = {}
    for user in users:
        user["birthday"] = user["birthday"].replace(year=current_date.year) # changing birthday year to current for a correct week and weekday
        if current_date.isocalendar().week == user["birthday"].isocalendar().week and user["birthday"].isocalendar().weekday in (6, 7): # for weekend
            if user["birthday"].strftime("%A") in users_for_congratulate:
                users_for_congratulate[user["birthday"].strftime("%A")].append(user["name"])
            else:
                users_for_congratulate[user["birthday"].strftime("%A")] = [user["name"]]
        
        elif current_date.isocalendar().week + 1 == user["birthday"].isocalendar().week and user["birthday"].isocalendar().weekday in (1, 2, 3, 4, 5): #for next week
            if user["birthday"].strftime("%A") in users_for_congratulate:
                users_for_congratulate[user["birthday"].strftime("%A")].append(user["name"])
            else:
                users_for_congratulate[user["birthday"].strftime("%A")] = [user["name"]]
                
    for day, user in users_for_congratulate.items():
        users = ", ".join(user)
        print(f"{day}: {users}")
            
# example
# Monday: Bill, Jill
# Friday: Kim, Jan


users = [{"name": "John", "birthday": datetime(year=1990, month=10, day=10)}, #befor
         {"name": "Jim", "birthday": datetime(year=1990, month=10, day=19)}, #current
         {"name": "Pol", "birthday": datetime(year=1990, month=10, day=22)}, #weekend   Saturdate
         {"name": "Mary", "birthday": datetime(year=1990, month=10, day=22)}, #weekend  Saturdate
         {"name": "Pit", "birthday": datetime(year=1990, month=10, day=24)},  #         Monday        
         {"name": "Garry", "birthday": datetime(year=1990, month=10, day=28)}, #        Friday
         {"name": "Davide", "birthday": datetime(year=1990, month=10, day=29)}, # next weekend
         {"name": "Jess", "birthday": datetime(year=1990, month=11, day=15)},  # +2 week
         ]

get_birthdays_per_week(users)