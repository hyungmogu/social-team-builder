import unittest
from django.test import TestCase

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Project, Skill, Position
# Create your tests here.


# -----------
# MODEL TESTS
# -----------

"""
USER MODEL
"""
class UserModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='hello',
            password='hello'
        )

        self.user2 = User.objects.create(
            username='world',
            password='world'
        )

    def test_return_user_model_with_query_count_of_2(self):
        expected = 2

        result = User.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_hello_as_username_and_password_when_queried_with_pk_of_1(self):
        expected_username = 'hello'
        expected_password = 'hello'

        user = User.objects.get(pk=1)
        result_username = user.username
        result_password = user.password

        self.assertEqual(expected_username, result_username)
        self.assertEqual(expected_password, result_password)

    def test_return_world_as_username_and_password_when_queried_with_pk_of_2(self):
        expected_username = 'world'
        expected_password = 'world'

        user = User.objects.get(pk=2)
        result_username = user.username
        result_password = user.password

        self.assertEqual(expected_username, result_username)
        self.assertEqual(expected_password, result_password)

    def test_return_username_when_queried_object_is_type_casted(self):
        expected = 'hello'

        result = str(User.objects.get(pk=1))

        self.assertEqual(expected, result)

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
        self.user = User.objects.create(
            username='test',
            password='12345'
        )

        self.skill1 = Skill.objects.create(
            name='Swift'
        )

        self.skill2 = Skill.objects.create(
            name='Java'
        )

        self.skill3 = Skill.objects.create(
            name='C'
        )

        self.project1 = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )

        self.project2 = Project.objects.create(
            title='Test project 2',
            user=self.user,
            timeline='20 days',
            applicant_requirements='Test requirement 2',
            description='Test description 2'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            project=self.project1,
            description='Test description 1'
        )
        self.position1.related_skills.add(self.skill1)

        self.position2 = Position.objects.create(
            name='Test position 2',
            project=self.project2,
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

    def test_return_project_title_test_project_1_given_pk_1(self):
        expected = 'Test project 1'

        query = Position.objects.get(pk=1)
        result = query.project.title

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

    def test_return_project_title_test_project_2_given_pk_1(self):
        expected = 'Test project 2'

        query = Position.objects.get(pk=2)
        result = query.project.title

        self.assertEqual(expected, result)


"""
PROJECT MODEL
"""
class TestProjectModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12345'
        )

        self.project1 = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )

        self.project2 = Project.objects.create(
            title='Test project 2',
            user=self.user,
            timeline='20 days',
            applicant_requirements='Test requirement 2',
            description='Test description 2'
        )

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



# -----------
# VIEW TESTS
# -----------

"""
/accounts/sign_up (GET)
"""
class SignUpGETRequestTestCase(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('accounts:sign_up'))

    def test_returns_status_200_on_visit(self):
        expected = 200

        result = self.resp.status_code

        self.assertEqual(expected, result)

    def test_return_layoutHTML_as_template_used(self):
        expected = 'layout.html'

        self.assertTemplateUsed(self.resp, expected)

    def test_return_signinHTML_as_template_used(self):
        expected = 'accounts/signup.html'

        self.assertTemplateUsed(self.resp, expected)

"""
/projects/create
"""
class ProjectCreateGETTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('moe', 'moe@example.com', '12345')
        self.client = APIClient()

    def test_return_status_okay_if_logged_in(self):
        expected = 200

        self.client.login(username='moe', password='12345')
        response = self.client.get(reverse('project_create'))
        result = response.status_code

        self.assertEqual(result, expected)

    @unittest.expectedFailure # will be replaced when login/signup page is created
    def test_return_302_if_not_logged_in(self):
        expected = 302

        response = self.client.get(reverse('project_create'))
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_layoutHtml_as_template_used_if_logged_in(self):
        expected = 'layout.html'

        self.client.login(username='moe', password='12345')
        response = self.client.get(reverse('project_create'))

        self.assertTemplateUsed(response, expected)

    def test_return_projectCreateHtml_as_template_used_if_logged_in(self):
        expected= 'main/project_create.html'

        self.client.login(username='moe', password='12345')
        response = self.client.get(reverse('project_create'))

        self.assertTemplateUsed(response, expected)


class CreateProjectPOSTTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create(
            username='test'
        )
        self.user.set_password('12345') # this approach used to avoid login returns False error
        self.user.save()

        self.project1 = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )

        self.project2 = Project.objects.create(
            title='Test project 2',
            user=self.user,
            timeline='20 days',
            applicant_requirements='Test requirement 2',
            description='Test description 2'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            project=self.project1,
            description='Test description 1'
        )

        self.position2 = Position.objects.create(
            name='Test position 2',
            project=self.project1,
            description='Test description 2'
        )

        self.position3 = Position.objects.create(
            name='Test position 3',
            project=self.project2,
            description='Test description 3'
        )



    @unittest.expectedFailure
    def test_return_302_if_try_to_create_while_not_logged_in(self):
        expected = 302

        response = self.client.post(reverse('project_create'), {
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        })
        result = response.status_code

        self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_return_login_page_if_try_to_create_while_not_logged_in(self):
        expected = 'accounts/signin.html'

        response = self.client.post(reverse('project_create'), {
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        }, follow=True)

        self.assertTemplateUsed(response, expected)


    def test_retrun_projects_model_with_length_3_if_create_successful(self):
        expected = 3

        res = self.client.login(username='test', password='12345')

        response = self.client.post(reverse('project_create'), {
            'positions-TOTAL_FORMS': '1',
            'positions-INITIAL_FORMS': '0',
            'positions-MIN_NUM_FORMS': '0',
            'positions-MAX_NUM_FORMS': '1000',
            'positions-0-name': 'e',
            'positions-0-description': 'f',
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        })

        result = Project.objects.all().count()

        self.assertEqual(expected, result)


    def test_retrun_position_model_with_length_4_if_create_successful(self):
        expected = 4

        res = self.client.login(username='test', password='12345')

        response = self.client.post(reverse('project_create'), {
            'positions-TOTAL_FORMS': '1',
            'positions-INITIAL_FORMS': '0',
            'positions-MIN_NUM_FORMS': '0',
            'positions-MAX_NUM_FORMS': '1000',

            'positions-0-name': 'e',
            'positions-0-description': 'f',

            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        })

        result = Position.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_status_302_if_create_successful(self):
        expected = 302

        self.client.login(username='test', password='12345')
        res = self.client.post(reverse('project_create'), {
            'positions-TOTAL_FORMS': '1',
            'positions-INITIAL_FORMS': '0',
            'positions-MIN_NUM_FORMS': '0',
            'positions-MAX_NUM_FORMS': '1000',
            'positions-0-name': 'e',
            'positions-0-description': 'f',
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        })

        result = res.status_code

        self.assertEqual(expected, result)

    def test_return_projectHTML_as_template_used_if_create_successful(self):
        expected = 'main/project.html'

        self.client.login(username='test', password='12345')
        result = self.client.post(reverse('project_create'), {
            'positions-TOTAL_FORMS': '1',
            'positions-INITIAL_FORMS': '0',
            'positions-MIN_NUM_FORMS': '0',
            'positions-MAX_NUM_FORMS': '1000',
            'positions-0-name': 'e',
            'positions-0-description': 'f',
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        }, follow=True)

        self.assertTemplateUsed(result, expected)