# FlaskServerDatabase 
A project made with Flask (python framework for web) that have some functions with API RESTful and CRUD's.  
The project above was created to learn how Server-Side programming and some of python frameworks works. Classes were taught by professor Andrei Carniel at University Católica de Jaraguá do Sul - Santa catarina, Brazil.  
**(All the code comments were written in brazilian portuguese.)**

## Libraries used

*   [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Main library that runs the server and routes.
*   [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) - MySQL Database 
*   [UJSON](https://pypi.org/project/ujson/) - Responsable to transform list data to JSON in a fast way.
*   [OS](https://docs.python.org/3/library/os.html) - Only used to define the main folders pages.

## Project Setup

It's required that you have installed two basic programs in your computer: [Python3.11.0](https://www.python.org/downloads/) or above and [MySQL Workbench Server](https://dev.mysql.com/downloads/installer/). With the two already set in your computer, now install the libraries:

Flask server:
``` 
pip install flask
```
MySQL Workbench Server:
```
pip install mysql-connector-python
```
UJSON library:
```
pip install ujson
```

## Run Project
First you need change the connection settings of your own MySQL Workbench Sever in the dbconnection.py file:
![alt text](https://i.imgur.com/9G5PAmm.png "Connection to the database example")

After that, the only thing needed is to create the database in MySQL Workbench, the database has some basic data to test is in the n3Database.SQL

## Authors
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/80847876?v=4" width=115><br><sub>Nicolas Conte</sub>](https://github.com/MrNicolass) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/141787745?v=4" width=115><br><sub>Higor Azevedo</sub>](https://github.com/HigorAz) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/141975272?v=4" width=115><br><sub>Nathan Cielusinski</sub>](https://github.com/AoiteFoca) |
| :---: | :---: | :---: |
