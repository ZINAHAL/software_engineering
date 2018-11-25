from github import Github 


class DataGathererAndVisualiser():

    def __init__(self, username):
        self.username = username
        self.g = Github()
        self.languagesUsed = {}
        

    def gather_used_languages_in_repos(self):
        for repo in self.g.get_user(self.username).get_repos():
            for key, value in repo.get_languages().items():
                value = self.languagesUsed.get(key, 0) + value
                self.languagesUsed.update({key: value})
        
        #print(self.languagesUsed)
    

    def visualise_gathered_data_as_pie(self):
        pass