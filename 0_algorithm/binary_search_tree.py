# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/binary_search_tree
class Node(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def __repr__(self):
        return str(self.key)

class BinarySearchTree(object):
    def __init__(self,*key):
        self.root=Node(key[0])
        self.__len=1
        self.__count=0
        if len(key)>1:
            for i in range(1,len(key)): self.insert(key[i])

    def search(self,key):
        node=self.__search_with_parent(key)[0]
        if node:
            print("Found!")
            return node
        else:
            print("Not Found!")

    def __search_with_parent(self,key):
        parent=None
        node=self.root
        direction=None # left,right
        while node:
            if node.key>key:
                parent=node
                node=node.left
                direction="left"
            elif node.key<key:
                parent=node
                node=node.right
                direction="right"
            else:
                return node,parent,direction
        return None,None,None

    def insert(self,key):
        self.__len+=1
        node=self.root
        while node:
            parent=node
            if node.key>key:
                flag="left"
                node=node.left
            elif node.key<key:
                flag="right"
                node=node.right
            else:
                print("Data already exists.")
                return
        new=Node(key)
        if flag=="left":
            parent.left=new
        else:
            parent.right=new

    def delete(self,key):
        node,parent,direction=self.__search_with_parent(key)
        if not node: return # なければ何もしない
        elif self.__len==1: raise ValueError("Node0個になるがな")
        self.__len-=1
        # nodeの子がいくつあるかで場合分け
        # nodeの子が0のとき(rootではない):親からその子を消す
        if (not node.left) and (not node.right):
            if direction=="left":
                parent.left=None
            else:
                parent.right=None
                
        # nodeの子が1個のとき:nodeの子を親に接続する
        elif (node.left and (not node.right)) or ((not node.left) and node.right):
            if direction=="left":
                parent.left=node.left if node.left else node.right
            elif direction=="right":
                parent.right=node.left if node.left else node.right
            else:
                self.root=node.left if node.left else node.right

        # nodeの子が2個のとき:
        # node.key未満で最大のnodeを取得し、再帰的にそれを削除(子は高々1つ)
        # 上記nodeを親につけ(後)、そのnodeの子の接続を修正する(先)
        else:
            a=node.left
            while(a.right): a=a.right
            self.delete(a.key)
            a.left,a.right=node.left,node.right
            if direction=="left":
                parent.left=a
            elif direction=="right":
                parent.right=a
            else:
                self.root=a
            
    def traverse(self,node="hoge"): # inorder
        if node=="hoge": node=self.root # これもう少しマシな書き方ありそう
        if node is None: return
        self.traverse(node.left)
        print(node,end=' ')
        self.traverse(node.right)
        self.__count+=1
        if self.__count==self.__len:
            print()
            self.__count=0
