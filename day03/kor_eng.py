import re


English = 'She is a vegetarian. '
English +='She does not eat meat.'
English +='She thinks that animals should not be killed. '
English +='It is hard for her to hang out with people. '
English +='Many people like to eat meat. '
English +='She told his parents not to have meat. '
English +='They laughed at her. She realized they couldn\'t give up meat.'

Korean = '그녀는 채식주의자입니다.'
Korean +='그녀는 고기를 먹지 않습니다. '
Korean +='그녀는 동물을 죽이지 말아야한다고 생각합니다. ' 
Korean +='그녀가 사람들과 어울리는 것은 어렵습니다. '
Korean +='많은 사람들이 고기를 좋아합니다. '
Korean +='그녀는 부모에게 고기를 먹지 말라고 말했습니다. '
Korean +='그들은 그녀를 비웃었다.' 
Korean +='그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'

# print(English)
# print(Korean)

English_list = re.split('\.',English)
print(English_list)


Korean_list = re.split('\.',Korean)
print(Korean_list)

total = []
for i in range(len(English_list)):
    total.append([English_list[i],Korean_list[i]])


print(total)
print('----------------------------')

ek = []
for e,k in zip(English.split('.'), Korean.split('.')):
    ek.append([e,k])
print(ek)