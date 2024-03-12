def checkVowel(m):
  match m:
    case 'a': return "Vowel alphabet"
    case 'e': return "Vowel alphabet"
    case 'i': return "Vowel alphabet"
    case 'o': return "Vowel alphabet"
    case 'u': return "Vowel alphabet"
    case _: return "Simple alphabet"
print (checkVowel('i'))
print (checkVowel('o'))
print (checkVowel('w'))
