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
Modify the view function "index" in views.py to render a template (call it "list.html"), The dictionary should only contain one key pair that represent the ToDoList object we are interested in. 


- Create a template for the webpage under the name "aboutme.html", it should extend the base template "base.html"
- The body of the webpage should display the text "I like learning Django", the footer should display the text "Copyright 2021 FT3"

Modify the view function "index" in views.py. 
