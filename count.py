def quotients(votelist, voteQ, seatlist):
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
    return keyM

def main(seats, votelist):
    seatlist={}
    for key in votelist.keys():
        seatlist[key]=0

    voteQ={}

    for seat in range(seats):
        voteQ=quotients(votelist, voteQ, seatlist)
        keyM=ret_max(voteQ)
        seatlist[keyM]+=1

    return seatlist

if __name__=="__main__":
    seats=16
    votelist={"Party1":0, "P2":2, "P3":3}
    print(main(seats, votelist))
