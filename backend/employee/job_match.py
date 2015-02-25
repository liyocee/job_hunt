from employer.models import EmployerJobs


class JobMatch(object):

    def __init__(self, employee, jobs):
        self.employee = employee
        self.jobs = jobs

    def matches(self):
        matches = set()
        skills = [skill['id'] for skill in self.employee.skills.values()]
        industries = [indu['id'] for indu in self.employee.industry.values()]
        # match by skill
        for skill in skills:
            temp_jobs = self.jobs.filter(
                skills__in=skills, is_active=True)
            if temp_jobs:
                matches.update(self.get_employer_ids(temp_jobs))

        # filter by industry
        temp_jobs = self.jobs.filter(
            industry__in=industries
        )
        matches.update(self.get_employer_ids(temp_jobs))

        return EmployerJobs.objects.filter(id__in=matches)

    def get_employer_ids(self, jobs):
        ids = []
        for job in jobs:
            emp = EmployerJobs.objects.get(job=job)
            ids.append(emp.pk)

        return ids
