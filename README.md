# QuizDemo
Python Quiz App



A simple console-based quiz application written in Python.
The program presents multiple-choice questions, collects user answers, checks correctness, and displays the final score.
This project is useful for practicing classes, object-oriented programming, and user input handling in Python.

Features
Object-oriented structure using Question and Quiz classes
Automatic score tracking
Displays question progress
Interactive console input
Easily extendable (you can add more questions)
Project Structure
quiz_app/
│
├── quiz.py          # Main quiz code
└── README.md        # Project documentation

How It Works
1. Question Class


Each question has:

text: The question itself
choices: A list of possible answers
answer: The correct answer



It also includes a method checkAnswer() to verify the user's response.

2. Quiz Class



Manages:

The list of questions
Current score
Current question index



Handles displaying questions, checking answers, and showing progress.

Example Code Snippet
q1 = Question("Who is the creator of the Python programming language?",
              ["James Gosling","Guido van Rossum","Dennis Ritchie","Bjarne Stroustrup"],
              "Guido van Rossum")

q2 = Question("In which year was Python released?",
              ["1985","1991","1995","2000"],
              "1991")

q3 = Question("What type of language is Python?",
              ["High-level","Low-level","Machine","Assembly"],
              "High-level")

questions = [q1, q2, q3]
quiz = Quiz(questions)
quiz.loadQuestion()

Running the Program

Clone this repository:

git clone https://github.com/<your-username>/python-quiz-app.git
cd python-quiz-app


Run the script:

python quiz.py


Answer the questions interactively in the terminal.

Sample Output
********************Question 1 of 3********************
Question 1: Who is the creator of the Python programming language?
- James Gosling
- Guido van Rossum
- Dennis Ritchie
- Bjarne Stroustrup
Answer: Guido van Rossum
********************Question 2 of 3********************
...
Score:  3
