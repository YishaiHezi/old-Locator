# from xlrd import open_workbook
# from xlutils.copy import copy


def foo(x):
  return x*2


# class Excel_tools:

#     def __init__(self):
#         self.EXCEL_PATH = None

#     def read_excel_to_dict(self):
#         # Give the location of the file
#         wb = open_workbook(self.EXCEL_PATH)
#         sheet = wb.sheet_by_index(0)

#         d = {}

#         i = 0

#         # For row 0 and column 0 (raw, column)
#         for item in sheet.get_rows():
#             i += 1

#             if i > 100:
#                 break

#             if item[0].value == '' or item[1].value == '':
#                 continue

#             d[str(item[0].value)] = item[1].value

#         return d

#     def print_excel(self):
#         d = self.read_excel_to_dict()
#         print(d)

#     def write_to_excel(self, row, col, text):
#         """
#         A method that write to the excel file in row, col - the text.
#         """
#         rb = open_workbook(self.EXCEL_PATH)
#         wb = copy(rb)

#         s = wb.get_sheet(0)
#         s.write(row, col, text)
#         wb.save(self.EXCEL_PATH)

#     def get_last_row(self):
#         wb = open_workbook(self.EXCEL_PATH)
#         sheet = wb.sheet_by_index(0)
#         i = 0
#         # For row 0 and column 0 (raw, column)
#         for item in sheet.get_rows():
#             i += 1

#         return i

#     def find_key_in_excel(self, key):
#         wb = open_workbook(self.EXCEL_PATH)
#         sheet = wb.sheet_by_index(0)
#         i = 0

#         for item in sheet.get_rows():
#             if item[0].value == key:
#                 return i

#             i += 1

#         return False

#     def get_value_from_key(self, key):
#         wb = open_workbook(self.EXCEL_PATH)
#         sheet = wb.sheet_by_index(0)

#         for item in sheet.get_rows():
#             if item[0].value == key:
#                 return item[1].value

#         return None
