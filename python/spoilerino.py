print('Enter your text: ', end=' ')
text = str(input())

text = text.split(' ')
out = ''
for i, x in enumerate(text):
	if i%2==0:
		out = out + ' ||' + x + '|| '
	else:
		out = out + x
print(out)