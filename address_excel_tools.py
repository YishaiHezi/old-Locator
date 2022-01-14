from excel_tools import Excel_tools

class Addresses_Excel_Tools(Excel_tools):

    def __init__(self):
        super().__init__()

        self.EXCEL_PATH = \
            "C:\\Users\\USER\\Desktop\\python_projects\\locator\\mac_to_address.xls"


    def write_mac_to_excel(self, mac, address):
        row = self.get_last_row()
        self.write_to_excel(row, 0, mac)
        self.write_to_excel(row, 1, address)
