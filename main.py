from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import openpyxl
import pandas as pd 


original_file = "data.xlsx"
data = {"word": [], 'Definition': [],}
        
# #Kiểm tra file excel có tồn tại không. Nếu không, tạo file đó.
# def check_existence_and_create_file(file):
    
#     global data
        
#     if not os.path.exists(file):
            
#         data_frame = pd.DataFrame(data)
#         data_frame.to_excel(file, index=False)
            
# #Lấy tên subjects
def get_subject_name(file):
    
    file_info = pd.read_excel(file, sheet_name =None)
    subject_name = list(file_info.keys())
    
    return subject_name

# #Tạo subject
# def create_subject(file, new_subject_name):
    
#     global data
    
#     if new_subject_name in get_subject_name(file):
#         print(f"{new_subject_name} already exists. Please check again.")
    
#     else :
#         #Tạo DataFrame trống
#         data_frame = pd.DataFrame(data)
#         #chuyển DF vào file excel
#         with pd.ExcelWriter(file) as writer:
#             data_frame.to_excel(writer, sheet_name = new_subject_name, index = False)
            
# # Xóa subject
# def delete_subject(file, subject_name_to_delete):
#     #nếu user chọn All thì xóa cả file
#     if subject_name_to_delete == "All" :
        
#         if os.path.exists(file):
#             os.remove(file)
            
#     else: 
#         #mở file excel
#         with pd.ExcelWriter(file) as writer:
#             #Xóa sheet
#             writer.sheets.pop(subject_name_to_delete, None)
        
# #tạo flashcard
# def create_flashcard(file,subject_name, card_info):
#     file_info = pd.read_excel(file, subject_name)
#     new_card = pd.DataFrame([card_info], columns = file_info.columns)
#     file_info = pd.concat([file_info, new_card], ignore_index = True)

# #Xóa card
# def delete_card(file,subject_name, card_to_delete):
#     #đọc file
#     file_info = pd.read_excel(file, subject_name)
#     #xóa hàng chứa card cần xóa, .iloc[:0] sẽ loại bỏ các giá trị giống với card cần xóa
#     file_info = file_info[file_info.iloc[:,0]] != card_to_delete
#     #ghi lại nội dung của file_info vào sheet
#     with pd.ExcelWriter(file) as writer:
#         file_info.to_excel(writer, sheet_name = subject_name, index = False)

#PROGRAM
#import
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
        
#export
def export_file(name_file):
    efile = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=(("Excel files", "*.xlsx"),("all files","*.*")))
    if efile:
        name_file.to_excel(efile, index = False)

#tạo window
window = Tk()
#set size (wxh)
#position (width x high + a + b)
window.geometry("1000x600")
#tên app
window.title("Flash Card App")
#set icon
window.iconbitmap('icon.ico')
#set background color
window.configure(bg='#6E17BF')
#khả năng thay đổi kích thước của cửa sổ
window.resizable(True, True)

#CÁC HÀM GIAO DIỆN
#MAIN
#tạo label
def create_label(ntext, fs):
    new_label = Label(window, text = ntext,
                font = ("Cooper Black", fs),  #forn, size
                fg = "white",                 # Màu chữ
                bg = "#6E17BF",               #Màu background
                justify = CENTER, wraplength = 800)               
    return new_label
    
#tạo button
def create_button(name_button,fs, nwidth, ndef):
    new_button = Button(window, text = name_button, 
                        font = ("Cooper Black", fs),
                        width = nwidth, pady = 5,
                        fg = "white",
                        bg = "#bd46bd",
                        relief="raise",
                        activebackground = "#BF17BC",
                        command = ndef)   #kiểu button
    return new_button
#hiện button & label mainscreen
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
    
#IMPORT
#xóa button & label mainscreen, hiện import
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

def create_checkbutton(name_labelframe, ndef):
    #tạo thanh trượt
    scroll_bar = Scrollbar(name_labelframe, orient="vertical")
    scroll_bar.pack(side="right", fill="y")
    #tạo text widget lket với scrollbar
    text_scroll =Text(name_labelframe, yscrollcommand=scroll_bar.set, bg = "#cba3f0", height = 20, width = 70)
    text_scroll.pack(side="left", fill="both")
    text_scroll.config(cursor="")
    #kết nối scrollbar với text
    def on_scroll(*args):
        text_scroll.yview(*args)
    scroll_bar.config(command=on_scroll)
    scroll_bar.pack(side="right", fill="y")
    #nút All
    def toggle_all():
        # Lặp qua tất cả các Checkbutton và cập nhật trạng thái của chúng
        for var in checkbutton_var.values():
            var.set(select_all_var.get())

    select_all_var = IntVar()
    select_all_checkbox = Checkbutton(name_labelframe, text="All", variable=select_all_var, command=toggle_all,fg = "white", bg = "#cba3f0",activebackground = "#cba3f0", selectcolor = "#cba3f0", font = ("Cooper Black", 15))
    select_all_checkbox.pack()
 
    #tạo checkbutton
    checkbutton_var = {}
    for option in ndef:
        checkbutton_var[option] = IntVar()
        checkbutton =  Checkbutton(text_scroll, text=f"{option}", variable=checkbutton_var[option], fg = "white", bg = "#cba3f0",activebackground = "#cba3f0", selectcolor = "#cba3f0", font = ("Cooper Black", 15), justify = LEFT)
        #checkbuttons.append([checkbutton_var, checkbutton])
        text_scroll.window_create("end", window=checkbutton)
        text_scroll.insert("end", "\n")
    return checkbutton_var

def select_option(check_name):
    
    selected_options = []
    for option, var in check_name.items():
        if var.get() == 1:
            selected_options.append(option)
    return selected_options

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

#chương trình chính
#Mainscreen
#tạo label main screen
label_main = create_label("FLASHCARD", 80)
#tạo button
library_button = create_button("Library",25,10,show_library_screen)
import_button = create_button("Import", 25,10,show_import_screen)
#hiển thị mainscreen
show_main_label_button()

#Import    
#tạo label
label_import = create_label("Please upload your file similar to the sample file below", 35)
#tạo button
down_sample_button = create_button("Download Sample File", 20, 20,lambda: export_file(pd.DataFrame(data)))
up_file_button = create_button("Upload Your File", 20, 20, import_file)
imtomain_back_button = create_button("Back", 12, 5, lambda: back_main_screen("import"))

#Library
#labelframe chứa select option
subject_label_frame = LabelFrame(window, text = "Yours subject", bg = "#cba3f0",  font = ("Cooper Black", 25), fg = "white")
#tạo checkbutton cho subject
#labelframe chứa select export
litomain_back_button = create_button("Back", 12, 5, lambda: back_main_screen("library"))
delete_subject_button = create_button("Delete", 15, 10, lambda: delete_subject(select_subject))
download_button = create_button("Download", 15, 10, lambda: back_main_screen("library"))
see_card_button = create_button("See Card", 15, 10, lambda: back_main_screen("library"))
add_subject_button = create_button("Add subject", 15, 10, lambda: back_main_screen("library"))
study_button = create_button("STUDY", 20, 10, lambda: back_main_screen("library"))

select_subject = create_checkbutton(subject_label_frame, get_subject_name(original_file))


#chay
window = mainloop()
    