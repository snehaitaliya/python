s={34,56,71,12,97,57}

for i in s.copy():
    if i%2==1:
        s.remove(i)
    
print(s)

