#Data Visualication report #2
#by Ghicheon Lee

import networkx as nx
import matplotlib.pyplot as plt
import math

G = nx.Graph()

#just for debugging
#count=100

with open("facebook_combined.txt") as f:
  for record in f:
    record = record.replace('\n','')
    record = record.replace('\r','').strip()
    record = record.split(' ')

    G.add_edge( int(record[0]) , int(record[1]))

#    count -= 1
#    if count == 0 :
#        break

print(nx.info(G))

plt.figure()
plt.title("facebook network")
plt.axis("off")

d = nx.degree(G)

keys = []
values = []
for (a,b) in d:
        keys.append(a)
        values.append(b)

nx.draw(G,nodelist=keys ,node_size = [math.log(v) for v in values])

plt.show()
