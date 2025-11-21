# -- importing the text wrap module -- 
import textwrap


# -- color palette --
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"


# -- variable declarations --
low_weight = normal_weight = overweight = obese_1 = obese_2 = obese_3 = 0
pacients = []
highest_weight = 0
amount_of_people = 0


# -- initial greeting block -- 
print(BOLD + BLUE + "=" * 80 + RESET)
print(BOLD + WHITE + " WELCOME TO THE BMI CALCULATOR ".center(80) + RESET)
print(BOLD + BLUE + "=" * 80 + RESET)
print(BOLD + CYAN + "If you want to stop the program, just enter 0!".center(80) + RESET)
print(BOLD + BLUE + "-" * 80 + RESET)


# -- loop until doctor enters 0 for height, name or weight -- 
while True:
    try:
        # -- Collecting the values -- 
        name = str(input(BOLD + YELLOW +"Enter the patient´s name: " + RESET))
        weight = float(input("Enter their weight: "))
        height = float(input("Enter their height: "))

        # -- if the doctor wants to end the program -- 
        if weight == 0 or height == 0 or name == 0 :
            print(BOLD + RED + "END PROGRAM" + RESET)
            break

        # -- calculating the BMI -- 
        BMI_calculator = round(weight / (height**2), 2)

        # -- saving the BMI value inside a variable -- 
        BMI_value = BMI_calculator

        # -- calculating the minimum and maximum of the ideal weight  -- 
        weight_ideal = round(18.6 * (height**2), 2)
        weight_ideal_max = round(24.9 * (height**2), 2)

        # -- checking the classification of the BMI value -- 
        if BMI_value <= 18.5:
            classification = "Underweight"
            message = "See a nutritionist and a doctor to learn more about your health!"
            low_weight += 1
        elif BMI_value <= 24.9:
            classification = "Normal weight "
            message = "Congratulations, Keep taking care of yourself!"
            normal_weight += 1
        elif BMI_value <= 29.9:
            classification = "Overweight"
            message = "Avoid unhealthy, high-calorie foods!"
            overweight += 1
        elif BMI_value <= 34.9:
            classification = "Obese 1"
            message = "See a nutritionist and a doctor. Start doing some physical exercise!"
            obese_1 += 1
        elif BMI_value <= 39.9:
            classification = "Obese 2"
            message = "Seek clinical help before it becomes harder to reverse the obesity!"
            obese_2 += 1
        else: 
            classification = "Obese 3"
            message = "See a doctor before it becomes too late to restore your health!"
            obese_3 += 1
        
        # -- Collecting the amount of pacients that entered the program -- 
        amount_of_people += 1
        
        # -- printing each patient's ideal weight values, medical recommendations, BMI value and its classification -- 
        print(BOLD + BLUE + "\n" + "=" * 60 + RESET)
        print(BOLD + WHITE + f"Resulf of {name.upper()}".center(60) + RESET)
        print(BOLD + BLUE + "=" * 60 + RESET)
        print(f"{WHITE}BMI value: {BOLD}{BMI_value}{RESET}")
        print(f"{WHITE}Classification: {BOLD}{classification}{RESET}")
        print(f"{WHITE}Ideal minimum weight: {BOLD}{weight_ideal} kg{RESET}")
        print(f"{WHITE}Ideal max weight: {BOLD}{weight_ideal_max} kg{RESET}")
        recomendation = "\n".join(textwrap.wrap(message, width=40))
        print(f"{BOLD}Recomendation:{RESET} {recomendation}")
        print(BOLD + BLUE + "-" * 60 + RESET)

        # -- Collecting the values of each pacient in a dictionary -- 
        pacients.append({
            'name' : name,
            'weight' : weight,
            'height': height,
            'BMI': BMI_value,
        })        
    
    # -- if the doctor enters a value that isn't the correct number type -- 
    except ValueError:
        print("Invallid Entered! Enter only numbers")
    except KeyboardInterrupt:
        print("Ending the program")
        break


# -- Collecting data of each pacient --
if pacients:
    weight = [i['weight'] for i in pacients]
    height = [i['height'] for i in pacients]
    BMI = [i['BMI'] for i in pacients]

    heighst_weight = max(weight)
    Lower_weight = min(weight)
    Higher_height = max(height)
    Lower_height = min(height)
    Higher_BMI = max(BMI)
    Lower_BMI = min(BMI)

    # -- calculating the media of BMI for the amount of pacients -- 
    BMI_media = round(sum(BMI) / amount_of_people,2)
        

    # -- Block to show the pacients' results -- 
    print("\n" + BOLD + CYAN + "=" * 80 + RESET)
    print(BOLD + WHITE + "Resume of the pacients".center(80) + RESET)
    print(BOLD + CYAN + "=" * 80 + RESET)
    print(f"{YELLOW}Under the weight:{RESET} {low_weight}")
    print(f"{GREEN}Normal weight:{RESET} {normal_weight}")
    print(f"{ORANGE}Overweight:{RESET} {overweight}")
    print(f"{RED}Obesity 1:{RESET} {obese_1}")
    print(f"{RED}Obesity 2:{RESET} {obese_2}")
    print(f"{MAGENTA}Obesity 3:{RESET} {obese_3}\n")

    print(f"{WHITE}Higher weight: {BOLD}{heighst_weight} kg{RESET}")
    print(f"{WHITE}Lower weight: {BOLD}{Lower_weight} kg{RESET}")
    print(f"{WHITE}Higher height: {BOLD}{Higher_height} m{RESET}")
    print(f"{WHITE}Lower height: {BOLD}{Lower_height} m{RESET}")
    print(f"{WHITE}Higher BMI: {BOLD}{Higher_BMI}{RESET}")
    print(f"{WHITE}Lower BMI: {BOLD}{Lower_BMI}{RESET}")
    print(f"{WHITE}Midium of BMI: {BOLD}{CYAN}{BMI_media}{RESET}")

    print(BOLD + BLUE + "\n" + "=" * 80 + RESET)
    print(BOLD + WHITE + " END OF RESUME".center(80) + RESET)
    print(BOLD + BLUE + "=" * 80 + RESET)
