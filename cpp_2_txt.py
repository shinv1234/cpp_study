import os

def cpp_2_txt():
    directory = input('directory: ')
    os.chdir(directory)
    num = int(input('The number of file is: '))
    lst = list()
    while len(lst) < num:
        file = input('Source code file name is: ')
        lst.append(file)
    txt_name = input('TXT file name is: ')
    with open(txt_name + '.txt', 'w') as w:
        for i in lst:
            with open(i, 'r') as f:
                # f_name = '[' + f.name + ']'
                w.write('[' + f.name + ']\n\n')
                for j in f.readlines():
                    w.write(j)
                w.write('\n\n')
    return None



if __name__ == '__main__':
    cpp_2_txt()