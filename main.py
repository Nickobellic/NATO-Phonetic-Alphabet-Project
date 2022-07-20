import pandas

nato = pandas.read_csv('nato_phonetic_alphabet.csv')
dic = nato.to_dict()
correct_entry = True

nato_lett = [letter for letter in dic['letter'].values()]
nato_wor = [word for word in dic['code'].values()]

nato_dic = {b:a for (a,b) in zip(nato_wor,nato_lett)}

while correct_entry:
    n = input('Enter the Word: ').upper()
    try:
        t = [nato_dic[i] for i in n]
    except KeyError:
        print("Only Alphabets should be entered. Please try again")
    else:
        print(t)
        correct_entry = False