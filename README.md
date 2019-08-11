# THPWD12 - Social Team Builder

This is the final project to team tree house's Python Web Tech Degree.

## Deliverables / Objectives

1. Using supplied design assets
    - The site should resemble the supplied design.

2. Registration of an account
    - The user should be able to sign up for an account.

3. Login
    - The user should be able to log into his/her own account

4. Logout
    - The user should be able to log out of his/her own account

5. Edit profile
    - The use should be able to edit his/her profile
    - The user should be able to use Markdown in the 'about me' part of the profile. This Markdown is rendered on his/her profile page.

6. Upload avatar
    - The user should be able to upload an avatar image for his/her profile.

7. List skills
    - The user should be able to pick skills for his/her profile.

8. Create Project
    - The user should be able to create a project that he/she need help on.
    - The user can use Markdown in the project description. This Markdown is rendered on the project page.

9. Create position
    - The user should be able to create multiple positions for a project. Positions relate to a particular skill.
    - The user should be able to specify the positions where his/her project needs help with a name, a description, and related skill.
    - The user should be able to use use Markdown for the position description. This Markdown is rendered on the project page.

10. See project applicants
    - The user should be able to see all of the applicants for his/her project's positions.

11. Approve applicant
    - The user should be able to approve an applicant for a position in his/her project.

12. Reject applicant
    - The user should be able to reject an applicant for a position in his/her project.

13. Position notification
    - The user should get a notification if user is rejected or approved for a position

14. Search projects
    - The user should be able to search for projects based on words in their titles or descriptions. Search is case-insensitive.

15. Filter projects
    - The user should be able to filter projects by the positions they need filled.

16. Apply for a position
    - The user should be able to apply for a position in a project.

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In `project` folder, install dependencies by typing `pipenv install`
3. In `project` folder, enter virtual environment by typing `pipenv shell`
4. In `project` folder, run `python manage.py makemigrations main`
5. In `project` folder, run `python manage.py migrate`
6. In `project` folder, run app by typing `python manage.py runserver`
7. View the project by opening a browser like Chrome and entering the provided url (i.e. `http://127.0.0.1:8000/`)
8. When done, exit by pressing `Ctrl`+`C` and virtual environment by typing `exit`