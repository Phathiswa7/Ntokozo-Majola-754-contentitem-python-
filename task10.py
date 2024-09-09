def task10(str1, str2):
  str1_lower = ''.join(filter(str.isalpha, str1)).lower()
  str2_lower = ''.join(filter(str.isalpha, str2)).lower()

  common_letters_set = set(str1_lower).intersection(set(str2_lower))

  common_letters_str = sorted(common_letters_set)

  if len(common_letters_str) > 1:
        common_letters_str_formatted = ', '.join(common_letters_str[:-1]) + f" and {common_letters_str[-1]}"
  elif len(common_letters_str) == 0:
        common_letters_str_formatted = "no common letters"
  else:
        common_letters_str_formatted = ', '.join(common_letters_str)

  print(common_letters_str_formatted)


task10("Ho!use", "com!puters")

