import re
l = '445.155#45$5412/4#-8@5%'
# m = re.findall(r'^(-\d|\d)[\d\./]*(\d|%)', l)
m = re.findall(r'(-\d|\d)+[\d\./]*\d+', l)
print(m)
