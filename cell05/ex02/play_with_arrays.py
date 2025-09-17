ori_lit = [2, 8, 9, 48, 8, 22, -12, 2]
new_lit = [x + 2 for x in ori_lit]
fornew = []
for i in range(len(new_lit)):
    if new_lit[i] > 5:
        new_lit[i] = fornew.append(new_lit[i])
print(ori_lit, "\n", fornew)