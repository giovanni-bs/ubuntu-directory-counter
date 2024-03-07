import subprocess
print("Imagens pendentes\n")
print("Tinder\n")
def count_files_in_directory(name, directory):
    try:
        # Run the find command and capture the output
        command = f"find {directory} -type f -name '*jpg'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Count the number of files by splitting the output
        file_list = result.stdout.split('\n')
        file_count = len(file_list) - 1  # Subtract 1 to exclude the empty string at the end

        # Print the custom name, directory, and file count
        #print(f"Nome: {name}, Diretório: {directory}, File Count: {file_count}")
        print(f"Classificador: {name} - Pendentes: {file_count}")

    except Exception as e:
        print(f"Error: {e}")

# List of custom names and directories to scan
directories_to_scan = [
    ('João - Buraco', '/workspace/production/projects/sgc/tinder/buraco/joao_a/todo/'),
    ('João - Entulho', '/workspace/production/projects/sgc/tinder/entulho/joao_a/todo/'),
    ('João - Saco de Varrição', '/workspace/production/projects/sgc/tinder/saco_de_varricao/joao_a/todo/'),
    ('João - Tampa de PV', '/workspace/production/projects/sgc/tinder/tampa_de_pv/joao_a/todo/'),
    ('Rafael - Buraco', '/workspace/production/projects/sgc/tinder/buraco/rafael_c/todo/'),
    ('Rafael - Entulho', '/workspace/production/projects/sgc/tinder/entulho/rafael_c/todo/'),
    ('Rafael - Saco de Varrição', '/workspace/production/projects/sgc/tinder/saco_de_varricao/rafael_c/todo/'),
    ('Rafael - Tampa de PV', '/workspace/production/projects/sgc/tinder/tampa_de_pv/rafael_c/todo/'),
    ('Thiago - Buraco', '/workspace/production/projects/sgc/tinder/buraco/thiago_h/todo/'),
    ('Thiago - Entulho', '/workspace/production/projects/sgc/tinder/entulho/thiago_h/todo/'),
    ('Thiago - Saco de Varrição', '/workspace/production/projects/sgc/tinder/saco_de_varricao/thiago_h/todo/'),
    ('Thiago - Tampa de PV', '/workspace/production/projects/sgc/tinder/tampa_de_pv/thiago_h/todo/')
]

# Scan each directory and print the file count
for name, directory in directories_to_scan:
    count_files_in_directory(name, directory)