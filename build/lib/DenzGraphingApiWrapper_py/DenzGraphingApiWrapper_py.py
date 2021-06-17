import urllib.parse

python_anywhere_BASEURL = "http://denzven.pythonanywhere.com/"
heroku_BASEURL = "https://denz-graphing-api-heroku.herokuapp.com/"


def py_anywhere_graph(formula_input):
    formula_output = urllib.parse.quote(formula_input, safe='')
    url = python_anywhere_BASEURL + f'graph?formula={formula_output}'
    return url


def heroku_graph(formula_input):
    formula_output = urllib.parse.quote(formula_input, safe='')
    url = heroku_BASEURL + f'graph?formula={formula_output}'
    return url
