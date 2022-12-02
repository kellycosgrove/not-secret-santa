# libraries
import random
import logging

# logging

logging.basicConfig(filename='secret_santa.log', filemode='w', format='%(levelname)s:%(message)s', level=logging.DEBUG)

# global vars

HOUSEHOLD_PAIRS = False


# functions
def get_names():
    global HOUSEHOLD_PAIRS
    _out_name_list = []
    hh = input("Would you like to allow same-household pairings? [Y/N]: ")
    if hh == "Y":
        HOUSEHOLD_PAIRS = True
    while True:
        nm = input("Insert name, or press enter if done: ")
        if nm == "":
            break
        if HOUSEHOLD_PAIRS == True:
            addr = ""
        else:
            addr = input(f"Great! Where does {nm} live? ")
        _out_name_list.append((nm, addr))
    logging.info('Names list: ' + str(_out_name_list))
    return _out_name_list


def generate_pair_list(_in_name_list):
    list_len = len(_in_name_list)
    _out_pair_list = random.sample(range(0, list_len), list_len)
    return _out_pair_list


def match_names(_in_name_list):
    unique_pairs = False
    while unique_pairs == False:
        pair_list = generate_pair_list(_in_name_list)
        unique_pairs = True
        for i in range(len(pair_list)):
            if (i == pair_list[i]) or ((_in_name_list[i][1] == _in_name_list[pair_list[i]][1]) and not HOUSEHOLD_PAIRS):
                unique_pairs = False
    logging.info('Pair indices: ' + str(pair_list))
    _out_names_dict = {}
    for i in range(len(_in_name_list)):
        _out_names_dict[_in_name_list[i]] = _in_name_list[pair_list[i]]
    logging.info('Secret Santa dictionary: ' + str(_out_names_dict))
    return _out_names_dict


def announce_pairs(_in_ss_pairs):
    for key in _in_ss_pairs:
        print(key[0] + ' is buying for ' + _in_ss_pairs[key][0])


if __name__ == '__main__':
    reroll = True

    name_list = get_names()
    while reroll:
        ss_pairs = match_names(name_list)
        announce_pairs(ss_pairs)
        rr = input("Reroll? [Y/N]: ")
        if rr == "N":
            reroll = False
