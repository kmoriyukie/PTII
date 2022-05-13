from PyQt5.QtWidgets import QWidget, QDialog, QListWidgetItem, QLabel, QFormLayout, QSizePolicy
from PyQt5 import uic

from serial.tools import list_ports

class port_item(QWidget):
    def __init__(self, name, description):
        super(port_item, self).__init__()
        uic.loadUi('widgets\port_item.ui', self)
        
        self.port_name.setText(name)
        self.port_description.setText(description)
        


class port_dialog(QDialog):
    def __init__(self, parent):
        super(port_dialog, self).__init__()
        uic.loadUi('widgets\port_dialog.ui', self)
        
        self.parent = parent
        ls = list(list_ports.comports())
        
        for port in ls:
            item = QListWidgetItem(self.com_list)
            item_widget = port_item(port.name, port.description)
            item.setSizeHint(item_widget.frame.size())
            self.com_list.addItem(item)
            self.com_list.setItemWidget(item, item_widget)

        self.com_list.itemClicked.connect(self.select_com)
    def select_com(self, obj):
        port_name = self.com_list.itemWidget(self.com_list.item(
                                        self.com_list.indexFromItem(obj).row())).port_name.text()
        self.parent.set_com_port(port_name)
            
        