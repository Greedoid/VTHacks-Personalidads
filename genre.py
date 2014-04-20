import sys

def cap(num):
	if (num>5):
		num = 5;
	elif (num<1):
		num = 1;
	return num;

def convert(genre):
	reflective = intense = upbeat = energetic = 1;
	if genre == "blues":
		reflective += .85;
		intense += .01;
		upbeat += -.09;
		energetic += .12;
	elif genre == "jazz":
		reflective += .83;
		intense += .04;
		upbeat += .07;
		energetic += .15;
	elif genre == "classical":
		reflective += .66;
		intense += .14;
		upbeat += .02;
		energetic += -.13;
	elif genre == "folk":
		reflective += .64;
		intense += .09;
		upbeat += .15;
		energetic += -.16;
	elif genre == "rock":
		reflective += .17;
		intense += .85;
		upbeat += -.04;
		energetic += -.07;
	elif genre == "alternative":
		reflective += .02;
		intense += .8;
		upbeat += .13;
		energetic += .04;
	elif genre == "retro metal":
		reflective += .07;
		intense += .75;
		upbeat += -.11;
		energetic += .04;
	elif genre == "country":
		reflective += -.06;
		intense += .05;
		upbeat += .72;
		energetic += -.03;
	elif genre == "pop":
		reflective += -.2;
		intense += .06;
		upbeat += .59;
		energetic += .45;
	elif genre == "rap":
		reflective += -.19;
		intense += -.12;
		upbeat += .17;
		energetic += .79;
	elif genre == "soul":
		reflective += .39;
		intense += -.11;
		upbeat += .11;
		energetic += .69;
	elif genre == "electronic":
		reflective += -.02;
		intense += .15;
		upbeat += -.01;
		energetic += .6;
	scale1 = 10;
	reflective *= scale1;
	intense *= scale1;
	upbeat *= scale1;
	energetic *= scale1;
	
	extra = (reflective*.013 + intense*(-.083) + upbeat*.057 + energetic*.163)/.316;
	agree = (reflective*(-.015) + intense*(-.063) + upbeat*.119 + energetic*.095)/.392;
	conc = (reflective*(-.044) + intense*(-.094) + upbeat*.217 + energetic*.013)/.368;
	emot = (reflective*.027 + intense*(-.053) + upbeat*(-.051) + energetic*.072)/.202;
	open = (reflective*.361 + intense*.226 + upbeat*(-.128) + energetic*.093)/.808;
	
	scale = .60;
	
	extra *= scale;
	agree *= scale;
	conc *= scale;
	emot *= scale;
	open *= scale;
	
	shift = 1;
	extra += shift;
	agree += shift;
	conc += shift;
	emot += shift;
	open += shift;
	emot = 5 - emot;#convert from emotional stability to neuroticism 

	
	extra = cap(extra);
	agree = cap(agree);
	conc = cap(conc);
	emot = cap(emot);
	open = cap(open);
	person = [extra, agree, conc, emot, open];
	return person;
	
#def main():
#	genre = sys.argv[1]
#	person = convert(genre);
#	print person
#	return

	

#main()