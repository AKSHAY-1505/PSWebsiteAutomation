from TestAssesmentMethods import TestAssesmentMethods


class TestAssesment():
    def test_assesment_1(self):
        obj = TestAssesmentMethods()

        obj.admin_login()
        obj.redirect_to_report_benifit()
        obj.select_employee_status()
        obj.check_unmask_ssn()
        obj.select_plan_year()
        obj.select_benefit_type()
        obj.select_plan()
        obj.select_plan_fields()
        obj.select_available_employee_fields()
        obj.run_report()


obj = TestAssesment()
obj.test_assesment_1()