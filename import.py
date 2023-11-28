
def import_file():
    #nhập file
    iFile = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx; *.xls"),("all files","*.*")))
    
    #đọc file nhập và file gốc
    if iFile:
        df_iFile = pd.read_excel(iFile, sheet_name = None)
    df_original_file = pd.read_excel(original_file, sheet_name = None)
    
    # #nếu có subject trùng 
    for subject_name in get_subject_name(original_file):
        if subject_name in get_subject_name(iFile):
            df_original_file[subject_name] = pd.concat([df_original_file[subject_name], df_iFile[subject_name]], axis=0, ignore_index=True)

    # add những subject còn lại
    for subject_name in get_subject_name(iFile):
        if subject_name not in get_subject_name(original_file):
            df_original_file[subject_name] = df_iFile[subject_name]

    #ghi dữ liệu vào file gốc
    with pd.ExcelWriter(original_file, mode = 'a', if_sheet_exists = 'replace') as writer:
        for sheet_name, df in df_original_file.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)