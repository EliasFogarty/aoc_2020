filename = "day_01_input.txt"
    
with open(filename) as f:
    content = [line.strip() for line in f]

c_len = len(content)

for i in range(0, c_len): 
    content[i] = int(content[i]) 

for a in range(0,c_len):
    #print("A = " , (content[a]))
    for b in range(0,c_len):
        #print("B = " , (content[b]))
        if (content[a]+content[b]) == 2020:
            print ("A = ",(content[a]))
            print ("B = ",(content[b]))
            print ("Product = ",(content[a] * content[b]))