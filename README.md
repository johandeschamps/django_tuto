# **Tutorial Django**  
## Exercice d'administration


### Question 1
In "admin.py" add these codes
```
from .models import Choice
```
```
admin.site.register(Choice)
```
https://github.com/johandeschamps/django_tuto/blob/main/media/q1.png

### Question 2

https://github.com/johandeschamps/django_tuto/blob/main/media/Sans%20titre.png

https://github.com/johandeschamps/django_tuto/blob/main/media/Sans%20titre2.png

### Question 3 

Yes

### Question 4 

1. Add admin class
2. Add options for admin classes
3. Save the admin classes like this 
```
admin.site.register(Question, QuestionAdmin)
```
### Question 5 

No

### Question 6

Need to Check box "Statut équipe", password changed

### Question 7

Uncheck box "Actif"