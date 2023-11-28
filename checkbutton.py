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