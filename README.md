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

### Question 5 :

Display the number of choice for each question.

````python
from polls.models import Question
questions = Question.objects.all()
for question in questions:
    num_choices = question.choice_set.count()
    print(f"ID: {question.id}, Number of Choices: {num_choices}") 
ID: 1, Number of Choices: 3
ID: 2, Number of Choices: 3
ID: 3, Number of Choices: 3
ID: 4, Number of Choices: 3
ID: 5, Number of Choices: 3
````

### Question 6 :

...

### Question 7 :

Sorted in antechronological order.

````python
from polls.models import Question

questions = Question.objects.all().order_by('-pub_date')
for question in questions:
    print(f"ID: {question.id}, Question Text: {question.question_text}, Pub Date: {question.pub_date}")
ID: 5, Question Text: What's your favorite car's brand ?, Pub Date: 2024-10-09 07:02:29+00:00
ID: 2, Question Text: What's your favorite sport ?, Pub Date: 2024-10-08 13:50:27+00:00
ID: 1, Question Text: What's up?, Pub Date: 2024-10-08 12:18:03+00:00
ID: 3, Question Text: What's your favorite country ?, Pub Date: 2024-10-05 11:55:20+00:00
ID: 4, Question Text: What's your favorite hobbie?, Pub Date: 2024-10-01 06:58:29+00:00
````

### Question 8 :

...

### Question 9 :

Create question.

````python
from polls.models import Question
from django.utils import timezone
q = Question(question_text="Where is the world's highest bungee jump?", pub_date=timezone.now())
q.save()
````

### Question 10 :

Add three choices to the question.

````python
from polls.models import Choice, Question
q.choice_set.create(choice_text="China",votes=0)
<Choice: China>
q.choice_set.create(choice_text="France",votes=0) 
<Choice: France>
q.choice_set.create(choice_text="United States of America",votes=0)
<Choice: United States of America>

````

### Question 11 :

Question listed recently (last 3 days) 

````python
from polls.models import Question
from datetime import datetime, timedelta

date_limit = datetime.now() - timedelta(days=7)
recent_questions = Question.objects.filter(pub_date__gte=date_limit)

for question in recent_questions:
    print(f"ID: {question.id}, Question Text: {question.question_text}, Pub Date: {question.pub_date}")
````
