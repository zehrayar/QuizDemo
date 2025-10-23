class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('-' + q)
        
        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber= self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("The quiz is done.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,'*'))


        

q1 = Question("Who is the creator of the Python programming language?", ["James Gosling","Guido van Rossum","Dennis Ritchie","Bjarne Stroustrup"],"Guido van Rossum")
q2 = Question("In which year was the Python programming language released?", ["1985","1991","1995","200"], "1991")
q3 = Question("What type of language is Python?", ["High-level","Low-level","Machine","Assembly"],"High-level")
questions = [q1,q2,q3]

# print(q1.checkAnswer("James Gsoling"))
# print(q2.checkAnswer("1991"))

quiz = Quiz(questions)
quiz.loadQuestion()
