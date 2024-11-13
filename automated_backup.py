

def backup_directory(source_dir, backup_dir):
    """
    Compresses the source directory into a zip file and stores it in the backup directory.
    
    :param source_dir: The directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    """
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist!")
        return

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_filename = os.path.join(backup_dir, f"backup-{timestamp}.zip")
    
    shutil.make_archive(backup_filename.replace('.zip', ''), 'zip', source_dir)
    print(f"Backup of {source_dir} created successfully at {backup_filename}")

if __name__ == "__main__":
    source_directory = input("Enter the directory you want to back up: ")
    backup_directory_path = input("Enter the directory where the backup should be stored: ")

    backup_directory(source_directory, backup_directory_path)
