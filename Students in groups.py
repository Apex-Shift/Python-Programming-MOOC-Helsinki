students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

num_grp = (students + group_size - 1)// group_size

print("Number of groups formed:",num_grp)
