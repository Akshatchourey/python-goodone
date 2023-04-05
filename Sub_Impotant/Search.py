from googlesearch import  search

question = "How to become the best programer in 2 Minutes?"

for url in search(question, tld="co.in", num=30, stop=30, pause=2):
    print(url)

a = int(input("enter to exit"))
