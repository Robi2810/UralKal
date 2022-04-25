from database import db_session
import models
from flask import *
import jinja2.ext
import random


app = Flask(__name__)

@app.route("/", methods = ['GET'])
def main():
	return_block = request.args.get('block')
	data = models.Area.query.all()
	return render_template('index.html', areas = data, return_block = return_block)


@app.route("/sector/<sector>/sp/<sp_number>", methods = ['GET'])
def sp(sector, sp_number):
	area = models.Area.query.filter_by(id = sector).first()
	if area == None:
		abort(404)
	if int(sp_number)-1 < 0 or int(sp_number)-1 >= len(area.sp):
		abort(404)
	data = area.sp[int(sp_number)-1]
	base_url = area.base_url
	return render_template('sp-page.html', sp_data = data, sector = sector, sp_number = sp_number, base_url = base_url)

@app.route("/sector/<sector>/sp/<sp_number>/object/<obj_number>", methods = ['GET'])
def object(sector, sp_number, obj_number):
	area = models.Area.query.filter_by(id = sector).first()
	if area == None:
		abort(404)
	if int(sp_number)-1 < 0 or int(sp_number)-1 >= len(area.sp):
		abort(404)
	sp_data = area.sp[int(sp_number)-1]
	data = sp_data.objects[int(obj_number)-1]
	return render_template('object-page.html', sector = sector, sp = sp_number, object = data)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5678, debug = True)
