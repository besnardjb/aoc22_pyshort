print(max([ sum([ int(y) for y in x.split(";") if y != '']) for x in  ";".join(open("d.dat","r") .read().split("\n")).split(";;")]))
