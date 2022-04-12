class StringUtility:
  def __init__(self, string):
    '''constructor
    args: self, string
    return: none'''
    self.mystring = string

  def __str__(self):
    '''convert objet to string
    args: self
    return: self.mystring'''
    return self.mystring

  def vowels(self):
    '''find vowels
    args:self
    return: many/ 3 or less'''
    count = 0
    for c in self.mystring:
        if c in [ 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
            count += 1
    if count >= 5:
        return 'many'
    else:
        return '{0}'.format(count)

  def bothEnds(self):
    '''find first and last two
    args: self
    returnfirst and last two strings
    '''
    if len(self.mystring) <= 2:
        return ''
    first_two = self.mystring[:2]
    last_two = self.mystring[-2:]
    return first_two + last_two

  def fixStart(self):
    '''make all the characters except first start
    args: self
    return converted new string'''
    if len(self.mystring) <= 1:
        return self.mystring
    first_char = self.mystring[0]
    second_to_end = self.mystring[1:]
    new_string = '' + first_char
    for c in second_to_end:
        if c == first_char:
            new_string += '*'
        else:
            new_string += c
    return new_string

  def asciiSum(self):
    """ord(char) will return the ascii value of char
    https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
    args: self
    return ascii values of char
    """
    sum_of_string_ascii_values = 0
    for c in self.mystring:
      sum_of_string_ascii_values += ord(c)
    return sum_of_string_ascii_values

  def cipher(self):
    """increment char ascii value by length of string, it could wrap around a few times
    args self
    return return an encoded string by incrementing all letters by the length of the string.
    """
    new_string = ''
    shift_value = len(self.mystring)
    shift_value = shift_value % 26 # take a modulo so that we can skip the looping back to its' own position every 26 chars
    for c in self.mystring:
        if c >= 'a' and c <= 'z': # lower case
            if ord(c) + shift_value > ord('z'): # need to wrapp around to 'a'
              shifting_from_beginning = (shift_value - (ord('z') - ord(c) + 1))
              new_c_ascii_value = ord('a') + shifting_from_beginning
              new_c = chr(new_c_ascii_value)
              new_string += new_c
            else:
              new_c_ascii_value = ord(c) + shift_value
              new_c = chr(new_c_ascii_value)
              new_string += new_c
        elif c >= 'A' and c <= 'Z': # upper case
            if ord(c) + shift_value > ord('Z'):  # need to wrapp around to 'a'
              shifting_from_beginning = (shift_value - (ord('Z') - ord(c) + 1))
              new_c_ascii_value = ord('A') + shifting_from_beginning
              new_c = chr(new_c_ascii_value)
              new_string += new_c
            else:
              new_c_ascii_value = ord(c) + shift_value
              new_c = chr(new_c_ascii_value)
              new_string += new_c
        else: # not a letter
          new_string += c
    return new_string