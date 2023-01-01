import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)

folder_name = input("Enter Folder Name: ")
folder_dir = os.path.join(BASE_DIR , folder_name)
print("http://localhost:5500/" + folder_name + "/index.html")
# Open with live server 

os.makedirs(folder_dir , exist_ok=True)

file_html = "index.html"
file_css = "style.css"
file_js = "script.js"

file_path = os.path.join(folder_dir , file_html)
if os.path.exists(file_path):
    print("Skipped HTML File")
with open(file_path , "w" , encoding = "utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This Web page</title>
    <link rel="stylesheet" href="style.css" type = "text/css" >
</head>
<body>
    Hello World!
    <script src="script.js"></script>
</body>
</html>""")

file_path = os.path.join(folder_dir , file_css)
if os.path.exists(file_path):
    print("Skipped CSS File")
with open(file_path , "w" , encoding = "utf-8") as f:
    f.write("""html , body {
    height : 100%;
    width : 100%;
}""")

file_path = os.path.join(folder_dir , file_js)
if os.path.exists(file_path):
    print("Skipped JS File")
with open(file_path , "w") as f:
    f.write("")

