print([sum(1+.5*l.index(b)for b in[g[0]+g[2]for g in open('2')])for l in['BXCYAZAXBYCZCXAYBZ','BXCXAXAYBYCYCZAZBZ']])

#### Extremely long solutions
l='BXCYAZAXBYCZCXAYBZ'
for _ in[0,1]:
    print(sum(1+.5*l.index(b)for b in[l[0]+l[2]for l in open('2')]))
    l='BXCXAXAYBYCYCZAZBZ'

#with newlines
#g=open('2').read().replace(' ','')
#without whitespace (one character more)
g=''.join(open('2').read().split())
l='BXCYAZAXBYCZCXAYBZ'
for _ in[0,1]:
    print(sum(g.count(l[c*2:(c+1)*2])*(l.index(l[c*2:(c+1)*2])*0.5+1)for c in range(0,9)))
    l='BXCXAXAYBYCYCZAZBZ'