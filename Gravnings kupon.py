gravpris1=1000
gravpris2=300
gravpris3=100
gravpris4=1000
sum=0

def menu():
   print("1) Gravning i stor by, 1000,- pr. meter")
   print("2) Gravning i mindre by, 300,- pr. meter")
   print("3) Gravning ude på landet, 100,- pr. meter")
   print("4) Gravning med underboring, 1000,- pr. meter")
   print("5) Stop programmet")

if __name__ == "__main__":
   File_navn=input("Hvad skal den stå under?")
   f = open(File_navn, "w") #Filen oprettes og hvis der eksistere en i forvejen overskrives den!

menu()
valg=int(input("Vælg et nr."))
meny=1

while meny==1:
   if valg ==1:
       print("Du har valgt stor by")
       Destination1=input("Indtast de 2 destinationer")
       Destination1=Destination1+"\n"
       f.write('Destinationer:'+"\n")
       f.write(Destination1)
       afs1=float(input("Indtast afstand i meter"))

       afs1file="Afstand mellem destinationer: "+str(afs1)+" meter"+"\n"
       f.write(str(afs1file))
       print("Pris i alt",gravpris1*afs1,"kr")
       sum=sum+afs1*gravpris1
       sum1=afs1*gravpris1
       print("Samlet pris ",sum1)
       sumfile="Pris for gravning: "+str(sum1)+"Kr."+"\n"
       f.write(sumfile)
       f.write(" "+"\n")
       print("")
       menu()
       valg=int(input('Vælg et nr.'))


   if valg==2:
       print("Du har valgt mindre by")
       Destination2=input("Indtast de 2 destinationer")
       Destination2=Destination2+"\n"
       f.write('Destinationer:'+"\n")
       f.write(Destination2)
       afs2=float(input("Indtast afstand i meter"))

       afs2file="Afstand mellem destinationer: "+str(afs2)+" meter"+"\n"
       f.write(str(afs2file))
       print("Pris i alt",gravpris2*afs2,"kr")
       sum=sum+afs2*gravpris2
       sum2=afs2*gravpris2
       print("Samlet pris ",sum2)
       sumfile2="Pris for gravning: "+str(sum2)+"Kr."+"\n"
       f.write(sumfile2)
       f.write(" "+"\n")
       print("")
       menu()
       valg=int(input('Vælg et nr.'))

   if valg==3:
       print("Du har valgt ude på landet")
       Destination3=input("Indtast de 2 destinationer")
       Destination3=Destination3+"\n"
       f.write('Destinationer:'+"\n")
       f.write(Destination3)
       afs3=float(input("Indtast afstand i meter"))

       afs3file="Afstand mellem destinationer: "+str(afs3)+" meter"+"\n"
       f.write(afs3file)
       print("Pris i alt",gravpris3*afs3,"kr")
       sum=sum+afs3*gravpris3
       sum3=afs3*gravpris3
       print("Samlet pris ",sum3)
       sumfile3="Pris for gravning: "+str(sum3)+"Kr."+"\n"
       f.write(sumfile3)
       f.write(" "+"\n")
       print("")
       menu()
       valg=int(input('Vælg et nr.'))

   if valg==4:
       print("Du har valgt underboring")
       Destination4=input("Indtast de 2 destinationer")
       Destination4=Destination4+"\n"
       f.write('Destinationer:'+"\n")
       f.write(Destination4)
       afs4=float(input("Indtast afstand i meter"))

       afs4file="Afstand mellem destinationer: "+str(afs4)+" meter"+"\n"
       f.write(afs4file)
       print("Pris i alt",gravpris4*afs4,"kr")
       sum=sum+afs4*gravpris4
       sum4=afs4*gravpris4
       print("Samlet pris ",sum4)
       sumfile4="Pris for gravning: "+str(sum4)+"Kr."+"\n"
       f.write(sumfile4)
       f.write(" "+"\n")
       print("")
       menu()
       valg=int(input('Vælg et nr.'))

   if valg==5:
       print('Stopper')
       meny=2

       totalsum="Total pris:" +str(sum)+ "Kr."+"\n"
       f.write(totalsum)
       f.close()
