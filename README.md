# **Tutorial Django**  
## 2.2.1 Exercice d'administration


### Question 1 :
In "admin.py" add these codes
``` python
from .models import Choice

admin.site.register(Choice)
```

https://github.com/johandeschamps/django_tuto/blob/main/media/q1.png

### Question 2 :

https://github.com/johandeschamps/django_tuto/blob/main/media/Sans%20titre.png

https://github.com/johandeschamps/django_tuto/blob/main/media/Sans%20titre2.png

### Question 3 : 

Yes

### Question 4 :

1. Add admin class
2. Add options for admin classes
3. Save the admin classes like this 
``` pyhton
admin.site.register(Question, QuestionAdmin)
```
### Question 5 : 

No

### Question 6 :

Need to Check box "Statut équipe", password changed

### Question 7 :

Uncheck box "Actif"

## 2.2.2 Exercice shell

### Question 1 :

Display attributs for each questions

````python
from polls.models import Question

questions = Question.objects.all()
for question in questions:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date: {question.pub_date}")

ID: 1, Texte: What's up?, Date: 2024-10-08 12:18:03+00:00
ID: 2, Texte: What's your favorite sport ?, Date: 2024-10-08 13:50:27+00:00
ID: 3, Texte: What's your favorite country ?, Date: 2024-10-05 11:55:20+00:00
ID: 4, Texte: What's your favorite hobbie?, Date: 2024-10-01 06:58:29+00:00
ID: 5, Texte: What's your favorite car's brand ?, Date: 2024-10-09 07:02:29+00:00
```` 

### Question 2 :

Filter by day
exemple : 09

````python
from polls.models import Question
from datetime import datetime

day = 9
questions_by_day = Question.objects.filter(pub_date__day=day)
for question in question_by_day:
    print(f"ID: {question.id}, Question Text: {question.question_text}, Pub Date: {question.pub_date}")
    
ID: 5, Question Text: What's your favorite car's brand ?, Pub Date: 2024-10-09 07:02:29+00:00
````

### Question 3 :

Find seconde question and display attributs 

````python
from polls.models import Question
question = Question.objects.get(id=2)
print(f"ID: {question.id}, Question Text: {question.question_text}, Pub Date: {question.pub_date}")
````

For display all choices
````python
from polls.models import Choice, Question
q = Question.objects.get(id=2)
q.choice_set.all()
<QuerySet [<Choice: Football>, <Choice: Golf>, <Choice: Tennis>]>
````

### Question 4 :

Display attributs and choices of each questions.

````python
from polls.models import Choice, Question
questions = Question.objects.all()
for question in questions:
    print(f"ID: {question.id}, Texte: {question.question_text}, Date: {question.pub_date}")

choices = question.choice_set.all()
for choice in choices:
    print(f"    Choice ID: {choice.id}, Choice Text: {choice.choice_text}, Votes: {choice.votes}")
````