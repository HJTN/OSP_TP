def uni_inter_set(set1, set2):
	union = set1.union(set2)
	inter = set1.intersection(set2)
	print(list(union))
	print(list(inter))

if __name__ == '__main__':
	set1=set(map(int,(input("input the 1st list: ").split())))
	set2=set(map(int,(input("input the 2nd list: ").split())))
	uni_inter_set(set1, set2)
