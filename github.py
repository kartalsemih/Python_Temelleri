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


    def deleteRepository(self,username,repositoryname):
        response=requests.delete(self.api_url+"/repos/"+username+"/"+repositoryname,headers=self.token)
        print("repository silindi")
        return response

        

github=Github()

while True:
    secim = input("1-Find User\n2-Get Repositories\n3-Creat Repository\n4-Exit\n5-Delete Repository\nSeçim: ")

    if secim=="4":
        break
    else:
        if secim=="1":
            username=input("username: ")
            result=github.getUser(username)
            print("*"*20)
            print(f"name: {result['name']} \npublic repos: {result['public_repos']} \nfollower: {result['followers']}\n")
            print("*"*20)
        elif secim=="2":
            username=input("username: ")
            result=github.getRepositories(username)
            print("*"*20)
            for repo in result:
                print(repo["name"])
            print("*"*20)
        elif secim=="3":
            name=input("repository name: ")
            result=github.createRepository(name)
            print("*"*20)
            print(result)
            print("*"*20)
        elif secim == "5":
            username=input("username:")
            repositoryname=input("repository name:")
            result=github.deleteRepository(username,repositoryname)
            print(result)

        else:
            print("yanlis secim")





