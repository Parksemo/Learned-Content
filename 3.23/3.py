class S_list:
    class Node:
        def __init__(self, data=None, link=None):
            self.data = data
            self.link = link
    def __init__(self):
        self.h=None
    def f_add(self,data):
        self.h=self.Node(data,self.h)

    def print_l(self):
        pt=self.h
        while pt.link:
            print(pt.data,"->")
            pt=pt.link
        else:
            print(pt.data)

"""  
a=Node(10)
a.link=Node(20)
a.link.link=Node(30)
pt=a
while pt:
    print(pt.data,end=" ")
    pt=pt.link
"""

s_l=S_list()
s_l.f_add(10)
s_l.f_add(20)
s_l.f_add(30)
s_l.print_l()





