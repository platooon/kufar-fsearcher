import requests
from bs4 import BeautifulSoup
import re


def search_gpu(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find_all('h3', class_='styles_title__TUPni')
    cost = soup.find_all('p', class_='styles_price__Bdda5')
    link = soup.find_all('a', class_='styles_wrapper__2ZGa_', href=True)

    lst_name = []
    lst_cost = []
    lst_link = []

    for i in range(40):
        lst_name.append(re.sub('[^a-z0-9 / \.]', '', name[i].text.lower()).strip())

    for i in range(40):
        lst_cost.append(cost[i].text)

    for i in range(40):
        lst_link.append(str(link[i])[47:74])

    s = 'str'
    d = []
    for i in range(len(lst_cost)):
        lst_cost[i] = lst_cost[i][:-3]
        if len(lst_cost[i]) > 3:
            try:
                if type(lst_cost[i]) == type(s):
                    lst_cost[i] = float(lst_cost[i])
                    d.append(lst_cost[i])
            except:
                lst_cost[i] = lst_cost[i][0] + lst_cost[i][2:]
        try:
            if type(lst_cost[i]) == type(s):
                lst_cost[i] = int(lst_cost[i])
                d.append(lst_cost[i])
        except:
            try:
                if type(lst_cost[i]) == type(s):
                    lst_cost[i] = float(lst_cost[i])
                    d.append(lst_cost[i])
            except:
                lst_name.pop(i)
                lst_link.pop(i)

    data = {}

    for i in range(0, len(lst_name)):
        data.setdefault(lst_name[i], []).append([d[i], lst_link[i]])

    act_lst = []

    for k, v in data.items():
        # GPU

        # NVIDIA

        # 1660

        if '1660' in k \
                and 'super' not in k \
                and 'ti' not in k \
                and v[0][0] <= 500:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '1660' in k \
                and 'super' in k \
                and v[0][0] <= 550:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '1660' in k \
                and 'ti' in k \
                and v[0][0] <= 550:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 2060

        if '2060' in k \
                and 'super' not in k \
                and v[0][0] <= 750:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2060' in k \
                and 'super' in k \
                and v[0][0] <= 800:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 2070

        if '2070' in k \
                and 'super' not in k \
                and v[0][0] <= 800:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2070' in k \
                and 'super' in k \
                and v[0][0] <= 850:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 2080

        if '2080' in k \
                and 'super' not in k \
                and 'ti' not in k \
                and v[0][0] <= 1100:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2080' in k \
                and 'super' in k \
                and v[0][0] <= 1200:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2080' in k \
                and 'ti' in k:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 3050

        if '3050' in k \
                and v[0][0] <= 850:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 3060

        if '3060' in k \
                and 'ti' not in k \
                and v[0][0] <= 1350:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '3060' in k \
                and 'ti' in k \
                and v[0][0] <= 1450:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 3070

        if '3070' in k \
                and 'ti' not in k \
                and v[0][0] <= 1600:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '3070' in k \
                and 'ti' in k \
                and v[0][0] <= 1750:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 3080

        if '3080' in k \
                and 'ti' not in k \
                and v[0][0] <= 2000:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '3080' in k \
                and 'ti' in k \
                and v[0][0] <= 2300:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 3090

        if '3090' in k \
                and 'ti' not in k \
                and v[0][0] <= 3000:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '3090' in k \
                and 'ti' in k \
                and v[0][0] <= 3500:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # AMD

        # 6600

        if '6600' in k \
                and 'xt' not in k \
                and v[0][0] <= 700:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6600' in k \
                and 'xt' in k \
                and v[0][0] <= 800:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6650' in k \
                and 'xt' not in k \
                and v[0][0] <= 900:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6650' in k \
                and 'xt' in k \
                and v[0][0] <= 1000:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 6700

        if '6700' in k \
                and 'xt' not in k \
                and v[0][0] <= 1300:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6700' in k \
                and 'xt' in k \
                and v[0][0] <= 1450:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6750' in k \
                and 'xt' not in k \
                and v[0][0] <= 1500:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6750' in k \
                and 'xt' in k \
                and v[0][0] <= 1600:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 6800

        if '6800' in k \
                and 'xt' not in k \
                and v[0][0] <= 1900:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6800' in k \
                and 'xt' in k \
                and v[0][0] <= 2100:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6850' in k \
                and 'xt' not in k \
                and v[0][0] <= 2300:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6850' in k \
                and 'xt' in k \
                and v[0][0] <= 2500:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 6900

        if '6900' in k \
                and 'xt' not in k \
                and v[0][0] <= 2900:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6900' in k \
                and 'xt' in k \
                and v[0][0] <= 3200:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6950' in k \
                and 'xt' not in k \
                and v[0][0] <= 3300:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '6950' in k \
                and 'xt' in k \
                and v[0][0] <= 3600:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

    return act_lst
