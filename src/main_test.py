from objects.inputer import NewMC, NewFT


def main():
    question_main = NewMC(question='Use setting stored in profile?', true_ans={'Y': 'yes', 'N': 'no'}).ask()
    if question_main == 'N':
        questions = []
        questions.append(NewMC(question='Filter by property type:', true_ans={'A': 'house', 'B': 'condo (PH)', 'C': 'department', '0': 'don\'t filter'}).ask())
        questions.append(NewMC(question='Filter by operation type:', true_ans={'A': 'rent', 'B': 'buy', '0': 'don\'t filter'}).ask())
        questions.append(NewFT(question='Filter by room quantity. Options are:', prompt=' ■ Specific quantities: 1,2,4\n ■ Range: 1-3\n ■ 0: don\'t filter\nNote: available options go from 1 to 6, 6 meaning 5+.', validate=r'[-,0-9]+').ask())
        tmp_q_1 = NewMC(question='Filter by price range (first select currency, then range):', true_ans={'A': '$ (Arg peso)', 'B': 'U$S (US dollar)', '0': 'don\'t filter'}).ask()
        if tmp_q_1 in ['A', 'B']:
            questions.append(tmp_q_1)
            tmp_q_2 = NewFT(question='Indicate price range. Options are:', prompt=' ■ min,max: you want a minimum and a maximum\n ■ 0,max: you want a maximum but no minimum\n ■ min,0: you want a minimum but no maximum', validate=r'[,0-9]+').ask()
            if tmp_q_2 != '0':
                questions.append(tmp_q_2)
            else:
                questions[3] = '0'
                questions.append('0')
        else:
            questions.append('0')
            questions.append('0')
        questions.append(NewMC(question='Filter by primary location (city):', true_ans={'A': 'capital federal', 'B': 'gran buenos aires norte', 'C': 'gran buenos aires sur', 'D': 'gran buenos aires oeste', '0': 'don\'t filter'}).ask())
        questions.append(NewFT(question='Filter by secondary location (neighborhood):', prompt='Enter locations comma-separated. Use 0+enter if you don\'t want to filter by location').ask())

        print(questions)


if __name__ == "__main__":
    main()

