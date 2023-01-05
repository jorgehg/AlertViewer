list = ["registro_id", "Fecha_y_Hora", "user_ID", "Endpoint", "BU", "Politica", "Regla", "Canal_DLP", "count", "severidad", "Accion_DLP", "escalamiento", "CC", "argos_capa"]

s = ""
for i in list:
    s = s + " " + i + ","

s = s[:-1]

s  = "SELECT"+s+" FROM alertassoc"
print(s)