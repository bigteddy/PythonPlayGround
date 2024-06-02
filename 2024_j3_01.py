score = []
third_score = 0
third_num = 1
i = 1


for num in range(int(input())):
    score.append(int(input()))
    
# score.append(0)
score.sort(reverse=True) 

# while score[0] == score[1]:
#     score.remove(0)
    
# while score[1] == score[2]:
#     score.remove(1)

# while score[2] == score[3]:
#     score.remove(2)
#     i = i+1
# i = str(i)

a = max(score)

print(score)
print(len(score))

for i in range(len(score)):
    print(i)
    print(score[i])
    if a == score[i]:
        pass
    #     score.remove(score[i])
        
# print(score)
# score = str(score)

# print(score[2] + " " + i)

