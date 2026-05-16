i=0
while i <=5201314:
     i=int(input('请输入年份'))
     if (i % 4 and i% 100!=0) or (i % 400==0):
          print:(i,'年是闰年')
     else:
          print(i,'年 是平年')
i=i+1