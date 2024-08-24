import subprocess

def delete_data_from_media_container(path_to_delete):
    try:
        command = f"rm -rf {path_to_delete}"
        subprocess.run(command, shell=True, check=True)
        print(f"{path_to_delete} deleted")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete {path_to_delete} Error: {e}")
