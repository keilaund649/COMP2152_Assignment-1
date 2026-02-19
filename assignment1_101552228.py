"""
Author: Keilaund Saunders
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton" #str
preferred_weight_kg = 20.5 #float
highest_reps = 25 #int
membership_active = True #bool

# Step c: Create a dictionary named workout_stats

# They keys are the the friends name(str) and the values are a tuples of workout minutes for yoga, running, and weightlifting (int, int ,int)   
workout_stats = {
    "Alex": (30, 45, 25),
    "Jamie": (25, 100, 50),
    "Taylor": (30, 45, 35)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary

for name, minutes in workout_stats.copy().items():
    total = minutes[0] + minutes[1] + minutes[2]
    workout_stats[name + "_Total"] = total
print(workout_stats)

# Step e: Create a 2D nested list called workout_list
#this is a 2d list(list of list)
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]
# Step f: Slice the workout_list

for row in workout_list:
    print(row[0:2])

for row in workout_list[1:]:
    print(row[2])
# Step g: Check if any friend's total >= 120

for friend in ["Alex", "Jamie", "Taylor"]:
    total= workout_stats[friend + "_Total"]
    if total >= 120:
        print("Great Job staying active," + friend + "!")

# Step h: User input to look up a friend

user = input("Enter a name: ")

if user in workout_stats:
    print("Workout minutes: ", workout_stats[user])
    print("Total workout minutes: ", workout_stats[user + "_Total"])
else:
    print("user " + user + " not found in the records.")    

# Step i: Friend with highest and lowest total workout minutes

totals = {"Alex": workout_stats["Alex_Total"], 
          "Jamie": workout_stats["Jamie_Total"], 
          "Taylor": workout_stats["Taylor_Total"]}

print("Highest:", max(totals, key=totals.get))
print("Lowest:", min(totals, key=totals.get))