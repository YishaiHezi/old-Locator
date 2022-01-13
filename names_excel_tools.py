from excel_tools import Excel_tools

class Names_Excel_Tools(Excel_tools):

    def __init__(self):
        super().__init__()

        self.EXCEL_PATH = \
            "C:\\Users\\USER\\Desktop\\python_projects\\locator\\names_to_macs.xls"


    def write_mac_to_excel(self, mac, name):
        row = self.get_last_row()
        self.write_to_excel(row, 0, name)
        self.write_to_excel(row, 1, mac)
