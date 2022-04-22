from flask import *
import random


app = Flask(__name__)


def fill_data(count):
	data = {}
	for x in range(count):
		data[x+1] = [f'Название объекта {x+1}', random.randint(5,100)]
	return data


def get_sp_json():
	data = {
		'name': 'Соликамск',
		'city': 'Solikamsk/city.png',
		'sp': [
			'Solikamsk/sp-1.png',
			'Solikamsk/sp-2.png',
			'Solikamsk/sp-3.png',
			'Solikamsk/sp-4.png'
		]
	}
	return data

def get_sectors():
	data = []
	data.append(get_sp_json())
	data.append({
		'name': 'Москва',
		'city': 'Solikamsk/city.png',
		'sp': [
			'Solikamsk/city.png',
			'Solikamsk/city.png',
			'Solikamsk/city.png',
			'Solikamsk/city.png'
		]
	})
	return data

@app.route("/", methods = ['GET'])
def main():
	return_block = request.args.get('block')
	return render_template('index.html', sectors = get_sectors(), return_block = return_block, data_cards = ['0']*10)


@app.route("/sector/<sector>/sp/<sp_number>", methods = ['GET'])
def sp(sector, sp_number):
	return render_template('sp-page.html', table_data = fill_data(46), sector = sector, sp_number = sp_number)

@app.route("/sector/<sector>/sp/<sp_number>/object/<obj_number>", methods = ['GET'])
def object(sector, sp_number, obj_number):
	return render_template('object-page.html', sp = sp_number, obj = obj_number)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)