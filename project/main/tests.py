import unittest
from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from django.core.urlresolvers import reverse
from accounts.models import User
from rest_framework.test import APIClient

from .models import Project, Skill, Position, Profile
# Create your tests here.

# -----------
# MODEL TESTS
# -----------

# # """
# # USER MODEL
# # """
# class UserModelTestCase(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#             email='hyungmo@helloworld.com',
#             password='hello'
#         )

#         self.user2 = User.objects.create(
#             email='world@helloworld.com',
#             password='world'
#         )

#     def test_return_user_model_with_query_count_of_2(self):
#         expected = 2

#         result = User.objects.all().count()

#         self.assertEqual(expected, result)

#     def test_return_hyungmo_as_email_and_password_when_queried_with_pk_of_1(self):
#         expected_email = 'hyungmo@helloworld.com'
#         expected_password = 'hello'

#         user = User.objects.get(pk=1)
#         result_email = user.email
#         result_password = user.password

#         self.assertEqual(expected_email, result_email)
#         self.assertEqual(expected_password, result_password)

#     def test_return_world_as_email_and_password_when_queried_with_pk_of_2(self):
#         expected_email = 'world@helloworld.com'
#         expected_password = 'world'

#         user = User.objects.get(pk=2)
#         result_email = user.email
#         result_password = user.password

#         self.assertEqual(expected_email, result_email)
#         self.assertEqual(expected_password, result_password)

#     def test_return_email_when_queried_object_is_type_casted(self):
#         expected = 'hyungmo@helloworld.com'

#         result = str(User.objects.get(pk=1))

#         self.assertEqual(expected, result)

# """
# PROFILE MODEL
# """

# class TestProfileModel(TestCase):
#     def setUp(self):

#         self.user1 = User.objects.create(
#             email='hyungmo@helloworld.com',
#             password='hello'
#         )

#         self.user2 = User.objects.create(
#             email='world@helloworld.com',
#             password='world'
#         )

#         self.profile1 = Profile.objects.create(
#             user=self.user1,
#             name='Profile 1',
#             short_bio='Bio 1',
#             profile_image = 'image_1.png'
#         )

#         self.profile2 = Profile.objects.create(
#             user=self.user2,
#             name='Profile 2',
#             short_bio='Bio 2',
#             profile_image = 'image_2.png'
#         )

#     def test_return_profiles_of_length_2_when_all_queried(self):
#         expected = 2

#         result = Profile.objects.all().count()

#         self.assertEqual(expected, result)

#     @unittest.expectedFailure
#     def test_return_error_when_profile_of_same_user_id_is_created(self):
#         profile3 = Profile.objects.create(
#             user=self.user1,
#             name='Hello',
#             short_bio='this is a short bio'
#         )

#         profile4 = Profile.objects.create(
#             user=self.user1,
#             name='Hello',
#             short_bio='this is a short bio'
#         )


#     def test_return_name_profile_1_when_queried_with_pk_of_1(self):
#         expected = "Profile 1"

#         query = Profile.objects.get(pk=1)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_short_bio_bio_1_when_queried_with_pk_of_1(self):
#         expected = "Bio 1"

#         query = Profile.objects.get(pk=1)
#         result = query.short_bio

#         self.assertEqual(expected, result)

#     def test_return_profile_image_image_1_when_queried_with_pk_of_1(self):
#         expected = "image_1.png"

#         query = Profile.objects.get(pk=1)
#         result = query.profile_image.name

#         self.assertEqual(expected, result)


#     def test_return_name_profile_2_when_queried_with_pk_of_2(self):
#         expected = "Profile 2"

#         query = Profile.objects.get(pk=2)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_short_bio_bio_2_when_queried_with_pk_of_2(self):
#         expected = "Bio 2"

#         query = Profile.objects.get(pk=2)
#         result = query.short_bio

#         self.assertEqual(expected, result)

#     def test_return_profile_image_image_2_when_queried_with_pk_of_2(self):
#         expected = "image_2.png"

#         query = Profile.objects.get(pk=2)
#         result = query.profile_image.name

#         self.assertEqual(expected, result)



# """
# SKILL MODEL
# """
# class TestSkillModel(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#             email='hyungmo@helloworld.com',
#             password='hello'
#         )

#         self.user2 = User.objects.create(
#             email='world@helloworld.com',
#             password='world'
#         )

#         self.profile1 = Profile.objects.create(
#             user=self.user1,
#             name='Profile 1',
#             short_bio='Bio 1',
#             profile_image = 'image_1.png'
#         )

#         self.profile2 = Profile.objects.create(
#             user=self.user2,
#             name='Profile 2',
#             short_bio='Bio 2',
#             profile_image = 'image_2.png'
#         )

#         self.skill1 = Skill.objects.create(
#             name="Swift",
#             profile= self.profile1
#         )

#         self.skill2 = Skill.objects.create(
#             name="Java",
#             profile= self.profile2
#         )

#     def test_return_skill_model_with_query_count_of_2(self):
#         expected = 2

#         result = Skill.objects.all().count()

#         self.assertEqual(expected, result)

#     def test_return_name_swift_when_queried_with_pk_of_1(self):
#         expected = "Swift"

#         query = Skill.objects.get(pk=1)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_profile_profile_1_when_queried_with_pk_of_1(self):
#         expected = "Profile 1"

#         query = Skill.objects.get(pk=1)
#         result = query.profile.name

#         self.assertEqual(expected, result)

#     def test_return_name_java_when_queried_with_pk_of_2(self):
#         expected = "Java"

#         query = Skill.objects.get(pk=2)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_profile_profile_2_when_queried_with_pk_of_2(self):
#         expected = "Profile 2"

#         query = Skill.objects.get(pk=2)
#         result = query.profile.name

#         self.assertEqual(expected, result)

#     def test_return_skill_name_when_type_casted_as_str(self):
#         expected = "Java"

#         query = Skill.objects.get(pk=2)
#         result = str(query)

#         self.assertEqual(expected, result)


# # """
# # POSITION MODEL
# # """
# class TestPositionModel(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create(
#             email='hyungmo@helloworld.com',
#             password='hello'
#         )

#         self.user2 = User.objects.create(
#             email='world@helloworld.com',
#             password='world'
#         )

#         self.profile1 = Profile.objects.create(
#             user=self.user1,
#             name='Profile 1',
#             short_bio='Bio 1',
#             profile_image = 'image_1.png'
#         )

#         self.profile2 = Profile.objects.create(
#             user=self.user2,
#             name='Profile 2',
#             short_bio='Bio 2',
#             profile_image = 'image_2.png'
#         )

#         self.skill1 = Skill.objects.create(
#             name='Swift',
#             profile=self.profile1
#         )

#         self.skill2 = Skill.objects.create(
#             name='Java',
#             profile=self.profile1
#         )

#         self.skill3 = Skill.objects.create(
#             name='C',
#             profile=self.profile2
#         )

#         self.project1 = Project.objects.create(
#             title='Test project 1',
#             user=self.user1,
#             timeline='10 days',
#             applicant_requirements='Test requirement 1',
#             description='Test description 1'
#         )

#         self.project2 = Project.objects.create(
#             title='Test project 2',
#             user=self.user2,
#             timeline='20 days',
#             applicant_requirements='Test requirement 2',
#             description='Test description 2'
#         )

#         self.position1 = Position.objects.create(
#             name='Test position 1',
#             project=self.project1,
#             description='Test description 1'
#         )
#         self.position1.related_skills.add(self.skill1)
#         self.position1.related_skills.add(self.skill2)

#         self.position2 = Position.objects.create(
#             name='Test position 2',
#             project=self.project2,
#             description='Test description 2'
#         )
#         self.position2.related_skills.add(self.skill3)

#     def test_return_position_model_with_length_2(self):
#         expected = 2

#         result = Position.objects.all().count()

#         self.assertEqual(result, expected)


#     def test_return_name_test_position_1_given_pk_1(self):
#         expected = 'Test position 1'

#         query = Position.objects.get(pk=1)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_project_title_test_project_1_given_pk_1(self):
#         expected = 'Test project 1'

#         query = Position.objects.get(pk=1)
#         result = query.project.title

#         self.assertEqual(expected, result)

#     def test_return_description_test_description_1_given_pk_1(self):
#         expected = 'Test description 1'

#         query = Position.objects.get(pk=1)
#         result = query.description

#         self.assertEqual(expected, result)

#     def test_return_related_skills_with_length_2_given_pk_1(self):
#         expected = 2

#         query = Position.objects.get(pk=1)
#         result = query.related_skills.count()

#         self.assertEqual(expected, result)

#     def test_return_swift_as_first_related_skill_given_pk_1(self):
#         expected = 'Swift'

#         query = Position.objects.get(pk=1)
#         related_skills = query.related_skills.all()
#         result = related_skills[0].name

#         self.assertEqual(expected, result)


#     def test_return_Java_as_second_related_skill_given_pk_1(self):
#         expected = 'Java'

#         query = Position.objects.get(pk=1)
#         related_skills = query.related_skills.all()
#         result = related_skills[1].name

#         self.assertEqual(expected, result)

#     def test_return_name_test_position_2_given_pk_2(self):
#         expected = 'Test position 2'

#         query = Position.objects.get(pk=2)
#         result = query.name

#         self.assertEqual(expected, result)

#     def test_return_name_test_description_2_given_pk_2(self):
#         expected = 'Test description 2'

#         query = Position.objects.get(pk=2)
#         result = query.description

#         self.assertEqual(expected, result)

#     def test_return_related_skills_with_length_2_given_pk_2(self):
#         expected = 1

#         query = Position.objects.get(pk=2)
#         result = query.related_skills.count()

#         self.assertEqual(expected, result)

#     def test_return_C_as_first_related_skill_given_pk_2(self):
#         expected = 'C'

#         query = Position.objects.get(pk=2)
#         related_skills = query.related_skills.all()
#         result = related_skills[0].name

#         self.assertEqual(expected, result)

#     def test_return_name_when_type_casted_as_str(self):
#         expected = 'Test position 1'

#         res = Position.objects.get(pk=1)
#         result = res.name

#         self.assertEqual(expected, result)


#     def test_return_project_title_test_project_2_given_pk_1(self):
#         expected = 'Test project 2'

#         query = Position.objects.get(pk=2)
#         result = query.project.title

#         self.assertEqual(expected, result)


# """
# PROJECT MODEL
# """
# class TestProjectModel(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             username='test',
#             password='12345'
#         )

#         self.project1 = Project.objects.create(
#             title='Test project 1',
#             user=self.user,
#             timeline='10 days',
#             applicant_requirements='Test requirement 1',
#             description='Test description 1'
#         )

#         self.project2 = Project.objects.create(
#             title='Test project 2',
#             user=self.user,
#             timeline='20 days',
#             applicant_requirements='Test requirement 2',
#             description='Test description 2'
#         )

#     def test_return_project_model_with_length_2(self):
#         expected = 2

#         result = Project.objects.all().count()

#         self.assertEqual(expected, result)


#     def test_return_title_test_project_1_given_pk_1(self):
#         expected = 'Test project 1'

#         query = Project.objects.get(pk=1)
#         result = str(query)

#         self.assertEqual(expected, result)

#     def test_return_user_with_username_test_given_pk_1(self):
#         expected = 'test'

#         query = Project.objects.get(pk=1)
#         result = query.user.username

#         self.assertEqual(expected, result)

#     def test_return_timeline_10_days_given_pk_1(self):
#         expected = '10 days'

#         query = Project.objects.get(pk=1)
#         result = query.timeline

#         self.assertEqual(expected, result)


#     def test_return_applicant_requirements_test_requirement_1_given_pk_1(self):
#         expected = 'Test requirement 1'

#         query = Project.objects.get(pk=1)
#         result = query.applicant_requirements

#         self.assertEqual(expected, result)

#     def test_return_description_test_description_1_given_pk_1(self):
#         expected = 'Test description 1'

#         query = Project.objects.get(pk=1)
#         result = query.description

#         self.assertEqual(expected, result)

#     def test_return_title_test_project_2_given_pk_2(self):
#         expected = 'Test project 2'

#         query = Project.objects.get(pk=2)
#         result = str(query)

#         self.assertEqual(expected, result)

#     def test_return_user_with_username_test_given_pk_2(self):
#         expected = 'test'

#         query = Project.objects.get(pk=2)
#         result = query.user.username

#         self.assertEqual(expected, result)

#     def test_return_timeline_20_days_given_pk_2(self):
#         expected = '20 days'

#         query = Project.objects.get(pk=2)
#         result = query.timeline

#         self.assertEqual(expected, result)

#     def test_return_applicant_requirements_test_requirement_2_given_pk_2(self):
#         expected = 'Test requirement 2'

#         query = Project.objects.get(pk=2)
#         result = query.applicant_requirements

#         self.assertEqual(expected, result)

#     def test_return_description_test_description_2_given_pk_2(self):
#         expected = 'Test description 2'

#         query = Project.objects.get(pk=2)
#         result = query.description

#         self.assertEqual(expected, result)

#     def test_return_name_when_type_casted_as_str_for_pk_1(self):
#         expected = 'Test project 1'

#         query = Project.objects.get(pk=1)
#         result = str(query)

#         self.assertEqual(expected, result)


# -----------
# VIEW TESTS
# -----------

"""
/accounts/login (GET)
"""
class LoginGETRequest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('accounts:login'))

    def test_returns_status_200_on_visit(self):
        expected = 200

        result = self.resp.status_code

        self.assertEqual(expected, result)

    def test_return_layoutHTML_as_template_used(self):
        expected = 'layout.html'

        self.assertTemplateUsed(self.resp, expected)

    def test_return_signinHTML_as_template_used(self):
        expected = 'accounts/signin.html'

        self.assertTemplateUsed(self.resp, expected)


"""
/accounts/login (POST)
"""
class LoginPOSTRequest(TestCase):
    def setUp(self):
        self.resp = self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

    def test_return_to_sign_in_page_if_signup_unsuccessful(self):
        expected = 'accounts/signin.html'

        response1 = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello1'
        })

        response2 = self.client.post(reverse('accounts:login'), {
            'username': 'hello@ example.com',
            'password': 'hello1'
        })

        self.assertTemplateUsed(response1, expected)
        self.assertTemplateUsed(response2, expected)

    def test_return_to_home_page_if_login_successful(self):
        resp = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        self.assertRedirects(resp, reverse('home'), fetch_redirect_response=False)


"""
/accounts/sign_up (GET)
"""
class SignUpGETRequest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('accounts:sign_up'))

    def test_returns_status_200_on_visit(self):
        expected = 200

        result = self.resp.status_code

        self.assertEqual(expected, result)

    def test_return_layoutHTML_as_template_used(self):
        expected = 'layout.html'

        self.assertTemplateUsed(self.resp, expected)

    def test_return_signupHTML_as_template_used(self):
        expected = 'accounts/signup.html'

        self.assertTemplateUsed(self.resp, expected)


"""
/accounts/sign_up (POST)
"""
class SignUpPOSTRequest(TestCase):
    def setUp(self):
        self.resp = self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

    def test_return_to_sign_up_page_if_signup_unsuccessful(self):
        expected = 'accounts/signup.html'

        response1 = self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello1',
            'password2': 'hello2'
        })

        response2 = self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@ example.com',
            'password1': 'hello1',
            'password2': 'hello1'
        })

        self.assertTemplateUsed(response1, expected)
        self.assertTemplateUsed(response2, expected)

    def test_return_user_model_with_count_of_1_if_signup_successful(self):
        expected = 1

        result = User.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_to_login_page_if_signup_successful(self):
        self.assertRedirects(self.resp, reverse('accounts:login'), fetch_redirect_response=True)



# """
# /profile/{id}
# """

class ProfileGETTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='hyungmo@helloworld.com',
            password='hello'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            name='Test Profile 1',
            short_bio='Test Bio 1',
            profile_image = 'image_1.png'
        )

        self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        })


    def test_return_status_code_200_if_successful(self):
        expected = 200

        response = self.client.get(reverse('profile', kwargs={
            'pk': 1
        }))

        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_profileHTML_as_template_used(self):
        expected= 'main/profile.html'



        response = self.client.get(reverse('profile', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_layoutHTML_as_template_used(self):
        expected= 'layout.html'

        response = self.client.get(reverse('profile', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_correctly_used_profile(self):
        expected = 'Test Profile 1'

        response = self.client.get(reverse('profile', kwargs={
            'pk': 1
        }), follow=True)

        result = response.context['profile'].name

        self.assertEqual(expected, result)



# """
# /projects/{id}
# """

class ProjectGETTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='hyungmo@helloworld.com',
            password='hello'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            name='Test Profile 1',
            short_bio='Test Bio 1',
            profile_image = 'image_1.png'
        )

        self.project = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            project=self.project,
            description='Test description 1'
        )

        self.position2 = Position.objects.create(
            name='Test position 2',
            project=self.project,
            description='Test description 2'
        )

    def test_return_status_code_200_if_successful(self):
        expected = 200

        response = self.client.get(reverse('project', kwargs={
            'pk': 1
        }))

        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_projectHTML_as_template_used(self):
        expected= 'main/project.html'

        response = self.client.get(reverse('project', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_layoutHTML_as_template_used(self):
        expected= 'layout.html'

        response = self.client.get(reverse('project', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_project_1_as_the_project_used(self):
        expected = 'Test project 1'

        response = self.client.get(reverse('project', kwargs={
            'pk': 1
        }), follow=True)

        result = response.context['project'].title

        self.assertEqual(expected, result)


# """
# /projects/{id}/edit
# """

class EditProjectGETRequest(TestCase):
    def setUp(self):
        self.resp = self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.user = User.objects.get(pk=1)
        self.profile = self.user.profile
        self.profile.name = 'Test Profile 1'
        self.profile.short_bio = 'Test Bio 1'
        self.profile.profile_image = 'image_1.png'

        self.project = Project.objects.create(
            title='Test project 1',
            user=self.user,
            timeline='10 days',
            applicant_requirements='Test requirement 1',
            description='Test description 1'
        )

        self.position1 = Position.objects.create(
            name='Test position 1',
            project=self.project,
            description='Test description 1'
        )

        self.position2 = Position.objects.create(
            name='Test position 2',
            project=self.project,
            description='Test description 2'
        )

    def test_return_status_code_200_if_successful(self):
        expected = 200

        resp = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        })

        response = self.client.get(reverse('project_edit', kwargs={
            'pk': 1
        }))

        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_projectHTML_as_template_used(self):
        expected= 'main/project_edit.html'

        resp = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        })

        response = self.client.get(reverse('project_edit', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_layoutHTML_as_template_used(self):
        expected= 'layout.html'

        resp = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        })

        response = self.client.get(reverse('project_edit', kwargs={
            'pk': 1
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_project_1_as_the_project_used(self):
        expected = 'Test project 1'

        resp = self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        })

        response = self.client.get(reverse('project_edit', kwargs={
            'pk': 1
        }), follow=True)

        result = response.context['project'].title

        self.assertEqual(expected, result)



class EditProjectPOSTRequest(TestCase):
    def setUp(self):
        self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.user = User.objects.get(pk=1)

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

        self.edit_data = {
            'positions-TOTAL_FORMS': '2',
            'positions-INITIAL_FORMS': '0',
            'positions-MIN_NUM_FORMS': '0',
            'positions-MAX_NUM_FORMS': '1000',
            'positions-0-name': 'e1',
            'positions-0-description': 'f1',
            'positions-1-name': 'g',
            'positions-1-description': 'h',
            'project-title': 'Revised test project 1',
            'project-user': self.user,
            'project-timeline': 'Revised timeline 1',
            'project-description':'Revised description 1',
            'project-applicant_requirements': 'Revised applicant requirements 1'
        }


    def test_return_302_if_try_to_edit_while_not_logged_in(self):
        expected = 302

        response = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), {
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        })
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_login_page_if_try_to_create_while_not_logged_in(self):
        expected = 'accounts/signin.html'

        response = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), {
            'project-title': 'Test project 3',
            'project-user': self.user,
            'project-timeline': 'This is test timeline 3',
            'project-description':'This is test description 3',
            'project-applicant_requirements': 'This is test applicant requirements'
        }, follow=True)

        self.assertTemplateUsed(response, expected)

    def test_retrun_project_with_title_revised_test_project_1_if_edit_successful(self):
        expected = 'Revised test project 1'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        self.resp = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), self.edit_data)

        result = Project.objects.get(pk=1).title

        self.assertEqual(expected, result)


    def test_retrun_project_timeline_revised_timeline_1_if_edit_successful(self):
        expected = 'Revised timeline 1'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        self.resp = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), self.edit_data)

        result = Project.objects.get(pk=1).timeline

        self.assertEqual(expected, result)

    def test_retrun_project_description_revised_description_1_if_edit_successful(self):
        expected = 'Revised description 1'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        self.resp = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), self.edit_data)

        result = Project.objects.get(pk=1).description

        self.assertEqual(expected, result)

    def test_retrun_project_description_revised_applicant_requirements_1_if_edit_successful(self):
        expected = 'Revised applicant requirements 1'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        self.resp = self.client.post(reverse('project_edit', kwargs={
            'pk': 1
        }), self.edit_data)

        result = Project.objects.get(pk=1).applicant_requirements

        self.assertEqual(expected, result)


    def test_return_status_302_if_edit_successful(self):
        expected = 302

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        res = self.client.post(reverse('project_create'), self.edit_data)

        result = res.status_code

        self.assertEqual(expected, result)

    def test_return_projectHTML_as_template_used_if_edit_successful(self):
        expected = 'main/project.html'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        result = self.client.post(reverse('project_create'), self.edit_data, follow=True)

        self.assertTemplateUsed(result, expected)

# """
# /projects/create
# """
class CreateProjectGETRequest(TestCase):
    def setUp(self):
        self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.client = APIClient()

    def test_return_status_200_if_logged_in(self):
        expected = 200

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        response = self.client.get(reverse('project_create'), follow=True)

        result = response.status_code

        self.assertEqual(result, expected)

    def test_return_302_if_not_logged_in(self):
        expected = 302

        response = self.client.get(reverse('project_create'))
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_login_page_if_not_logged_in(self):
        expected = 'accounts/signin.html'

        result = self.client.get(reverse('project_create'), follow=True)

        self.assertTemplateUsed(result, expected)

    def test_return_projectCreateHtml_as_template_used_if_logged_in(self):
        expected= 'main/project_create.html'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        response = self.client.get(reverse('project_create'), follow=True)

        self.assertTemplateUsed(response, expected)

class CreateProjectPOSTRequest(TestCase):
    def setUp(self):
        self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.user = User.objects.get(pk=1)

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

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

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

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

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

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

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

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

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

"""
/projects/delete
"""
class DeleteProjectGETRequest(TestCase):
    def setUp(self):
        self.client.post(reverse('accounts:sign_up'), {
            'email': 'hello@example.com',
            'password1': 'hello!234',
            'password2': 'hello!234'
        })

        self.user = User.objects.get(pk=1)

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

    def test_return_200_if_delete_while_logged_in(self):
        expected = 200

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        response = self.client.get(reverse('project_delete', kwargs={
            'pk': self.project1.pk
        }))

        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_layoutHTML_as_template_used(self):
        expected = 'layout.html'

        response = self.client.get(reverse('project_delete', kwargs={
            'pk': self.project1.pk
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_project_deleteHTML_as_template_used(self):
        expected = 'main/project_delete.html'

        self.client.post(reverse('accounts:login'), {
            'username': 'hello@example.com',
            'password': 'hello!234'
        }, follow=True)

        response = self.client.get(reverse('project_delete', kwargs={
            'pk': self.project1.pk
        }), follow=True)

        self.assertTemplateUsed(response, expected)

    def test_return_302_if_try_to_delete_while_not_logged_in(self):
        expected = 302

        response = self.client.get(reverse('project_delete', kwargs={
            'pk': self.project1.pk
        }))

        result = response.status_code

        self.assertEqual(expected, result)


    def test_return_to_sign_in_if_try_to_delete_while_not_logged_in(self):
        expected = 'accounts/signin.html'

        response = self.client.get(reverse('project_delete', kwargs={
            'pk': self.project1.pk
        }), follow=True)

        self.assertTemplateUsed(response, expected)
