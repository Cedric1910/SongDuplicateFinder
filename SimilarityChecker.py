from difflib import SequenceMatcher
import itertools

def main():

	songs = ["A.M.C, Teddy Killerz   NITRO (Teddy Killerz Remix)","A.M.C, Redpill   ENERGY (Redpill Remix",
	"Mob Tactics - Eject","Mob_Tactics-Eject"]
	list1=[1,2,3,4,5,1,2,3]
	list2=[1,2,2]

	for a, b in itertools.combinations(songs, 2):
		#print(a,b)
		seq = SequenceMatcher(a=a,b=b)
		if(seq.ratio() >= 0.1):
			print(a,b,seq.ratio())

if __name__ == "__main__":
    main()