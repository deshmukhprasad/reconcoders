from .models import Disease

def chart1():
	a=Disease.objects.all()
	b=[]
	d=[]
	for i in range(len(a)):
		b.append(a[i].disease_possible)
	c=list(set(b))
	zeros = [ [0] * 12 for _ in range(len(c))]
	z=0
	for i in c:
		a=Disease.objects.filter(disease_possible=i)
		for k in a :
			g=str(k.date)
			g1=g.split()
			g2=g1[0].split('-')
			j=int(g2[1])
			zeros[z][j-1]+=1
		z+=1
	return(zeros,c)

def chart2():
	a=Disease.objects.all()
	b=[]
	d=[]
	for i in range(len(a)):
		b.append(a[i].disease_possible)
	c=list(set(b))
	for i in c:
		a=Disease.objects.filter(disease_possible=i)
		d.append(len(a))
	for i in range(len(d)-2):
		for j in range(i+1,len(d)):
			if d[j]>d[i]:
				d[j],d[i]=d[i],d[j]
				c[j],c[i]=c[i],c[j]
	return(c,d)


