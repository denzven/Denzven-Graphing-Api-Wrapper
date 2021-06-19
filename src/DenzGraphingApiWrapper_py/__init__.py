import urllib.parse
import aiohttp

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


def async_file_graph_json(formula_input):
    if input_json == None:
        sample_input_json = {
            "file1.png": "x-y",
            "file2.png": "x+y"
        }
        input_json = sample_input_json
    if input_json != None:
        print(input_json)
        pass

    for file in input_json:
        async with aiohttp.ClientSession() as session:
            print(input_json[file])
            formula_output = urllib.parse.quote(input_json[file], safe='')
            url = python_anywhere_BASEURL + f'graph?formula={formula_output}'
            print(url)
            print(formula_output)
            async with session.get(url) as r:
                file_ = open(file, "wb")
                file_.write(await r.read())
                file_.close()
                await ctx.send(file=discord.File(file))

def async_file_graph(formula_input):
        async with aiohttp.ClientSession() as session:
            print(input_json[file])
            formula_output = urllib.parse.quote(formula_input, safe='')
            url = python_anywhere_BASEURL + f'graph?formula={formula_output}'
            print(url)
            print(formula_output)
            async with session.get(url) as r:
                file_ = open(file, "wb")
                file_.write(await r.read())
                file_.close()