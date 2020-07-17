"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
# add key value pairs
word_definitions['Adaptability'] = 'the quality of being able to adjust to new conditions.'
# print(word_definitions)
"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions['Balance'] = 'a condition in which different elements are equal or in the correct proportions.'
word_definitions['Conscientiousness'] = "the quality of wishing to do one's work or duty well and thoroughly."
word_definitions['Determination'] = 'firmenss of purpose; resoluteness.'
word_definitions['Effervescent'] = 'vivacious and enthusiastic'
word_definitions['Facilitate'] = 'make (an action or process) easy or easier.'
word_definitions['Gratitude'] = 'the quality of being thankful; readiness to show appreciation for and to return kindness.'
word_definitions[
    'Hygge'] = 'a quality of coziness and comfortable conviviality that engenders a feeling of contentment or well-being (regarded as a defining characteristic of Danish culture).'
# print(word_definitions)
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print("First Word:", word_definitions["Hygge"])
# print("Second Word:", word_definitions["Adaptability"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for word, definiton in word_definitions.items():
    print(f'The definition of {word} is {definiton}', "\n")
