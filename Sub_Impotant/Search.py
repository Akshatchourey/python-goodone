from googlesearch import  search

question = "How to become the best programer in 2 Minutes?"

for url in search(question):
    print(url)

a = int(input("enter to exit"))
