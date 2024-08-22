questions = ("Q1. What is the capital of france? ",
             "Q2. Which planet is known as Red planet? ",
             "Q3. What is the square root of 16?",
             "Q4. Which continent is the Sahara Desert located on?")
options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
           ("A. 8", "B. 10", "C. 4", "D. 2"),
          ("A. Asia", "B. South America","C. Africa", "D. Australia"))
answers = ("C", "B", "C", "C")
guesses = []
score = 0 
question_num = 0
for question in questions:
    print("-------------------------------------------")
    print("Choose the correct answer:")
    print(" ")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input ("Enter your answer A/B/C/D : ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT ANSWER")
    else:
        print("INCORRECT ANSWER!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
print("*******************")
print("TOTAL SCORE : ", + score)
print("*******************")
