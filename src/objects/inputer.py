import re


class _FgColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    WHITE = '\033[38m'
    RESET = '\033[0m'


# esta seria la super clase de la cual MC (multiple choice) y FT (free text) heredarian
class NewQuestion:
    def __init__(self, question: str, prompt: str = ''):
        self.question = question + '\n'
        self.prompt = prompt

    def _print(self, text: str = '', color: str = '') -> None:
        try:
            print(getattr(_FgColors, color) + text + _FgColors.RESET)
        except AttributeError:
            print(_FgColors.RESET)
            print('No color named {}'.format(color))

    def _input(self, text_lst: list, color_lst: list) -> str:
        try:
            text = [getattr(_FgColors, color_lst[i]) + text_lst[i] + _FgColors.RESET for i in range(len(text_lst))]
        except IndexError as e:
            print('Exception raised ({}) because "text_lst" items are more than "color_lst" items'.format(e))
            exit()
        except AttributeError as e:
            print(_FgColors.RESET)
            print('Exception raised ({}) because you declared a color that does not exist'.format(e))
            exit()
        return str.upper(input(''.join(text)))


class NewMC(NewQuestion):
    def __init__(self, question: str, true_ans: dict, prompt: str = '', trials_max: int = 3):
        NewQuestion.__init__(self, question, prompt)
        self.true_ans = true_ans
        self.trials_max = trials_max

    def ask(self):
        if not self.prompt:
            _prompt = ''.join(
                [' ■ ' + str(key) + ': ' + str(self.true_ans[key]) + '\n' for key in self.true_ans.keys()])
        else:
            _prompt = self.prompt + '\n'
        user_ans = ''
        trials_cnt = 0
        while user_ans not in self.true_ans.keys() and trials_cnt < self.trials_max:
            user_ans = super()._input([self.question, _prompt, '\t-- your choice: '], ['BLUE', 'BLUE', 'RED'])
            print('\n')
            trials_cnt += 1
        if user_ans in self.true_ans.keys():
            return user_ans
        else:
            return ''


class NewFT(NewQuestion):
    def __init__(self, question: str, prompt: str = '', validate: str = r'[ ,A-Za-z0-9]+'):
        NewQuestion.__init__(self, question, prompt)
        self.validate = validate  # seria una regex para validar el texto ingresado

    def _fix(self, text: str):
        text = text.replace(', ', ',')
        text = text.replace(' ,', ',')
        text = text.replace(' ', '-')
        text = text.replace('Á', 'A')
        text = text.replace('É', 'E')
        text = text.replace('Í', 'I')
        text = text.replace('Ó', 'O')
        text = text.replace('Ú', 'U')
        return text

    def ask(self):
        if not self.prompt:
            _prompt = 'Enter some free text as answer (or 0 + enter as an escape)\n'
        else:
            _prompt = self.prompt + '\n'
        pattern = re.compile(self.validate)
        user_ans = super()._input([self.question, _prompt, '\t-- your choice: '], ['BLUE', 'BLUE', 'RED'])
        user_ans = self._fix(user_ans)
        if not re.fullmatch(pattern, user_ans):
            user_ans = '0'
            print('Your input doesn\'t match validation (' + self.validate + '). Filter ignored.')
        print('\n')
        return user_ans
