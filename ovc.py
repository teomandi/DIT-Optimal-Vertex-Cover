import time

edges =[]
ovc = []
t1 = time.time()

# reads a file with the edges ONLY just like the output of the rgg.c 
# program (withou the <nodes | density> line)
f = open("graph.txt", "r")
for line in f:
	linfo = line.split()
	edges.append((int(linfo[0]), int(linfo[1])))

# calculates from the given edges the vertices 
# and the amount of the connections that each one has.
def get_vertices(edges):
	vertices = {}
	for a,b in edges:
		if a not in vertices:
			vertices[a] = 1
		else:
			vertices[a] += 1
		if b not in vertices:
			vertices[b] = 1
		else:
			vertices[b] += 1
	return dict(sorted(vertices.items(), key = lambda kv:(kv[1], kv[0]), reverse = True))

print("Edges:", edges, " ", len(edges))
print("-------")

while (1):
	vs = get_vertices(edges)
	v = list(vs.keys())[0] 
	ovc.append(v)
	for i in range(len(edges)-1, -1, -1):
		if v in edges[i]:
			edges.remove(edges[i])

	if len(edges) == 0:
		break
		
print("OVC list: ", ovc, " length: ", len(ovc))
print("Completed in ", time.time()-t1)