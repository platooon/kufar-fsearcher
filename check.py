def check(file, file_1, act_lst):

    check_lst = []
    with open(file_1, 'r') as txt:
        lines = txt.readlines()
        for i in lines:
            check_lst.append(i.split(','))

    if check_lst != act_lst:

        with open(file_1, 'w') as txt:
            for k in act_lst:
                txt.write(' '.join(k))

        pre_lst = []
        with open(file, 'r') as txt:
            lines = txt.readlines()
            for i in lines:
                pre_lst.append(i.split(', '))

        for i in act_lst:
            if i not in pre_lst:
                with open(file, 'w') as txt:
                    for k in act_lst:
                        txt.write(' '.join(k))

        if not pre_lst:
            with open(file, 'w') as txt:
                for i in act_lst:
                    if i not in check_lst:
                        txt.write(' '.join(i))

        if act_lst == pre_lst or act_lst == []:
            with open(file, 'w') as txt:
                txt.write('')

    else:
        with open(file, 'w') as txt:
            txt.write('')
