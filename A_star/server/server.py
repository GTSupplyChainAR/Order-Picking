from flask import Flask, request
import a_star as pf
import json
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
CORS(app)

def get_shortest(start, ends, walls, r, c):

    min_l = float('+inf')
    for i in ends:
        a = pf.AStar()
        a.init_grid(r, c, walls, start, i)
        path = a.solve()
        if len(path) < min_l:
            min_l = len(path)
            path_ret = path

    return path_ret

@app.route('/', methods=['GET'])
def grid_exec():
    raw_str = request.args['info']
    json_str = json.loads(raw_str)

    r = json_str['rows']
    c = json_str['cols']
    start = tuple(json_str['start'])
    end = json_str['end']
    end = [tuple(x) for x in end]
    walls = tuple([tuple(x) for x in json_str['walls']])

    whl_ctr = len(end)

    paths = []
    ctr = 0
    while ctr < whl_ctr:
        shortest_p = get_shortest(start, end, walls, r, c)
        paths.append(shortest_p)
        start = paths[-1][-1]
        end.remove(start)
        ctr += 1

    return jsonify(paths)

if __name__ == '__main__':
    app.run(debug=True)