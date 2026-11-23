aa =(25,26,6,9,7,4,58,52)
print ("arrray element",aa)
biggest = aa [0]
smallest = aa[0]
for num in aa:
    if num > biggest:
     biggest = num
    if num < smallest:
        smallest = num
        print(aa)
        print("smallest",smallest)
        print("biggest",biggest)
        
