other = ['Arsenal (ENG)', 'Astana (KAZ)', 'Atlético (ESP)',  ' BATE (BLR)',  'CSKA Moskva (RUS)', 'Dinamo Zagreb (CRO)', 'Dynamo Kyiv (UKR)',
     'Galatasaray (TUR)', 'Gent (BEL)',  'Leverkusen (GER)', 'Lyon (FRA)', 'M. Tel-Aviv (ISR)',
     'Malmö (SWE)', 'Man. City (ENG)', 'Man. United (ENG)', 'Mönchengladbach (GER)', 'Olympiacos (GRE)',
     'Porto (POR)',  'Real Madrid (ESP)', 'Roma (ITA)', 'Sevilla (ESP)', 'Shakhtar Donetsk (UKR)',
     'Valencia (ESP)', 'Wolfsburg (GER)', ]
champions=['Barcelona (ESP)',' Bayern (GER)','Benfica (POR)', 'Chelsea (ENG)','Juventus (ITA)','Paris (FRA)','PSV (NED)','Zenit (RUS)']
import random
groupA=[]
groupAc=[]
groupBc=[]
groupB=[]
groupCc=[]
groupC=[]
groupDc=[]
groupD=[]
groupEc=[]
groupE=[]
groupFc=[]
groupF=[]
groupGc=[]
groupG=[]
groupHc=[]
groupH=[]
i=1
while i<=8:
    x=random.randint(0,len(champions)-1)
    ans=champions.pop(x)
    a=ans[-2:-5:-1]
    if i==1:
        groupA.append(ans)
        groupAc.append(a)
    if i==2:
        groupB.append(ans)
        groupBc.append(a)
    if i==3:
        groupC.append(ans)
        groupCc.append(a)
    if i==4:
        groupD.append(ans)
        groupDc.append(a)
    if i==5:
        groupE.append(ans)
        groupEc.append(a)
    if i==6:
        groupF.append(ans)
        groupFc.append(a)
    if i==7:
        groupG.append(ans)
        groupGc.append(a)
    if i==8:
        groupH.append(ans)
        groupHc.append(a)
    i += 1

i=1
while i<=8:
    y=random.randint(0,len(other)-1)
    ans=other.pop(y)
    a=ans[-2:-5:-1]
    if i==1:
        if a not in groupAc:
            groupA.append(ans)
            groupAc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupAc:
                x=other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupA.append(ans)
            groupAc.append(a)
            i += 1
    if i==2:
        if a not in groupBc:
            groupB.append(ans)
            groupBc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupBc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupB.append(ans)
            groupBc.append(a)
            i += 1
    if i==3:
        if a not in groupCc:
            groupC.append(ans)
            groupCc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupCc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupC.append(ans)
            groupCc.append(a)
            i += 1
    if i==4:
        if a not in groupDc:
            groupD.append(ans)
            groupDc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupDc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupD.append(ans)
            groupDc.append(a)
            i += 1
    if i==5:
        if a not in groupEc:
            groupE.append(ans)
            groupEc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupEc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupE.append(ans)
            groupEc.append(a)
            i += 1
    if i==6:
        if a not in groupFc:
            groupF.append(ans)
            groupFc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupFc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupF.append(ans)
            groupFc.append(a)
            i += 1
    if i==7:
        if a not in groupGc:
            groupG.append(ans)
            groupGc.append(a)
            i += 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupGc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupG.append(ans)
            groupGc.append(a)
            i += 1
    if i==8:
        if a not in groupHc:
            groupH.append(ans)
            groupHc.append(a)
            i = 1
        else:
            other.append(ans)
            while other[0][-2:-5:-1] in groupHc:
                x = other.pop(0)
                other.append(x)
            ans = other.pop(0)
            a = ans[-2:-5:-1]
            groupH.append(ans)
            groupHc.append(a)
            i = 1
    print(ans)