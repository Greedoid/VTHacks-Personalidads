from genre import *
def personality(genre_dict):
	personality = [0, 0, 0, 0, 0]
	genres = genre_dict.keys()
	num = len(genres)
	numsongs = 0
	for i in range(0, num):
		temp = convert(str(genres[i]))
		print temp
		for x in range(0, 5):
			temp[x] = (genre_dict[genres[i]]) * (temp[x])
		numsongs += int(genre_dict[genres[i]])
		personality = [x + y for x, y in zip(personality, temp)]
	print "Personality.........."
	print personality
	newList = [x/numsongs for x in personality]
	print "New List..............."
	print newList
	return newList