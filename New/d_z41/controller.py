from vewiy import UserInterfase
from model import AticalModel

class Controller:
    def __init__(self):
        self.aticalc_model = AticalModel() # model
        self.user_interfase =UserInterfase() # view

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interfase.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer =="1":
            atical = self.user_interfase.add_user_aticals()
            self.aticalc_model.add_atical(atical)
        elif answer =='2':
            aticals = self.aticalc_model.get_all_aticals()
            self.user_interfase.show_all_aticals(aticals)
        elif answer == '3':
            atical_title = self.user_interfase.get_user_atical()
            try:
                atical = self.aticalc_model.get_single_atical(atical_title)
            except KeyError:
                self.user_interfase.show_incorrect_title_error(atical_title)
            else:
                self.user_interfase.show_single_atical(atical)
        elif answer == '4':
            atical_title = self.user_interfase.get_user_atical()
            try:
                title = self.aticalc_model.remuve_atical(atical_title)
            except KeyError:
                self.user_interfase.show_incorrect_title_error(atical_title)
            else:
                self.user_interfase.remove_single_atical(title)
        elif answer =="q":
            self.aticalc_model.save_data()
        else:
            self.user_interfase.show_incorrect_answer_error(answer)