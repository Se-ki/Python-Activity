from word_bank import setFirstName, setLastName, storeWords, fname, lname

setFirstName("ck")
setLastName("autor")
storeWords()

import reverse
print(reverse.string("Ratava: Eht Tsal Ria Redneb"))

from generate import passcode
print(passcode(fname="Christian Kyle", lname="Autor", dayOfBirth=14, monthOfBirth=3))