
from application import db

achievement = db.Table(
    "achievement",
    db.Column('score', db.Numeric, comment="分数"),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    """学生信息"""
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    name = db.Column(db.String(64), index=True, comment="姓名" )
    sex = db.Column(db.Boolean, default=True, comment="性别")
    class_number = db.Column(db.String(32), nullable=True, index=True, comment="班级")
    age = db.Column(db.SmallInteger, comment="年龄")
    description = db.Column(db.Text, comment="签名")
    courses = db.relationship(
        'Course', # 模型名称
        secondary=achievement, # 表关系变量
        backref='students', # 当外键反过来获取主键信息时,使用的字段名称,可以自定义,接下来的使用例如: course.students 获取某个课程下所有的学生
        lazy='dynamic'
    )

class Course(db.Model):
    """课程信息"""
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True,comment="主键ID")
    name = db.Column(db.String(64), unique=True,comment="课程名称")