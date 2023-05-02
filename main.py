import trees
import pandas as pd

#专家库作用
#1、录入数据
#2、构建推理机 对于录入冲突数据 利用ID3算法进行冲突消解
#3、为模型训练生成更多数据，相比于直接从此推理，卷积训练出的模型泛化能力更好

path = './expert_com.csv'  #通信
# path = './expert_pos.csv' #定位

#添加规则
def add_rule(k,v):
    f = open(path, 'a',encoding='utf-8')
    f.write('\n')
    print(k)
    str = ' '.join(k)
    str += ' '
    str += v
    f.write(str)
    f.close()

if __name__ == '__main__':
    df = pd.read_csv(path)
    col = df.columns.tolist()
    data = df.values.tolist()
    tree = trees.createTree(data, col)
    # print(tree)
    # col = df.columns.tolist()[:-1]
    # input1 = [0, 2, 4, 4, 5]
    # print('level result:', trees.classify(tree, col, input1))

    while True:
        choice = input("请输入选择：'test/add/show/exit'，默认'test' >>> ")
        if choice == 'add':
            k = input('请输入添加的特征组合：').strip().split(' ')
            v = input('请输入添加的结论：')
            add_rule(k,v)

        elif choice == 'show':
            print('可视化结构：',tree)

        elif choice == 'exit':
            exit(0)

        else:
            k = input('请输入测试的特征组合：').strip().split(' ')
            key = []
            for i in k:
                key.append(int(i))
            print('level result:', trees.classify(tree, col, key))



