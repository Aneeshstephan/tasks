#55. Update a Global Dictionary
#Define a global dictionary student_scores and write functions to:


student_score={}
def add_score(name,score):
    global student_score
    student_score[name]=score
    print(f"score added for {name}:{score}")

def update_score(name,score):
    if name in student_score:
      student_score[name]=score
      print(f"score update for {name}: {score}")
    else:
       print(f"{name} not found")

def display_score():
   global student_score
   print("student score",student_score)

add_score("alice",56)
add_score("jamse",67)
display_score()
update_score("alice",89)  


