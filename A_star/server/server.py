from flask import Flask, request
import a_star as pf
import json
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def grid_exec():
    raw_str = request.args['info']
    json_str = json.loads(raw_str)

    r = json_str['rows']
    c = json_str['cols']
    start = tuple(json_str['start'])
    end = tuple(json_str['end'])
    walls = tuple([tuple(x) for x in json_str['walls']])

    a = pf.AStar()
    a.init_grid(r, c, walls, start, end)
    path = a.solve()

    return jsonify(path)

if __name__ == '__main__':
    app.run(debug=True)