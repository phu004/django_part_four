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

## 2. Useing a template to display items of a ToDoList 
Modify the view function "index" in "main/views.py" to render a template (call it "list.html"), The dictionary should only contain a single key pair which represents the ToDoList object we are interested in. 

<details>
  <summary>Click for solution</summary>
  
```sh
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "main/list.html", {"ls": ls})
```
</details>

