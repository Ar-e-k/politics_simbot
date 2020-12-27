def quotients(votelist, seatlist):
    voteQ={}
    for key, value in votelist.items():
        den=2*seatlist[key]+1
        voteQ[key]=value/den
    return voteQ

def ret_max(voteQ):
    mx=0
    keyM=None
    for key, value in voteQ.items():
        if value>mx:
            keyM=key
            mx=value
    return keyM

def main(seats, votelist):
    seatlist={}
    for key in votelist.keys():
        seatlist[key]=0

    voteQ={}

    for seat in range(seats):
        voteQ=quotients(votelist, seatlist)
        keyM=ret_max(voteQ)
        seatlist[keyM]+=1

    return seatlist

if __name__=="__main__":
    seats=16
    votelist={'conservative party': 4, 'labour party': 0, 'ukip party': 1, 'lib dem party': 0, 'green party': 1, 'nlp national labour party': 1, 'pink party': 2, 'sinn féin party': 1, 'bird party': 1}
    print(main(seats, votelist))
