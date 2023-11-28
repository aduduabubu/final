def get_subject_name(file):
    
    file_info = pd.read_excel(file, sheet_name =None)
    subject_name = list(file_info.keys())
    
    return subject_name
