from searcherGPU import search_gpu
from searcherRAM import search_ram
from check import check
from mail import mail
import threading
from datetime import datetime


def p(page1):
    s1 = ''
    p1 = []
    with open(page1, 'r') as txt:
        lines = txt.readlines()
        for i in lines:
            p1.append(i)
        if p1:
            s1 = ' '.join(p1)
            print(s1)
        else:
            if 'ram' in page1:
                print('Nothing new on RAM')
            elif 'page' in page1:
                print('Nothing new on GPU')

    # s2 = ''
    # p2 = []
    # with open(page2, 'r') as txt:
    #     lines = txt.readlines()
    #     for i in lines:
    #         p2.append(i)
    #     if p2:
    #         s2 = ' '.join(p2)
    #         print(s2)
    #     else:
    #         if 'ram' in page2:
    #             print('Nothing new on page №2 RAM')
    #         elif 'page' in page2:
    #             print('Nothing new on page №2 GPU')

    return s1

    # p3 = []
    # with open(page3, 'r') as txt:
    #     lines = txt.readlines()
    #     for i in lines:
    #         p3.append(i)
    #     if p3:
    #         mail(', '.join(p3))
    #         print('Something new on page №3')
    #     else:
    #         print('Nothing new on page №3')


def run_5min():
    threading.Timer(60, run_5min).start()

    dt = datetime.now()
    t = dt.strftime("Time: %H:%M")
    print(t)

    act_lst = search_gpu('https://www.kufar.by/l/r~minsk/videokarty?cmp=0&sort=lst.d')
    check('page_1.txt', 'page_1_1.txt', act_lst)
    gpu = p('page_1.txt')

    print('\n')

    act_lst = search_ram('https://www.kufar.by/l/r~minsk/operativnaya-pamyat?cmp=0&sort=lst.d')
    check('ram_1.txt', 'ram_1_1.txt', act_lst)
    ram = p('ram_1.txt')
    print('__________________\n')

    if gpu + ram != '':
        mail(gpu + ram)


run_5min()
