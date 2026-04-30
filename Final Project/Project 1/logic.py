# Caelan Charleston & Evan Rathke
from PyQt6.QtWidgets import *
from gui import *
import sys
import csv

class Logic(QMainWindow, Ui_MainWindow):
    """
    Class containing logic for the Voting tool GUI
    """
    def __init__(self) -> None:
        """
        Method to initialize the window, establish variables, and toggle off Candidate Menu
        """
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(700, 600)
        self.button_vote.clicked.connect(lambda: self.vote())
        self.button_exit.clicked.connect(lambda: self.exit())
        self.button_submit.clicked.connect(lambda: self.submit())
        # Initialize Variables
        self.__isabella: int = 0
        self.__genji: int = 0
        self.__hannah: int = 0
        self.__voters: dict = {}
        # Disable Candidate Menu
        self.button_submit.hide()
        self.radio_candidate1.hide()
        self.radio_candidate2.hide()
        self.radio_candidate3.hide()

    def vote(self) -> None:
        """
        Method to switch from Vote Menu to the Candidate Menu and validate ID
        """
        # Validate ID
        try:
            if self.input_id.text().isdigit() and len(self.input_id.text()) == 4:
                if self.input_id.text() not in self.__voters:
                    # Disable Vote Menu & Enable Candidate Menu
                    self.button_vote.hide()
                    self.button_exit.hide()
                    self.label_enterid.hide()
                    self.label_idinfo.hide()
                    self.input_id.hide()
                    self.label_error.clear()

                    self.label_title.setText('CANDIDATE MENU')
                    self.button_submit.show()
                    self.radio_candidate1.show()
                    self.radio_candidate2.show()
                    self.radio_candidate3.show()
                else:
                    self.label_error.setText('ID has already voted')
            else:
                self.label_error.setText('Invalid ID')
        except:
            self.label_error.setText('Invalid ID')

    def exit(self) -> None:
        """
        Method to write final data to a CSV file and exits
        """
        # Write data to CSV
        with open('results.csv', 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerow(['Voter', 'Candidate'])
            for value in self.__voters.items():
                writer.writerow(value)
            writer.writerow(['Isabella Votes', self.__isabella])
            writer.writerow(['Genji Votes', self.__genji])
            writer.writerow(['Hannah Votes', self.__isabella])
            writer.writerow(['Total Votes', (self.__isabella + self.__genji + self.__hannah)])
        sys.exit()

    def submit(self) -> None:
        """
        Method to check the user vote and switch back to Vote Menu
        """
        # Check vote
        if not self.radio_candidate1.isChecked() and not self.radio_candidate2.isChecked() and not self.radio_candidate3.isChecked():
            self.label_error.setText('Please select a candidate')
        else:
            if self.radio_candidate1.isChecked():
                self.__isabella += 1
                self.__voters[self.input_id.text()]: str = 'Isabella'
            elif self.radio_candidate2.isChecked():
                self.__genji += 1
                self.__voters[self.input_id.text()]: str = 'Genji'
            elif self.radio_candidate3.isChecked():
                self.__hannah += 1
                self.__voters[self.input_id.text()]: str = 'Hannah'
            # Disable Candidate Menu
            self.button_submit.hide()
            self.radio_candidate1.hide()
            self.radio_candidate2.hide()
            self.radio_candidate3.hide()
            self.label_error.clear()
            # Reset Inputs
            for radio in (self.radio_candidate1, self.radio_candidate2, self.radio_candidate3):
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
            self.input_id.clear()
            # Enable Vote Menu
            self.label_title.setText('VOTE MENU')
            self.button_vote.show()
            self.button_exit.show()
            self.label_enterid.show()
            self.label_idinfo.show()
            self.input_id.show()
            self.label_isabella_votes.setText(f'Isabella: {self.__isabella}')
            self.label_genji_votes.setText(f'Genji: {self.__genji}')
            self.label_hannah_votes.setText(f'Hannah: {self.__hannah}')