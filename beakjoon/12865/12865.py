n, m = map(int, input().split())
#해당 무게에서 가질 수 있는 최고의 가치를 찾아가는 것
#나중에 아주 효율적인 물건이 대거 등장할 수 있음. 그럼 기존 물건을 빼는 계산을 해야함. -> 복잡함. 
#그럼 에초에 적은 용량으로 관리되는 가방을 하나 만들어두고 있다면? 효율성이 좋은 물건을 넣고 무거워진 가방보다 가치가 높으면 그 무게의 가방을 대체해서 추적하면 됨.

bags = [0]
#bags[i] = i weight에 담을 수 있는 최대 가치

def bag_survival(weight, value):
    if weight > m:
        return 1; #한계 무게가 넘으면 계산 하지 않음. 
    while len(bags) < weight+1:
        bags.append(0)
    bags[weight] = max(bags[weight], value)
    return 0;
    
def add_to_bag(weight, value):
    for i in range(len(bags)-1, 0, -1):
        if bags[i]:
            bag_survival(i+weight, bags[i]+value)
    bag_survival(weight, value) #그 물건 하나만 넣는 경우

for i in range(n):
    w, v = map(int, input().split())
    add_to_bag(w, v)
    #print(i, ": ", w, v, bags)

print(max(bags))