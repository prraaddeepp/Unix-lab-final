import sys
def encrypt(s):
  message = input()
  result = ""
  five_letters_block = ""
  final_result = ""
  my_message = message.upper()
  for i in range(len(my_message)):
    character = my_message[i]
    if character.isalpha():
        result += chr((ord(character) + s-65) % 26 + 65)
  five_letters_block = [result[i:i+5] for i in range(0,len(result),5)]
  k=1
  for element in five_letters_block:
      if k % 2 == 0:
          final_result += element + '\n'
      else:
          final_result += element + ' '
      k+=1
  return (final_result)
q = int(sys.argv[1])
print(encrypt(q))

