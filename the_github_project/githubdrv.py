from github import Github 


class DataGatherer():

    def __init__(self, username):
        self.username = username
        self.g = Github()
        

    def gather_used_languages_in_repos(self):
        languagesUsed = {}

        for repo in self.g.get_user(self.username).get_repos():
            for key, value in repo.get_languages().items():
                value = languagesUsed.get(key, 0) + value
                languagesUsed.update({key: value})

        return languagesUsed
