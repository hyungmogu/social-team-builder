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



"""
VIEW MODEL
"""
# class ProjectCreateGETTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('moe', 'moe@example.com', '12345')
#         self.client = APIClient()

#     def test_return_status_okay_if_logged_in(self):
#         expected = 200

#         self.client.login(username='moe', password='12345')
#         response = self.client.get(reverse('project_create'))
#         result = response.status_code

#         self.assertEqual(result, expected)

#     def test_return_302_if_not_logged_in(self):
#         expected = 302

#         response = self.client.get(reverse('item_edit', kwargs={'pk': 1}))
#         result = response.status_code

#         self.assertEqual(expected, result)

#     def test_return_layoutHtml_as_template_used_if_logged_in(self):
#         expected = 'layout.html'

#         self.client.login(username='moe', password='12345')
#         response = self.client.get(reverse('item_edit', kwargs={'pk': 1}))

#         self.assertTemplateUsed(response, expected)

#     def test_return_itemEditHtml_as_template_used_if_logged_in(self):
#         expected= 'menu/item_edit.html'

#         self.client.login(username='moe', password='12345')
#         response = self.client.get(reverse('item_edit', kwargs={'pk': 1}))

#         self.assertTemplateUsed(response, expected)


# class CreateProjectPOSTTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('laceywill', 'laceywill@example.com', '12345')
#  self.user = User.objects.create(
#             username='test',
#             password='12345'
#         )

#         self.position1 = Position.objects.create(
#             name='Test position 1',
#             description='Test description 1'
#         )

#         self.position2 = Position.objects.create(
#             name='Test position 2',
#             description='Test description 2'
#         )

#         self.position3 = Position.objects.create(
#             name='Test position 3',
#             description='Test description 3'
#         )

#         self.project1 = Project.objects.create(
#             title='Test project 1',
#             user=self.user,
#             timeline='10 days',
#             applicant_requirements='Test requirement 1',
#             description='Test description 1'
#         )
#         self.project1.needs.add(self.position1)

#         self.project2 = Project.objects.create(
#             title='Test project 2',
#             user=self.user,
#             timeline='20 days',
#             applicant_requirements='Test requirement 2',
#             description='Test description 2'
#         )
#         self.project2.needs.add(self.position2)
#         self.project2.needs.add(self.position3)

#     def test_return_302_if_try_to_edit_while_not_logged_in(self):
#         expected = 302

#         response = self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         })
#         result = response.status_code

#         self.assertEqual(expected, result)

#     def test_return_login_page_if_try_to_edit_while_not_logged_in(self):
#         expected = 'accounts/sign_in.html'

#         response = self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         }, follow=True)

#         self.assertTemplateUsed(response, expected)


#     def test_retrun_item_with_name_scrambled_egg_if_edit_successful(self):
#         expected = 'Scrambled Egg'

#         self.client.login(username='moe', password='12345')
#         self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         })

#         item = Item.objects.get(pk=1)
#         result = item.name

#         self.assertEqual(expected, result)


#     def test_return_item_with_ingredients_of_length_2_if_edit_successful(self):
#         expected = 2

#         self.client.login(username='moe', password='12345')
#         self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         })

#         item = Item.objects.get(pk=1)
#         result = item.ingredients.count()

#         self.assertEqual(expected, result)

#     def test_return_item_with_chef_laceywill_if_edit_successful(self):
#         expected = 'laceywill'

#         self.client.login(username='moe', password='12345')
#         self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         })

#         item = Item.objects.get(pk=1)
#         result = item.chef.username

#         self.assertEqual(expected, result)

#     def test_return_item_with_standard_as_true_if_edit_successful(self):
#         expected = True

#         self.client.login(username='moe', password='12345')
#         self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['2'],
#             'standard':True
#         })

#         item = Item.objects.get(pk=1)
#         result = item.standard

#         self.assertEqual(expected, result)

#     def test_return_back_to_item_detail_page_if_edit_successful(self):
#         expected = 'menu/item_detail.html'

#         self.client.login(username='moe', password='12345')
#         response = self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':['1'],
#             'standard':True
#         }, follow=True)

#         self.assertTemplateUsed(response, expected)


#     def test_return_item_edit_page_if_edit_not_successful(self):
#         expected = 'menu/item_edit.html'

#         self.client.login(username='moe', password='12345')
#         response = self.client.post(reverse('item_edit', kwargs={'pk':1}), {
#             'name': 'Scrambled Egg',
#             'ingredients': ['2','3'],
#             'description':'this is a delicious stuff',
#             'chef':3,
#             'standard':True
#         }, follow=True)

#         self.assertTemplateUsed(response, expected)