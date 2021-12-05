import gzip
import json
import ast

# with gzip.open("2021-11-25-15.json.gz") as f:
# 	data = f.read()
# 	j = json.loads(data.decode('utf-8'))
# 	print(j[0])



# f = open('2021-11-25-15.json')
# data = json.load(f)
# for i in data:
#     print(i)

# f.close()

tweets = []

for line in open('2021-11-25-15.json', 'r'):
	# print(ast.literal_eval(line))
	# print(json.loads(line))
	if "PullRequestReviewEvent" in line:
		print(line)
	# print(type(line))
	# break
#     tweets.append(json.loads(line))
#     break

# print(tweets)

