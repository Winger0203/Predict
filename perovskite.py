import pandas as pd
import numpy as np

element_1 = ['Li', 'Na', 'K', 'Rb', 'Cs']
element_2 = ['Ge', 'Sn', 'Pb', 'Ba', 'Zn', 'Ca', 'Cd', 'Co', 'Cr', 'Cu', 'Fe', 'Mg', 'Mn', 'Ni']
element_3 = ['F', 'Cl', 'Br', 'I']


element = [[], [], [], [], [], [], [], [], []]

for ele1_1 in element_1:

    for ele1_2 in element_1:
        # 判断元素1如果两个重复汇总
        ele1 = ele1_1 + ele1_2
        if ele1_1 == ele1_2:
            ele1 = ele1_1 + '2'
        for ele2 in element_2:

            for ele3_1 in element_3:

                for ele3_2 in element_3:

                    for ele3_3 in element_3:

                        for ele3_4 in element_3:

                            ele3 = ''
                            # 3个重复汇总
                            if ele3_1 == ele3_2 == ele3_3 == ele3_4:
                                ele3 = ele3_1 + '4'
                            elif ele3_1 == ele3_2 == ele3_3:
                                ele3 = ele3_1 + '3' + ele3_4
                            elif ele3_1 == ele3_2 == ele3_4:
                                ele3 = ele3_1 + '3' + ele3_3
                            elif ele3_1 == ele3_3 == ele3_4:
                                ele3 = ele3_1 + '3' + ele3_2
                            elif ele3_2 == ele3_3 == ele3_4:
                                ele3 = ele3_2 + '3' + ele3_1

                            # 两个重复汇总
                            elif ele3_1 == ele3_2:
                                if ele3_3 == ele3_4:
                                    ele3 = ele3_1 + '2' + ele3_3 + '2'
                                else:
                                    ele3 = ele3_1 + '2' + ele3_3 + ele3_4
                            elif ele3_1 == ele3_3:
                                if ele3_2 == ele3_4:
                                    ele3 = ele3_1 + '2' + ele3_2 + '2'
                                else:
                                    ele3 = ele3_1 + '2' + ele3_2 + ele3_4
                            elif ele3_1 == ele3_4:
                                if ele3_2 == ele3_3:
                                    ele3 = ele3_1 + '2' + ele3_2 + '2'
                                else:
                                    ele3 = ele3_1 + '2' + ele3_2 + ele3_3
                            elif ele3_2 == ele3_3:
                                if ele3_1 == ele3_4:
                                    ele3 = ele3_2 + '2' + ele3_1 + '2'
                                else:
                                    ele3 = ele3_2 + '2' + ele3_1 + ele3_4
                            elif ele3_2 == ele3_4:
                                if ele3_1 == ele3_3:
                                    ele3 = ele3_2 + '2' + ele3_1 + '2'
                                else:
                                    ele3 = ele3_2 + '2' + ele3_1 + ele3_3
                            elif ele3_3 == ele3_4:
                                if ele3_1 == ele3_2:
                                    ele3 = ele3_3 + '2' + ele3_1 + '2'
                                else:
                                    ele3 = ele3_3 + '2' + ele3_1 + ele3_2

                                ele = ele1 + ele2 + ele3

                                element[0].append(ele)
                                element[1].append(ele1_1)
                                element[2].append(ele1_2)
                                element[3].append(ele2)
                                element[4].append(ele3)
                                element[5].append(ele3_1)
                                element[6].append(ele3_2)
                                element[7].append(ele3_3)
                                element[8].append(ele3_4)

# print(element)
Name = element[0]
A1 = element[1]
A2 = element[2]
B = element[3]
X1 = element[5]
X2 = element[6]
X3 = element[7]
X4 = element[8]
dict1 = {'Name': Name, 'A1': A1, 'A2': A2, 'B': B, 'X1': X1, 'X2': X2, 'X3': X3, 'X4': X4}
df = pd.DataFrame(dict1)

df.to_csv("perovskite.csv")
