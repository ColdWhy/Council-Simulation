import random
from tabulate import tabulate
from collections import Counter

year = 1000

first_names = [
    "Alexander", "Victoria", "Sebastian", "Charlotte", "Theodore", "Genevieve", "Nathaniel", "Isabella",
    "Maximilian", "Evangeline", "Frederick", "Seraphina", "Harrison", "Anastasia", "Graham", "Catherine",
    "Benedict", "Arabella", "Phillip", "Vivienne", "Julian", "Elizabeth", "Charles", "Margot", "Edmund",
    "Josephine", "Nicholas", "Penelope", "Reginald", "Aurora", "Augustus", "Rosalind", "Quincy", "Florence",
    "Percival", "Beatrice", "Sullivan", "Daphne", "Chester", "Adelaide", "Everett", "Henrietta", "Tristan",
    "Cordelia", "Sterling", "Lydia", "Ambrose", "Eliza", "Dominic", "Lucinda", "Atticus", "Clementine",
    "Montgomery", "Eleanor", "Sinclair", "Helena", "Rupert", "Camilla", "Oliver", "Scarlett", "Laurence",
    "Celeste", "Winston", "Athena", "Fitzgerald", "Arabella", "Hugo", "Vivian", "Alistair", "Lucille",
    "Rafferty", "Delilah", "Dorian", "Francesca", "Emerson", "Amelia", "Cornelius", "Eloise", "Dominick",
    "Ophelia", "Tobias", "Madeleine", "Bartholomew", "Harriet", "Rowland", "Georgina", "Lysander", "Clarissa",
    "Bertram", "Hermione", "Giles", "Clara", "Dashiell", "Priscilla", "Lucian", "Winifred", "Tennyson",
    "Veronica", "Thaddeus", "Felicity", "Roderick", "Mirabelle", "Crispin", "Lavinia"
]

last_names = [
    "Abernathy", "Vanderbilt", "Winthrop", "Harrington", "Fitzwilliam", "Montague", "Kingsley", "Chamberlain",
    "Ashcroft", "Bradbury", "Whitmore", "Covington", "Beauregard", "Langley", "Wellington", "Fairchild",
    "Sterling", "Lockwood", "Kensington", "Abercrombie", "Blackwell", "Hawthorne", "Langford", "Sinclair",
    "Carnegie", "Winslow", "Fitzgerald", "Hamilton", "Beaumont", "Somerset", "Worthington", "Livingston",
    "Cunningham", "Thornhill", "Barington", "Huntington", "Prescott", "Baxter", "Delacroix", "Berkshire",
    "Valentine", "Sutherland", "Kensington", "Monroe", "Chatsworth", "Davenport", "Ellington", "Merriwether",
    "Gladstone", "Whitman", "Windsor", "Branford", "Rutherford", "Cromwell", "Montgomery", "Radcliffe",
    "Eastwood", "Langdon", "Pemberton", "Wentworth", "Silverstone", "Northcote", "Harrington", "Calloway",
    "Hartford", "Buckingham", "Shelburne", "Dunmore", "Tremaine", "Fairfax", "Hollingsworth", "Pembroke",
    "Addington", "Blanchard", "Savoy", "Marchbanks", "Kingsley", "Lancaster", "Beverly", "Fairbanks",
    "Buchanan", "Carrington", "Fitzpatrick", "Huntington", "Pendleton", "Cheswick", "Ashford", "Benedict",
    "Delafield", "Southwell", "Waterford", "Haverford", "Braxton", "Westcott", "Charleston", "Marchmont",
    "Beckett", "Warwick", "Aldrich", "Tennyson", "Whitlock", "Cornwall", "Thornton", "Holland", "Wortham"
]

# this is a flag that says if a new speaker or minister is necessary.
# it starts True because no one occupies those positions.
# ideally there be something checking this on the first loop
# but im too lazy for that so for now you'll have to manually switch
# these to True or False when you decide to start a simulation
# with a speaker or high minister.
new_speaker = True
new_minister = True

pool = []

for _ in range(300):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    pool.append(f'{first_name} {last_name}')


# there are 42 seats, an even number. the reason for that is because
# once a magister is elevated to minister they can no longer vote on bills.
#
# [name, years until replacement, are they speaker?, are they high minister?]

council = {
    'A1': ['Rohenna Geron', 10, '', ''],  # Replaced in 10 years
    'A2': ['', 10, '', ''],
    'A3': ['', 10, '', ''],
    'A4': ['', 10, '', ''],
    'A5': ['', 10, '', ''],

    'B1': ['', 9, '', ''],   # Replaced in 9 years
    'B2': ['', 9, '', ''],
    'B3': ['', 9, '', ''],
    'B4': ['', 9, '', ''],
    'B5': ['', 9, '', ''],

    'C1': ['', 8, '', ''],   # Replaced in 8 years
    'C2': ['', 8, '', ''],
    'C3': ['', 8, '', ''],
    'C4': ['', 8, '', ''],

    'D1': ['', 7, '', ''],   # Replaced in 7 years
    'D2': ['', 7, '', ''],
    'D3': ['', 7, '', ''],
    'D4': ['', 7, '', ''],

    'E1': ['', 6, '', ''],   # Replaced in 6 years
    'E2': ['', 6, '', ''],
    'E3': ['', 6, '', ''],
    'E4': ['', 6, '', ''],

    'F1': ['', 5, '', ''],   # Replaced in 5 years
    'F2': ['', 5, '', ''],
    'F3': ['', 5, '', ''],
    'F4': ['', 5, '', ''],

    'G1': ['', 4, '', ''],   # Replaced in 4 years
    'G2': ['', 4, '', ''],
    'G3': ['', 4, '', ''],
    'G4': ['', 4, '', ''],

    'H1': ['', 3, '', ''],   # Replaced in 3 years
    'H2': ['', 3, '', ''],
    'H3': ['', 3, '', ''],
    'H4': ['', 3, '', ''],

    'I1': ['', 2, '', ''],   # Replaced in 2 years
    'I2': ['', 2, '', ''],
    'I3': ['', 2, '', ''],
    'I4': ['', 2, '', ''],

    'J1': ['', 1, '', ''],   # Replaced in 1 year
    'J2': ['', 1, '', ''],
    'J3': ['', 1, '', ''],
    'J4': ['', 1, '', ''],
}


# this vote is called when the term of the speaker ends.
# the high council is asked if they should be allowed another
# term to keep serving as speaker.
#
# although the High Minister usually cannot vote, an exception
# is created here to avoid a tie.

def speakerVote(speaker, speaker_name):
    speaker_vote_result = []

    for magister in council:
        if magister == speaker:
            continue

        # they have a 55% chance of voting to keep the speaker
        vote_rng = random.randint(1, 100)

        if vote_rng <= 55:
            vote = 'Y'
        else:
            vote = 'N'

        speaker_vote_result.append([
            magister,
            council[magister][0],
            vote
        ])

    print(
        f'\nShould {speaker_name} serve another term '
        f'in the council and remain the speaker?'
    )

    print(
        tabulate(
            speaker_vote_result,
            headers=['Seat', 'Name', 'Vote'],
            tablefmt='simple'
        )
    )

    vote_counts = Counter(
        [vote for _, _, vote in speaker_vote_result]
    )

    print(f"\nYes: {vote_counts['Y']}")
    print(f"No: {vote_counts['N']}")

    if vote_counts['Y'] > vote_counts['N']:
        return "Yes"
    else:
        return "No"


# this vote is called when the term of the high minister ends.
# the high council is asked if they should be allowed another
# term to keep serving as high minister.

def ministerVote(minister, minister_name):
    minister_vote_result = []

    for magister in council:
        if magister == minister:
            continue

        # they have a 55% chance of voting to keep the high minister
        vote_rng = random.randint(1, 100)

        if vote_rng <= 55:
            vote = 'Y'
        else:
            vote = 'N'

        minister_vote_result.append([
            magister,
            council[magister][0],
            vote
        ])

    print(
        f'\nShould {minister_name} serve another term '
        f'in the council and remain the High Minister?'
    )

    print(
        tabulate(
            minister_vote_result,
            headers=['Seat', 'Name', 'Vote'],
            tablefmt='simple'
        )
    )

    vote_counts = Counter(
        [vote for _, _, vote in minister_vote_result]
    )

    print(f"\nYes: {vote_counts['Y']}")
    print(f"No: {vote_counts['N']}")

    if vote_counts['Y'] > vote_counts['N']:
        return "Yes"
    else:
        return "No"


# this is a placeholder. ideally the magisters would hold a vote
# to decide the speaker/high minister.

def newSpeaker():
    while True:
        speaker_seat = random.choice(list(council.keys()))

        if council[speaker_seat][3] == 'X':
            continue
        else:
            break

    council[speaker_seat][2] = 'X'

    print(
        f'\n{council[speaker_seat][0]} '
        f'was chosen as the new Speaker.'
    )


def newMinister():
    while True:
        minister_seat = random.choice(list(council.keys()))

        if council[minister_seat][2] == 'X':
            continue
        else:
            break

    council[minister_seat][3] = 'X'

    print(
        f'\n{council[minister_seat][0]} '
        f'was chosen as the new High Minister.'
    )


while True:

    # ------- manages the length of magisters' terms

    for magister, details in council.items():

        if (
            details[1] == 1
            and details[2] == ''
            and details[3] == ''
        ):

            if details[0] != '':
                pool.append(details[0])

            pick = random.randint(0, len(pool) - 1)

            details[0] = pool[pick]
            pool.pop(pick)

            details[1] = 10

        elif details[0] == '':

            pick = random.randint(0, len(pool) - 1)

            details[0] = pool[pick]
            pool.pop(pick)

            if details[1] <= 5:
                details[1] += 10
                details[1] -= 1
            else:
                details[1] -= 1

        # ---------

        # Speaker vote

        elif details[1] == 1 and details[2] == 'X':

            vote_result = speakerVote(
                magister,
                details[0]
            )

            if vote_result == "Yes":

                details[1] = 10

            else:

                pool.append(details[0])

                pick = random.randint(0, len(pool) - 1)

                details[0] = pool[pick]
                details[2] = ''

                pool.pop(pick)

                new_speaker = True
                details[1] = 10

        # High minister vote

        elif details[1] == 1 and details[3] == 'X':

            vote_result = ministerVote(
                magister,
                details[0]
            )

            if vote_result == "Yes":

                details[1] = 10

            else:

                pool.append(details[0])

                pick = random.randint(0, len(pool) - 1)

                details[0] = pool[pick]
                details[3] = ''

                pool.pop(pick)

                new_minister = True
                details[1] = 10

        else:
            details[1] -= 1

    if new_speaker:
        newSpeaker()
        new_speaker = False

    if new_minister:
        newMinister()
        new_minister = False

    council_list = [
        [
            seat,
            details[0],
            details[1],
            details[2],
            details[3]
        ]
        for seat, details in council.items()
    ]

    print(f'\n')
    print(f'Year {year}')

    print(
        tabulate(
            council_list,
            headers=[
                'Seat',
                'Name',
                'Years left',
                'Speaker',
                'High minister'
            ],
            tablefmt='simple'
        )
    )

    print(f'\n')

    loop_end = input(
        f'Press 0 to stop. Press anything to continue: '
    )

    if loop_end == '0':
        break
    else:
        year += 1
        continue