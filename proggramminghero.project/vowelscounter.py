def vowel_count(sentence):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  count = 0
  for vwls_count in sentence:
      if vwls_count in vowels:
          count += 1
  return count
x = vowel_count(input("Enter sentence to find vowels: "))
print("There are ", x, "vowels in the line")