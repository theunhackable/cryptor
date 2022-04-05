# Cryptor

**Cryptor** is a website that demonstrate simple **encryption** and **decryption** of files. The websites takes a **text file** as input, either  encrypt or decrypt the input file and produce the result as a text file which can be downloaded by the user.

Deployed code is [here](https://cryptor-app.herokuapp.com/) so that anyone can use it.

## Web technologies used

- **HTML** 
- **CSS** 
- **JavaScript** 
- **Flask ( Python Backend)**

## File structure

As we are using **Flask**, a micro-web-framework, it will look for the html and other static files in some default folders. So, the files should be organized in the following way:

```
main_folder/
            static/
                css_files_and_js_files
            templates/
                html_files
            app.py
    
```


We could change the default folders so that Flask will look for the static files in the folder that are given by the developer.but it's not necessary in this project.
So the project file structure looks like the following:

```
cryptor/
    downloads/
    myenv/
        Some_folders_and_files_of_virtual_environment
    static/
        css/
            styles.css
        js/ 
            index.js
    templates/
        index.html
    additional.py
    app.py
```

### Procfile

**Procfile** is a simple text file without any extensions,  used by the **Heroku** cloud server for running a specific **command** by the app on startup.
Heroku cloud server only stores the files that are pushed into the repository but don't know what to do with the files inside the repository. Hence we must specify the command which is used to run the

#### Procfile syntax

A **Procfile** declares its process types on individual lines, each with the following format: 

```bash 
    <process type>: <command>
```

- \<process type\> is an alphanumeric name for your command, such as web, worker, urgentworker, clock, and so on.
- \<command\> indicates the command that every process type should execute on startup, such as:
 
```bash
    bash: echo "Hello World"
``` 

## Requirements for python

- click 8.0.3
- Flask 2.0.2
- gunicorn 20.1.0
- itsdangerous 2.0.1
- Jinja2 3.0.2
- MarkupSafe 2.0.1
- Werkzeug 2.0.2


