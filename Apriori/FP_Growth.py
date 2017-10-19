# coding=utf-8

class treeNode:  
    def __init__(self,nameValue,numOccur,parentNode):  
        self.name = nameValue # Name
        self.count = numOccur # Count 
        self.nodeLink = None # Linked to same name's node
        self.parent = parentNode # Parent node  
        self.children = {}   # Child node
    def inc(self,numOccur):  
        self.count += numOccur  
    def disp(self,ind = 1):   # Print out   
        print (' ' * ind,self.name,' ',self.count) 
        for child in self.children.values():  
            child.disp(ind + 1)  


def createTree(dataSet, minSup=1): 
    headerTable = {}
    #遍历数据集两次
    for trans in dataSet:#统计
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    delete = []
    for k in headerTable.keys():  #移除不满足最小支持度的元素项
        if headerTable[k] < minSup: 
            # print(k,headerTable[k])
            delete.append(k)
            # del(headerTable[k])
    for i in delete:
        del(headerTable[i])
    freqItemSet = set(headerTable.keys())
    print ('freqItemSet: ',freqItemSet)
    if len(freqItemSet) == 0: return None, None  #都不满足，则退出
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #修改为下一步准备
    print ('headerTable: ',headerTable)
    retTree = treeNode('Null Set', 1, None) #根节点
    for tranSet, count in dataSet.items():  #第二次遍历
        # print(tranSet,count)
        localD = {}
        for item in tranSet:  #排序
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        print("local",localD.items())
        for v in sorted(localD.items(), key=lambda p: p[1], reverse=True):
            print (v[0])


        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            
            # print(headerTable)
            updateTree(orderedItems, retTree, headerTable, count)#用排序后的频率项进行填充
    return retTree, headerTable 

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#检查第一个元素是否作为子节点存在
        inTree.children[items[0]].inc(count) #更新计数
    else:   #新建一个子节点添加到树中
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#对剩下的元素项迭代调用，每一次奥调用去掉第一个元素
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
        
def updateHeader(nodeToTest, targetNode):   #确保节点链接指向树中该元素项的每一个实例
    while (nodeToTest.nodeLink != None):    #直达链尾
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

def ascendTree(leafNode, prefixPath): #迭代回溯整棵树
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

#遍历链表直到到达结尾，每遇到一个元素项都会调用ascendTree()函数来上溯FP树，ing收集所有遇到的元素项的名称    
def findPrefixPath(basePat, treeNode): 
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink

    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    for v in headerTable.items():
        print (v[0],v[1][0])
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0])]#对头指针表的元素项按照其出现的频率进行排序
    
    print(bigL)
    # for basePat in bigL:  #从头指针的底端开始
    #     newFreqSet = preFix.copy()
    #     newFreqSet.add(basePat)
    #     freqItemList.append(newFreqSet)
    #     condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
    #     myCondTree, myHead = createTree(condPattBases, minSup)
    #     if myHead != None: #递归调用
    #         print ('conditional tree for: ',newFreqSet)
    #         myCondTree.disp(1)      
    #         mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)





if __name__ == "__main__":



    simpDat = loadSimpDat()
    # print(simpDat)

    initSet = createInitSet(simpDat)
    # print("xxx",initSet.items())

    FP_tree , Headertab = createTree(initSet ,3 )
    FP_tree.disp()
    print(Headertab['x'])
    print(findPrefixPath('x',Headertab['r'][1]))
    freqItems = []
    mineTree(FP_tree, Headertab, 3, set([]),freqItems)

