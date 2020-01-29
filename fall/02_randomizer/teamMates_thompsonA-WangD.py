import random
KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa','Eric','ray','Jesse','Tiffany','Amanda',
    'Junhee','Jackie','Tyler','Emory','Ivan','Elizabeth','Pratham','Shaw','Eric',
    'Yaru','Kelvin','Hong Wei','Michael','Kiran','Amanda','Joseph','Tanzim','David',
    'Yevgeniy'],

    'rex': ['William','Joseph','Calvin','Ethan','Moody','Mo','Big Mo', 'Peihua',
    'Saad','Benjamin','Justin', 'Alice','Hilary','Ayham','Michael','Matthew','Jionghao',
    'Devin','David','Jacob','Will','Hannah','Alex'],

    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor','Jason','Tammy','Albert',
    'Kazi','Derek','Brandon','Kenneth','Lauren','Biraj','Jeff','Jackson','Taejoon',
    'Kevin','Jude','Sophia','Henry','Coby','Manfred','Leia','Ahmed','Winston']
}

def randName():
    x = random.randint(0, 3)
    if (x == 0): team = 'orpheus'
    if (x == 1): team = 'rex'
    if (x == 2): team = 'endymion'
    print(KREWES[team][random.randint(0, len(KREWES[team]))]);

randName()
