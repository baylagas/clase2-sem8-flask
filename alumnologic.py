from Logic import Logic


class AlumnoLogic(Logic):
    def __init__(self):
        super().__init__()

    def insertNewAlumno(self, name, age):
        database = self.get_databaseXObj()
        sql = (
            "insert into cardexdb.alumno (id, name, age) "
            + f"values (0, '{name}', {age});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
