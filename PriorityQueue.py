import sys

def leftChild(i):
    return 2 * i + 1


def rightChild(i):
    return 2 * i + 2


def parent(i):
    return ((i - 1) // 2)

class PriorityQueue:
    def __init__(self):
        self.a=[]
        self.size=0


    def up_heap(self, i):
        while i > 0:
            p = parent(i)
            if self.a[p] <= self.a[i]:
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p

    def insert(self, x):
        self.size+=1
        self.a.append(x)
        self.up_heap(len(self.a)-1)

    def down_heap(self,i):
        while i<self.size:
            left=leftChild(i)
            right=rightChild(i)
            # if i is larger than its children
            if right<self.size and left<self.size:

                if self.a[i]>self.a[left] and self.a[i]>self.a[right]:

                    if self.a[left]<self.a[right]:
                        self.a[i],self.a[left]=self.a[left],self.a[i]
                        i=left
                    else:
                        self.a[i], self.a[right] = self.a[right], self.a[i]
                        i=right
                elif  self.a[i]>self.a[left] and self.a[i]<=self.a[right]:
                    self.a[i], self.a[left] = self.a[left], self.a[i]
                    i=left
                elif self.a[i]>self.a[right] and self.a[i]<=self.a[left]:
                    self.a[i], self.a[right] = self.a[right], self.a[i]
                    i=right
                else:
                    # if it is less than it's children
                    break



            elif right>self.size-1 and left<self.size and self.a[left]<self.a[i]:
                self.a[i], self.a[left] = self.a[left], self.a[i]
                i=left
            elif right>self.size-1 and left<self.size and self.a[left]>=self.a[i]:
                break
            elif right>self.size-1 and left>self.size-1:
                break


    def remove_smallest(self):
        head=self.a[0]

        self.a[0]=self.a[self.size-1]
        self.a.pop(self.size-1)
        self.size-=1
        self.down_heap(0)

        return head

    def count(self):
        return self.size

    def __repr__(self):
        s=''
        for i in range(self.size):
            s+=f'=={i}=={self.a[i]}\n'
        return s
def printPair(pair):
    print(pair[1],pair[0])

# input
n=int(input())

pq=PriorityQueue()

for line in sys.stdin:
    line=line.split()
    rating=(float(line[1]),line[0])
    pq.insert(rating)


    if pq.count()==n:

        printPair(pq.remove_smallest())

length=pq.count()
for _ in range(length):
    printPair(pq.remove_smallest())



