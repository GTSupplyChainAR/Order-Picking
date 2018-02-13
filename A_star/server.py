from flask import Flask, request
import a_star as pf
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def grid_exec():
	raw_str = request.args['info']
	json_str = json.loads(raw_str)

	r = json_str['rows']
	c = json_str['cols']
	start = json_str['start']
	end = json_str['end']
	walls = json_str['walls']

	a = pf.AStar()
	a.init_grid(r, c, walls, start, end)
	path = a.solve()

	return str(path)

if __name__ == '__main__':
    app.run(debug=True)