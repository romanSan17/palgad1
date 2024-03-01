from module1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-andmed_veerudes\n1-andemete lisamine\n2-andmete_eemaldamine_nimi_jargi\n3-kellel_on_suurim_palk\n4-kellel_on_vaiksem_palk\n5-sorteerimine\n6-vordsed_palgad\n")
    valik=int(input())
    if valik==1:
        inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisamine?")))
    elif valik==0:
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed,palgad)
    elif valik==3:
        kellel_on_suurim_palk()
    elif valik==4:
        kellel_on_vaiksem_palk()
    elif valik==5:
        sorteerimine(inimesed,palgad)
    elif valik==6:
        vordsed_palgad()
    elif valik==7:
        isiku=input("kasutajanimi?")