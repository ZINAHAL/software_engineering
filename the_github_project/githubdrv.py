from github import Github 


class DataGatherer():

    def __init__(self, username):
        self.username = username
        self.g = Github("***REMOVED***", "***REMOVED***")
        

    def gather_used_languages_in_repos(self):
        languagesUsed = {}

        for repo in self.g.get_user(self.username).get_repos():
            if not repo.fork:
                for key, value in repo.get_languages().items():
                    value = languagesUsed.get(key, 0) + value
                    languagesUsed.update({key: value})

        return languagesUsed
