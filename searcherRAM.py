import requests
from bs4 import BeautifulSoup
import re


def search_ram(url):
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
                # lst_cost.pop(i)
                lst_link.pop(i)

    data = {}

    for i in range(0, len(lst_name)):
        data.setdefault(lst_name[i], []).append([d[i], lst_link[i]])

    act_lst = []

    for k, v in data.items():
        # RAM

        # 8gb

        if '8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 70:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 16gb

        if '16' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2x8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2 8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2*8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        # 32gb

        if '32' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 250:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2x16' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 250:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2 16' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '2*16' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 150:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '4x8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 250:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '4 8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 250:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

        if '4*8' in k and 'ddr3' not in k \
                and 'ddr2' not in k \
                and 'so dimm' not in k \
                and 'sodimm' not in k \
                and v[0][0] <= 250:
            act_lst.append([k + ' ' + v[0][1] + ' ' + str(v[0][0]) + ' ' + '\n'])
            act_lst.append([' \n'])

    return act_lst

