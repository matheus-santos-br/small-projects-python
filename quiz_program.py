quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer?: ")

    if(answer.lower() == value["answer"].lower()):
        print("Correct!")
        score += 10
    else:
        print("Wrong answer!")
    
    print(F"Your score is {str(score)}")
    print("")
    print("")

print(F"You got {str(score)} points ({str((score * 100) / (len(quiz) * 10))}%).")