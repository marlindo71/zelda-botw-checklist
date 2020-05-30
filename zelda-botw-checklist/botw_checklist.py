import openpyxl
import json

try:
    import importlib.resources as importlib_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources

class BOTWChecklist(object):
    def __init__(self,savefile,outfile):
        self.data_folder = 'data'
        self.xlsx_template_file = 'Template.xlsx'
        gamedata_file = 'quests.json'
        self.savefile = savefile
        self.outfile = outfile

        with importlib_resources.open_binary(self.data_folder, gamedata_file) as g_file:
            self.gamedata = json.load(g_file)

        self.get_savefile_data(self.savefile)

    def get_savefile_data(self,savefile):
        c_size = 4
        savefile.seek(12)
        
        while True:
            rf_chunk = savefile.read(c_size)
            if len(rf_chunk) <= 0:
                break

            id_int = int.from_bytes(rf_chunk, byteorder='big',signed=True)
            
            if id_int == -1:
                break
            
            quest = self.gamedata.get(str(id_int))

            if quest:
                if quest['Properties']['Type'] == 'bool':
                    rf_chunk = savefile.read(c_size)
                    quest['Value'] = int.from_bytes(rf_chunk, byteorder='big')
            else:
                savefile.seek(c_size, 1)

    def write_xls(self):

        with importlib_resources.open_binary(self.data_folder, self.xlsx_template_file) as template_file:
            wb = openpyxl.load_workbook(template_file)
        
        ws = wb['Savegame_Data']

        row = ['Name','Type','Region','Location','Value']
        ws.append(row)

        for key, value in self.gamedata.items():
            row = [value['Quest_Name'],value['Quest_Type'],value['Region'],value['Location'],value['Value']]
            ws.append(row)

        filename = self.outfile + '.xlsx'
        wb.save(filename)
        print(filename)