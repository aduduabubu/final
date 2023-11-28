def export_file(name_file):
    efile = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=(("Excel files", "*.xlsx"),("all files","*.*")))
    if efile:
        name_file.to_excel(efile, index = False)