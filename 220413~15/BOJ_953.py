player_foul=input().split()
player=list(set(player_foul))
foul=[player_foul.count(player[i]) for i in range(len(player))]
player_foul_dic=dict(zip(player,foul))
foul_min=min(foul)
for i,j in player_foul_dic.items():
    if j==foul_min:
        print(i)
print(foul_min)