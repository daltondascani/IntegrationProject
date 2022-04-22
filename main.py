"""Welcome to my Integration Project. This program is designed to help the user
achieve their fitness goals and guide them in the correct direction."""
__author__ = "Dalton Dascani"

import time


def main():
    """
This is an introduction to the user and main entry to the program, which then
executes the menu and gives the user options for what they want to see.
    """
    user_name = input("What is your name? ")
    print("Welcome", user_name, end='. ')
    print(
        "This program is designed to help you achieve your fitness goals and "
        "supply exercise options that are catered toward your desires.")
    print("Lets get started!")
    time.sleep(4)
    menu()


def menu():
    """
The menu loads and prompts the user to select an option of their preference.
    """
    loop_progress = True
    while loop_progress:
        try:
            answer = int(input(
                "Please select an option number: \n1. Calculate calories\n"
                "2. Workout "
                "Routines\n3. Cardio Routines\n4. Daily Calorie Tracker"
                "\n5. Quit Program\n"))
            if answer == 1:
                calorie_calculator()
            elif answer == 2:
                workout_program()
            elif answer == 3:
                cardio_routine()
            elif answer == 4:
                calorie_tracker()
            elif answer == 5:
                quit()
            else:
                print("Invalid Input. Please try again.")
                loop_progress = False
        except ValueError:
            print("Invalid Input. Please try again bro.")
            menu()


def calorie_calculator():
    """
Function designated to calculate the user's calories based off of their body's
metrics. Function then prompts user to decide if they want to lose fat or gain
muscle, and it returns the proper amount of calories to eat.
    :return:
    """
    print("This section of the program will calculate the calories you need to"
          " gain muscle or to lose fat.")
    time.sleep(2)
    weight = int(input("Enter your weight (lbs): "))
    if weight == ValueError:
        print("Invalid input. Please try again")
        calorie_calculator()
    height = int(input("Enter your height (inches): "))
    if height == ValueError:
        print("Invalid input. Please try again")
        calorie_calculator()
    age = int(input("Enter your age number: "))
    if age == ValueError:
        print("Invalid input. Please try again")
        calorie_calculator()
    bmr_male = 66.5 + (13.75 * weight) + (5 ** 1 * height) - (
            6.755 * age)
    # created a formula to help calculate calories
    # using the +,-,* operators.
    bmr_female = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    # calorie/BMR formula found using a quick google search.
    male_gain_muscle = round(bmr_male * 1.3)
    female_gain_muscle = round(bmr_female * 1.3)
    male_fatloss = round(bmr_male * 2.75 // 2 - 700)
    female_fatloss = round(bmr_female * 3 / 2.2 - 500)
    gender = input("Are you a male or a female? ")
    if gender == "male":
        print("to gain muscle quickly, you should be eating around",
              male_gain_muscle, "calories a day.")
        time.sleep(3)
        print("To lose fat quickly, you should be eating around",
              male_fatloss, "calories a day.")
    elif gender == "female":
        print(",to gain muscle quickly, you should be eating",
              female_gain_muscle, "calories a day.")
        time.sleep(3)
        print("To lose fat quickly, you should be eating",
              female_fatloss,
              "calories a day.")
    else:
        print("Error, exiting program.", sep='')
        print("Calorie calculation complete."
              " Returning to main menu...")
        time.sleep(4)
        menu()


# This code will create beginner style weight training workouts based on what
# muscle groups you would like to train/improve on.
def workout_program():
    """
Function designated to provide workouts for each muscle group that user wants
to train. If they can't decide there is a random option to generate one of
the following in the list.
    :return:
    """
    import random
    workout_type = input((
        "Please select from the following:\nchest\nback\narms"
        "\nlegs\nshoulders\nrandom\n"))
    chest = (
        "4 sets of 8 barbell bench press, 3 sets of 10 incline dumbbell press,"
        " 3 sets of 12 cable chest flyes, 3 sets of 15 push-ups,"
        " and 3 sets of 10 dips.")
    back = (
        "4 sets of 6 barbell deadlifts, 3 sets of 10 lateral pull-downs,"
        " 3 sets of 12 barbell rows, 3 sets of 8 pull-ups,"
        " and 3 sets of 10 cable pullovers.")
    legs = (
        "4 sets of 8 barbell squats, 3 sets of 10 barbell deadlifts, "
        "3 sets of 12 leg extensions, 3 sets of 12 hamstring curls,"
        " and 3 sets of 10 lunges")
    arms = (
        "3 sets of 10 barbell curls, 3 sets of 20 cable tricep extensions,"
        " 3 sets of 20 dumbbell curls, 3 sets of 20 hammer curls,"
        " and 4 sets of 20 bench dips.")
    shoulders = (
        "3 sets of 10 overhead press, 4 sets of 12 dumbbell lateral raises,"
        " 3 sets of 10 cable face pulls, and 3 sets of 10 push-ups.")
    count = 0
    items = [chest, back, legs, arms, shoulders]
    if workout_type == "chest":
        count += 1
        print(chest)
    elif workout_type == "back":
        count += 1
        print(back)
    elif workout_type == "legs":
        count += 1
        print(legs)
    elif workout_type == "arms":
        count += 1
        print(arms)
    elif workout_type == "shoulders":
        count += 1
        print(shoulders)
    elif workout_type == "random":  # found this out using datagy.io website,
        count += 1
        random = random.choice(items)
        print(random)
    if count >= 1:
        time.sleep(3)
        user_input = input("Do you want to make another selection? (yes/no) ")
        if user_input == "yes":
            workout_program()
        else:
            print("Returning to main menu...")
            time.sleep(2)
            menu()
    else:
        print("Invalid input! Please try again.")
        workout_program()


# Cardio routine if the user would like it.
def cardio_routine():
    """
Function provides the user with cardiovascular exercise at their choice
if they decline, they are prompted to go back to menu.
    :return:
    """
    cardio = input("Are you interested in doing cardio exercise? (yes/no) ")
    if cardio == "yes":
        print(
            "25 minutes on the treadmill with the incline set to 10,"
            "\nor a 30 minute run/jog outside"
            " will be a beneficial cardio workout.")
        time.sleep(2)
        user_input = input("Would you like to return to the main menu? "
                           "(yes/no) ")
        if user_input == "yes":
            menu()
        elif user_input == "no":
            cardio_routine()
        else:
            print("Invalid Input! Please try again.")
            cardio_routine()
    elif cardio != "yes":
        print("No cardio selected, returning to main menu...")
        time.sleep(2)
        menu()


def calorie_tracker():
    """
function designated for tracking the user's calories they consume daily.
    :return:
    """
    print("This section is made to help track your calories as you eat.")
    calories = int(input("Enter the calories for the food you consumed: "))
    total_cals = 0
    count = 0
    while calories >= 0:
        count += 1
        total_cals += calories
        calories = int(input("Enter the calories for the food you consumed: "))
        if count >= 1:
            user_input = input(
                "Do you want to enter another item? (yes/no) ")
            if user_input == "yes":
                calories = int(
                    input("Enter the calories for the food you consumed: "))
                total_cals += calories
            else:
                total_cals += calories
                print("Total calories consumed: ", total_cals)
        user_input = input(
            "Would you like to return to the main menu? (yes/no) ")
        if user_input == "yes":
            menu()


def unused():
    """
An unused part of my program that could not work in naturally.
    """
    print("below is an example of a for loop because  "
          "I could not fit it naturally into my program.")
    for i in range(3):
        for j in range(3):
            print("*")


# main function gets executed and runs entire program from menu
if __name__ == "__main__":
    main()
