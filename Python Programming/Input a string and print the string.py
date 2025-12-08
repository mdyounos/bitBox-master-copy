# String=input("Which is the Best Guide for Govt. Job?\n")
# print("Your answer is: ",String)



# A better, cleaner, and more Pythonic version of your question program

def ask_questions():
    questions = [
        "Which is the Best Guide for Govt. Job?",
        "Which subject do you find most difficult?",
        "How many hours do you study daily?",
        "Which exam are you preparing for?",
        "Do you prefer online or offline coaching?"
    ]
    
    answers = {}  # Dictionary to store question-answer pair

    print("\n--- Welcome to the Study Feedback Program ---\n")

    for index, question in enumerate(questions, start=1):
        user_input = input(f"{index}. {question}\n")
        answers[question] = user_input
        print()  # blank line for clean spacing

    return answers


def show_answers(answers):
    print("\n--- Your Answers Summary ---\n")
    for question, answer in answers.items():
        print(f"{question}\n↪️  {answer}\n")


# MAIN PROGRAM
responses = ask_questions()
show_answers(responses)
