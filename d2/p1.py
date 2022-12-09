to_op = {"A" : "A", "B" : "B", "C" : "C", "X" : "A", "Y" : "B", "Z" : "C"}
score = {"A" : 1, "B" : 2 , "C" : 3}
outcome = {"AA": 3, "AB" : 6, "AC" : 0, "BA" : 0, "BB" : 3, "BC" : 6, "CA" : 6, "CB" : 0, "CC" : 3}
print(sum([ outcome[z] + score[z[1]] for z in ["".join([to_op[y] for y in x]) for x in open("dat.dat", "r").read().replace(" ","").split("\n")] ]))
