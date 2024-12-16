from typing import List, Dict

from app.dbs.files.csv_repo import load_data
from app.dbs.psql.models import Student, Lifestyle, CoursePerformance, Class, Teacher, Relationship
from app.dbs.psql.repository.class_repo import insert_class
from app.dbs.psql.repository.course_performance_repo import insert_course_performance
from app.dbs.psql.repository.lifestyle_repo import insert_lifestyle
from app.dbs.psql.repository.relationships_repo import insert_relationship
from app.dbs.psql.repository.student_repo import insert_student
from app.dbs.psql.repository.teacher_repo import insert_teacher


def save_student(filename):
    for chunk in load_data(filename):
        students_models = [Student(**student.to_dict()) for _, student in chunk.iterrows()]
        results = [insert_student(student).value_or("Problem") for student in students_models]
        print(results)


def save_lifestyle(filename):
    for chunk in load_data(filename):
        lifestyle_models = [Lifestyle(**lifestyle.to_dict()) for _, lifestyle in chunk.iterrows()]
        results = [insert_lifestyle(lifestyle).value_or("Problem") for lifestyle in lifestyle_models]
        print(results)


def save_course(filename):
    for chunk in load_data(filename):
        course_performance_models = [CoursePerformance(**course_performance.to_dict()) for _, course_performance in
                                     chunk.iterrows()]
        results = [insert_course_performance(course_performance).value_or("Problem") for course_performance in
                   course_performance_models]
        print(results)


def save_classes(Dict_from_json: Dict[str, List[Dict[str, str]]]):
    classes_model = [Class(**class_to_model) for class_to_model in Dict_from_json["classes"]]
    results = [insert_class(class_model).value_or("Problem") for class_model in classes_model]
    print(results)


def save_teachers(Dict_from_json: Dict[str, List[Dict[str, str]]]):
    classes_model = [Teacher(**class_to_model) for class_to_model in Dict_from_json["teachers"]]
    results = [insert_teacher(class_model).value_or("Problem") for class_model in classes_model]
    print(results)


def save_relationship(Dict_from_json: Dict[str, List[Dict[str, str]]]):
    classes_model = [Relationship(**class_to_model) for class_to_model in Dict_from_json["relationships"]]
    results = [insert_relationship(class_model).value_or("Problem") for class_model in classes_model]
    print(results)
