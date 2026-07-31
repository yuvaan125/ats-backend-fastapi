from app.database.connection import get_connection

def get_all_jobs():
    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    id,
                    title,
                    company,
                    salary,
                    location,
                    description,
                    created_at
                FROM jobs
                ORDER BY id;
            """)

            jobs = cur.fetchall()
            return jobs

    finally:
        conn.close()