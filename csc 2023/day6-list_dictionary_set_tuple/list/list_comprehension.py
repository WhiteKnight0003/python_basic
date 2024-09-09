listHS = [
    ['lê','chung',9.5],
    ['phan','hải',7.5],
    ['lê','huyền',4.5],
    ['hoàng','an',10],
    ['thành','an',5.0],
    ['trương','vinh',9],
    ['trần','đăng',2]
]

# c1 : bthg
listHSD=[]
for hs in listHS:
    dtb = hs[2]
    if dtb>=5: listHSD.append(hs)

print(listHSD)

# c2 : comprehension
listHSD2 = [hs for hs in listHS if hs[2]>=5]
print(listHSD2)