noghat = input()
list_noghat =noghat.split(" ")
for i in range (len(list_noghat)):
    list_noghat[i] = int(list_noghat[i])
list_noghat.sort()

max_list = max(list_noghat)
min_list = min(list_noghat)
min_list2 = int(min_list)
max_list2 = int(max_list)

print (min_list2)
print (max_list2)
print(max_list2 - min_list2 )