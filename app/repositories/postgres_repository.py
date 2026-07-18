from app.db import get_connection


class PostgresRepository:

    def get_all(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM students ORDER BY id")

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [
            {
                "id": r[0],
                "name": r[1],
                "age": r[2],
                "course": r[3]
            }
            for r in rows
        ]

    def get_by_id(self, student_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM students WHERE id=%s",
            (student_id,)
        )

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "course": row[3]
            }

        return None

    def create(self, student):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO students(name,age,course)
            VALUES(%s,%s,%s)
            RETURNING id
            """,
            (
                student["name"],
                student["age"],
                student["course"]
            )
        )

        student["id"] = cur.fetchone()[0]

        conn.commit()

        cur.close()
        conn.close()

        return student

    def update(self, student_id, student):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE students
            SET name=%s,
                age=%s,
                course=%s
            WHERE id=%s
            """,
            (
                student["name"],
                student["age"],
                student["course"],
                student_id
            )
        )

        conn.commit()

        cur.close()
        conn.close()

        return self.get_by_id(student_id)

    def delete(self, student_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM students WHERE id=%s",
            (student_id,)
        )

        conn.commit()

        cur.close()
        conn.close()