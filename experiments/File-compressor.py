import PySimpleGUI as Psg

label1 = Psg.Text("Select files to compress:")
input1 = Psg.Input()
choose_button1 = Psg.FolderBrowse("Choose")

label2 = Psg.Text("Select files to compress")
input2 = Psg.Input()
choose_button2 = Psg.FolderBrowse("Choose")
compress_button=Psg.Button("Compress")

window = Psg.Window("File Compressor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],[compress_button]])
window.read()
window.close()