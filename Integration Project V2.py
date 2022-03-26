#Dalton Dascani
#Description: A program that interacts with the user's fitness goals by creating a workout program for them.
import time
user_Name=input("What is your name? ")
print("Welcome", user_Name, end = '. ')
print("This program is designed to help you acheive your fitness goals and supply exercise options that are catered toward your desires.")
print("Lets get started!")
time.sleep(4)
def main():
    menu()

def menu():
    answer = int(input("Please select an option: \n1. Calculate calories\n2. Workout Routines\n3. Cardio Routines\n4. Daily Calorie Tracker\n5. Quit Program\n"))
    loop_done = 0
    while not(loop_done):
        if answer < 1 or answer > 5:
            print("Invalid selection. Try again.")
        else:
            if answer == 1:
                CalorieCalculator()
            elif answer == 2:
                WorkoutProgram()
            elif answer == 3:
                CardioRoutine()
            elif answer == 4:
                CalorieTracker()
            elif answer == 5:
                quit()
            else:
                loop_done += 1

#This code will ask the user for their weight, height, gender, and body goals in order to calculate the amount of calories they should be eating.
def CalorieCalculator():
    print("This section of the program will calculate the calories you need to gain muscle or to lose fat.")
    time.sleep(2)
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
        print(user_Name + ",to gain muscle quickly, you should be eating around",(Male_Gain_Muscle),"calories a day.")
        time.sleep(3)
        print("To lose fat quickly, you should be eating around",(Male_Fatloss),"calories a day.")
    elif gender=="female":
        print(user_Name + ",to gain muscle quickly, you should be eating",(Female_Gain_Muscle),"calories a day.")
        time.sleep(3)
        print("To lose fat quickly, you should be eating",(Female_Fatloss),"calories a day.")
    else:
        print("Error, exiting program.", sep = '')
    print("Calorie calculation complete. Returning to main menu...")
    time.sleep(4)
    return menu()

#This code will create beginner style weight training workouts based on what muscle groups you would like to train/improve on.
def WorkoutProgram():
    import random
    workout_type = input(("Please select from the following:\nchest\nback\narms\nlegs\nshoulders\nrandom\n"))
    chest=("4 sets of 8 barbell bench press, 3 sets of 10 incline dumbbell press, 3 sets of 12 cable chest flyes, 3 sets of 15 pushups, and 3 sets of 10 dips.")
    back=("4 sets of 6 barbell deadlifts, 3 sets of 10 lateral pulldowns, 3 sets of 12 barbell rows, 3 sets of 8 pullups, and 3 sets of 10 cable pullovers.")
    legs=("4 sets of 8 barbell squats, 3 sets of 10 barbell deadlifts, 3 sets of 12 leg extensions, 3 sets of 12 hamstring curls, and 3 sets of 10 lunges")
    arms=("3 sets of 10 barbell curls, 3 sets of 20 cable tricep extensions, 3 sets of 20 dumbbell curls, 3 sets of 20 hammer curls, and 4 sets of 20 bench dips.")
    shoulders=("3 sets of 10 overhead press, 4 sets of 12 dumbbell lateral raises, 3 sets of 10 cable face pulls, and 3 sets of 10 pushups.")
    count = 0
    items = [chest, back, legs, arms, shoulders]
    if workout_type=="chest":
        count += 1
        print(chest)
    elif workout_type=="back":
        count += 1
        print(back)
    elif workout_type=="legs":
        count += 1
        print(legs)
    elif workout_type=="arms":
        count += 1
        print(arms)
    elif workout_type=="shoulders":
        count += 1
        print(shoulders)
    elif workout_type=="random": #found this out using datagy.io website,
        count += 1
        random = random.choice(items)
        print(random)
    if count >= 1:
        time.sleep(3)
        user_input = input("Do you want to make another selection? (yes/no) ")
        if user_input == "yes":
            WorkoutProgram()
        else:
            print("Returning to main menu...")
            time.sleep(2)
            return menu()
    else:
        print("Invalid input! Returning to main menu...")
        return menu()

#Cardio routine if the user would like it.
def CardioRoutine():
    Cardio = input("Are you interested in doing cardio exercise? (yes/no) ")
    if Cardio == ("yes"):
        print("25 minutes on the treadmill with the incline set to 10,\nor a 30 minute run/jog outside will be a beneficial cardio workout.")
        time.sleep(2)
        user_input = input("Would you like to return to the main menu? (yes/no) ")
        if user_input == ("yes"):
            return menu()
        elif user_input == ("no"):
            CardioRoutine()
        else:
            print("Error. returning to main menu...")
            return menu()
    elif Cardio != "yes":
        print("No cardio selected, returning to main menu...")
        time.sleep(2)
        return menu()

def CalorieTracker():
    print("This section is made to help track your calories as you eat.")
    Calories = int(input("Enter the calories for the food you consumed: "))
    total_cals = 0
    count = 0
    while Calories >= 0:
        count += 1
        total_cals += Calories
        Calories = int(input("Enter the calories for the food you consumed: "))
        if count >= 1:
            user_input = input(("Do you want to enter another item? (yes/no) "))
            if user_input == "yes":
                Calories = int(input("Enter the calories for the food you consumed: "))
                total_cals += Calories
            else:
                total_cals += Calories
                print("Total calories consumed: ",total_cals)
        user_input = input("Would you like to return to the main menu? (yes/no) ")
        if user_input == "yes":
            return menu()
#main function gets executed and runs entire program from menu
main()



    






    


