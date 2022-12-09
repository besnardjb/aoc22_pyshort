score = lambda i : ord(i) - ord("A") + 27 if ord(i) < ord("a") else ord(i) - ord("a") + 1
print(sum([sum({ score(s) for s in z}) for z in [ set(y[: len(y)//2]).intersection(set(y[len(y)//2:]))  for y in  [ list(x) for x in open("d.dat", "r").read().split("\n") ] ] ]))

