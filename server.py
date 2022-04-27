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
	return render_template('sp-page.html', sp_data = data, sector = sector, sp_number = sp_number, base_url = base_url, city = area.city)

@app.route("/sector/<sector>/sp/<sp_number>/object/<obj_number>", methods = ['GET'])
def object(sector, sp_number, obj_number):
	area = models.Area.query.filter_by(id = sector).first()
	if area == None:
		abort(404)
	if int(sp_number)-1 < 0 or int(sp_number)-1 >= len(area.sp):
		abort(404)
	sp_data = area.sp[int(sp_number)-1]
	if int(obj_number)-1 < 0 or int(obj_number)-1 >= len(sp_data.objects):
		abort(404)
	data = sp_data.objects[int(obj_number)-1]
	base_url = area.base_url
	render_name = 'object-page.html'
	if len(data.docs) == 0:
		render_name = 'no-object-page.html'
	return render_template(
			render_name,
			sector = sector,
			sp = sp_number,
			object = data,
			obj_number = obj_number,
			area_name = area.name,
			sp_name = sp_data.name,
			base_url = base_url)

@app.errorhandler(404)
def not_found(e):
	return render_template('error-page.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5678, debug = True)
