from django.test import TestCase

from django.contrib.auth.models import User

from .models import Project, Skill, Position
# Create your tests here.


# -----------
# MODEL TESTS
# -----------

"""
SKILL MODEL
"""
class TestSkillModel(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(
            name="Swift"
        )

        self.skill2 = Skill.objects.create(
            name="Java"
        )

    def test_return_skill_model_with_query_count_of_2(self):
        expected = 2

        result = Skill.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_name_swift_when_queried_with_pk_of_1(self):
        expected = "Swift"

        query = Skill.objects.get(pk=1)
        result = query.name

        self.assertEqual(expected, result)

    def test_return_name_java_when_queried_with_pk_of_2(self):
        expected = "Java"

        query = Skill.objects.get(pk=2)
        result = query.name

        self.assertEqual(expected, result)

    def test_return_skill_name_when_type_casted_as_str(self):
        expected = "Java"


        query = Skill.objects.get(pk=2)
        result = str(query)

        self.assertEqual(expected, result)


"""
POSITION MODEL
"""
class TestPositionModel(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(
            name='Swift'
        )

        self.skill2 = Skill.objects.create(
            name='Java'
        )

        self.skill3 = Skill.objects.create(
            name='C'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            description='Test description 1'
        )
        self.position1.related_skills.add(self.skill1)

        self.position2 = Position.objects.create(
            name='Test position 2',
            description='Test description 2'
        )
        self.position2.related_skills.add(self.skill2)
        self.position2.related_skills.add(self.skill3)

    def test_return_position_model_with_length_2(self):
        expected = 2

        result = Position.objects.all().count()

        self.assertEqual(result, expected)


    def test_return_name_test_position_1_given_pk_1(self):
        expected = 'Test position 1'

        query = Position.objects.get(pk=1)
        result = query.name

        self.assertEqual(expected, result)

    def test_return_description_test_description_1_given_pk_1(self):
        expected = 'Test description 1'

        query = Position.objects.get(pk=1)
        result = query.description

        self.assertEqual(expected, result)

    def test_return_related_skills_with_length_1_given_pk_1(self):
        expected = 1

        query = Position.objects.get(pk=1)
        result = query.related_skills.count()

        self.assertEqual(expected, result)

    def test_return_swift_as_first_related_skill_given_pk_2(self):
        expected = 'Swift'

        query = Position.objects.get(pk=1)
        related_skills = query.related_skills.all()
        result = related_skills[0].name

        self.assertEqual(expected, result)

    def test_return_name_test_position_2_given_pk_2(self):
        expected = 'Test position 2'

        query = Position.objects.get(pk=2)
        result = query.name

        self.assertEqual(expected, result)

    def test_return_name_test_description_2_given_pk_2(self):
        expected = 'Test description 2'

        query = Position.objects.get(pk=2)
        result = query.description

        self.assertEqual(expected, result)

    def test_return_related_skills_with_length_2_given_pk_2(self):
        expected = 2

        query = Position.objects.get(pk=2)
        result = query.related_skills.count()

        self.assertEqual(expected, result)

    def test_return_Java_as_first_related_skill_given_pk_2(self):
        expected = 'Java'

        query = Position.objects.get(pk=2)
        related_skills = query.related_skills.all()
        result = related_skills[0].name

        self.assertEqual(expected, result)


    def test_return_C_as_first_related_skill_given_pk_2(self):
        expected = 'C'

        query = Position.objects.get(pk=2)
        related_skills = query.related_skills.all()
        result = related_skills[1].name

        self.assertEqual(expected, result)

    def test_return_name_when_type_casted_as_str(self):
        expected = ''


"""
PROJECT MODEL
"""
class TestProjectModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12345'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            description='Test description 1'
        )

        self.position2 = Position.objects.create(
            name='Test position 2',
            description='Test description 2'
        )

        self.position3 = Position.objects.create(
            name='Test position 3',
            description='Test description 3'
        )

        self.project1 = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )
        self.project1.needs.add(self.position1)

        self.project2 = Project.objects.create(
            title='Test project 2',
            user=self.user,
            timeline='20 days',
            applicant_requirements='Test requirement 2',
            description='Test description 2'
        )
        self.project2.needs.add(self.position2)
        self.project2.needs.add(self.position3)

    def test_return_project_model_with_length_2(self):
        expected = 2

        result = Project.objects.all().count()

        self.assertEqual(expected, result)


    def test_return_title_test_project_1_given_pk_1(self):
        expected = 'Test project 1'

        query = Project.objects.get(pk=1)
        result = str(query)

        self.assertEqual(expected, result)

    def test_return_user_with_username_test_given_pk_1(self):
        expected = 'test'

        query = Project.objects.get(pk=1)
        result = query.user.username

        self.assertEqual(expected, result)

    def test_return_needs_with_length_1_given_pk_1(self):
        expected = 1

        query = Project.objects.get(pk=1)
        result = query.needs.all().count()

        self.assertEqual(expected, result)

    def test_return_test_position_1_as_first_need_given_pk_1(self):
        expected = 'Test position 1'

        query = Project.objects.get(pk=1)
        needs = query.needs.all()
        result = needs[0].name

        self.assertEqual(expected, result)

    def test_return_timeline_10_days_given_pk_1(self):
        expected = '10 days'

        query = Project.objects.get(pk=1)
        result = query.timeline

        self.assertEqual(expected, result)


    def test_return_applicant_requirements_test_requirement_1_given_pk_1(self):
        expected = 'Test requirement 1'

        query = Project.objects.get(pk=1)
        result = query.applicant_requirements

        self.assertEqual(expected, result)

    def test_return_description_test_description_1_given_pk_1(self):
        expected = 'Test description 1'

        query = Project.objects.get(pk=1)
        result = query.description

        self.assertEqual(expected, result)

    def test_return_title_test_project_2_given_pk_2(self):
        expected = 'Test project 2'

        query = Project.objects.get(pk=2)
        result = str(query)

        self.assertEqual(expected, result)

    def test_return_user_with_username_test_given_pk_2(self):
        expected = 'test'

        query = Project.objects.get(pk=2)
        result = query.user.username

        self.assertEqual(expected, result)

    def test_return_needs_with_length_2_given_pk_2(self):
        expected = 2

        query = Project.objects.get(pk=2)
        result = query.needs.all().count()

        self.assertEqual(expected, result)

    def test_return_test_position_2_as_first_need_given_pk_2(self):
        expected = 'Test position 2'

        query = Project.objects.get(pk=2)
        needs = query.needs.all()
        result = needs[0].name

        self.assertEqual(expected, result)

    def test_return_test_position_3_as_second_need_given_pk_2(self):
        expected = 'Test position 3'

        query = Project.objects.get(pk=2)
        needs = query.needs.all()
        result = needs[1].name

        self.assertEqual(expected, result)

    def test_return_timeline_20_days_given_pk_2(self):
        expected = '20 days'

        query = Project.objects.get(pk=2)
        result = query.timeline

        self.assertEqual(expected, result)


    def test_return_applicant_requirements_test_requirement_2_given_pk_2(self):
        expected = 'Test requirement 2'

        query = Project.objects.get(pk=2)
        result = query.applicant_requirements

        self.assertEqual(expected, result)

    def test_return_description_test_description_2_given_pk_2(self):
        expected = 'Test description 2'

        query = Project.objects.get(pk=2)
        result = query.description

        self.assertEqual(expected, result)

    def test_return_name_when_type_casted_as_str_for_pk_1(self):
        expected = 'Test project 1'

        query = Project.objects.get(pk=1)
        result = str(query)

        self.assertEqual(expected, result)