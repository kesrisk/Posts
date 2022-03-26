# Installation

For this small project we are using file based sqlite3, everything is being taken care of in venv, we don't need any external dependency

## steps

- Close this repository
- cd into project
- create virtual env
  ```
    python3 -m venv venv
  ```
 - activate venv
    ```
      for mac
      source venv/bin/activate

      for windows
      venv/Scripts/activate
    ```
 - install requirements
    ```
      pip install -r requirements.txt
    ```
 
 - make and run migrations
    ```
      python manage.py makemigrations

      python manage.py migrate
    ```
  - run server
     ```
      python manage.py runserver
      
      this will server the server at localhost:8000 or 127.0.0.1:8000
     ```
     
  api documentation
  postman requests: https://www.getpostman.com/collections/e4b2d4a655dc6d820aa7
  postman documentaion: https://documenter.getpostman.com/view/1574580/UVyn1e46
  
  
  
We also can use docker to set this up
checkout to branch docker-implementaion

```
    git checkout docker-implementaion
```
