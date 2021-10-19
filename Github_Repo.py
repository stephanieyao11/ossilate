import base64
from github import Github
from pprint import pprint
from multiprocessing import Pool

# username = "stephanieyao11"
# g = Github()
# user = g.get_user(username)
# for repo in user.get_repos():
# 	print(repo)
# 	print(repo.url)

def f(repo_name):
	g = Github()
	repo = g.get_repo(repo_name)
	releases = repo.get_releases()
	for release in releases:
		print(release.title)

if __name__ == "__main__":
	# list of 5 trending github repositories
	repo_list = ["apache/apisix", "PanJiaChen/vue-element-admin", "ddosify/ddosify", "ascoders/weekly", "thingsboard/thingsboard"]
	with Pool(5) as p:
		p.map(f, repo_list)







# repo = g.get_repo("apache/apisix")
# releases = repo.get_releases()
# for release in releases:
# 	print(release)
# 	print(release.title)
