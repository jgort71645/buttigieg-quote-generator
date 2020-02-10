import numpy as np

def buzzword():
    buzzwords = ["hope",
                 "vision",
                 "democracy",
                 "issue",
                 "service",
                 "values",
                 "faith",
                 "election",
                 "purpose",
                 "nation",
                 "presidency",
                 "equality",
                 "family",
                 "community",
                 "neighborhood",
                 "policy",
                 "voice",
                 "mental health",
                 "workplace",
                 "movement",
                 "economy",
                 "unity",
                 "belonging",
                 "life",
                 "politics",
                 "health",
                 "people",
                 "unification",
                 "empowerment",
                 "glorification",
                 "president",
                 "choice",
                 "path",
                 "leadership",
                 "bold ideas",
                 "difference",
                 "action",
                 "answers",
                 "resilience",
                 "message",
                 "future",
                 "addition",
                 "boldness",
                 "big things",
                 "solutions",
                 "wine cave",
                 "dream",
                 "justice",
                 "prosperity",
                 "citizenship"
                 ]
    N = len(buzzwords)
    c = int(np.floor(N*np.random.uniform()))
    return buzzwords[c]

def badword():
    badwords = ["division",
                "voter suppression",
                "gerrymandering",
                "white supremacy",
                "gun violence",
                "prejudice",
                "fear",
                "HIV/AIDS",
                "challenge",
                "broken policies",
                "broken politics",
                "exhaustion",
                "cynicism",
                "exclusion",
                "desolation",
                "rat poison",
                "interference",
                "rejection",
                "exclusion",
                "dysfunction",
                "corruption",
                "injustice",
                "hopelessness",
                "polarization",
                "climate change"
                ]
    N = len(badwords)
    c = int(np.floor(N*np.random.uniform()))
    return badwords[c]

def buzzverb():
    buzzverbs = ["galvanize",
                 "inspire",
                 "unite",
                 "embolden",
                 "govern",
                 "win",
                 "rally"
                 ]
    N = len(buzzverbs)
    c = int(np.floor(N*np.random.uniform()))
    return buzzverbs[c]

def badverb():
    badverbs = ["polarize",
                "divide"
                ]
    N = len(badverbs)
    c = int(np.floor(N*np.random.uniform()))
    return badverbs[c]
    
def quote():
    N = 27
    c = np.ceil(N*np.random.uniform())
    quotes = [(f"I believe the {buzzword()} belongs to people of {buzzword()} and no {buzzword()}\r\n"
               +f"at all. I also believe that people of {buzzword()} have a choice to make when it\r\n"
               +f"comes to this {buzzword()}."),
              
              (f"Our {buzzword()}s are being threatened by foreign {badword()}--and\r\n"
               +f"{badword()} here at home. {badword().capitalize()} is {badword()}.\r\n"
               +f"Racial {badword()} is {badword()}.\r\n"
               +f"We need a 21st Century Voting Rights Act."),
              
              (f"{buzzword().capitalize()} struggles affect every {buzzword()}, every {buzzword()},\r\n"
               +f"every {buzzword()}, every {buzzword()}.\r\n"
               +f"I will be a president who not only works to get the {buzzword()} right,\r\n"
               +f"but gives {buzzword()} to those struggles."),
              
              f"This is an extraordinary moment for the {buzzword()} we're building.",
              
              (f"Trayvon Martin would have been 25 today.\r\n"
               +f"How many 25th birthdays have been stolen from us by\r\n"
               +f"{badword()}, {badword()}, {badword()}, and {badword()}?"),
              
              f"(Incoherent rat noises)",
              
              (f"I believe in American {buzzword()}.\r\n"
               +f"I believe in American {buzzword()}."),
              
              f"I believe the {buzzword()} has a {buzzword()}.",
              
              (f"If you're ready to build an American {buzzword()} defined by {buzzword()},\r\n"
               +f"this is our chance.\r\n"
               +f"If you're ready to build an American {buzzword()} defined by {buzzword()},\r\n"
               +f"this is our chance."),
              
              (f"Your {buzzword()} should never be determined by who you are, what you \r\n"
               +f"look like, or whom you love. Yet Black Americans are disproportionately\r\n"
               +f"affected by {badword()}. It's unacceptable.\r\n"
               +f"My White House will commit to ending the {badword()} epidemic by 2030."),
              
              (f"If you're ready to build an American {buzzword()} defined by {buzzword()} in the\r\n"
               +f"face of our greatest {badword()}, this is our chance."),
              
              (f"The {buzzword()} of the {buzzword()} is not the {buzzword()} of the {buzzword()},\r\n"
               +f"it is the {buzzword()} and {buzzword()} of the {buzzword()}."),
              
              (f"You chose to move on not just from the {badword()} of the last few years,\r\n"
               +f"but the {badword()} that got us here. Tomorrow, because of what we\r\n"
               +f"did here, the {buzzword()} will have that {buzzword()} too."),
              
              f"Tonight, Iowa chose a new {buzzword()}.",
              
              (f"We could see an American majority yearning for {buzzword()} to rally us\r\n"
               +f"together behind {buzzword()} that would make {buzzword()} in our lives."),
              
              (f"We had the belief that in the face of {badword()}, {badword()}, and\r\n"
               +f"{badword()}--in spite of every trampled norm and poisonous tweet,\r\n"
               +f"that a rising majority of Americans was hungry for {buzzword()}\r\n"
               +f"and ready for new {buzzword()}."),
              
              (f"I joined this race a year ago seeing how the last presidential\r\n"
               +f"election led to {badword()} and {badword()}. But after\r\n"
               +f"spending months on the trail bringing our {buzzword()} to millions,\r\n"
               +f"I saw firsthand the {buzzword()} of American families and the\r\n"
               +f"{buzzword()} they carry for the {buzzword()}."),
              
              (f"Americans are hungry for a {buzzword()} and a {buzzword()}\r\n"
               +f"that will rally us all around a shared {buzzword()} for the\r\n"
               +f"{buzzword()}--one defined not by {badword()} but by {buzzword()}."),
              
              (f"The {buzzword()} of our {buzzword()} is the {buzzword()} that affects every\r\n"
               +f"other {buzzword()}."),
              
              (f"I will not pursue {buzzword()} by telling people they can't be at\r\n"
               +f"our side if they're not with us 100% of the time.\r\n"
               +f"This is a time for {buzzword()}, not {badword()},\r\n"
               +f"for {buzzword()}, not {badword()}."),
              
              (f"I'm not interested in labels. I'm interested in the style of\r\n"
                +f"{buzzword()} that we need to put forward to finally turn the page."),
              
              (f"Not just in order to {buzzverb()}, but in order to {buzzverb()}.\r\n"
                +f"The next president will face unprecedented {badword()}s that require\r\n"
                +f"bringing the American people together."),
              
              (f"It's time to {buzzverb()}--not {badverb()}--the American people around\r\n"
                +f"{buzzword()} and actually get things done."),
              
              (f"I'm seeing a hunger for {buzzword()} oriented toward the {buzzword()}.\r\n"
                +f"It's time to believe we can {buzzverb()}.\r\nIt's time to turn the page."),
              (f"I'm running to be a president who will help Americans believe we can get\r\n"
                +f"{buzzword()} done together."),
              
              (f"If you've had enough of the {badword()} and {badword()} in Washington,\r\n"
                +f"chip in here: https://www.webstaurantstore.com/49839/mayonnaise.html"),
              (f"My {buzzword()} will {buzzverb()} Americans with {buzzword()},\r\n"
                +f"not {badverb()} Americans with {badword()}."),
              
              f"{buzzword().capitalize()} guarantees {buzzword()}.\r\nWould you like to know more?",
              
              (f"If you believe in an American {buzzword()} defined by {buzzword()}...\r\n"
               +f"{buzzword()}...{buzzword()}, this is our chance. New Hampshire,\r\n"
               +f"let's make history and go on to defeat Donald Trump in November."),
              
              (f"We can't write people off because of who they used to vote for or\r\n"
               +f"if they don't agree with us 100% of the time.\r\n"
               +f"{buzzword().capitalize()} isn't just what we need, it's how we {buzzverb()}."),
              
              (f"During tonight's #DemDebate, I made the case for breaking with the\r\n"
               +f"{buzzword()} of the past and delivering a better {buzzword()}\r\n"
               +f"before it's too late. If you're with me, join me vote for me, and chip in."),

              (f"Fast fact for your caucus conversations: Pete Buttigieg can {buzzverb()}\r\n"
               +f"Americans together to achieve {buzzword()}."),

              (f"Fast fact for your caucus conversations: Pete Buttigieg will turn the\r\n"
               +f"page on Washington {badword()}.")
              ]
    N = len(quotes)
    c = int(np.floor(N*np.random.uniform()))
    return quotes[c]
    
def mayo(t=1):
    for i in range(t):
        print(f"{quote()}\r\n")

print("Welcome to the Pete Buttigieg Quote Generator!\r\n")
print("To generate a Pete Buttigieg campaign quote, please type mayo().")
print("Typing mayo(N) will generate N campaign quotes for your enjoyment!\r\n")
