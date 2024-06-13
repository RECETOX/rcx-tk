import pandas as pd
import os
from rcx_tk.process_metadata_file import read_file


def test_read_file():
    d = {
        'File path': [
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\1_instrumental blank_01.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\4_Alkane mix_04.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\6_instrumental blank_06.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\7_procedural blank_07.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\8_QC non-dilute_08.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\11_QC 16_11.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\12_QC 8_12.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\15_QC non-dilute_15.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\18_QC 4 _18.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\19_QC 8_19.raw",
            "Z:\000020-Shares\hram\MS_omics\Personal Folders\COUFALIKOVA Katerina\ATHLETE\finalni data zaloha\batch1-20231121-Katerina Coufalikova\RAW_profile\29_instrument blank_29.raw"
        ],
        'File name': [
            "1_instrumental blank_01",
            "4_Alkane mix_04",
            "6_instrumental blank_06",
            "7_procedural blank_07",
            "8_QC non-dilute_08",
            "11_QC 16_11",
            "12_QC 8_12",
            "15_QC non-dilute_15",
            "18_QC 4 _18",
            "19_QC 8_19",
            "29_instrument blank_29"
        ],
       'Type': [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard"
       ]
    }

    expected = pd.DataFrame(data = d)
    file_path = os.path.join("test_data", "batch_specification1.xlsx")
    #actual = read_file(file_path)
    #assert expected == actual
    print(file_path)