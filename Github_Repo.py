import base64
from pprint import pprint
from multiprocessing import Pool
from github3 import login
import csv

#old code:

# def f(repo_name):
# 	g = Github()
# 	print(repo_name)
# 	repo = g.get_repo(repo_name)
# 	releases = repo.get_releases()
# 	for release in releases:
# 		print(release.title)

# if __name__ == "__main__":
# 	# list of 5 trending github repositories
# 	repo_list = ["apache/apisix",
# 	 "PanJiaChen/vue-element-admin",
# 	 "ddosify/ddosify",
# 	 "ascoders/weekly",
# 	 "thingsboard/thingsboard"]
# 	 # "qiurunze/miaosha",
# 	 # "electron-userland/electron-builder",
# 	 # "sentsin/layui",
# 	 # "Chakazul/Lenia",
# 	 # "twbs/icons"]
# 	with Pool(5) as p:
# 		p.map(f, repo_list)



account_lis = [('stephanieyao11', 'animals01234!'), ('syao11', 'tibbles11!'), ('syao12', 'Animals012!'), ('syao14', 'Animals0123!'), ('syao16', 'Animals012345!')]
account_lis_ptr = 0

def f(repo_name):
	account = account_lis[account_lis_ptr % 5]
	gh = login(account[0], account[1])
	print(repo_name)
	owner, repo = repo_name.split('/')
	repository = gh.repository(owner = owner, repository = repo)
	for tag in repository.tags():
		print(tag)


if __name__ == "__main__":
	file = open('100_repos.csv')
	reader = csv.reader(file)
	header = next(reader)
	repo_lis = []
	for row in reader:
		repo_lis.append(row[0])
	file.close()

	
	# checking how github3 works:
	gh = login('stephanieyao11', password = 'animals01234')
	owner, repo = repo_lis[0].split('/')
	repository = gh.repository(owner = owner, repository = repo)
	for tag in repository.tags():
		print(tag)

	with Pool(100) as p:
		for i in range(0, 100, 5):
			p.map(f, repo_lis[i : i + 5])
			account_lis_ptr += 1





