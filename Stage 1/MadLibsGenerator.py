print("==========================================")
print("           ALIEN JOB INTERVIEW            ")
print("==========================================")
print("\nWelcome, human.\nYou are applying for a job on Planet Zorblax.\nLet's see if you are qualified...\n")
name = input("What is your name? ")
age = int(input("How old are you? "))
print("\nChoose your strongest skill:")
print("1. Coding\n2. Eating\n3. Sleeping")
skill = input("> ")
print("\nThe alien interviewer looks at your application...\n")
if skill == "1":
    print(f"Alien: Interesting, {name}.\nAlien: We need programmers.\nAlien: You might actually be useful.")

elif skill == "2":
    print(f"Alien: Hmm... {name}.\nAlien: We don't have a food department.\nAlien: But we respect your dedication.")
    
elif skill == "3":
    print(f"Alien: {name}...\nAlien: Our employees work 20 hours a day.\nAlien: You have made a terrible career choice.")
    
else:
    print("Alien: That wasn't one of the options.\nAlien: you seem sus! Bye!")
    print("------------------------------------------")
    print("\nInterview complete.\n")
    exit()

if age < 18:
    print("Alien: You are too young for this position.\nRESULT: REJECTED\n")

else:
    print("\nAlien: You meet the age requirement.")
    if skill == "1":
        print("RESULT: HIRED!\nWelcome to Planet Zorblax!")
    else:
        print("RESULT: REJECTED\nPlease improve your skills and try again.")

print("\n------------------------------------------")
print("\nInterview complete.\n")