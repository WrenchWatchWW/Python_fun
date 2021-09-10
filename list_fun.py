print('Day 6 of #100Daysofcode')
wrench_list = ["wrench", "Lappland", "Febri","Fubuki","Kirtik"]
#lets add ammar sir too
wrench_list.append("Ammar")
print(wrench_list)
#lets make something new
print(wrench_list[2][0])
print(wrench_list[3][1])
print(wrench_list[0][4])
print(wrench_list[3][4])
#let's find of it's len ?
print("\n") 
print(len(wrench_list)) #well len does not mean index tho
#but what if anyone also wanna join ? suddenly and at 2nd position ?
#well python is awesome 
index = 1
wrench_list.insert(index, "Mystical")
print(wrench_list)
#well we can also add someone without declaring like
wrench_list.insert(4,"R_S")
print(wrench_list)
#let's use all functions at once
print(wrench_list.index("Ammar"))
print(max(wrench_list))
print(min(wrench_list))
print(wrench_list.count("Wrench"))
print(wrench_list.remove("Fubuki"))
print(wrench_list.reverse())
print(wrench_list)
