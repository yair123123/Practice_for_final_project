from app.dbs.files.json_repo import load_json_data
from app.dbs.psql.service.save_in_psql import *


def fill_data_to_psql():
    data_from_json = load_json_data("academic_network.json")
    save_student("students-profiles.csv")
    save_lifestyle("student_lifestyle.csv")
    save_course("student_course_performance.csv")
    save_classes(data_from_json)
    save_teachers(data_from_json)
    save_relationship(data_from_json)