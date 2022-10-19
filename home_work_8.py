from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now() 
    interval = timedelta(weeks=1)
    users_for_congratulate = {}
    for user in users:
        # user["birthday"] = user["birthday"].replace(year=current_date.year) # changing birthday year to current for a correct week and weekday
        if current_date < user["birthday"].replace(year=current_date.year) <= current_date + interval:
            day_name = "Monday" if user["birthday"].replace(year=current_date.year).weekday() in (5,6) else user["birthday"].replace(year=current_date.year).strftime("%A")
            if day_name in users_for_congratulate:
                users_for_congratulate[day_name].append(user["name"])
            else:
                users_for_congratulate[day_name] = [user["name"]]
        

                
    for day, user in users_for_congratulate.items():
        print(f"{day}: {', '.join(user)}")
            
# example
# Monday: Bill, Jill
# Friday: Kim, Jan


users = [{"name": "John", "birthday": datetime(year=1990, month=10, day=10)}, #befor
         {"name": "Jim", "birthday": datetime(year=1990, month=10, day=19)}, #current   Wednesday
         {"name": "Pol", "birthday": datetime(year=1990, month=10, day=22)}, #weekend   Saturdate -> Monday
         {"name": "Mary", "birthday": datetime(year=1990, month=10, day=23)}, #weekend  Sanday    -> Monday
         {"name": "Pit", "birthday": datetime(year=1990, month=10, day=24)},  #         Monday        
         {"name": "Garry", "birthday": datetime(year=1990, month=10, day=25)}, #        Tuesday
         {"name": "Davide", "birthday": datetime(year=1990, month=10, day=26)}, # next  Wednesday
         {"name": "Jess", "birthday": datetime(year=1990, month=10, day=27)},  # too late
         ]


get_birthdays_per_week(users)

# result
# Monday: Pol, Mary, Pit
# Tuesday: Garry
# Wednesday: Davide

