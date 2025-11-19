#!/usr/bin/env python3
"""
Script to update the aspenson user's full name from 'April Penson' to 'Ashica Penson'
Run this script to fix the database record.
"""

import sys
from database_utils import DatabaseConnectionPool

def update_aspenson_name():
    """Update the aspenson user's full name in the database"""

    DB_CONFIG = {
        'host': 'ep-tiny-paper-ad8glt26-pooler.c-2.us-east-1.aws.neon.tech',
        'port': 5432,
        'database': 'neondb',
        'user': 'neondb_owner',
        'password': 'npg_2Nm6hyPVWiIH',
        'sslmode': 'require'
    }

    print("Connecting to database...")
    db_pool = DatabaseConnectionPool()

    try:
        db_pool.initialize(DB_CONFIG, min_conn=1, max_conn=2)

        with db_pool.get_cursor() as cursor:
            # Check current name
            cursor.execute("SELECT full_name FROM users WHERE username = %s", ('apenson',))
            result = cursor.fetchone()

            if result:
                current_name = result['full_name'] if isinstance(result, dict) else result[0]
                print(f"Current name: {current_name}")

                # Update the name
                cursor.execute(
                    "UPDATE users SET full_name = %s WHERE username = %s",
                    ('Ashica Penson', 'apenson')
                )

                # Verify the update
                cursor.execute("SELECT full_name FROM users WHERE username = %s", ('apenson',))
                result = cursor.fetchone()
                new_name = result['full_name'] if isinstance(result, dict) else result[0]

                print(f"Updated name: {new_name}")
                print("✓ Successfully updated aspenson user's name to 'Ashica Penson'")
            else:
                print("✗ User 'apenson' not found in database")

    except Exception as e:
        print(f"✗ Error updating name: {e}")
        sys.exit(1)
    finally:
        db_pool.close_all()

    print("\nPlease restart the application for changes to take effect.")

if __name__ == "__main__":
    update_aspenson_name()
