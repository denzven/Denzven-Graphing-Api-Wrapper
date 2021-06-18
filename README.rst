DenzGraphingApiWrapper_py
======== 

DenzGraphingApi_py is an ApiWrapper for DenzGraphingApi. this will make life easy and makes using the api a hassle free experience  

Features
-------- 

- makes life easier
- Supports discord embeds for discord bots 

Installation
~~~~~~~~~~~~~ 

Install DenzGraphingApiWrapper by running:  	
``pip install DenzGraphingApiWrapper-py`` 	
or
``pip install git+https://github.com/denzven/DenzGraphingApiWrapper_py.git``

Import it like this: 	``import DenzGraphingApiWrapper_py as GraphingApi`` 

Usage
~~~~~~
Here are some examples on how to use this wrapper
::

    >>> # Shell Example  
    >>> import DenzGraphingApiWrapper_py as GraphingApi  
    >>> formula = 'x**2+y**2-10'  
    >>> GraphingApi.heroku_graph(formula) 	'<https://denz-graphing-api-heroku.herokuapp.com/graph?formula=x%2A%2A2%2By%2A%2A2-10>' 
    >>> GraphingApi.py_anywhere_graph(formula) 	'<http://denzven.pythonanywhere.com/graph?formula=%28x%2A%2A2%2By%2A%2A2-10>'  

you can use this url as a picture in discord and also in embeds  like this 

::  	

import DenzGraphingApiWrapper_py as GraphingApi 	
insert epik code  

Contribute
~~~~~~~~~~ 
- Issue Tracker: <https://github.com/denzven/DenzGraphingApiWrapper_py/issues>
- Source Code: https://github.com/denzven/DenzGraphingApiWrapper_py


- Documentation = https://denzgraphingapiwrapper-py.readthedocs.io/en/latest/

Support
~~~~~~~ 
If you are having issues, please let us know.
Join the Discord Server! https://dsc.gg/chilly_place

License
~~~~~~~~ 
The project is licensed under the MIT license.
