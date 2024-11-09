#sum of first n natural no
# n(n-1)/2

def cal_sum(n):
    if n==1:
        return 1
    return cal_sum(n-1) + n

print(cal_sum(5))


#print all elements in list using resursion
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list([3,2,6,8,2,4],4)