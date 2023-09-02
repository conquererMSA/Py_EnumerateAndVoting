'''
Voting System application:

'''
votterInput=input('Enter votter id, id separete by space: ')
votter=list(set(votterInput.split(' ')))
print(votter)

candidate1=input('Enter candidate 1 name: ')
candidate2=input('Enter candidate 2 name: ')
candidate1Vote=0
candidate2Vote=0
vottedId=[]

while True:
    if votter==[]:
        if candidate1Vote>candidate2Vote:
            print(f"{candidate1} is won with {candidate1Vote} vote")
        elif candidate1Vote<candidate2Vote:
            print(F"{candidate2} is won with {candidate2Vote} vote")
        else:
            print(F"Election is tied! Each candidate gain {candidate2Vote} vote")
        break
    else:
        votterId=input('Enter your nid num: ')
        print(votterId)
        if votterId in votter:
            if votterId not in vottedId:
                print("Congrats! You'r able to vote")
                voteAns=input(f"Chose your candidate: \n 1. {candidate1} \n 2."
                            f" {candidate2}:"
                          f"\n Ans:  ")
                if voteAns=="1":
                    print(f"You voted {candidate1}")
                    candidate1Vote+=1
                    votter.remove(votterId)
                    vottedId.append(votterId)
                    print(votter)
                    print(vottedId)
                elif voteAns=='2':
                    print(f"You voted {candidate2}")
                    candidate2Vote+=1
                    votter.remove(votterId)
                    vottedId.append(votterId)
        elif votterId not in votter:
            print('You are not a votter!')
        elif votterId in vottedId:
            print('You already votted!')

