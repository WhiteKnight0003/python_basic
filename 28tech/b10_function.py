#function
#  a và b ở đây là các tham số : Parameter
def tong(a,b):         
    res = a+b
    return res

m,n = 10, 20    


# default  argument
def infor(name, job = 'xe om'): # nếu đc gán giá trị thì job sẽ thay đổi giá trị còn k sẽ theo giá trị mặc định đã được gán
    print(name, job)

#code để chạy chương trình
if __name__ == '__main__': # giống như main ở các chỗ khác v
    print(tong(m,n)) # m, n ở đây là các đối số            - Positional argument - các vị trí truyền vào tương ứng với các đối số ở trê n
    print(tong(b=20, a =10)) # ta cũng có thể gán như thế này - các vị trí truyền vào đc gán và có thể không theo đúng thứ tự ban đầu
    infor('28tech','Developer') # 28tech Developer 
    infor('teo') # teo xe om

