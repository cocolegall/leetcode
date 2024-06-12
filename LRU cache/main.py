import time

class Node :
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left : Node | None = None
        self.right : Node | None = None
    
    def __repr__(self) -> str:
        return f"{self.value}"


class LinkedList :
    def __init__(self) -> None:
        self.size : int = 0
        self.head : Node | None = None
        self.tail : Node | None = None

    def remove(self, node : Node) -> None :

        if node.left is None and node.right is None :
            self.head = self.tail = None
        elif node.left is None:
            self.head = node.right
            self.head.left = None
        elif node.right is None :
            self.tail = node.left
            self.tail.right = None
        else :
            node.left.right = node.right
            node.right.left = node.left

        self.size -= 1

    def add(self, node : Node) :
        if self.head is None :
            self.head = self.tail = node
        else :
            node.left = None
            node.right = self.head
            self.head.left = node
            self.head = node

        self.size += 1

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content : dict[int,Node] = {}
        self.queue = LinkedList()

    def get(self, key: int) -> int:
        if self.content.get(key) is not None :
            node = self.content[key]
            self.queue.remove(node)
            self.queue.add(node)

            return node.value
        return -1

    def put(self, key: int, value: int) -> None:

        node = Node(key=key, value=value)


        if self.content.get(key) is not None :
            self.queue.remove(self.content[key])
            self.queue.add(node)
            self.content[key] = node

        else :
            self.content[key] = node
            self.queue.add(node)

        if len(self.content)>self.capacity :
            self.content.pop(self.queue.tail.key)
            self.queue.remove(self.queue.tail)
        
        print(self.content)

start_time = time.time()
lRUCache = LRUCache(10)

func  = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
var = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
for i,f in enumerate(func) :
    print(f"action {f} with input {var[i]}")
    res = getattr(lRUCache,f)(*var[i])
    print(res)
    print("\n")
end_time = time.time()

print(f"execution time : {end_time-start_time}")