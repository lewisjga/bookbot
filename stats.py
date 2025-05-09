def count_words(text):
     text_full = text.split()
     return f'{len(text_full)}'

def count_chars(text):
     text_full = text.split()
     char_counts = {}
     for i in text_full:
          chars = list(i)
          for i in chars:
               current_char = i.lower()
               if current_char in char_counts:
                    char_counts[current_char] += 1
               else:
                    char_counts[current_char] = 1
     return(char_counts)

def count_sort(c):
     return c['num']

def chars_sort(char_dict):
     sorted_chars = []
     for i in (char_dict):
          current_dict = {}
          current_char = i
          if current_char.isalpha():
               current_val = char_dict[i]
               current_dict.update({'char':current_char})
               current_dict.update({'num':current_val})
               sorted_chars.append(current_dict)
          else:
               pass
     sorted_chars.sort(reverse=True, key=count_sort)
     for i in sorted_chars:
          print(f"{i['char']}: {i['num']}")
