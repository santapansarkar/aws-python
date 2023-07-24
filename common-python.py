#largest number
def find_largest_number(inp_number):
     largest_so_far = -1
     for curr_num in inp_number:
          if curr_num > largest_so_far:
               largest_so_far = curr_num
     print(f'Largest number in this collection is {largest_so_far}')          

def main():
    str_lst = input("Enter a collection of numbers, use space in between: ")
    str_lst = str_lst.split()
    int_lst = []
    for inp_num in str_lst:
         int_lst.append(int(inp_num))
    find_largest_number(int_lst)
    

if __name__ == "__main__":
     main()
