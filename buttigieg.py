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
    N = 21
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
    if c == 21:
        return "corruption"

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
        return (f"I believe the {buzzword()} belongs to people of {buzzword()} and no {buzzword()}\r\n"
                +f"at all. I also believe that people of {buzzword()} have a choice to make when it\r\n"
                +f"comes to this {buzzword()}.")
    if c == 2:
        return (f"Our {buzzword()}s are being threatened by foreign {badword()}--and\r\n"
                +f"{badword()} here at home. {badword().capitalize()} is {badword()}.\r\n"
                +f"Racial {badword()} is {badword()}.\r\n"
                +f"We need a 21st Century Voting Rights Act.")
    if c == 3:
        return (f"{buzzword().capitalize()} struggles affect every {buzzword()}, every {buzzword()},\r\n"
                +f"every {buzzword()}, every {buzzword()}.\r\n"
                +f"I will be a president who not only works to get the {buzzword()} right,\r\n"
                +f"but gives {buzzword()} to those struggles")
    if c == 4:
        return f"This is an extraordinary moment for the {buzzword()} we're building."
    if c == 5:
        return (f"Trayvon Martin would have been 25 today.\r\n"
                +f"How many 25th birthdays have been stolen from us by\r\n"
                +f"{badword()}, {badword()}, {badword()}, and {badword()}?")
    if c == 6:
        return f"(Incoherent rat noises)"
    if c == 7:
        return (f"I believe in American {buzzword()}.\r\n"
                +f"I believe in American {buzzword()}.")
    if c == 8:
        return f"I believe the {buzzword()} has a {buzzword()}."
    if c == 9:
        return (f"If you're ready to build an American {buzzword()} defined by {buzzword()},\r\n"
                +f"this is our chance.\r\n"
                +f"If you're ready to build an American {buzzword()} defined by {buzzword()},\r\n"
                +f"this is our chance.")
    if c == 10:
        return (f"Your {buzzword()} should never be determined by who you are, what you look like,\r\n"
                +f"or whom you love. Yet Black Americans are disproportionately affected\r\n"
                +f"by {badword()}. It's unacceptable.\r\n"
                +f"My White House will commit to ending the {badword()} epidemic by 2030.")
    if c == 11:
        return (f"If you're ready to build an American {buzzword()} defined by {buzzword()} in the\r\n"
                +f"face of our greatest {badword()}, this is our chance.")
    if c == 12:
        return (f"The {buzzword()} of the {buzzword()} is not the {buzzword()} of the {buzzword()},\r\n"
                +f"it is the {buzzword()} and {buzzword()} of the {buzzword()}.")
    if c == 13:
        return (f"You chose to move on not just from the {badword()} of the last few years,\r\n"
                +f"but the {badword()} that got us here. Tomorrow, because of what we\r\n"
                +f"did here, the {buzzword()} will have that {buzzword()} too.")
    if c == 14:
        return f"Tonight, Iowa chose a new {buzzword()}."
    if c == 15:
        return (f"We could see an American majority yearning for {buzzword()} to rally us\r\n"
                +f"together behind {buzzword()} that would make {buzzword()} in our lives.")
    if c == 16:
        return (f"We had the belief that in the face of {badword()}, {badword()}, and\r\n"
                +f"{badword()}--in spite of every trampled norm and poisonous tweet,\r\n"
                +f"that a rising majority of Americans was hungry for {buzzword()}\r\n"
                +f"and ready for new {buzzword()}.")
    if c == 17:
        return (f"I joined this race a year ago seeing how the last presidential\r\n"
                +f"election led to {badword()} and {badword()}. But after\r\n"
                +f"spending months on the trail bringing our {buzzword()} to millions,\r\n"
                +f"I saw firsthand the {buzzword()} of American families and the\r\n"
                +f"{buzzword()} they carry for the {buzzword()}.")
    if c == 18:
        return (f"Americans are hungry for a {buzzword()} and a {buzzword()}\r\n"
                +f"that will rally us all around a shared {buzzword()} for the\r\n"
                +f"{buzzword()}--one defined not by {badword()} but by {buzzword()}.")
    if c == 19:
        return (f"The {buzzword()} of our {buzzword()} is the {buzzword()} that affects every\r\n"
                +f"other {buzzword()}.")
    if c == 20:
        return (f"I will not pursue {buzzword()} by telling people they can't be at\r\n"
                +f"our side if they're not with us 100% of the time.\r\n"
                +f"This is a time for {buzzword()}, not {badword()}, for {buzzword()}, not {badword()}.")
    if c == 21:
        return (f"I'm not interested in labels. I'm interested in the style of\r\n"
                +f"{buzzword()} that we need to put forward to finally turn the page.")
    if c == 22:
        return (f"Not just in order to {buzzverb()}, but in order to {buzzverb()}.\r\n"
                +f"The next president will face unprecedented {badword()}s that require\r\n"
                +f"bringing the American people together.")
    if c == 23:
        return (f"It's time to {buzzverb()}--not {badverb()}--the American people around\r\n"
                +f"{buzzword()} and actually get things done.")
    if c == 24:
        return (f"I'm seeing a hunger for {buzzword()} oriented toward the {buzzword()}.\r\n"
                +f"It's time to believe we can {buzzverb()}.\r\nIt's time to turn the page.")
    if c == 25:
        return (f"I'm running to be a president who will help Americans believe we can get\r\n"
                +f"{buzzword()} done together.")
    if c == 26:
        return (f"If you've had enough of the {badword()} and {badword()} in Washington,\r\n"
                +f"chip in here: https://www.webstaurantstore.com/49839/mayonnaise.html")
    
def mayo(t=1):
    for i in range(t):
        print(f"{quote()}\r\n")
