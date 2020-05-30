# coding=utf-8
# main.py
# 2020, all rights reserved
import click as click
from botw_checklist import BOTWChecklist

@click.command()
@click.argument("savefile", type=click.File("rb"))
# @click.argument("outfile", type=click.File("wb"))
@click.option('--outfile', default='Zelda BOTW Checklist', help='Outputfile')

def main(savefile,outfile):
    # c_size = 4
    # savefile.seek(12)
    # rf_chunk = savefile.read(c_size)
    # # print(rf_chunk)
    # print(outfile)

    botw = BOTWChecklist(savefile,outfile)
    botw.write_xls()
    # break

    # with importlib_resources.open_binary('data', 'Template.xlsx') as template_file:
    #     wb = openpyxl.load_workbook(template_file)

    # with importlib_resources.open_binary('data', 'quests.json') as quests_file:
    #     quests = json.load(quests_file)
    #     print(quests)

    # f.seek(12)
    # while True:
    #     c_size = 4
    #     rf_chunk = f.read(c_size)
    #     if len(rf_chunk) <= 0:
    #         break

    #     id_int = int.from_bytes(rf_chunk, byteorder='big',signed=True)
        
    #     if id_int == -1:
    #         break
        
    #     quest = quests.get(str(id_int))

    #     if quest:
    #         if quest['Properties']['Type'] == 'bool':
    #             rf_chunk = f.read(c_size)
    #             quest['Value'] = int.from_bytes(rf_chunk, byteorder='big')
    #     else:
    #         f.seek(c_size, 1)
 

    # print(quests)

    # ws = wb['Savegame_Data']

    # row = ['Name','Type','Region','Location']
    # ws.append(row)

    # for key, value in quests.items():
    #     row = [value['Quest_Name'],value['Quest_Type'],value['Region'],value['Location'],value['Value']]
    #     ws.append(row)

    # wb.save('gamedata.xlsx')

if __name__ == '__main__':
    main()