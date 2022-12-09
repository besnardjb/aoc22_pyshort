score = lambda i : ord(i) - ord("A") + 27 if ord(i) < ord("a") else ord(i) - ord("a") + 1
d = [ list(x) for x in open("d.dat", "r").read().split("\n") ]
print(sum([ sum({score(aa) for aa in z}) for z in [ set(y[0]).intersection(set(y[1])).intersection(set(y[2])) for y in [ d[x:x+3] for x in range(0,len(d),3)] ]]))
