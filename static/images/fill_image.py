import os
from sys import argv

soli = [17,35,28,23,5,60,17,23,156,100,129,8,41]
ber = [21,1,22,6,6,109,88,131,18,11,10,7]
perm = [1]
pit = [1]

if __name__ == '__main__':
	source = argv[1]
	with open(source, 'rb') as f:
		data = f.read()
		for x in range(len(soli)):
			fpath = f'Solikamsk/sp-{x+1}/'
			if not os.path.exists(fpath):
				os.makedirs(fpath)
			count = soli[x]
			for i in range(1, count+1):
				with open(f'{fpath}{i}.png', 'wb') as t:
					t.write(data)
			print(f'[ OK ] "{fpath}{i}.png" created!')
		for x in range(len(ber)):
			fpath = f'Berezniki/sp-{x+1}/'
			if not os.path.exists(fpath):
				os.makedirs(fpath)
			count = ber[x]
			for i in range(1, count+1):
				with open(f'{fpath}{i}.png', 'wb') as t:
					t.write(data)
			print(f'[ OK ] "{fpath}{i}.png" created!')
		for x in range(len(perm)):
			fpath = f'Perm/sp-{x+1}/'
			if not os.path.exists(fpath):
				os.makedirs(fpath)
			count = perm[x]
			for i in range(1, count+1):
				with open(f'{fpath}{i}.png', 'wb') as t:
					t.write(data)
			print(f'[ OK ] "{fpath}{i}.png" created!')
		for x in range(len(pit)):
			fpath = f'Piter/sp-{x+1}/'
			if not os.path.exists(fpath):
				os.makedirs(fpath)
			count = pit[x]
			for i in range(1, count+1):
				with open(f'{fpath}{i}.png', 'wb') as t:
					t.write(data)
			print(f'[ OK ] "{fpath}{i}.png" created!')