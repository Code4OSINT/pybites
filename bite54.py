shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""

# part of Remember, by Christina Rosetti
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""

INDENT = 4

def print_hanging_indents(poem):
    text = []
    text = poem.strip("\n").strip(" ")
    text.replace("  ", "")
    return text
    
#text = print_hanging_indents(shakespeare_unformatted)

print(rosetti_unformatted.split("\n\n"))


#text = "\n".join([line for line in rosetti_unformatted.splitlines() if len(line)>2])
#print(text.replace("  ", ""))
 
text = ""

result = [line for line in rosetti_unformatted.splitlines() ]
#    while len(line) > 1:
#        result.append(line.lstrip())


#    if len(line) < 1:
#        for l in text.splitlines():
#            result = (" "*INDENT).join(line)
#            result.lstrip("")
print([item for item in result])
        