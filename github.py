import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token={"Authorization":"Bearer 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",
                    "Accept": "application/vnd.github+json"}

    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

    def createRepository(self,name):
        response=requests.post(self.api_url+"/user/repos?access_token=",headers=self.token,json={
            "id": 1296269,
            "homepage": "https://sadikturan.com",
            "name": name,
            "full_name": "octocat/Hello-World"
        })
        return response.json()

github=Github()

while True:
    secim = input("1-Find User\n2-Get Repositories\n3-Creat Repository\n4-Exit\nSeçim: ")

    if secim=="4":
        break
    else:
        if secim=="1":
            username=input("username: ")
            result=github.getUser(username)
            print(f"name: {result['name']} \npublic repos: {result['public_repos']} \nfollower: {result['followers']}\n")
        elif secim=="2":
            username=input("username: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim=="3":
            name=input("repository name: ")
            result=github.createRepository(name)
            print(result)
        else:
            print("yanlis secim")