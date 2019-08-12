from django.test import TestCase

from .models import Project, Skill
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
PROJECT MODEL
"""