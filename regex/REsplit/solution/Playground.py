'''
https://docs.python.org/3/library/re.html
https://docs.python.org/3.4/library/re.html
https://www.tutorialspoint.com/python3/python_reg_expressions.htm
'''

from re import match, I, M, X, search


# (pattern, string, flags)


def match_w_flags(pattern, _str, flags = 0):
    return match(pattern, _str, flags)


def search_w_flags(pattern, _str, flags = 0):
    return search(pattern, _str, flags)


def run_fn_match_wt_flags():
    strs = ["google"
        , "go0gle"
        , "gO0gle"
        , "GO0gl3"
        , "GO0g13"
        , "gO0g13"
        , "guogle"
        , "Googl1"
        , "G<><>gle"
        , "G<>0gle"
        , "G<>Ogle"
        , "G<>ogle"
        , "GO<>gle"
        , "G0()gle"
        , "G()()gle"
        , "G00gle"
        , "G0[]gle"
        , "G[][]gle"
        , "G[][]gl3"
        , "G[][]gL3"
        , "G[][]G13"
        , "G[][]Gi3"
            ]
    pattern = '([gG])([oO0]|\\(\\)|\\[\\]|\\<\\>){2}([gG])([lL1])([eE3])'
    for s in strs:
        print("%s -> %s" % (s, match_w_flags(pattern, s)))

'''
Diferenca entre a funcao match e search

A funcao match procura pelo padrao a partir do começo da string, se nao
encontra-lo no inicio nao a correspondencia. Ja a funcao search procura pelo padrao
por toda string, como o funcionamento padrao na linguagem Pearl

print(match_w_flags(r'chris', "Lucas christoffer", I)) -> None
print(search_w_flags(r'chris', "Lucas christoffer", I)) -> <_sre.SRE_Match object; span=(6, 11), match='chris'>
'''


def run_test_fn_match_w_flags():
    #print(match("\\s+", "       "))
    #print(match("\\s+", ""))
    #print(match("\\s+", " "))
    #print(match_w_flags(r'chris', "Lucas, Fernandes ChRiStoffer", I))
    #print(match_w_flags(r'chris', "christoffer", I))
    print(match_w_flags(r'chris', "Lucas christoffer", I))
    #print(match_w_flags(r'chris', "ChRiStoffer", I))
    #matches_obj = match_w_flags(r'chris', "ChRiStoffer\nChristofferson", I | M | X)
    #print(matches_obj)


def test_search_w_flags():
    print(search_w_flags('(.*) are (.*?) .*', "you are a dumb"))
    print(search_w_flags(r'chris', "Lucas christoffer", I))
    print(search_w_flags(r'chris', "Lucas, Fernandes ChRiStoffer", I))
    print(search_w_flags(r'chris', "Lucas, Fernandes ChRiStoffer"))
    print(search_w_flags("chris", "ChRisToFfus"))
    print(search_w_flags("chris", "ChRisToFfus", I))
    print(search_w_flags("chris", "Lucas Chriss", I))


if __name__ == '__main__':
    run_test_fn_match_w_flags()
    print("")
    test_search_w_flags()
