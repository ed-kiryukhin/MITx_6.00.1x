## COUNTING VOWELS
## Assume s is a string of lower case characters

count=0
for letter in s:
	if letter in "aeiou":
		count += 1
print "Number of vowels: %d" % (count)
