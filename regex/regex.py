import re

our_text = "How are you brain, i'm fine,How are you brain, i'm fine,How are you brain, i'm fine"
# Search at the beginning of a line
result_match = re.match('How', our_text)
print(result_match)
# Search at the all sentence (first)
result_search = re.search('are', our_text)
print(result_search)
print(result_search[0])
# Find all the matches in the sentence return list all
result_find_all = re.findall('are', our_text)
print('find all ')
print(result_find_all)
print(result_find_all[0])
# Split - separate out sentence
result_split = re.split(',', our_text, maxsplit=1)
print(len(result_split))
print(result_split)
# sub change any character to our pattern
result_sub = re.sub('H', 'Q', our_text)
print(result_sub)
# full match
result_full_match = re.fullmatch("How are you brain, i'm fine,How are you brain, i'm fine,How are you brain, i'm fine",
                                 our_text)
print(result_full_match)
# More difficult examples


more_difficult_text = ('Hello my name Stan +-***/+ , and i have a mobile number +380 63 953 9901.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9902.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9903.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9904.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9905.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9906.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9907.'
                       'Hello my name Stan , and i have a mobile number +380 63 953 9908. ')

phone_pattern = r'\+\d{3} \d{2} \d{3} \d{4}'

words_that_start_with_vowels = r'\b[aeiouAEIOU][a-zA-Z]*\b'
result_find_a_phone_number = re.search(phone_pattern, more_difficult_text)
result_find_a_phone_number1 = re.findall(words_that_start_with_vowels, more_difficult_text)
print(result_find_a_phone_number)
print("---------------------------")
print(result_find_a_phone_number1)
# Iterable
result_find_inter_a_phone_number = re.finditer(phone_pattern, more_difficult_text)
for i in result_find_inter_a_phone_number:
    print(i)
