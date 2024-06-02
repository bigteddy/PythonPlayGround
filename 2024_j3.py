score = []
third_score = 0
third_num = 0

for num in range(int(input())):
    score.append(int(input()))
    
def remove_max(x, score_list):
    new_list = []
    for i in score_list:
        if i != x:
            new_list.append(i)
    return new_list

# score.sort(reverse = True)    
# print(score)

score = remove_max(max(score),score)
# print(score)

score = remove_max(max(score),score)
# print(score)

third_score = max(score)
third_num = score.count(max(score))

print(f"{third_score} {third_num}")        
    