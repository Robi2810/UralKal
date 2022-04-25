from database import db_session
from models import *
import random
areas = [
	Area("Пром площадка 1", "Solikamsk", "Соликамск"),
	Area("Пром площадка 2", "Solikamsk", "Москва"),
	Area("Пром площадка 3", "Solikamsk", "Питер"),
	Area("Пром площадка 4", "Solikamsk", "Город 4")
]

sps = [
	Sp("Структурное подразделение 1"),
	Sp("Структурное подразделение 2"),
	Sp("Структурное подразделение 3"),
	Sp("Структурное подразделение 4"),
	Sp("Структурное подразделение 1"),
	Sp("Структурное подразделение 2"),
	Sp("Структурное подразделение 3"),
	Sp("Структурное подразделение 4"),
	Sp("Структурное подразделение 1"),
	Sp("Структурное подразделение 2"),
	Sp("Структурное подразделение 3"),
	Sp("Структурное подразделение 4"),
]

objects = []
for x in range(46):
	objects.append(SpObject(f"Название объекта {x+1}", random.randint(50,300)))

for obj in objects:
	db_session.add(obj)
	db_session.commit()

for sp in sps:
	for o in objects:
		sp.objects.append(o)
	db_session.add(sp)
	db_session.commit()

i = 0
s = Sp.query.all()
area = areas[0]
for i in range(len(sps)):
	area.sp.append(s[i])
db_session.add(area)
db_session.commit()