import requests, json

url = "http://localhost:5000"
r = requests.get(url)
print(r) # esta api no retorna json usando get

dna = '{"dna":["ATGCGA","CCGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}'
print(dna,type(dna))

url = "http://localhost:5000/mutant"
r = requests.post(url,data=dna)
print(r.json())
