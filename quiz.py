import requests
import mysql.connector
import random
import html

url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"
# Fetch questions from the url of open trivia database
response = requests.get(url)
data = response.json()

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "quiz_game"
)

cursor = db.cursor()

score = 0
name = input("Enter your name: ")

for item in data["results"]:
    print("\n")
    print(html.unescape(item["question"]))

    options = item["incorrect_answers"]
    options.append(item["correct_answer"])
    
    # Shuffles options
    random.shuffle(options)

    letters = ["A", "B", "C", "D"]
    
    # To show options
    for i in range(len(options)):
        print(html.unescape(f"{letters[i]}. {options[i]}"))

        
    user_answer = input("Answer : ").upper()     
    
    while user_answer not in letters:
        print("Please choose from options A, B, C, D!")
        user_answer = input("Answer : ").upper()     
        
    # Finds correct letter
    correct_index = options.index(item["correct_answer"])
    
    correct_letter = letters[correct_index]
    
    if user_answer.upper() == correct_letter:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer was ",correct_letter)
print("\nYour final score: ", score, "out of 10." )

def save_score(name, score):
    query = "INSERT INTO scores (name, score) VALUES (%s, %s)"
    values = (name, score)
    cursor.execute(query, values)
    db.commit()
    print("Score saved successfully!")
    
save_score(name, score)

if score == len(data):
    print("Outstanding!")
elif score >= 8:
    print("Excellent!")
elif score >= 6:
    print("Great Job!")
elif score >= 4:
    print("Good!")
else:
    print("Please Try Again!")       
