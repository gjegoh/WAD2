from glob import glob
lst = glob('Beginner/*.pdf')
beginner = [i.split("\\")[1].split(".")[0] for i in lst]
lst = glob('Intermediate/*.pdf')
intermediate = [i.split("\\")[1].split(".")[0] for i in lst]
lst = glob('Advanced/*.pdf')
advanced = [i.split("\\")[1].split(".")[0] for i in lst]
with open("Resources.html", "r") as f:
    new = f.readlines()
new[len(new)-3] = "<script> let beginner = {}; let intermediate = {}; let advanced = {};</script>\n".format(beginner, intermediate, advanced)
with open("Resources.html", "w") as f2:
    f2.writelines(new)
with open("Resources_light.html", "r") as f3:
    new2 = f3.readlines()
new2[len(new2)-3] = "<script> let beginner = {}; let intermediate = {}; let advanced = {};</script>\n".format(beginner, intermediate, advanced)
with open("Resources_light.html", "w") as f4:
    f4.writelines(new2)
f.closed
f2.closed
f3.closed
f4.closed