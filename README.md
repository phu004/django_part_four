# Django Workshop Exercise 4

In this exercise we will have a look at how "for" and "if" blocks are used in Django templates.
<br/><br/>
## 1. Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```
<br/><br/>

## 2. Using a template to display items of a ToDoList 
Modify the view function "index" in "main/views.py" to render a template (call it "list.html"), The dictionary should only contain a single key pair which represents the ToDoList object we are interested in. 

<details>
  <summary>Click for solution</summary>
  
```sh
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "main/list.html", {"ls": ls})
```
</details>

A template file - "list.html" has already been created in "main/templates/main/", open it and modify the "title" block to show the name of the ToDoList
<details>
  <summary>Click for solution</summary>
  
```sh
{% block title %}
    {{ls.name}}
{% endblock %}
```
</details>

Then Modify the "content" block to list all the items in the ToDoList in a similar way to how "todolist" is listed in "home.html" . (Hint: use "item_set.all" to get items from a ToDoList object)

<details>
  <summary>Click for solution</summary>
  
```sh
{% block content %}
    <ul>
        {% for item in ls.item_set.all %}
            <li>
                {{item.text}}
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```
</details>

<br/><br/>

## 2. Show the items of the list base on whether it is completed.

