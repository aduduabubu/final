def show_main_label_button():
    label_main.place(relx = 0.5, rely = 0.3, anchor = "center")
    library_button.place(relx = 0.5, rely = 0.65, anchor = "center")
    import_button.place(relx = 0.5, rely = 0.85, anchor = "center")
#Xóa label & button mainscreen
def clean_main_screen():
    label_main.place_forget()
    library_button.place_forget()
    import_button.place_forget()

#quay lại mainscreen   
def back_main_screen(screen):
    if screen == "import":
        label_import.place_forget()
        imtomain_back_button.place_forget()
        down_sample_button.place_forget()
        up_file_button.place_forget()
    
    if screen == "library":
        subject_label_frame.place_forget()
        litomain_back_button.place_forget()
        delete_subject_button.place_forget()
        download_button.place_forget()
        see_card_button.place_forget()
        add_subject_button.place_forget()
        study_button.place_forget()
        
    show_main_label_button()
    
def show_import_screen():
    clean_main_screen()
    
    label_import.place(relx = 0.5, rely = 0.35, anchor = "center")
    imtomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    down_sample_button.place(relx = 0.5, rely = 0.6, anchor = "center")
    up_file_button.place(relx = 0.5, rely = 0.75, anchor = "center")
    
#LIBRARY
#xóa button & label mainscreen, hiện export
def show_library_screen():
    clean_main_screen()
    subject_label_frame.place(relx = 0.5, rely = 0.4, anchor = "center")
    litomain_back_button.place(relx = 0.01, rely = 0.99, anchor = "sw")
    delete_subject_button.place(relx = 0.26, rely = 0.76, anchor = "center")
    download_button.place(relx = 0.42, rely = 0.76, anchor = "center")
    see_card_button.place(relx = 0.58, rely = 0.76, anchor = "center")
    add_subject_button.place(relx = 0.74, rely = 0.76, anchor = "center")
    study_button.place(relx = 0.99, rely = 0.99, anchor = "se")