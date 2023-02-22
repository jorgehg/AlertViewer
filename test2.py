import csv



header = ["registro_id","Fecha_y_Hora","BU","User_ID","Endpoint","Politica","Regla","Template","Severidad","Accion_DLP","Canal_DLP","Fileserver","File_Path","Filename","Extension","Request","Asunto","Remitente","Destinatario_Dominio","Destinatario", "Fuente"]
metele = ["registro_id","Fecha_y_Hora","BU","User_ID","Endpoint","Politica","Regla","Template","Severidad","Accion_DLP","Canal_DLP","Fileserver","File_Path","Filename","Extension","Request","Asunto","Remitente","Destinatario_Dominio","Destinatario", "Fuente"]
with open(r"C:\Users\Jorge\Documents\AlertViewer\export\prueba.csv",'w',encoding='UTF8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in metele:
        writer.writerow(row)