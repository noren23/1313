import time
import requests
import json
import jsonpath
import http.client


class Card:
    def __init__(self, f, n):
        self.flower = f
        self.num = n


global poker_1
global poker_2
global poker_3
global ans_1
global ans_2
global ans_3
global temp_1
global temp_2
global temp_3
global end_1
global end_2
global end_3
global s1
global s2
global s3
global r1
global r2
global r3
global end_ans
global hua
global number
global score
global cnt


def init_var():
    global poker_1
    global poker_2
    global poker_3
    global ans_1
    global ans_2
    global ans_3
    global temp_1
    global temp_2
    global temp_3
    global end_1
    global end_2
    global end_3
    global s1
    global s2
    global s3
    global r1
    global r2
    global r3
    global end_ans
    global hua
    global number
    global score
    global cnt
    poker_1 = [Card(0, 0) for i in range(14)]
    poker_2 = [Card(0, 0) for j in range(14)]
    poker_3 = [Card(0, 0) for k in range(14)]
    ans_1 = [Card(0, 0) for l in range(20)]
    ans_2 = [Card(0, 0) for m in range(20)]
    ans_3 = [Card(0, 0) for n in range(20)]
    temp_1 = [Card(0, 0) for o in range(20)]
    temp_2 = [Card(0, 0) for p in range(20)]
    temp_3 = [Card(0, 0) for q in range(20)]
    end_1 = [Card(0, 0) for r in range(20)]
    end_2 = [Card(0, 0) for s in range(20)]
    end_3 = [Card(0, 0) for t in range(20)]
    s1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    r1 = 5
    r2 = 5
    r3 = 3
    end_ans = 0
    hua = [0, 0, 0, 0, 0, 0]
    number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    score = 0.0
    cnt = 0


global e1, e2, e3
global a1, a2, a3


def init_cnt():
    for i in range(0, 6):
        hua[i] = 0
    for i in range(0, 20):
        number[i] = 0


def bubble_sort(nums, a, b):
    for i in range(b - a):
        for j in range(b - a - 1):
            if nums[a + j].num > nums[a + j + 1].num:
                nums[a + j], nums[a + j + 1] = nums[a + j + 1], nums[a + j]
    return nums


def ShunZi3(start):
    for i in range(start, start + 3):
        if number[i] < 1:
            return 0
    else:
        return 1


def ShunZi5(start):
    for i in range(start, start + 5):
        if number[i] < 1:
            return 0
    else:
        return 1


def first():
    global score
    init_cnt()
    bubble_sort(ans_3, 1, 3)
    for i in range(1, 4):
        hua[ans_3[i].flower] = hua[ans_3[i].flower] + 1
        number[ans_3[i].num] = number[ans_3[i].num] + 1
    x = 1
    for i in range(1, 5):
        if hua[i] == 3:
            if ShunZi3(ans_3[1].num) == 1:
                k = (9.0 + 0.9 / 11.0 * (ans_3[1].num - 1))
                score += k
                return k  # 3张同花顺
    x = 1
    for i in range(1, 5):
        if hua[i] == 3:
            k = (6.0 + 0.9 / (1300 + 130 + 13)
                 * ((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1)) * 1.0)
            score += k
            return k  # 3张同花
    x = 1
    if ShunZi3(ans_3[1].num) == 1:
        k = (5.0 + 0.9 / 11.0 * (ans_3[1].num - 1) * 1.0)
        score += k
        return k  # 3张顺子
    x = 1
    for i in range(3, 0, -1):
        if number[ans_3[i].num] == 3:
            k = (4.0 + 0.9 / 13.0 * (ans_3[1].num - 1) * 1.0)
            score += k
            return k  # 三条
    x = 1
    for i in range(3, 0, -1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_3[i].num - 1) * 10 + x - 1) * 1.0)
            score += k
            return k  # 单对
    x = 1
    k = 0.9 / (1300.0 + 130.0 + 13.0) * (
                (ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    score += k
    return k  # 散牌


def second():
    global score
    init_cnt()
    bubble_sort(ans_2, 1, 5)
    x = 1
    for i in range(1, 6):
        hua[ans_2[i].flower] = hua[ans_2[i].flower] + 1
        number[ans_2[i].num] = number[ans_2[i].num] + 1
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            if ShunZi5(ans_2[1].num) == 1:
                k = (9.0 + 0.9 / 9 * (ans_2[1].num - 1)) * 1.0
                score += k  # 14 13 12 11 10
                return k  # 同花顺
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            k = (8.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10)) * 1.0
            score += k
            return k  # 炸弹
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5, 0, -1):
                if number[ans_2[j].num] == 2:
                    k = (7.0 + 0.9 / (130 + 13) * ((x - 1) * 10 + ans_2[j].num - 1)) * 1.0
                    score += k
                    return k  # 葫芦
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            k = (6.0 + 0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                        (ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (
                            ans_2[2].num - 1) * 10 + (ans_2[1].num - 1))) * 1.0
            score += k
            return k  # 同花
    x = 1
    if ShunZi5(ans_2[1].num) == 1:
        k = (5.0 + 0.9 / 9 * (ans_2[1].num - 1) * 1.0)
        score += k
        return k  # 5张顺子
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5, 0, -1):
                if number[ans_2[j].num] == 1:
                    k = (4.0 + 0.9 / (1300 + 130 + 13) * ((x - 1) * 100))
                    score += k
                    return k  # 三条
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(
                        ans_2[i].num - ans_2[j].num) == 1:
                    k = (3.0 + 0.9 / 10 * (ans_2[j].num - 1 - 1)) * 1.0
                    score += k
                    return k  # 连对2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2:
                    k = (2.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10 + ans_2[j].num - 1)) * 1.0
                    score += k
                    return k  # 普通2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10 + x - 1)) * 1.0
            score += k
            return k  # 单对+3张散

    k = (0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                (ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (
                    ans_2[2].num - 1) * 10 + ans_2[1].num - 1)) * 1.0
    score += k
    return k


def third():
    global score
    init_cnt()
    bubble_sort(ans_1, 1, 5)
    x = 1
    for i in range(1, 6):
        hua[ans_1[i].flower] = hua[ans_1[i].flower] + 1
        number[ans_1[i].num] = number[ans_1[i].num] + 1
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            if ShunZi5(ans_1[1].num) == 1:
                k = (9.0 + 0.9 / 9 * (ans_1[1].num - 1)) * 1.0  # 14 13 12 11 10
                score += k
                return k  # 同花顺
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 4:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            k = (8.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10)) * 1.0
            score += k
            return k  # 炸弹
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5, 0, -1):
                if number[ans_1[j].num] == 2:
                    k = (7.0 + 0.9 / (130 + 13) * ((x - 1) * 10 + ans_1[j].num - 1)) * 1.0
                    score += k
                    return k  # 葫芦
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            k = (6.0 + 0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                        (ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (
                            ans_1[2].num - 1) * 10 + (ans_1[1].num - 1))) * 1.0
            score += k
            return k  # 同花
    x = 1
    if ShunZi5(ans_1[1].num) == 1:
        k = (5.0 + 0.9 / 9 * (ans_1[1].num - 1) * 1.0)
        score += k
        return k  # 5张顺子
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5, 0, -1):
                if number[ans_1[j].num] == 1:
                    k = (4.0 + 0.9 / (1300 + 130 + 13) * ((x - 1) * 100))
                    score += k
                    return k  # 三条
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_1[i].num != ans_1[j].num) and \
                        number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1:
                    k = (3.0 + 0.9 / 10 * (ans_1[j].num - 1 - 1)) * 1.0
                    score += k
                    return k  # 连对2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2:
                    k = (2.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10 + ans_1[j].num - 1)) * 1.0
                    score += k
                    return k  # 普通2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10 + x - 1)) * 1.0
            score += k
            return k  # 单对+3张散

    k = (0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                (ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (
                    ans_1[2].num - 1) * 10 + ans_1[1].num - 1)) * 1.0
    score += k
    return k


def StandOf():
    for i in range(1, 4):
        end_3[i] = ans_3[i]
    for i in range(1, 6):
        end_2[i] = ans_2[i]
    for i in range(1, 6):
        end_1[i] = ans_1[i]


def TempoF():
    for i in range(1, 4):
        ans_3[i] = temp_3[i]
    for i in range(1, 6):
        ans_2[i] = temp_2[i]
    for i in range(1, 6):
        ans_1[i] = temp_1[i]


def Print():
    for i in range(1, 4):
        if i == 3:
            print(ans_3[i].num)
        else:
            print(ans_3[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_2[i].num)
        else:
            print(ans_2[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_1[i].num)
        else:
            print(ans_1[i].num, end=" ")


def contrast_ans():
    global score, end_ans, cnt
    global e1, e2, e3
    global a1, a2, a3
    TempoF()
    k1 = first()
    e1 = score
    k2 = second()
    e2 = score - e1
    k3 = third()
    e3 = score - (e1+e2)
    score = k1 + k2 + k3
    if k1 > k2 or k2 > k3 or k1 > k3:
        score = 0
    if score > end_ans:
        end_ans = score
        a1 = e1
        a2 = e2
        a3 = e3
        StandOf()
    cnt += 1


def init_2():
    index = 0
    for i in range(1, 9):
        if s2[i] == 0:
            index = index + 1
            temp_3[index] = poker_2[i]


def dfs_2(d, index_2):
    for i in range(d, 9):
        temp_2[index_2] = poker_2[i]
        s2[i] = 1
        if index_2 == r2:
            init_2()
            contrast_ans()
        else:
            dfs_2(i + 1, index_2 + 1)
        s2[i] = 0


def init_1():
    index = 0
    for i in range(1, 14):
        if s1[i] == 0:
            index = index+1
            poker_2[index] = poker_1[i]


def dfs_1(d, index_1):
    for i in range(d, 14):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == r1:
            init_1()
            dfs_2(1, 1)
        else:
            dfs_1(i + 1, index_1 + 1)
        s1[i] = 0


def number_to_hua(x):
    if x == 1:
        return '&'
    if x == 2:
        return '$'
    if x == 3:
        return '#'
    if x == 4:
        return '*'


def hua_to_number(x):
    if x == '&':
        return 1
    if x == '$':
        return 2
    if x == '#':
        return 3
    if x == '*':
        return 4


def main():
    tic = time.time()
    init_var()
    url = "https://api.shisanshui.rtxux.xyz/auth/register"

    payload = "{\"username\":\"un\",\"password\":\"pw\"}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    url = "https://api.shisanshui.rtxux.xyz/auth/login"
    # payload = "{\"username\":\"\",\"password\":\"\"}"
    payload = "{\"username\":\"un\",\"password\":\"pw\"}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    # 解码
    response.encoding = 'utf8'
    # 读取reponse
    html = response.text
    # print(html)
    # 把json格式字符串转换成python对象
    html = json.loads(html)
    # print(html)
    # 获取score节点下的数据
    qq = jsonpath.jsonpath(html, '$..data.token')
    print(qq)
    tkk = qq[0]
    qq = jsonpath.jsonpath(html, '$..data.user_id')
    pl_id = qq[0]

    url = "https://api.shisanshui.rtxux.xyz/game/open"
    headers = {'x-auth-token': tkk}
    response = requests.request("POST", url, headers=headers)
    # print(response.text)
    # 解码
    response.encoding = 'utf8'
    # 读取reponse
    html = response.text
    # print(html)
    # 把json格式字符串转换成python对象
    html = json.loads(html)
    # print(html)
    # 获取score节点下的数据
    qq = jsonpath.jsonpath(html, '$..data.card')
    tk = qq[0]
    print(tk)
    tk = list(tk)
    # print(tk)
    qq = jsonpath.jsonpath(html, '$..data.id')
    idd = qq[0]
    # print(idd)
    idd = str(idd)
    # print(idd)
    # print(len(tk))
    i=1
    for eachline in range(len(tk)):
        if i == 13 and (tk[eachline] == '&' or tk[eachline] == '$' or tk[eachline] == '#' or tk[eachline] == '*'):
            if tk[eachline + 1] == '2':
                px = 2
            elif tk[eachline + 1] == '3':
                px = 3
            elif tk[eachline + 1] == '4':
                px = 4
            elif tk[eachline + 1] == '5':
                px = 5
            elif tk[eachline + 1] == '6':
                px = 6
            elif tk[eachline + 1] == '7':
                px = 7
            elif tk[eachline + 1] == '8':
                px = 8
            elif tk[eachline + 1] == '9':
                px = 9
            elif tk[eachline + 1] == '1':
                px = 10
            elif tk[eachline + 1] == 'J':
                px = 11
            elif tk[eachline + 1] == 'Q':
                px = 12
            elif tk[eachline + 1] == 'K':
                px = 13
            elif tk[eachline + 1] == 'A':
                px = 14
            if tk[eachline] == '&':
                poker_1[i] = Card(1, px)
            elif tk[eachline] == '$':
                poker_1[i] = Card(2, px)
            elif tk[eachline] == '#':
                poker_1[i] = Card(3, px)
            elif tk[eachline] == '*':
                poker_1[i] = Card(4, px)
            break
        if tk[eachline+1] == '2':
            px = 2
        elif tk[eachline+1] == '3':
            px = 3
        elif tk[eachline+1] == '4':
            px = 4
        elif tk[eachline+1] == '5':
            px = 5
        elif tk[eachline+1] == '6':
            px = 6
        elif tk[eachline+1] == '7':
            px = 7
        elif tk[eachline+1] == '8':
            px = 8
        elif tk[eachline+1] == '9':
            px = 9
        elif tk[eachline+1] == '1':
            px = 10
        elif tk[eachline+1] == 'J':
            px = 11
        elif tk[eachline+1] == 'Q':
            px = 12
        elif tk[eachline+1] == 'K':
            px = 13
        elif tk[eachline+1] == 'A':
            px = 14

        if tk[eachline] == '&':
            poker_1[i] = Card(1, px)
            i = i + 1
        elif tk[eachline] == '$':
            poker_1[i] = Card(2, px)
            i = i + 1
        elif tk[eachline] == '#':
            poker_1[i] = Card(3, px)
            i = i + 1
        elif tk[eachline] == '*':
            poker_1[i] = Card(4, px)
            i = i + 1
        else:
            continue

    # poker_1[1] = Card(2, 2)
    # poker_1[2] = Card(3, 2)
    # poker_1[3] = Card(4, 2)
    # poker_1[4] = Card(1, 3)
    # poker_1[5] = Card(1, 4)
    # poker_1[6] = Card(4, 5)
    # poker_1[7] = Card(1, 6)
    # poker_1[8] = Card(1, 7)
    # poker_1[9] = Card(2, 9)
    # poker_1[10] = Card(3, 8)
    # poker_1[11] = Card(4, 4)
    # poker_1[12] = Card(4, 8)
    # poker_1[13] = Card(3, 5)
    dfs_1(1, 1)
    qian = ""
    zhong = ""
    hou = ""
    for i in range(1, 4):
        anss = number_to_hua(end_3[i].flower)
        ans = end_3[i].num
        if(ans == 14):
            ans = 'A'
        elif (ans == 13):
            ans = 'K'
        elif (ans == 12):
            ans = 'Q'
        elif (ans == 11):
            ans = 'J'
        elif (ans == 10):
            ans = '10'
        elif (ans == 9):
            ans = '9'
        elif (ans == 8):
            ans = '8'
        elif (ans == 7):
            ans = '7'
        elif (ans == 6):
            ans = '6'
        elif (ans == 5):
            ans = '5'
        elif (ans == 4):
            ans = '4'
        elif (ans == 3):
            ans = '3'
        elif (ans == 2):
            ans = '2'
        qian += anss
        qian += ans
        if i != 3:
            qian += ' '
    for i in range(1, 6):
        anss = number_to_hua(end_2[i].flower)
        ans = end_2[i].num
        if (ans == 14):
            ans = 'A'
        elif (ans == 13):
            ans = 'K'
        elif (ans == 12):
            ans = 'Q'
        elif (ans == 11):
            ans = 'J'
        elif (ans == 10):
            ans = '10'
        elif (ans == 9):
            ans = '9'
        elif (ans == 8):
            ans = '8'
        elif (ans == 7):
            ans = '7'
        elif (ans == 6):
            ans = '6'
        elif (ans == 5):
            ans = '5'
        elif (ans == 4):
            ans = '4'
        elif (ans == 3):
            ans = '3'
        elif (ans == 2):
            ans = '2'
        zhong += anss
        zhong += ans
        if i != 5:
            zhong += ' '
    for i in range(1, 6):
        anss = number_to_hua(end_1[i].flower)
        ans = end_1[i].num
        if (ans == 14):
            ans = 'A'
        elif (ans == 13):
            ans = 'K'
        elif (ans == 12):
            ans = 'Q'
        elif (ans == 11):
            ans = 'J'
        elif (ans == 10):
            ans = '10'
        elif (ans == 9):
            ans = '9'
        elif (ans == 8):
            ans = '8'
        elif (ans == 7):
            ans = '7'
        elif (ans == 6):
            ans = '6'
        elif (ans == 5):
            ans = '5'
        elif (ans == 4):
            ans = '4'
        elif (ans == 3):
            ans = '3'
        elif (ans == 2):
            ans = '2'
        hou += anss
        hou += ans
        if i != 5:
            hou += ' '
    # print(qian)
    # print(zhong)
    # print(hou)

    url = "https://api.shisanshui.rtxux.xyz/game/submit"
    payload = "{\"id\":" + idd + ",\"card\":[\"" + qian + "\",\"" + zhong + "\",\"" + hou + "\"]}"
    print(payload)
    headers = {
        'content-type': "application/json",
        'x-auth-token': tkk
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    toc = time.time()
    print(toc-tic)

    # url = "https://api.shisanshui.rtxux.xyz/history"
    # querystring = {"page": "9", "limit": "6", "player_id":"207"}
    # headers = {'x-auth-token': tkk}
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)

    # url = "https://api.shisanshui.rtxux.xyz/history/4826"
    # headers = {'x-auth-token': tkk}
    # response = requests.request("GET", url, headers=headers)
    # print(response.text)

    # url = "https://api.shisanshui.rtxux.xyz/rank"
    # response = requests.request("GET", url)
    # print(response.text)


if __name__ == '__main__':
    main()
