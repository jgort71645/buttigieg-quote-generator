import numpy as np

def buzzword():
    N = 46
    c = np.ceil(N*np.random.uniform())
    if c == 1:
        return "hope"
    if c == 2:
        return "vision"
    if c == 3:
        return "democracy"
    if c == 4:
        return "issue"
    if c == 5:
        return "service"
    if c == 6:
        return "values"
    if c == 7:
        return "faith"
    if c == 8:
        return "election"
    if c == 9:
        return "purpose"
    if c == 10:
        return "nation"
    if c == 11:
        return "presidency"
    if c == 12:
        return "equality"
    if c == 13:
        return "family"
    if c == 14:
        return "community"
    if c == 15:
        return "neighborhood"
    if c == 16:
        return "policy"
    if c == 17:
        return "voice"
    if c == 18:
        return "mental health"
    if c == 19:
        return "workplace"
    if c == 20:
        return "movement"
    if c == 21:
        return "economy"
    if c == 22:
        return "unity"
    if c == 23:
        return "belonging"
    if c == 24:
        return "life"
    if c == 25:
        return "politics"
    if c == 26:
        return "health"
    if c == 27:
        return "people"
    if c == 28:
        return "unification"
    if c == 29:
        return "empowerment"
    if c == 30:
        return "glorification"
    if c == 31:
        return "president"
    if c == 32:
        return "choice"
    if c == 33:
        return "path"
    if c == 34:
        return "leadership"
    if c == 35:
        return "bold ideas"
    if c == 36:
        return "difference"
    if c == 37:
        return "action"
    if c == 38:
        return "answers"
    if c == 39:
        return "resilience"
    if c == 40:
        return "message"
    if c == 41:
        return "future"
    if c == 42:
        return "addition"
    if c == 43:
        return "boldness"
    if c == 44:
        return "big things"
    if c == 45:
        return "solutions"
    if c == 46:
        return "wine cave"
    
def badword():
    N = 20
    c = np.ceil(N*np.random.uniform())
    if c == 1:
        return "division"
    if c == 2:
        return "voter suppression"
    if c == 3:
        return "gerrymandering"
    if c == 4:
        return "white supremacy"
    if c == 5:
        return "gun violence"
    if c == 6:
        return "prejudice"
    if c == 7:
        return "fear"
    if c == 8:
        return "HIV/AIDS"
    if c == 9:
        return "challenge"
    if c == 10:
        return "broken policies"
    if c == 11:
        return "broken politics"
    if c == 12:
        return "exhaustion"
    if c == 13:
        return "cynicism"
    if c == 14:
        return "exclusion"
    if c == 15:
        return "desolation"
    if c == 16:
        return "rat poison"
    if c == 17:
        return "interference"
    if c == 18:
        return "rejection"
    if c == 19:
        return "exclusion"
    if c == 20:
        return "dysfunction"

def buzzverb():
    N = 6
    c = np.ceil(N*np.random.uniform())
    if c == 1:
        return "galvanize"
    if c == 2:
        return "inspire"
    if c == 3:
        return "unite"
    if c == 4:
        return "embolden"
    if c == 5:
        return "govern"
    if c == 6:
        return "win"

def badverb():
    N = 2
    c = np.ceil(N*np.random.uniform())
    if c == 1:
        return "polarize"
    if c == 2:
        return "divide"
    
def quote():
    N = 26
    c = np.ceil(N*np.random.uniform()) 
    if c == 1:
        return f"I believe the {buzzword()} belongs to people of {buzzword()} and no {buzzword()} at all.\r\nI also believe that people of {buzzword()} have a choice to make when it\r\ncomes to this {buzzword()}."
    if c == 2:
        return f"Our {buzzword()}s are being threatened by foreign {badword()}--and\r\n{badword()} here at home. {badword().capitalize()} is {badword()}.\r\nRacial {badword()} is {badword()}.\r\nWe need a 21st Century Voting Rights Act."
    if c == 3:
        return f"{buzzword().capitalize()} struggles affect every {buzzword()}, every {buzzword()},\r\nevery {buzzword()}, every {buzzword()}.\r\nI will be a president who not only works to get the {buzzword()} right,\r\nbut gives {buzzword()} to those struggles"
    if c == 4:
        return f"This is an extraordinary moment for the {buzzword()} we're building."
    if c == 5:
        return f"Trayvon Martin would have been 25 today.\r\nHow many 25th birthdays have been stolen from us by\r\n{badword()}, {badword()}, {badword()}, and {badword()}?"
    if c == 6:
        return f"(Incoherent rat noises)"
    if c == 7:
        return f"I believe in American {buzzword()}.\r\nI believe in American {buzzword()}."
    if c == 8:
        return f"I believe the {buzzword()} has a {buzzword()}."
    if c == 9:
        return f"If you're ready to build an American {buzzword()} defined by {buzzword()},\r\nthis is our chance.\r\nIf you're ready to build an American {buzzword()} defined by {buzzword()},\r\nthis is our chance."
    if c == 10:
        return f"Your {buzzword()} should never be determined by who you are, what you look like,\r\nor whom you love. Yet Black Americans are disproportionately affected\r\nby {badword()}. It's unacceptable.\r\nMy White House will commit to ending the {badword()} epidemic by 2030."
    if c == 11:
        return f"If you're ready to build an American {buzzword()} defined by {buzzword()} in the\r\nface of our greatest {badword()}, this is our chance."
    if c == 12:
        return f"The {buzzword()} of the {buzzword()} is not the {buzzword()} of the {buzzword()},\r\nit is the {buzzword()} and {buzzword()} of the {buzzword()}."
    if c == 13:
        return f"You chose to move on not just from the {badword()} of the last few years,\r\nbut the {badword()} that got us here. Tomorrow, because of what we\r\ndid here, the {buzzword()} will have that {buzzword()} too."
    if c == 14:
        return f"Tonight, Iowa chose a new {buzzword()}."
    if c == 15:
        return f"We could see an American majority yearning for {buzzword()} to rally us\r\ntogether behind {buzzword()} that would make {buzzword()} in our lives."
    if c == 16:
        return f"We had the belief that in the face of {badword()}, {badword()}, and\r\n{badword()}--in spite of every trampled norm and poisonous tweet,\r\nthat a rising majority of Americans was hungry for {buzzword()}\r\nand ready for new {buzzword()}."
    if c == 17:
        return f"I joined this race a year ago seeing how the last presidential\r\nelection led to {badword()} and {badword()}. But after\r\nspending months on the trail bringing our {buzzword()} to millions,\r\nI saw firsthand the {buzzword()} of American families and the\r\n{buzzword()} they carry for the {buzzword()}."
    if c == 18:
        return f"Americans are hungry for a {buzzword()} and a {buzzword()}\r\nthat will rally us all around a shared {buzzword()} for the\r\n{buzzword()}--one defined not by {badword()} but by\r\n{buzzword()}."
    if c == 19:
        return f"The {buzzword()} of our {buzzword()} is the {buzzword()} that affects every\r\nother {buzzword()}."
    if c == 20:
        return f"I will not pursue {buzzword()} by telling people they can't be at\r\nour side if they're not with us 100% of the time.\r\nThis is a time for {buzzword()}, not {badword()},\r\nfor {buzzword()}, not {badword()}."
    if c == 21:
        return f"I'm not interested in labels. I'm interested in the style of\r\n{buzzword()} that we need to put forward to finally turn the page."
    if c == 22:
        return f"Not just in order to {buzzverb()}, but in order to\r\n{buzzverb()}. The next president will face unprecedented\r\n{badword()}s that require bringing the American people together."
    if c == 23:
        return f"It's time to {buzzverb()}--not {badverb()}--the American people\r\naround {buzzword()} and actually get things done."
    if c == 24:
        return f"I'm seeing a hunger for {buzzword()} oriented toward\r\nthe {buzzword()}. It's time to believe we can {buzzverb()}.\r\nIt's time to turn the page."
    if c == 25:
        return f"I'm running to be a president who will help Americans\r\nbelieve we can get {buzzword()} done together."
    if c == 26:
        return f"If you've had enough of the {badword()} and {badword()} in\r\nWashington, chip in here: http://p4a.us/Fox-Town-Hall"
    
def mayo(t=1):
    for i in range(t):
        print(f"{quote()}\r\n")
