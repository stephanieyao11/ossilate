import base64
from pprint import pprint
from multiprocessing import Pool
from github3 import login
import csv
import json


account_lis = [('stephanieyao11', 'animals01234!'), ('syao11', 'tibbles11!'), ('syao12', 'Animals012!'), ('syao14', 'Animals0123!'), ('syao16', 'Animals012345!')]
account_lis_ptr = 0

def f(repo_name):
	account = account_lis[account_lis_ptr % 5]
	gh = login(account[0], account[1])
	owner, repo = repo_name.split('/')
	repository = gh.repository(owner = owner, repository = repo)
	release_info_list = []
	release_count = 0
	for release in repository.releases():
		release_info_list.append((release.tag_name, release.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)")))
		release_count += 1

	contributor_list = []
	for contributor in repository.contributors():
		contributor_list.append(str(contributor))


	repo_creation_date = repository.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)")

	dictionary = {}
	dictionary["release_info"] = release_info_list
	dictionary["number_releases"] = release_count
	dictionary["author_name"] = owner
	dictionary["contributors"] = contributor_list
	dictionary["number_open_issues"] = repository.open_issues_count
	dictionary["repo_creation_date"] = repo_creation_date
	json_object = json.dumps(dictionary, indent = 4)
	with open(str(owner), "w") as outfile:
		outfile.write(json_object)


if __name__ == "__main__":
	file = open('100_repos.csv')
	reader = csv.reader(file)
	header = next(reader)
	repo_lis = []
	for row in reader:
		repo_lis.append(row[0])
	file.close()



	# for testing:
	# checking how github3 works with one repository:
	gh = login('syao16', 'Animals012345!')
	owner, repo = repo_lis[0].split('/')
	repository = gh.repository(owner = owner, repository = repo)
	user = gh.user(owner)
	# release_info_list = []
	# release_count = 0
	# for release in repository.releases():
	# 	release_info_list.append((release.tag_name, release.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)")))
	# 	release_count += 1

	# contributor_list = []
	# for contributor in repository.contributors():
	# 	contributor_list.append(str(contributor))


	# repo_creation_date = repository.created_at.strftime("%d-%b-%Y (%H:%M:%S.%f)")

	dictionary = {}
	# dictionary["release_info"] = release_info_list
	# dictionary["number_releases"] = release_count
	# dictionary["author_name"] = owner
	# dictionary["contributors"] = contributor_list
	# dictionary["number_open_issues"] = repository.open_issues_count
	# dictionary["repo_creation_date"] = repo_creation_date
	# json_object = json.dumps(dictionary, indent = 4)
	# with open("sample.json", "w") as outfile:
	# 	outfile.write(json_object)
	# dictionary["stargazers_count"] = repository.stargazers_count
	# dictionary["forks"] = repository.fork_count


	# dictionary["followers"] = user.followers
	# dictionary["email"] = user.email
	# dictionary["organizations_url"] = user.organizations_url
	# dictionary["bio"] = user.bio
	# dictionary["location"] = user.location
	# dictionary["blog"] = user.blog

	

	



	# with Pool(100) as p:
	# 	for i in range(0, 100, 5):
	# 		p.map(f, repo_lis[i : i + 5])
	# 		account_lis_ptr += 1





