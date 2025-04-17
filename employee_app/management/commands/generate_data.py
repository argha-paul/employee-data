from django.core.management.base import BaseCommand
from employee_app.models import Employee, Department, Attendance
from faker import Faker
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']
        dept_objs = []

        for dept_name in departments:
            dept = Department.objects.create(name=dept_name, description=fake.text(50))
            dept_objs.append(dept)

        employees = []
        for _ in range(5):  # create 5 employees
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=random.choice(dept_objs),
                hire_date=fake.date_between(start_date='-2y', end_date='today'),
                salary=random.randint(50000, 150000)
            )
            employees.append(emp)

        for emp in employees:
            for day in range(1, 6):  # attendance for last 5 days
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_month(),
                    status=random.choice(['Present', 'Absent'])
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated employee data!'))