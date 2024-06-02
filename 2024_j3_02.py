score = []
third_score = 0
third_num = 1
i = 1


for num in range(int(input())):
    score.append(int(input()))
    
score.sort(reverse=True) 

# while score[0] == score[1]:
#     score.remove(0)
    
# while score[1] == score[2]:
#     score.remove(1)

# while score[2] == score[3]:
#     score.remove(2)
#     i = i+1
# i = str(i)
# score = str(score)

# print(score[2] + " " + i)

# i = len(score) -1
# a = max(score)
# rank = 1
# count = 1

# while score[i] != a:
#     a = score[i+1]
    
# while rank < 4 :
# for i in range(len(score)):
#     # print(f"{i} {score[i]} {rank} {count}")
#     if score[i] == a:
#         count += 1
#     else:
#         count = 1
#         if score[i] != a:
#             rank += 1
#         if rank >4:
#             break
#         a = score[i]

   
score = [v for v in score if v != max(score)]
score = [v for v in score if v != max(score)]

print(score)
# print(f"{a} {count}")

third_score = max(score)
third_num = score.count(max(score))

print(f"{third_score} {third_num}")  
