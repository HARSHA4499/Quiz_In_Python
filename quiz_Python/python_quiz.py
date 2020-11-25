from random import shuffle
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

name=input("WELCOME...ENTER YOUR NAME TO START THE GAME  ")

print("HELLO ",name, " HAVE FUN")

print("*******************************************************")

question_prompts = [
     "who is the prime minister of india\n(a) Narendra Modi\n(b)MAnmohan Singh  ",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow  ",
     "who built Taj Mahal?\n (a)Shahjahan (b)Mohammad ALi  ",
     "who is the father of the Nation?(a)vallabai patel (b)Nehry (c)Gandhi  ",
     "who is Founder of Python?(a)Guido Van Rossum (b)Bill Gates (c)Dennis Ri0tchie  "
     ]




questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[4], "a"),
    
]

shuffle(questions)

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          print("------------------------------------------------------------")
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))
     print("----------------------------------------------------------")

while(True):
    run_quiz(questions)
    res=input("Do you want to Play Again type yes/no")
    if res=="no":
        break
    elif res=="yes":
        continue
    else:
        print("you have typed something else")
        break

