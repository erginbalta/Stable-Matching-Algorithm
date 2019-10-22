import collections
import random

preferred_rankings_women = {
}

preferred_rankings_men = {
}
men = []
women = []
tentative_engagements = []

free_man = []
#-----------------------------------------

def add_lists():
    l = int(input("how many men and women entered : "))
    
    print("men")
    for i in range(l):
        m = input("->")
        men.append(m)
    print("women")
    for i in range(l):
        w = input("->")
        women.append(w)
    for x in men:
        random.shuffle(women)
        preferred_rankings_men[x] = women
    
    for y in women:
        random.shuffle(men)
        preferred_rankings_women[y] = men
        
#-----------------------------------------
def init_free_men():
    for man in preferred_rankings_men.keys():
        free_man.append(man)
#-----------------------------------------
def stable_matching (): 
    while(len(free_man) > 0):
        for man in free_man:
            begin_matching(man)
#-----------------------------------------
def begin_matching (man):
    print("dealing with " +man)
    for woman in preferred_rankings_men[man]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if (len(taken_match) == 0):
            tentative_engagements.append([man,woman])
            free_man.remove(man)
            print(man +" is no longer a free man and now tentatively engaged to " +woman)
            break
        elif (len(taken_match) > 0):
            print (woman +" is taken already..")
            current_man = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_man = preferred_rankings_women[woman].index(man)

            if (current_man < potential_man):
                print("she is satisfied with " +taken_match[0][0])
            else:
                print(man +" is better than " +taken_match[0][0])
                print("making " +taken_match[0][0] +" free again... and than tentatively accept dance between " +man +" and " +woman)

                free_man.remove(man)

                free_man.append(taken_match[0][0])

                taken_match[0][0] = man
                break
#-----------------------------------------            
def main():
    add_lists()
    init_free_men()
    stable_matching()
    print("complete matching acceptances\n")
    print(tentative_engagements)

if __name__ == "__main__":
    main()

            
