def gcd(m, M):
  if M==0:
    return m
  else:
    return gcd(M, m%M)

def gcd(m,M):
  if M==0:
    return m # gcd
  else:
    return gcd(M,m%M)

m,M=map(int, input().split())

print(gcd(m,M))
print(m*M//gcd(m,M))