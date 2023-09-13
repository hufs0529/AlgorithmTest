n, m = map(int, input().split())
for_member, for_team = {}, {}

for _ in range(n):
    team_name = input()
    members = []
    for _ in range(int(input())):
        member_name = input()
        members.append(member_name)
        for_member[member_name] = team_name
    for_team[team_name] = members

for _ in range(m):
    problem = input()
    tp = int(input())
    if tp == 1:
        print(for_member[problem])
    else:
        memb = for_team[problem]
        print('\n'.join(sorted(memb)))