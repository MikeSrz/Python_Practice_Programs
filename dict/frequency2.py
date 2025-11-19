#Autor: Michael
#
#Descripción: Contar la frecuencia de las palabras de un texto.

def dict_counter(dct, key):
    return dct.get(key, 0)+1

def freq_max(dct):
    max_list = []
    max_value = 0
    for value in dct.values():
        if value > max_value:
            max_value = value

    for key, value in dct.items():
        if max_value == value:
            max_list.append(key)

    return max_list

def freq_min(dct):
    min_list = []
    min_value = 0
    for value in dct.values():
        min_value = value
        break

    for value in dct.values():
        if value < min_value:
            min_value = value

    for key, value in dct.items():
        if min_value == value:
            min_list.append(key)
    return min_list

text = """Did you leave them in the nursery?”
 “I wanted to dress too. Oh, that horrid Africa. What can they see in it?”
 “Well, in five minutes we’ll be on our way to Iowa. Lord, how did we ever get
in this house? What prompted us to buy a nightmare?”
 “Pride, money, foolishness.”
 “I think we’d better get downstairs before those kids get engrossed with those
damned beasts again.”
 Just then they heard the children calling, “Daddy, Mommy, come quick—
quick!”
 They went downstairs in the air flue and ran down the hall. The children
were nowhere in sight. “Wendy? Peter!”
 They ran into the nursery. The veldtland was empty save for the lions
waiting, looking at them. “Peter, Wendy?”
 The door slammed.
 “Wendy, Peter!”
 George Hadley and his wife whirled and ran back to the door.
 “Open the door!” cried George Hadley, trying the knob. “Why, they’ve locked it
from the outside! Peter!” He beat at the door. “Open up!”
 He heard Peter’s voice outside, against the door.
 “Don’t let them switch off the nursery and the house,” he was saying.
 Mr. and Mrs. George Hadley beat at the door. “Now, don’t be ridiculous,
children. It’s time to go. Mr. McClean’ll be here in a minute and…”
 And then they heard the sounds.
 The lions on three sides of them, in the yellow veldt grass, padding through
the dry straw, rumbling and roaring in their throats.
 The lions.
 Mr. Hadley looked at his wife and they turned and looked back at the beasts
edging slowly forward crouching, tails stiff.
 Mr. and Mrs. Hadley screamed.
 And suddenly they realized why those other screams had sounded familiar.
 “Well, here I am,” said David McClean in the nursery doorway, “Oh,
hello.” He stared at the two children seated in the center of the open glade
eating a little picnic lunch. Beyond them was the water hole and the yellow
veldtland; above was the hot sun. He began to perspire. “Where are your father
and mother?”
 The children looked up and smiled. “Oh, they’ll be here directly.”
 “Good, we must get going.” At a distance Mr. McClean saw the lions fighting
and clawing and then quieting down to feed in silence under the shady trees.
 He squinted at the lions with his hand tip to his eyes.
 Now the lions were done feeding. They moved to the water hole to drink.
 A shadow flickered over Mr. McClean’s hot face. Many shadows flickered. The
vultures were dropping down the blazing sky.
 “A cup of tea?” asked Wendy"""

words = text.lower().replace(",","").replace(".","").replace("\"","").replace("?","").replace("!","").replace("“","").replace("”","").split()
words_frequency = {}

for word in words:
   words_frequency[word] = dict_counter(words_frequency, word)

for word,value in words_frequency.items():
    print(f"{word} = {value} {'vez' if value == 1 else 'veces'}")

most_used_words = freq_max(words_frequency)
print(f"las palabra más usada es: {most_used_words} \n")

least_used_words = freq_min(words_frequency)
print (least_used_words)



