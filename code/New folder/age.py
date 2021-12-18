#f=open('text.txt')
#f1=f.readlines()
#for i in f1:
#  print(i)


def countwords():
   filename=input('enter your file name')
   f=open(filename,'r')
   word=0
   for i in f:
       w=i.split()
       word=word+len(w)

   print(word)

 




countwords()