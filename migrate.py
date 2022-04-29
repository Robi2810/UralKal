from database import db_session
from models import *
import random


documents = [
	Document("EL", "doc3.pdf"),
	Document("HT", "doc4.pdf"),
]

areas = [
	Area("ПП1\nСоликамск", "Solikamsk", "Соликамск"),
	Area("ПП2\nБерезники", "Berezniki", "Березники"),
	Area("ПП3\nПермь", "Perm", "Пермь"),
	Area("ПП4\nСанкт-Петербург", "Piter", "Санкт-Петербург")
]

sps = [
	Sp("ООО «Автотранскалий»"),
	Sp("ООО «Водоканал»"),
	Sp("СМТ БШСУ"),
	Sp("УСД, г.Соликамск"),
	Sp("Строения, арендуемые АО «Новая недвижимость» у ПАО «Уралкалий»"),
	Sp("Административные и социальные ЗиС г.Соликамск (ЦОГР)"),
	Sp("ООО «Уралкалий-Ремонт»"),
	Sp("ЦОГР ПАО «Уралкалий» (Промпорт)"),
	Sp("СКРУ-1"),
	Sp("СКРУ-2"),
	Sp("СКРУ-3"),
	Sp("ООО ВДБ"),
	Sp("ООО «Автотранскалий»"),
	Sp("АО «ВНИИ Галургии»"),
	Sp("СМТ БШСУ"),
	Sp("Строения, арендуемые АО «Новая недвижимость» у ПАО «Уралкалий»"),
	Sp("БКПРУ-1"),
	Sp("БКПРУ-2"),
	Sp("БКПРУ-3"),
	Sp("БКПРУ-4"),
	Sp("ООО «Уралкалий-Ремонт»"),
	Sp("УСД г.Березники"),
	Sp("ООО ВДБ"),
	Sp("Административные и социальные ЗиС г.Березники"),
	Sp("АО «ВНИИ Галургии»"),
	Sp("АО «ББТ»"),
]

sps_objects_count = [17,35,28,23,5,60,17,23,156,100,129,8, 21,1,22,6,6,109,88,131,18,11,10,7,1,1, 1,1]
objects = {}
for x in range(len(sps)):
	objects[sps[x]] = []
for i in range(len(sps)):
	for j in range(sps_objects_count[i]):
		obj = SpObject(f"Название объекта {j+1}", random.randint(50,300))
		if (i == 0 and j == 0):
			for doc in documents:
				obj.docs.append(doc)
		objects[sps[i]].append(obj)
		db_session.add(obj)
		


db_session.commit()
print('[ OK ] Added Objects')

for sp in sps:
	for o in objects[sp]:
		sp.objects.append(o)
	db_session.add(sp)

db_session.commit()
print('[ OK ] Added SPs')



for i in range(0,12):
	areas[0].sp.append(sps[i])
for i in range(12,24):
	areas[1].sp.append(sps[i])
for i in range(24,25):
	areas[2].sp.append(sps[i])
for i in range(25,26):
	areas[3].sp.append(sps[i])

for area in areas:
	db_session.add(area)
db_session.commit()
print('[ OK ] Added Areas')