#Dalton Dascani
#Description: A program that interacts with the user's fitness goals by creating a workout program for them.
user_Name=input("What is your name? ")
print("Welcome", user_Name, end = '. ')
print("This program is designed to help you acheive your fitness goals and supply exercise options that are catered toward your desires.")
print("Let's get started with calculating your calorie intake.")

#This code will ask the user for their weight, height, gender, and body goals in order to calculate the amount of calories they should be eating.
weight=int(input("Enter your weight (lbs): "))
height=int(input("Enter your height (inches): "))
age=int(input("Enter your age: "))
BMR_Male=66.5 + (13.75 * weight) + (5**1 * height) - (6.755 * age) # created a formula to help calculate calories using the +,-,* operators.
BMR_Female= 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age) #calorie/BMR formula found using a quick google search.
Male_Gain_Muscle= round(BMR_Male * 1.3)
Female_Gain_Muscle= round(BMR_Female * 1.3)
Male_Fatloss= round(BMR_Male * 2.75//2 - 700)
Female_Fatloss= round(BMR_Female * 3/2.2 - 500)
gender=input("Are you a male or a female? ")
if gender=="male":
    print(user_Name + ",to gain muscle quickly, you should be eating around",(Male_Gain_Muscle),"calories a day."),
    print("To lose fat quickly, you should be eating around",(Male_Fatloss),"calories a day.")
elif gender=="female":
    print(user_Name + ",to gain muscle quickly, you should be eating",(Female_Gain_Muscle),"calories a day.")
    print("To lose fat quickly, you should be eating",(Female_Fatloss),"calories a day.")
else:
    print("Error, exiting program.", sep = '')
    quit()

#This code will create beginner style weight training workouts based on what muscle groups you would like to train/improve on.
print("Please select from the following: chest, back, arms, legs, shoulders, or random.")
workout_type=input("Enter your selection: ")
chest=("4 sets of 8 barbell bench press, 3 sets of 10 incline dumbbell press, 3 sets of 12 cable chest flyes, 3 sets of 15 pushups, and 3 sets of 10 dips.")
back=("4 sets of 6 barbell deadlifts, 3 sets of 10 lateral pulldowns, 3 sets of 12 barbell rows, 3 sets of 8 pullups, and 3 sets of 10 cable pullovers.")
legs=("4 sets of 8 barbell squats, 3 sets of 10 barbell deadlifts, 3 sets of 12 leg extensions, 3 sets of 12 hamstring curls, and 3 sets of 10 lunges")
arms=("3 sets of 10 barbell curls, 3 sets of 20 cable tricep extensions, 3 sets of 20 dumbbell curls, 3 sets of 20 hammer curls, and 4 sets of 20 bench dips.")
shoulders=("3 sets of 10 overhead press, 4 sets of 12 dumbbell lateral raises, 3 sets of 10 cable face pulls, and 3 sets of 10 pushups.")
if workout_type=="chest":
    print(chest)
if workout_type=="back":
    print(back)
if workout_type=="legs":
    print(legs)
if workout_type=="arms":
    print(arms)
if workout_type=="shoulders":
    print(shoulders)
if workout_type=="random": #found this out using datagy.io website,
    import random
    items = [chest,back,legs,arms,shoulders]
    random = random.choice(items)
    print(random)

#Extra Cardio routine if the user would like it.
input("Would you like to incorperate running to your workout as well? ")
if "yes":
    print("25 minutes on the treadmill with the incline set to 10, or a 30 minute run outside will be a beneficial cardio workout.")
    print("Goodbye!")
elif "no":
    print("I hope this program has helped you acheive your fitness goals. Goodbye!")
else:
    quit()





    






    


