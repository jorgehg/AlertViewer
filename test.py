import os

folder_path_emails = os.path.normpath(r"C:\Users\ext_johirayg\Documents\AlertViewer\office")
email_list = [file for file in os.listdir(folder_path_emails) if file.endswith(".csv")]

print(email_list)