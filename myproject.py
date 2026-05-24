
score = 0

questions = {    
    "Who is the current prime minister of Nepal?": {        
        "options": [
            "A. Balendra Shah",
            "B. KP Oli",
            "C. Pushpa Kamal Dahal",
            "D. Dr. Babu Ram Bhatta"
        ],
        "answer": "A"
    },
    
    "What is the national color of Nepal?": {
        "options": [
            "A. White",
            "B. Blue",
            "C. Crimson",
            "D. Purple",
        ],
        "answer": "C"
    },
    "Who is the father of Computer?": {
        "options": [
            "A. Ada Lovelace",
            "B. Alan Turing",
            "C. Grace Hopper",
            "D. Charles Babbage",
        ],
        "answer": "D"
    },
    
    "Which country won the FIFA world cup 2022?": {
        "options": [
            "A. Brazil",
            "B. Argentina",
            "C. Italy",
            "D. France",
        ],
        "answer": "B"
    },
    
    "How many times did Brazil win the FIFA world cup?": {
        "options": [
            "A. 2",
            "B. 3",
            "C. 4",
            "D. 5",
        ],
        "answer": "D"
    },
    
    "Who won the best Actress Oscar in 2026?": {
        "options": [
            "A. Jessie Buckley",
            "B. Emma Stone",
            "C. Jennifer Lawrence",
            "D. Kate Winslet",
        ],
        "answer": "A"
    },
    
    "Who was the first martyr of Nepal?": {
        "options": [
            "A. Shukraraj Shastri",
            "B. Dharma Bhakta Mathema",
            "C. Gangalal Shrestha",
            "D. Lakhan Thapa Magar",
        ],
        "answer": "D"
    },
    
    "Who is known as the Light of the world?": {
        "options": [
            "A. Jesus Christ",
            "B. Siddartha Gautam Buddha",
            "C. Mahatma Gandhi",
            "D. Aung San Suu Kyi",
        ],
        "answer": "A"
    },
    
    "Who won the Nobel Peace Prize in Nepal?": {
        "options": [
            "A. Dr. Sanduk Ruit",
            "B. Kailash Satyarthi ",
            "C. Parijat",
            "D. Laxmi Prasad Devkota",
        ],
        "answer": "B"
    },
    
    "When is the festival Christmas celebrated?": {
        "options": [
            "A. December 10",
            "B. December 15 ",
            "C. December 25",
            "D. December 26"
        ],
        "answer": "C"
    }
}

for question, data in questions.items():
    print("\n" + question)

    for option in data["options"]:
        print(option)
    
    user_answer = input("Answer: ").upper()
    
    if user_answer.upper() == data["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        
print("\nYour final score: ", score, "/", len(questions))

if score == len(questions):
    print("Outstanding!")
elif score >= 8:
    print("Excellent!")
elif score >= 6:
    print("Great Job!")
elif score >= 4:
    print("Good!")
else:
    print("Please Try Again!")       
