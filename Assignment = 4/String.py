#  Performed all the operations on string

#  1. capitalize
#  2. casefold
#  3. center
#  4. count
#  5. encode
#  6. endswith
#  7. expandtabs
#  8. find
#  9. format
#  10. index
#  11. isalnum
#  12. isalpha
#  13. isdecimal
#  14. isdigit
#  15. isidentifier
#  16. islower
#  17. isnumeric
#  18. isprintable
#  19. isspace
#  20. istitle
#  21. isupper
#  22. join
#  23. ljust
#  24. lower
#  25. lstrip
#  26. maketrans
#  27. partition
#  28. replace
#  29. rfind
#  30. rindex
#  31. rjust
#  32. rpartition
#  33. rsplit
#  34. rstrip
#  35. split
#  36. splitlines
#  37. startswith
#  38. strip
#  39. swapcase
#  40. title
#  41. translate
#  42. upper
#  43. zfill


s = "Sanket"

# capitalize
print(s.capitalize())
print('\n')

# casefold
print(s.casefold())
print('\n')

# center
print(s.center(20, '*'))
print('\n')

# count
print(s.count('e'))
print('\n')

# encode
print(s.encode())
print('\n')

# endswith
print(s.endswith('t'))
print('\n')

# expandtabs
print(s.expandtabs(2))
print('\n')

# find
print(s.find('e'))
print('\n')

# format
print(s.format())
print('\n')

# index
print(s.index('e'))
print('\n')

# isalnum
print(s.isalnum())
print('\n')

# isalpha
print(s.isalpha())
print('\n')

# isdecimal
print(s.isdecimal())
print('\n')

# isdigit
print(s.isdigit())
print('\n')

# isidentifier
print(s.isidentifier())
print('\n')

# islower
print(s.islower())
print('\n')

# isnumeric
print(s.isnumeric())
print('\n')

# isprintable
print(s.isprintable())
print('\n')

# isspace
print(s.isspace())
print('\n')

# istitle
print(s.istitle())
print('\n')

# isupper
print(s.isupper())
print('\n')

# join
print(s.join(['a', 'b', 'c']))
print('\n')

# ljust
print(s.ljust(20, '*'))
print('\n')

# lower
print(s.lower())
print('\n')

# lstrip
print(s.lstrip('S'))
print('\n')

# maketrans
print(s.maketrans('S', 's'))
print('\n')

# partition
print(s.partition('e'))
print('\n')

# replace
print(s.replace('e', 'a'))
print('\n')

# rfind
print(s.rfind('e'))
print('\n')

# rindex
print(s.rindex('e'))
print('\n')

# rjust
print(s.rjust(20, '*'))
print('\n')

# rpartition
print(s.rpartition('e'))
print('\n')

# rsplit
print(s.rsplit('e'))
print('\n')

# rstrip
print(s.rstrip('e'))
print('\n')

# split
print(s.split('e'))
print('\n')

# splitlines
print(s.splitlines())
print('\n')

# startswith
print(s.startswith('S'))
print('\n')

# strip
print(s.strip('S'))
print('\n')

# swapcase
print(s.swapcase())
print('\n')

# title
print(s.title())
print('\n')

# translate
print(s.translate(s.maketrans('S', 's')))
print('\n')

# upper
print(s.upper())
print('\n')

# zfill
print(s.zfill(20))
print('\n')


