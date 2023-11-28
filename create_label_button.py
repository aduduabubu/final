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