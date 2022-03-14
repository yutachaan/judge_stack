from typing import Any, Type

class Node:
    '''線形リスト用ノードクラス'''
    def __init__(self, data: Any = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    '''線形リストクラス'''

    class Empty(Exception):
        pass

    def __init__(self) -> None:
        self.no = 0  #ノードの個数
        self.head = None #先頭ノードを参照するポインタ
        self.current = None #着目ノードを参照するポインタ

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data: Any) -> None:
        '''先頭にノードを挿入'''
        ptr = self.head #挿入前の先頭ノードを参照するポインタ
        self.head = self.current = Node(data, ptr) #先頭ノードと着目ノードを更新
        self.no += 1

    def pop(self) -> Any:
        '''先頭ノードを取り出す'''
        if self.is_empty():
            raise LinkedList.Empty
        self.pop_data = self.current.data #着目ノードのデータをpop_dataに保存
        self.head = self.current = self.head.next #先頭ノードと着目ノードを次のノードに移動
        self.no -= 1
        return self.pop_data
