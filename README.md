# Automated Backup and Rotation System with Google Drive Integration

## 📌 Project Overview

This project implements an automated backup management solution using **Python scripting**, **rclone**, and **Google Drive** integration.

The system automatically creates compressed backups of a project directory, stores them in an organized local backup structure, uploads backup archives to Google Drive, manages old backups using a rotation policy, generates execution logs, and sends webhook notifications after successful backup completion.

This project demonstrates practical **DevOps automation, cloud storage integration, backup management, and scripting skills**.

---

# 🏗️ Architecture Workflow

```
                 Project Directory
                        |
                        |
                        v
              Python Backup Script
                        |
        +---------------+---------------+
        |                               |
        v                               v
  Create ZIP Backup              Backup Rotation
  Timestamp Format               Daily/Weekly/Monthly
        |
        |
        v
 Local Backup Storage
 C:\Users\<username>\backups
        |
        |
        v
 Google Drive Storage
 (Using rclone)
        |
        |
        v
 Webhook Notification
 (Backup Success Alert)
```

---

# ✨ Features

✅ Automated project directory backup  
✅ ZIP archive creation  
✅ Timestamp-based backup naming  
✅ Structured local backup storage  
✅ Google Drive integration using rclone  
✅ Backup rotation and cleanup  
✅ Backup execution logging  
✅ Webhook notification system  
✅ Configurable settings using JSON  
✅ Disable notification option using command-line argument  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backup automation script |
| rclone | Google Drive CLI integration |
| Google Drive | Cloud backup storage |
| PowerShell | Execution environment |
| Webhook.site | Notification testing |
| Git/GitHub | Version control |

---

# 📂 Project Structure

```
automated-backup-google-drive-project
│
├── backup_script.py          # Main automation script
├── config.json               # Configuration file
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
├── .gitignore                # Ignored files
│
└── sample-project            # Project to backup
    ├── app.py
    └── config.txt
```

---

# ⚙️ Prerequisites

Install the following tools:

- Python 3.x
- rclone
- Google Drive account
- Git

Verify Python:

```powershell
python --version
```

Verify rclone:

```powershell
rclone version
```

---

# 🔧 Installation Setup

## 1. Clone Repository

```bash
git clone <repository-url>

cd automated-backup-google-drive-project
```

---

## 2. Install Python Dependencies

Run:

```powershell
pip install -r requirements.txt
```

---

# ☁️ Google Drive Configuration

## Install rclone

Download rclone:

```
https://rclone.org/downloads/
```

---

## Configure Google Drive

Run:

```powershell
rclone config
```

Create a new remote:

```
Name: gdrive
Storage: Google Drive
```

Authenticate with your Google account.

Test connection:

```powershell
rclone lsd gdrive:
```

---

# 📝 Configuration File

Update `config.json` according to your environment.

Example:

```json
{
    "project_name": "sample-project",

    "source_directory": "C:/Users/sakshi/OneDrive/Documents/automated-backup-google-drive-project/sample-project",

    "backup_directory": "C:/Users/sakshi/backups",

    "gdrive_remote": "gdrive:BackupFolder",

    "daily_retention": 7,

    "weekly_retention": 4,

    "monthly_retention": 3,

    "webhook_url": "https://webhook.site/your-url"
}
```

---

# ▶️ Running the Backup Script

Run backup:

```powershell
python backup_script.py
```

The script performs:

1. Reads configuration
2. Creates ZIP archive
3. Generates timestamped filename
4. Stores backup locally
5. Uploads backup to Google Drive
6. Removes older backups
7. Creates logs
8. Sends notification

---

# 🔕 Disable Notification

To run backup without sending webhook notification:

```powershell
python backup_script.py --no-notify
```

---

# 📦 Backup Output

Backup file format:

```
ProjectName_YYYYMMDD_HHMMSS.zip
```

Example:

```
sample-project_20260715_151423.zip
```

Local storage:

```
C:\Users\sakshi\backups\sample-project\2026\07\15\
```

---

# 🔄 Backup Rotation Policy

The backup system automatically manages storage usage.

Default retention:

| Backup Type | Retention |
|-------------|-----------|
| Daily Backup | Last 7 backups |
| Weekly Backup | Last 4 backups |
| Monthly Backup | Last 3 months |

Older backup files are automatically deleted.

---

# 📋 Logging

The script generates:

```
backup.log
```

Example:

```
----------------------------------

Backup Time : 2026-07-15 15:14:23

Project     : sample-project

File        : sample-project_20260715_151423.zip

Upload      : SUCCESS

Deleted     : []
```

---

# 🔔 Webhook Notification

After successful backup, the system sends a POST request.

Example payload:

```json
{
    "project": "sample-project",
    "date": "2026-07-15",
    "test": "BackupSuccessful"
}
```

---

# 📸 Project Screenshots

## 1. Project Structure

(Add VS Code folder screenshot)

## 2. Backup Execution

(Add PowerShell backup execution screenshot)

## 3. Google Drive Upload

(Add Google Drive backup screenshot)

## 4. Webhook Notification

(Add webhook response screenshot)

## 5. GitHub Repository

(Add GitHub repository screenshot)

---

# 🔐 Security Best Practices

- Never upload Google credentials to GitHub
- Protect rclone configuration files
- Use `.gitignore` for sensitive files
- Avoid hardcoding secrets
- Use restricted Google Drive permissions
- Maintain backup logs
- Test backup restoration regularly

---

# 🚀 Future Enhancements

- Add AWS S3 backup support
- Add email notifications
- Encrypt backup archives
- Add Windows Task Scheduler automation
- Create backup restore functionality
- Add monitoring dashboard

---

# 👩‍💻 Author

**Sakshi Nikas**

Cloud Computing | AWS | DevOps Enthusiast

