# ==============================================================================
#
# Day 1 - Inverse Captcha
#
# Part 1: The captcha requires you to review a sequence of digits (your puzzle
# input) and find the sum of all digits that match the next digit in the list.
# The list is circular, so the digit after the last digit is the first digit
# in the list.
#
# Examples:
# 1122 produces a sum of 3 (1 + 2) because the first digit (1)
# matches the second digit and the third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches
# the next one is the last digit, 9.
#
# Part 2: Now, instead of considering the next digit, it wants you to consider
# the digit halfway around the circular list. That is, if your list contains 10
# items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.
#
# Examples:
# 1212 produces 6: the list contains 4 items, and all four digits
# match the digit 2 items ahead.
# 1221 produces 0, because every comparison is between a 1 and a 2.
# 123425 produces 4, because both 2s match each other, but no other
# digit has a match.
# 123123 produces 12.
# 12131415 produces 4.
# ==============================================================================

__author__ = 'Duyen Nguyen'

SAMPLE_INPUT = '9513446799636685297929646689682997114316733445451534532351778' \
               '5342514271721681836218746417115349172916743338574237993755126' \
               '2848942333229753821585517659263369263197482225916176623838592' \
               '2277893623911332569448978771948316155868781496698895492971356' \
               '3839969328855187329976242536786942796665721498316163124979948' \
               '5628887158677779345992695249131833699715955371458454189729411' \
               '7487641872629796825583725975692264125865827534677223541484795' \
               '8773719551244639892288864986824215396672249637836162456468321' \
               '5438475666325148766868142575453672282756365132752467418344369' \
               '6227523828832466473538347472991998913211857749878157579176457' \
               '3953756329955765693884558881564654517236937678876813925471892' \
               '7339194863272649986831374726182818673298662836577372858338718' \
               '4112323696592536446536231376615949825166773536471531487969852' \
               '5356997741131636672865371937675151193628651419256128494439834' \
               '8424526819484256315456763835464573533185589615514274166424671' \
               '5666899824364722914296492444672653852387389477634257768229772' \
               '3994165211986253934264434992236118437661348834412233282568834' \
               '9742332475322939239397462218142991353597332732395224167497967' \
               '7481518733692544535323219895684629719868384266425386835539719' \
               '2377163391984851639165624348545793659581119313545769915587712' \
               '3697724266875678213996163834725164482872478682775174839912366' \
               '8854393894787851872256667336215726674348886747128237416273154' \
               '9886192678243612278887515624456223876952181613418847567952234' \
               '6475186296565555914377942528315453325257394916549213817558161' \
               '5176611845489857169132936848668646319955661492488428427435269' \
               '1691736548121148425683816369823892242364556333168981781632974' \
               '5245329666766184962217454177866949438816745118635248855537958' \
               '1934999276412919598411422973399319799937518713422398874326665' \
               '3752164372464457916232838985846482789896744182421129576683974' \
               '8467111976155384727579987349536375926629647784415723742323916' \
               '3559391553961176475377151369399646747881452252547741718734949' \
               '9677525647741613417848335214924942436626584711213696496418155' \
               '6232769839529357399164835136976716264276347556154479598218371' \
               '4447737149239846151871434656618825566387329765118727515699213' \
               '9624779963997816521319189964341255596984279457145724883763421' \
               '26989157872118279163127742349'


def get_sequence():
    user_input = raw_input('Please provide a sequence of digits to perform '
                           'captcha summation on or "done" to exit: ')
    if user_input == 'done':
        return None
    else:
        try:
            int(user_input)
            return user_input
        except ValueError:
            print('Invalid input "{}". '
                  'Must be a sequence of digits.').format(user_input)
            return get_sequence()


def get_captcha_check():
    user_input = raw_input('Which captcha would you like to run? '
                           'Options are 1 or 2: ')
    if user_input not in ['1', '2']:
        print('Invalid input "{}". Must be 1 or 2.').format(user_input)
        return get_captcha_check()
    return int(user_input)

def calculate_captcha_summation(sequence, captcha_type):
    sum = 0
    if captcha_type == 1:
        prev_char = None
        for char in sequence:
            if prev_char:
                sum += int(char) if prev_char == char else 0
            prev_char = char
        sum += int(sequence[-1]) if sequence[0] == sequence[-1] else 0
    if captcha_type == 2:
        sequence_length = len(sequence) # assumed to be positive
        for i in range(sequence_length):
            if i < sequence_length/2:
                chars_to_compare = sequence[i::sequence_length/2]
            else:
                chars_to_compare = sequence[i::-sequence_length/2]
            sum += int(chars_to_compare[0])\
                if chars_to_compare[0] == chars_to_compare[1]\
                else 0

    return sum


if __name__ == '__main__':
    sequence = get_sequence()
    while sequence:
        captcha_type = get_captcha_check()
        print 'Captcha summation of is {}.'\
            .format(calculate_captcha_summation(sequence, captcha_type))
        sequence = get_sequence()
