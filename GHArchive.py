import gzip
import json

with gzip.open("2021-11-25-15.json.gz") as f:
	data = f.read()
	j = json.loads(data.decode('utf-8'))
	print(type(j))