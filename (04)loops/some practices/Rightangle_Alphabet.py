# j=input("Enter a word: ")
# for a in range(1,len(j)+1):
#     for b in range(a):
#         print(j,end=' ')
#     print()


i=input("Enter a word: ")# this work continuously. if i enter any character.
for k in range(1,8):
     for j in range(ord(i) , ord(i)+k):
         print(chr(j),end=" ")
     print()