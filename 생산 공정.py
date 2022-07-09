import sys

N = int(sys.stdin.readline())

dict = {}
for _ in range(N):
    process = sys.stdin.readline().rstrip()
    
    if process not in dict:
        dict[process] = 1
        
    else:
        dict[process] += 1
    
K = int(sys.stdin.readline())

for _ in range(K):
    result = sys.stdin.readline().rstrip()
    arr = []
    
    for current in sorted(dict.keys()):
        state = True
        
        for j in range(len(result)):
            if current[j] == result[j]:
                continue
            
            else:
                state = False
                break
         
        if state:
            arr.append(current)

    target = ""
    for word in sorted(arr):
        if len(target) < len(word):
            target = word
    
    if target == "":
        print(0)
    
    else:        
        print(target, dict[target])