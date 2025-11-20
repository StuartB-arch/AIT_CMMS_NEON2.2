# Database Backup Feature - Complete Guide

## Overview

The **Database Backup Manager** is a manager-exclusive feature that allows you to create, manage, restore, and export backups of the NEON PostgreSQL database. This enables disaster recovery, data preservation, and quick restoration for your CMMS system.

## Features

### 1. **Automated Backup Creation**
- One-click backup creation directly from the application
- Uses `pg_dump` with custom compression format for efficient storage
- Automatic backup verification after creation
- Timestamped backup files for easy identification

### 2. **Backup Management**
- View all available backups with file details
  - Filename
  - Size in MB
  - Creation date
  - Age in days
- Automatic cleanup of old backups based on retention policy
- Manual deletion of specific backups

### 3. **Restore from Backup**
- Upload and restore database from backup files
- Supports both local backups and uploaded files from external sources
- Multiple confirmation steps to prevent accidental overwrites
- Automatic verification of backup file integrity
- Clear warnings and safety recommendations

### 4. **Export to SharePoint**
- Export backup files to any location on your computer
- Suitable file format for uploading to SharePoint or cloud storage
- Full backup verification before export

### 5. **Configuration**
- Schedule backups: Daily, Weekly, or Monthly
- Set retention period (default: 30 days)
- Maximum backup limit (default: 50 backups)
- Backup verification is enabled by default

### 6. **Audit Trail**
- Complete logging of all backup operations
- Status tracking (success/failed)
- Detailed error messages for troubleshooting

## How to Use

### Accessing the Backup Manager

1. **Login to AIT CMMS** as a Manager
2. Look for the **"🗄️ Database Backup"** button in the Manager Tools toolbar
3. Click the button to open the Backup Manager window

### Creating a Backup

1. Click **"📥 Create Backup Now"** button
2. The system will:
   - Show progress in the status log
   - Create a compressed backup file
   - Verify the backup integrity
   - Display a success message
3. New backup appears in the list automatically

**Time to Complete**: 2-10 minutes (depending on database size)

### Exporting a Backup to SharePoint

1. Select a backup from the list
2. Click **"📂 Export Selected Backup"**
3. Choose where to save the file on your computer
4. The backup file will be copied and ready for upload
5. Upload the file to your SharePoint location

**File Format**: `.backup` (PostgreSQL custom format)

### Restoring a Backup

⚠️ **WARNING**: Restoring a backup will completely overwrite the current database. All current data will be lost!

1. Click **"📤 Restore/Upload Backup"** button
2. Read and confirm the warning dialog about overwriting the database
3. Select a backup file to restore:
   - Choose from the `./backups/` directory, OR
   - Browse to upload a backup file from another location
4. Review the final confirmation showing the filename
5. Click "Yes" to proceed with restore
6. The system will:
   - Show progress in the status log
   - Restore the database from the backup file
   - Display a success or error message
7. **IMPORTANT**: Restart the application after restore to refresh all connections

**Time to Complete**: 2-10 minutes (depending on database size)

**Recommended Before Restore**:
- Create a backup of the current database first
- Verify the backup file you're restoring is valid
- Ensure no other users are actively using the system
- Have a recent working backup as a safety measure

**Use Cases for Restore**:
- Recover from data corruption or loss
- Revert to a previous database state
- Migrate data from another environment
- Restore after accidental deletions

### Managing Backups

#### View Backup Details
1. Select a backup
2. Click **"📋 View Backup Details"**
3. See file size, creation date, and status information

#### Delete Old Backups
1. Select a backup
2. Click **"🗑️ Delete Selected"**
3. Confirm the deletion

#### Cleanup Automatically
1. Click **"🗑️ Cleanup Old Backups"**
2. This removes backups older than the retention period
3. Confirms number of backups removed

#### Right-Click Context Menu
- Right-click any backup for quick access to:
  - Export Backup
  - View Details
  - Delete Backup

### Configuring Backup Settings

1. Scroll to **"Backup Configuration"** section at bottom
2. Adjust settings:
   - **Schedule**: Select Daily, Weekly, or Monthly
   - **Retention (Days)**: Set how long to keep backups
3. Click **"Save Config"** to apply changes

## Backup Locations

### Automatic Backup Directory Selection

The application automatically selects a safe, writable location for backups:

**Primary Location (preferred):**
- Windows: `C:\Users\[YourUsername]\Documents\AIT_CMMS_Backups\`
- Linux/Mac: `~/Documents/AIT_CMMS_Backups/`

**Fallback Locations** (if primary location is not writable):
1. Application directory: `./backups/`
2. User home directory: `~/AIT_CMMS_Backups/`
3. System temp directory: `[TEMP]/AIT_CMMS_Backups/`

**Important:** The actual backup location is displayed in the Backup Manager window when you open it. Look for the "📁 Backup Location:" line at the top of the window.

### File Naming Convention
```
cmms_backup_YYYYMMDD_HHMMSS.backup
```

Example: `cmms_backup_20250119_143052.backup`

## Important Notes

### Database Size and Backup Time
- **Small database (< 100 MB)**: 2-3 minutes
- **Medium database (100-500 MB)**: 5-10 minutes
- **Large database (> 500 MB)**: 10+ minutes

### Storage Requirements
- Backup file size ≈ 50-70% of original database size
- Ensure sufficient disk space for multiple backups

### Backup Format
- **Format**: PostgreSQL Custom Format (`.backup`)
- **Compression**: Built-in compression
- **Verification**: Integrity checked automatically

## Regular Backup Schedule Recommendation

### For Production Environment
- **Frequency**: Daily at 2:00 AM
- **Retention**: 30 days
- **Manual Backup**: Before major updates or changes

### For Development Environment
- **Frequency**: Weekly
- **Retention**: 14 days
- **Manual Backup**: As needed

## Disaster Recovery

### Restoring a Backup

If you need to restore from a backup:

1. **Contact your IT administrator** or database manager
2. Provide the backup file (`.backup` file)
3. Use command line to restore:
   ```bash
   pg_restore -h <host> -p <port> -U <user> -d <database> \
     --clean --if-exists --no-owner --no-acl <backup_file>
   ```

### Backup Verification
- All backups are automatically verified after creation
- Verification confirms:
  - File integrity
  - Table data presence
  - Backup completeness

## Security Considerations

### Backup File Protection
- Store backup files in secure locations
- Restrict access to backup files
- Use HTTPS when uploading to cloud storage
- Consider encryption for sensitive databases

### Database Credentials
- Backups do not contain user passwords (they're hashed)
- Ensure backup files are properly protected
- Don't share backup files publicly

## Troubleshooting

### Backup Creation Failed
**Problem**: "pg_dump failed" error

**Solutions**:
1. Check internet connection to NEON database
2. Verify database credentials are correct
3. Ensure sufficient disk space
4. Wait and retry the backup

### Cannot Export Backup
**Problem**: File is locked or permission denied

**Solutions**:
1. Ensure backup is not in use
2. Check folder permissions
3. Try exporting to a different location

### Backups Disappear
**Problem**: Backups are being automatically cleaned up

**Solutions**:
1. Check retention settings in configuration
2. Increase retention days in Backup Configuration
3. Increase max backups limit

### Database Connection Error
**Problem**: Cannot connect to NEON database

**Solutions**:
1. Check your internet connection
2. Verify NEON database is running
3. Restart the application
4. Contact your system administrator

## Status Messages

### During Backup
```
[timestamp] Starting database backup...
[timestamp] ⏳ This may take several minutes...
```

### Success
```
[timestamp] ✅ Backup successful!
[timestamp] 📁 Location: ./backups/cmms_backup_....backup
[timestamp] 💾 Size: XX.XX MB
```

### Cleanup
```
[timestamp] ✅ Cleanup complete! Removed X old backup(s).
[timestamp] Found X backup(s)
```

## Best Practices

### Before Major Updates
1. Create a backup
2. Note the backup filename
3. Export the backup to SharePoint
4. Proceed with updates

### Weekly Maintenance
1. Review available backups
2. Delete any corrupted backups
3. Run cleanup if too many backups exist
4. Verify at least 1 recent backup exists

### Monthly Review
1. Export a backup for archival
2. Upload to SharePoint
3. Verify backups are being created automatically
4. Check backup log for any errors

## Technical Details

### Backup Process
1. **Initialization**: Connect to NEON database
2. **Dump**: Use pg_dump to create backup
3. **Compression**: Apply custom format compression
4. **Verification**: Run pg_restore --list to verify
5. **Logging**: Record backup status and metadata
6. **Completion**: Display success/failure message

### Configuration Files
- **Backup Config**: `./backups/backup_config.json`
- **Backup Log**: `./backups/backup_log.json`

### Example Configuration
```json
{
  "enabled": true,
  "schedule": "daily",
  "backup_time": "02:00",
  "retention_days": 30,
  "max_backups": 50,
  "compress": true,
  "verify_after_backup": true
}
```

## Support and Contact

For issues or questions about the backup feature:

1. **Check the Status Log** in the Backup Manager window
2. **Review this guide** for common solutions
3. **Contact IT Support** if the issue persists
4. **Provide the backup log** (`./backups/backup_log.json`) for debugging

## Frequently Asked Questions

### Q: Can I schedule automatic backups?
**A**: Yes! Configure the schedule in Backup Configuration. Automatic backups run in the background when enabled.

### Q: How do I restore a backup?
**A**: Contact your database administrator with the backup file. They can restore it using pg_restore.

### Q: Can I backup to multiple locations?
**A**: Export backups to different locations as needed.

### Q: What if my database is very large?
**A**: The backup will take longer but should complete. Ensure you have adequate disk space.

### Q: Are backups encrypted?
**A**: Backups use PostgreSQL's custom format compression. For additional security, encrypt the backup files before uploading to cloud storage.

## Version History

- **Version 1.0** (January 2025)
  - Initial release
  - Full backup/export functionality
  - Automatic cleanup and retention
  - Backup verification
  - Configuration management
