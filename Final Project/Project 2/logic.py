# Caelan Charleston & Evan Rathke
from PyQt6.QtWidgets import *
from gui import *
import csv
import sys

class Logic(QMainWindow, Ui_MainWindow):
    """
    Class containing logic for the GUI
    """
    def __init__(self) -> None:
        """
        Method to initialize the window, set default values, and toggle off payment menu
        """
        super().__init__()
        self.setupUi(self)
        # Initialize window
        self.setFixedSize(1000, 800)
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_void.clicked.connect(lambda: self.void())
        self.button_total.clicked.connect(lambda: self.total())
        self.button_confirm.clicked.connect(lambda: self.confirm())
        self.button_cart.clicked.connect(lambda: self.cart())
        # Hide payment menu
        self.label_selectpayment.hide()
        self.radio_cash.hide()
        self.radio_card.hide()
        self.radio_check.hide()
        self.button_confirm.hide()
        # Set default values
        self.__items: list = []
        self.__total_cost: float = 0
        self.__menu: str = 'main'
        self.label_totalitems.setText(f'Total Items: {len(self.__items)}')
        self.label_totalcost.setText(f'Total Cost: ${self.__total_cost:.2f}')

    def cleardata(self) -> None:
        """
        Method to erase the values inputted by the user
        """
        # Main menu
        self.input_item.clear()
        self.input_price.clear()
        self.input_quantity.clear()
        self.radio_clothing.setChecked(False)
        self.radio_bakery.setChecked(False)
        self.radio_produce.setChecked(False)
        self.radio_meat.setChecked(False)
        self.radio_other.setChecked(True)
        # Payment menu
        self.radio_cash.setChecked(True)
        self.radio_card.setChecked(False)
        self.radio_check.setChecked(False)

    def get_data(self) -> tuple[str, float, int, str] | type[TypeError]:
        """
        Method to retrieve user inputted values
        :return: Tuple containing values
        """
        try:
            # Check input boxes
            if self.input_item.text() == '':
                raise ValueError
            item: str = self.input_item.text().strip()
            price: float = float(self.input_price.text())
            quantity: int = int(self.input_quantity.text())
            # Check item radio buttons
            if self.radio_clothing.isChecked():
                type: str = 'Clothing'
            elif self.radio_bakery.isChecked():
                type: str = 'Bakery'
            elif self.radio_produce.isChecked():
                type: str = 'Produce'
            elif self.radio_meat.isChecked():
                type: str = 'Meat'
            elif self.radio_other.isChecked():
                type: str = 'Other'
            # Return values
            return item, price, quantity, type
        except:
            return TypeError

    def cart(self) -> None:
        """
        Display the contents of the cart
        """
        contents = f'{'-'*30}\nContents:\nQuantity, Item, Type, Price\n{'-'*30}\n'
        for item in self.__items:
            contents += f'{item[1]}, {item[0]}, {item[2]}, ${item[3]:.2f}\n'
        self.label_info.setText(contents)

    def enter(self) -> None:
        """
        Add an item to the cart
        """
        try:
            data: tuple = self.get_data()
            self.__items.append([data[0], data[2], data[3], data[1]])
            self.label_totalitems.setText(f'Total Items: {len(self.__items)}')
            self.__total_cost: float = self.__total_cost + data[1]
            self.label_totalcost.setText(f'Total Cost: ${self.__total_cost:.2f}')
            self.label_info.setText(f'Added {data[2]} {data[0]} to the cart.')
            self.cleardata()
        except:
            self.label_info.setText('Please enter valid values.')

    def void(self) -> None:
        """
        Remove an existing item from the cart
        """
        try:
            data: tuple = self.get_data()
            self.__items.remove([data[0], data[2], data[3], data[1]])
            self.label_totalitems.setText(f'Total Items: {len(self.__items)}')
            self.__total_cost: float = self.__total_cost - data[1]
            self.label_totalcost.setText(f'Total Cost: ${self.__total_cost:.2f}')
            self.label_info.setText(f'Removed {data[2]} {data[0]} from the cart.')
            self.cleardata()
        except:
            self.label_info.setText('Please enter valid values.')

    def total(self) -> None:
        """
        Switch between main and payment menus
        """
        if self.__menu == 'main':
            # Disable main menu
            self.label_enteritem.hide()
            self.label_enterprice.hide()
            self.label_enterquantity.hide()
            self.label_itemtype.hide()
            self.label_info.hide()
            self.input_item.hide()
            self.input_price.hide()
            self.input_quantity.hide()
            self.radio_clothing.hide()
            self.radio_bakery.hide()
            self.radio_produce.hide()
            self.radio_meat.hide()
            self.radio_other.hide()
            self.button_cart.hide()
            self.button_void.hide()
            self.button_enter.hide()
            self.button_total.setText('Back')
            # Enable payment menu
            self.label_selectpayment.show()
            self.radio_cash.show()
            self.radio_card.show()
            self.radio_check.show()
            self.button_confirm.show()
            self.__menu: str = 'payment'
        elif self.__menu == 'payment':
            # Disable payment menu
            self.label_selectpayment.hide()
            self.radio_cash.hide()
            self.radio_card.hide()
            self.radio_check.hide()
            self.button_confirm.hide()
            # Enable main menu
            self.label_enteritem.show()
            self.label_enterprice.show()
            self.label_enterquantity.show()
            self.label_itemtype.show()
            self.label_info.show()
            self.input_item.show()
            self.input_price.show()
            self.input_quantity.show()
            self.radio_clothing.show()
            self.radio_bakery.show()
            self.radio_produce.show()
            self.radio_meat.show()
            self.radio_other.show()
            self.button_cart.show()
            self.button_void.show()
            self.button_enter.show()
            self.button_total.setText('Total')
            self.__menu: str = 'main'

    def confirm(self) -> None:
        """
        Creates the receipt for the cart
        """
        with open('receipt.csv', 'w', newline='') as receipt:
            writer: writer = csv.writer(receipt)
            writer.writerow(['Quantity', 'Item', 'Type', 'Price'])
            for item in self.__items:
                writer.writerow([item[1], item[0], item[2], item[3]])
            # Check search radio buttons
            if self.radio_cash.isChecked():
                payment_type: str = 'Cash'
            elif self.radio_card.isChecked():
                payment_type: str = 'Card'
            elif self.radio_check.isChecked():
                payment_type: str = 'Check'
            writer.writerow(['Total', '', payment_type, self.__total_cost])
            sys.exit()