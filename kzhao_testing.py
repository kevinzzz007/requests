__author__ = 'RunzeZhao'
import requests

r= requests.get('https://api.github.com')
print r.status_code
print r.headers['content-type']
print r.text

def maxSum(N, A):
  flag = False
  temp = 0
  new = []
  lit1 = []
  lit2 = []
  interm=[]
  p = 0
  result = 0
  sum_of_interm = 0
  numb_flag = 1
  for index in range(N):
    if flag == False:
      temp = A[index]
      if temp >= 0:
        new.append(temp)
      else:
        flag = True
        p = index
        neg = temp
    else:
      temp = A[index]
      if temp >= 0:
        interm.append(temp)
      else:
        flag = False
      	for each in interm:
          sum_of_interm +=each
          if numb_flag ==1:
            if neg+sum_of_interm>0:
              lit1 = new.append(neg)+interm
            else:
              lit1 = new
          else:
            if neg+sum_of_interm>0:
              lit2 = new.append(neg)+interm
            else:
              lit2 = new

  for each in lit1:
    result = result + each
  for each in lit2:
    result = result +each
  return result