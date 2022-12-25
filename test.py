pulls = [[3753139396, 166740188573],
         [724520588560, 766050680304],
         [10457920653, 1051487855],
         [1722571966294, 2846977754550],
         [22496742244741, 4310194783973]]

def test(pulls):
# возможность
    for i in range(1, len(pulls)):
        if pulls[i][0] > pulls[i-1][1]:
            pulls[i][1] = pulls[i][1]*pulls[i-1][1]/pulls[i][0]
            pulls[i][0]=pulls[i-1][1]
# целесообразность
    pulls.reverse()
    for i in range(1, len(pulls)):
        if pulls[i-1][0] < pulls[i][1]:
            pulls[i][0] = pulls[i][0]*pulls[i-1][0]/pulls[i][1]
            pulls[i][1] = pulls[i-1][0]
    pulls.reverse()
# комиссия
    fee = pulls[0][0] * 0.003 * len(pulls)
# прибыль
    profit = pulls[-1][-1] - pulls[0][0] - fee
# результаты
    print(f"Продаем на первом шаге: {pulls[0][0]}\n\
            Покупаем на последнем шаге :{pulls[-1][-1]}\n\
            Прибыль :{profit}\n")
    for pull in pulls:
        print(pull)

test(pulls)


