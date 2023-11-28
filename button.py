def delete_subject(name):
    global original_file
    global subject_label_frame
    if not select_option(name):
        messagebox.showerror('Notification', 'You have not selected the subject to delete. Please check again')
    else :
        result = messagebox.askokcancel('Notification','Are you sure you want to delete the selected subject?')
        if result:
        
            try:
            # Mở workbook
                file_info = openpyxl.load_workbook(original_file)
                for subject in select_option(name):
                # Kiểm tra xem sheet có tồn tại không
                    if subject in file_info.sheetnames:
                        # Xóa sheet
                        file_info.remove(file_info[subject])

                        # Lưu lại workbook
                file_info.save(original_file)
                #create_checkbutton(subject_label_frame, get_subject_name(original_file))
            except Exception as e:
                print(f"Lỗi xảy ra khi xóa sheet: {str(e)}")