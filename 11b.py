import tools

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def append(self, data):
        new_node = Node(data)
        self.next = new_node
        new_node.prev = self
        return new_node
    
    def insert(self, data):
        # pridat prvok za tento (self)
        new_node = Node(data)
        
        new_node.prev = self
        new_node.next = self.next # moze byt None, ake je to posledny prvok

        if self.next != None: # existuje dalsi prvok
            self.next.prev = new_node
        self.next = new_node
        return new_node

if __name__ == "__main__":
    result = 0
    file_name = '11'
    arr = tools.get_rows_as_ints(file_name)[0]
    
    last_node = None 
    for num in arr:
        if last_node == None:
            last_node = Node(num)
        else:
            last_node = last_node.append(num)
        




    for step in range(75):
        print(step)
        current_node = last_node
        while current_node != None:
            if current_node.data == 0: # Ak je na kameni vyryté číslo 0, nahradí sa kameňom s číslom 1.
                current_node.data = 1
                current_node = current_node.prev
                continue
            
            sNum = str(current_node.data) # Ak má číslo na kameni párny počet cifier, kameň sa rozdelí na dva kamene.
            str_len = len(sNum)
            if str_len % 2 == 0:
                half = str_len // 2
                s1 = sNum[: half]
                s2 = sNum[half:]
                current_node.data = int(s1)
                new_node = current_node.insert(int(s2))
                if new_node.next == None:
                    last_node = new_node
                current_node = current_node.prev
                continue

            current_node.data *= 2024 # Ak sa neuplatní žiadne iné pravidlo, kameň sa nahradí novým kameňom, na ktorom je vyryté číslo získané vynásobením pôvodného čísla číslom 2024
            current_node = current_node.prev
            
    current_node = last_node
    while current_node:
        result += 1
        current_node = current_node.prev
    print(result)
