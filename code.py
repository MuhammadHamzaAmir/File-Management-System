'''It is the updated code of lab 6 in which there was a bug and now that is solved'''

import os
import sys

sys.setrecursionlimit(2000)

#Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.index = None
        self.total_size = 100
        self.id = None
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.l_size = 10000
        self.head = None
        self.t_nodes = 100
        self.nodes = 0

    def printList(self):
        temp = self.head
        text=""
        while (temp):
            text=text+temp.data+"#"+temp.id+"\n"
            temp = temp.next
        return text

    def compute_size(self):
        size_val = 1
        temp = self.head
        while (temp):
            size_val = size_val+1
            temp = temp.next
        return (size_val * 100)

    def insert_node(self, new_data, n_id):

        new_node = Node(new_data)
        new_node.id = n_id
        i = 0
        
        if (self.nodes <= self.t_nodes):
            if (len(new_data) <= new_node.total_size):
                
                if self.head is None:
                    new_node.index = i
                    #new_node.size = len(new_data)
                    self.nodes = self.nodes + 1
                    i = i+1
                    self.head = new_node
                    return
                
                
                last = self.head
                
                while (last.next):
                    last = last.next
                    i = i+1
                    
                last.next = new_node
                new_node.index = i+1
                self.nodes = self.nodes + 1
                #new_node.size = len(new_data)
            else:
                self.data_management(new_node, new_data, n_id)
        else:
            print("There no more new sectors available")

    def data_management(self, node, new_data, n_id):
        total_nodes = (len(new_data) // node.total_size) + 1

        for i in range((total_nodes)):
            data_to_add = new_data[i*100:(i+1)*100]
            self.insert_node(data_to_add, n_id)
    #append func

    def add_data(self, new_data, n_id):
        temp = self.head
        while (temp):
            if (temp.id == n_id):
                temp_size = temp.total_size - len(temp.data)
                if ((temp_size > 0)):
                    temp.data = temp.data + new_data[:temp_size]

            temp = temp.next
        if (temp_size < len(new_data)):
            self.data_management(self.head, new_data[temp_size:], n_id)

    def write_to_file_insert_node(self,new_data,n_id):
        temp = self.head
        j=0
        while (temp):
            if (temp.id == n_id):
                j=j+1
            temp=temp.next
        if (j>0):    
            #print("\ninside j")
            self.turncate(len(new_data),n_id)
            self.write_at_data_OVERWRITE(0,new_data,n_id)
        else:
            #print("\nelse why")
            self.insert_node(new_data,n_id)

    def delete_one_node(self,key):
        # Store head node  
        temp = self.head  
  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                self.nodes=self.nodes-1
                return
   
        while(temp is not None):  
            if temp.data == key:  
                self.nodes=self.nodes-1
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
  
        temp = None

    def deleteNode(self, n_id):

        temp = self.head
        prev = None

        while (temp != None and temp.id == n_id):
            self.head = temp.next
            temp = self.head
            self.nodes=self.nodes-1
        while (temp != None):

            while (temp != None and temp.id != n_id):
                prev = temp
                temp = temp.next
                self.nodes=self.nodes-1

            if (temp == None):
                return self.head

            prev.next = temp.next

            temp = prev.next
        self.indices_order()

    def indices_order(self):
        temp = self.head
        i = 0
        while (temp):
            temp.index = i
            i = i+1
            temp = temp.next

    def move_data_ll(self, start, to, size, n_id):
        temp = self.head
        text = ""
        while (temp):
            if (temp.id == n_id):
                text = text + temp.data
            temp = temp.next

        #getting the specific substring from the string
        part_text = text[start:start+size]
        #removing the specific substring from the string
        text = text[0:start:] + text[start+size::]
        #moving the specific substring to particular point in the string
        text = text[0:to] + part_text + text[to:]
        r_text = text
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    def write_at_data_noOVERWRITE(self, write_at, text, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        self.add_data(text, n_id)
        r_text = self.move_data_ll(len(o_text), write_at, len(text), n_id)
        return r_text

    def write_at_data_OVERWRITE(self, write_at, text, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        #part_text = o_text[write_at:write_at+len(text)]
        o_text = o_text[0:write_at:] + o_text[write_at+len(text)::]
        o_text = o_text[0:write_at] + text + o_text[write_at+len(text):]
        r_text = o_text
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = o_text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    #read data from start

    def read_file(self, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        return o_text

    #read data at a particular point
    def read_file_atpoint(self, n_id, start, size):
        text = self.read_file(n_id)
        part_text = text[start:start+size]
        return part_text

    def turncate(self, maxSize, n_id):
        temp = self.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        part_text = o_text[0:maxSize]
        temp = self.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = part_text[i*100:(i+1)*100]
                i = i+1
                temp.data = data_to_add
            temp = temp.next

        temp = self.head
        del_text = "HASTA_LA_VISTA_BABY"
        while (temp):
            if (temp.id == n_id):
                if (len(temp.data)<1):
                    temp.data = del_text
                    self.delete_one_node(del_text)
            temp = temp.next

        temp = self.head
        while (temp):
            if (temp.id == n_id):
                self.delete_one_node(del_text)
            temp = temp.next
        return part_text
        

    def memory_map(self):
        temp = self.head
        total_size = 0
        exlist = []
        while (temp):
            total_size = total_size+len(temp.data)
            print("File Name:", temp.id,
                  " Size of node occupying:", len(temp.data))
            exlist.append(temp.id)
            temp = temp.next
        exlist = list(set(exlist))
        print("Total Size occuppied: ", total_size)
        print("Total Size alloted: ", self.compute_size()-100)
        print("Total Size: ", self.l_size)
        print("Total Sectors: ",self.t_nodes)
        print("Available Sectors: ", self.t_nodes-self.nodes)
        print("Available sector size on disk: ", (100+self.l_size-self.compute_size()))
        print("Available size orignally: ",
              (self.l_size-(total_size)))

    def get_data(self,text):
        for line in text.splitlines():
            a_l = line.split("#")
            self.insert_node(a_l[0],a_l[1])
        self.indices_order()
        


class fileHandling:

    def __init__(self):
        p=""
        try:
            self.file = open("sample.dat", "r+")
            p = self.file.read()
            self.file.close()
        except:
            pass
        self.file = open("sample.dat","a+")
        self.file_name = ""
        self.llist = LinkedList()
        self.llist.get_data(p)


    def Create(self, fname):
        self.file_name = fname+".txt"
        try:
            self.file.close()
            self.file = open("sample.dat","a+")
            self.file.write("#"+fname)
            self.file.close()
            self.file = open("sample.dat", "w+")
        except:
            pass
        print("File is Created\n")

    def Delete(self, fname):
        self.file_name = ""
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            
            
            self.llist.deleteNode(fname+".txt")
            text=self.llist.printList()
            self.file.write(text)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("File is Deleted\n")
        except:
            pass

    def Open(self, fname, mode):
        self.file_name = fname+".txt"
        print("File is Opened\n")
        #return f

    def Close(self, fname):
        self.file_name = fname+".txt"
        print("File is Closed\n")

    #write_at_first_time
    def write_to_file(self, text):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file
            self.llist.write_to_file_insert_node(text, self.file_name)
            text=self.llist.printList()
            v.write(text)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("Text has been written\n")
        except:
            pass

    def write_at_OVERWRITE(self, write_at, text):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file
            s = text
            p = write_at
            self.llist.write_at_data_OVERWRITE(int(p), s, self.file_name)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("Text has been written\n")
        except:
            pass

    def write_at_noOVERWRITE(self, write_at, text):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file
            s = text
            p = write_at
            self.llist.write_at_data_noOVERWRITE(int(p), s, self.file_name)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("Text has been written\n")
        except:
            pass

    def Write_to_File(self, write_at, text):
        print("Do you want to Overwrite? If Yes then write 1 ")
        cond = input("Entre: ")
        if str(cond) == "1":
            self.write_at_OVERWRITE(int(write_at), text)
        else:
            self.write_at_noOVERWRITE(int(write_at), text)

    def Read_From_File(self):
        t = self.llist.read_file(self.file_name)
        print(t)

    #Write in End

    def appendFile(self, text):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file
            s = text
            self.llist.add_data(s, self.file_name)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("Text Has been Appended\n")
        except:
            pass

    def Move_within_file(self, start, size, target):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file
            p = start
            s = target
            size = size
            self.llist.move_data_ll(int(p), int(s), int(size), self.file_name)
            t = self.llist.printList()
            v.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("Text Has been Moved\n")
        except:
            pass

    def read_from_file(self, start, size):
        try:
            self.file.close()
            self.file = open("sample.dat","w+")
            v = self.file.name
            p = start
            size = size
            try:
                text = self.llist.read_file_atpoint( self.file_name, int(p), int(size))
                print(text)
                self.file.close()
                self.file = open("sample.dat", "a+")
            except:
                self.file.close()
                self.file = open("sample.dat", "a+")
                print("")
        except:
            pass

    def truncate(self, maxSize):
        v = self.file
        name = v.name
        try:
            self.file.close()
            self.file = open("sample.dat", "w+")
            self.llist.turncate(int(maxSize),  self.file_name)
            v = self.file
            t = self.llist.printList()
            self.file.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("File has been Truncated\n")
        except:
            self.file = open("sample.dat", "w+")
            self.llist.turncate(int(maxSize),  self.file_name)
            t = self.llist.printList()
            v = self.file
            self.file.write(t)
            self.file.close()
            self.file = open("sample.dat", "a+")
            print("File has been Truncated\n")

    def show_memory_map(self):
        try:
            self.llist.memory_map()
        except:
            pass
    
    def system_exit(self):
        self.file.close()


ob = fileHandling()


def mainMenu():

    while (True):
        print("**File Management System**")

        print("""
            1.Create file
            2.Delete file
            3.Open file
            4.Close file
            5.Read file
            6.Write in the file
            7.Append in the end of text file
            8.Read from a specific point
            9.Write at the specific point
            10.Truncate
            11.Move within a file
            12.Show memory map
            13.Exit System 
            """)

        choice = input("What would you like to do: ")

        if choice == "1":
            fname = input(
                "Enter the name for the text file (without extension): ")
            ob.Create(fname)
        elif choice == "2":
            fname = input(
                "Enter the name for the text file you want to delete(without extension): ")
            ob.Delete(fname)
        elif choice == "3":
            fname = input(
                "Enter the name of the file you want to open(without extension): ")
            mode = input("Enter the file mode (r,w,a)")
            ob.Open(fname, mode)
        elif choice == "4":
            fname = input(
                "Enter the name of the file you want to close(without extension): ")
            ob.Close(fname)
        elif choice == "5":
            ob.Read_From_File()
        elif choice == "6":
            text = input("Enter data: ")
            ob.write_to_file(text)
        elif choice == "7":
            text = input("Enter data: ")
            ob.appendFile(text)
        elif choice == "8":
            start = input("Enter the starting point: ")
            size = input("Enter the string you want to read till: ")
            ob.read_from_file(start, size)
        elif choice == "9":
            write_at = input("Enter the point where you want to write: ")
            text = input("Enter Data: ")
            ob.Write_to_File(write_at, text)
        elif choice == "10":
            maxsize = input("Enter the size of the file, you want: ")
            ob.truncate(maxsize)
        elif choice == "11":
            start = input("Enter starting index: ")
            size = input("Enter the size of string: ")
            target = input("Enter where you want to put the string: ")
            ob.Move_within_file(start, size, target)
        elif choice == "12":
            ob.show_memory_map()
        elif choice == "13":
            ob.system_exit()
            break
        elif choice != "":
            print("\n Not Valid Choice Try again")


mainMenu()

