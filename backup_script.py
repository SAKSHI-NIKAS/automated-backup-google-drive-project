import os
import json
import shutil
import argparse
import subprocess
import requests
from datetime import datetime


# Load configuration
with open("config.json", "r") as file:
    config = json.load(file)


# Command line argument
parser = argparse.ArgumentParser()

parser.add_argument(
    "--no-notify",
    action="store_true",
    help="Disable webhook notification"
)

args = parser.parse_args()


# Variables
project_name = config["project_name"]
source_directory = config["source_directory"]
backup_directory = config["backup_directory"]
gdrive_remote = config["gdrive_remote"]
webhook_url = config["webhook_url"]


# Timestamp
now = datetime.now()

timestamp = now.strftime("%Y%m%d_%H%M%S")

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")


# Create backup folder structure
backup_path = os.path.join(
    backup_directory,
    project_name,
    year,
    month,
    day
)

os.makedirs(
    backup_path,
    exist_ok=True
)


# Create ZIP backup
backup_name = f"{project_name}_{timestamp}"

zip_file_path = os.path.join(
    backup_path,
    backup_name
)


print("Creating backup...")

shutil.make_archive(
    zip_file_path,
    "zip",
    source_directory
)


zip_file_path = zip_file_path + ".zip"


print("Backup created:")
print(zip_file_path)



# Upload to Google Drive using rclone
print("Uploading to Google Drive...")


rclone_path = r"C:\Users\sakshi\Downloads\rclone-v1.74.4-windows-amd64\rclone-v1.74.4-windows-amd64\rclone.exe"


upload = subprocess.run(
    [
        rclone_path,
        "copy",
        zip_file_path,
        gdrive_remote
    ],
    capture_output=True,
    text=True
)


if upload.returncode == 0:
    upload_status = "SUCCESS"
    print("Upload successful")

else:
    upload_status = "FAILED"
    print("Upload failed")
    print(upload.stderr)



# Rotation Cleanup
def cleanup_old_backups():

    deleted_files = []

    all_backups = []

    for root, dirs, files in os.walk(
        os.path.join(
            backup_directory,
            project_name
        )
    ):

        for file in files:

            if file.endswith(".zip"):

                full_path = os.path.join(
                    root,
                    file
                )

                all_backups.append(full_path)


    # Sort newest first

    all_backups.sort(
        key=os.path.getmtime,
        reverse=True
    )


    keep = config["daily_retention"]


    old_files = all_backups[keep:]


    for file in old_files:

        os.remove(file)

        deleted_files.append(file)


    return deleted_files



deleted = cleanup_old_backups()



# Write log file

with open(
    "backup.log",
    "a"
) as log:

    log.write(
        f"""
----------------------------------
Backup Time : {now}
Project     : {project_name}
File        : {zip_file_path}
Upload      : {upload_status}
Deleted     : {deleted}

"""
    )



# Send webhook notification

if upload_status == "SUCCESS" and not args.no_notify:

    payload = {

        "project": project_name,

        "date": str(now),

        "test": "BackupSuccessful"

    }


    try:

        response = requests.post(
            webhook_url,
            json=payload
        )

        print(
            "Notification sent"
        )


    except Exception as error:

        print(
            "Notification failed:",
            error
        )


print("\nBackup process completed successfully!")