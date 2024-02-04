#largest number
def find_largest_number(inp_number):
     largest_so_far = None
     for curr_num in inp_number:
          if largest_so_far is None:
               largest_so_far = curr_num
          elif curr_num > largest_so_far:
               largest_so_far = curr_num
     print(f'Largest number in this collection is {largest_so_far}')   

def find_average_number(inp_number):
     total_num = 0 
     count_num = 0
     avg_num = 0
     for curr_num in inp_number:
          total_num += curr_num
          count_num += 1
     avg_num = total_num / count_num      
     print(f'Number of items in this collection are {count_num}')
     print(f'Sum of all numbers in the collection is {total_num}')
     print(f'Average number in this collection is {avg_num}')   
     
          
def loop_through_strings(inp_str):
     for letter in inp_str:
          print(letter)
                      

def main():
    str_lst = input("Enter a collection of numbers, use space in between: ")
    str_lst = str_lst.split()
    int_lst = []
    for inp_num in str_lst:
         int_lst.append(int(inp_num))
    #find_largest_number(int_lst)
    #find_average_number(int_lst)
    loop_through_strings('banana')
    

if __name__ == "__main__":
     main()
