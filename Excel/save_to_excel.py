# Excel/save_to_excel.py
import pandas as pd

class ExcelActivities:
    @staticmethod
    def save_to_excel(data, filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
