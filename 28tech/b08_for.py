#for và range()
'''range() - sẽ sinh ra 1 dãy số và bạn sẽ sử dụng for để duyệt qua từng số trong dãy đã sinh ra
cú pháp : range(start, stop, step)
start : giá trị bắt đầu - nếu k có nó mặc định là 0
stop :  giá trị dừng - chỉ lấy < chứ k lấy = 
step : bước nhảy  - nếu k có nó mặc định là 1

- cũng bắt buộc phải lùi đầu dòng để đúng cấp với câu lệnh
for i in range(1,10,3):
    print(i,end='--')  1--4--7--

# tại sao lại dùng arange cảu np mà k phải range bình thường 
# range chỉ dùng cho số nguyên 
# còn np.arange cho cả số thực 
'''



# in ra từ 1 -> 20 nhưng gặp chia hết cho 7 thì dừng - break
for i in range(1,21):
    print(i,end=' ')
    if i%7==0 :
        break
    print('đâssd')
'''
1 đâssd
2 đâssd
3 đâssd
4 đâssd
5 đâssd
6 đâssd
7
'''


#continue // bỏ qua vognf lặp hiện tại
for i in range(1,20):
    if i%2==0:
        print(i,end=' ')
    else: 
        continue