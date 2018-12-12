Planning the Christmas 2018 Website
===================================

I want to keep the same basic format this year but have a better, and more responsive, presentation. I am planning on
using Bootstrap 4 with the idea of using cards to display the gifts on the main page, perhaps three or four to a row
on a full computer. It would be good to use a local version of Bootstrap in order to be able to modify some of its
defaults and also to see if that is what might be causing the numerous errors I see concerning being "disconnected from
the server" finally resulting in something about "None object as no method 'split'."

Otherwise, in order to make it doable, I'm not thinking at the moment of adding anything new -- except possibly a
version of the story app. I won't worry about two entries being made at the same time and see what happens. Perhaps, if
that happens, I can create branches manually.

I have created the Christmas2018 project in PyCharm, created a development database to go with it, and created a space
on github to hold it. I learned, on github, that I have a "follower." Kind of makes me feel I'm being watched. I only
use github to be able to simply transfer my work from one computer to another and don't consider any of it worth
emulating.

The person following me, Mr. Xyfir, lists himself as the "Founder and developer @Xyfir." He runs a company out of
California which, among other things, offers simple advertising on the web. He refuses to display ads or links to "NFWS"
sites, "NFWS" referring to "Not Safe For Work" and that is good. He seems to be mostly a javascript developer.

Setting Up a Local Version of Bootstrap
---------------------------------------

How to do this is explained at http://getbootstrap.com/docs/4.1/getting-started/theming/ and I think I can use what they
call "Option B" for the changes I'm thinking of making -- just to the primary and perhaps secondary colors.

I believe I can still use Koala, as explained in Section 8, Lesson 45 of the "Bootstrap 4 From Scratch With 5 Projects"
from Udemy ( https://www.udemy.com/bootstrap-4-from-scratch-with-5-projects/learn/v4/t/lecture/10645918?start=0 ). The
instructor actually changes the Bootstrap core files but I do not plan on doing that.

I will create the following file structure::

    Christmas2018
    ├---c18
    |   ├-config
    |   └---static
    |       └---site
    |           ├---bootstrap
    |           |   ├---js
    |           |   └---scss
    |           ├---css
    |           |   ├---bootstrap.css
    |           |   └---custom.css
    |           └---scss
    |               └---custom.scss
    └---docs

(By the way, the ├ character was made by holding down Alt while entering 195 on the numpad. The └ character was entered
as Alt-192.)

I set up Koala to compile ``c18/static/site/bootstrap/scss/bootstrap.scss`` to ``c18/static/site/css/bootstrap.css`` and
``c18/static/site/scss/custom.scss`` to ``c18/static/site/css/custom.css`` and it may or may not be working. After
adding the ``.css`` files to git I will test them.

Testing the CSS Files
---------------------

In order to test the ``.css`` files I will need to create an ``.html`` file with bootstrap enabled, a view to render
that file, and a urlconf to call the view. Seems like a lot of trouble but some of these things I can use later.

I will create a ``templates`` directory in the ``c18`` directory and copy ``base.html`` from ``Confirmation2019``. I
will stub in ``header.html`` and ``footer.html`` and modify the link to bootstrap to point to the local
``bootstrap.css``. I will follow that with a link to my own ``custom.css`` file and make other changes as needed, such
as to the title.

I think I will also need to start an app, let's make it the gift app:

    ``python manage.py startapp gift``

[By the way, when going to the terminal to carry that out I noticed, already, there was the ``ConnectionAbortedError``
that appears periodically. It happened at 11:30 this morning I think. It must be a problem in ``runserver`` or some
other part of Django or perhaps even Python itself rather than anything I am doing wrong. This site doesn't have much
going on yet at all, and even less at that point!]

In order to get it to find the templates in ``c18/templates/`` I had to include that in the ``base.py`` file as
follows in the ``'DIRS': [...]`` line::

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

I discovered that I had to import ``bootstrap.scss`` in my ``custom.scss`` file as follows::


    $primary: #00ff00;
    $secondary: #ff0000;

    @import "../bootstrap/scss/bootstrap";

This creates a ``custom.css`` file that includes all of bootstrap. I don't think I have to link to the bootstrap file,
just ``custom.css``. It needs to be followed by a link to my own styles, perhaps ``styles.css`` which, itself, can come
from a ``styles.scss`` file.

Beginning to Work On favicon.ico
--------------------------------

Meanwhile I've added a ``favicon.ico`` to ``c18/static/site/images`` but it doesn't look very good in the small format.
I got it from **openclipart.org**, edited it in **inkscape** and converted the resulting ``.svg`` to an icon file online
at https://convertio.co/svg-ico/ . Perhaps a candle will work better than a star.

Candle didn't work well either. Many of the favicons I see being used involve alphabetic characters, like dj for the
**DjangoProject** site, or B for the **Bootstrap** site. They also use simple drawings, like the stack of red lines on
**StackOverflow** or the blender logo on the **Blender** site. I was thinking of the word "Noel" but that is probably
too long. Perhaps I can use one of my ornament images I made in Blender last year. I will try to hunt it down and
convert it to an icon. I think the website above converts from other formats besides ``svg``.

Undocumented Development
------------------------

I haven't documented very much here this year. Perhaps because I'm getting better at it -- although I must quickly add
I've still made my share of mistakes. Anyway, the site is up and running and people are already beginning to use it.
Now I want to add a new feature.

Planning the What Is It Activity
--------------------------------

Based on the Fictionary game I played at the Hudson house, and on the What Is It section of "Muse On," the Kalamazoo
Museum magazine, I want to create a "What Is It" activity on the website. I've already taken some pictures of odd
objects and have been thinking about how to use them. Here is my current idea:

The game will work in stages. In the first stage, an image will be displayed and family members will be invited to
write a description of what that object is and what it was for or anything else that might be included in a museum-like
description of the object. Each family member can only write one description but they can edit their description until
we get to the second stage. During this first stage the names of people who have added descriptions so far will be
listed under the picture or it will say "No descriptions yet" or "Only Jim's description so far." Actually, it will be
better to give them an opportunity to add or edit their description right on that page under the list of contributors.

In the second stage all of the descriptions will be listed below the picture and visitors will be allowed to vote for
the one they think is correct and perhaps also for the one they think most creative. Each family member can only vote
once but they may change their vote until stage three. No one can vote for their own entry. The tally of the votes is
not listed on the site in this stage.

Finally, in the third stage, all is revealed. The authors of each description is identified along with the number of
votes they got in each category. The correct description is also revealed.

There should probably be a "landing page" for this activity for the case when several objects are being displayed,
perhaps in different stages. The user can click on its image to enter it's page.

Models
******

From the above it seems there should be an Object model with the following fields:

#. name or number: to identify the object on each page where it is pictured
#. publish: a boolean to indicate if this object should be open for play
#. stage: the current stage, one, two or three, that this object's game is in.
#. correct_description: a correct description for this object

There will also need to be a Description model with the following fields:

#. object: the object to which this description belongs
#. author: the family member writing this description
#. description: the description they wrote for this object
#. voted_correct: the number of times this description is voted as the correct one
#. voted_creative: the number of times this description is voted the most creative

There should also be a Contribution model that keeps information about what each user has contributed:

#. user: the family member making the contribution
#. object: the object for which this contribution was made
#. type: the type of contribution this is: either a description, a vote for correct, or a vote for most creative

URL Scheme
**********

Here is a list:

+------------------------------+-------------------------------------------------------------------------------------+
| URL                          | Destination                                                                         |
+==============================+=====================================================================================+
| ``whatsit``                  | goes to the object list page                                                        |
+------------------------------+-------------------------------------------------------------------------------------+
| ``whatsit/objects/``         | goes to the object list page                                                        |
+------------------------------+-------------------------------------------------------------------------------------+
| ``whatsit/<n>/``             | goes to object n's page                                                             |
+------------------------------+-------------------------------------------------------------------------------------+
| ``whatsit/edit/<d>/``        | allows a user to create or edit their description (d) for an object                 |
+------------------------------+-------------------------------------------------------------------------------------+
| ``whatsit/<n>/desc_delete/`` | allows a user to delete their description                                           |
+------------------------------+-------------------------------------------------------------------------------------+
| ``whatsit/<n>/votes/``       | allows a user to vote for most correct and most creative entries                    |
+------------------------------+-------------------------------------------------------------------------------------+

Creating a New Branch
*********************

Perhaps I should make a branch of the current form of the website but I'd hate to be practicing with so short a time
left to Christmas. Yet, the alternative of having to correct files at webfaction with files already modified for this
new activity, would be even worse. I should learn more about git!

But I will make a branch called "whatsit" and hope it all works.

I did it by selecting VCS-->Git-->Branches...-->+ New Branch and entering "whatsit" as the branches name and kept the
checkout box checked. Now PyCharm shows "Git:whatsit" at the lower right.

Implementation
**************

This seems like the order I should follow in the implementation of the What Is It? activity:

#. Create the app and add it to InstalledApps
#. Create the models.
#. Register the models with the admin.
#. Make migrations and migrate the changes to the database.
#. Add the migrations to git.
#. Create a static folder for the images.
#. Add an object or some objects to the database.
#. Create the URL patterns to arrive at the object list page.
#. Link to the object list page from the activity list page.
#. Stub in the template object_list.html.
#. Create ObjectListView.
#. Fill out the template object_list.html.
#. Stub in a stage one object page: whatsit_one.html.
#. Create ObjectView.
#. Fill out the stage_one.html page.
#. Stub in a page to accept descriptions: description_edit.html. (maybe include this on whatsit_one.html?)
#. Create DescriptionEditView (see memory.views.py).
#. Fill out description_edit.html.
#. Test for being able to create and edit descriptions.
#. Stub in a page to confirm deletions description_delete.html.
#. Create DescriptionDeleteView (see memory.views.py).
#. Fill out description_delete.html.
#. Stub in a stage two object page: stage_two.html.
#. Edit ObjectView to produce stage two views.
#. Fill out stage_two.html.
#. Stub in a stage three object page: stage_three.html.
#. Edit ObjectView to produce stage three views.
#. Fill out stage_three.html.

Planning the Guess the Recipe Activity
--------------------------------------

Janet gave me some of Aunt Helen O'Brien's old recipes and I'm thinking that I could list the ingredients for each
recipe, and give a list of possible names for the dish for family members to select. It would be like a matching quiz.

Narrative Runthrough
********************

A family member comes to the website and clicks "Activities" on the menu. Among the other activities listed is one
called "Guess the Recipe." When they click on the button that says "Play 'Guess the Recipe'" they are taken to a
scoreboard page listing the scores for each family member so far if there are any. Perhaps there can also be an
explanation of the game on that page, complete with a picture of Aunt Helen. A button appears that either says "First
Set" or "Next Set" like the Trivia game.

Upon clicking that button the family member is taken to a page listing several sets of recipe ingredients in
alphabetical order. At this point I don't know if I will include amounts or not but, at the moment, I'm thinking it
might be more interesting if I don't give the amounts.

At the top of the page is a list of the names for what Aunt Helen might have been making with each of the recipes.
Within the card for each recipe's ingredients (designed to look like a recipe card?) is a selection box where family
members can select which name goes with which ingredients. At the bottom of the page is a Submit Guesses button. To keep
things simple, it will be possible to guess the same name for several sets of ingredients.

Upon making their guesses they are sent to a results page which shows the correct answer for each list of ingredients
and provides a button where the family member can view the complete recipe. Perhaps the recipe can be printed out if I
learn how to do printer friendly html, or a photo, or photos, of Aunt Helen's own recipes can be shown and family
members can print or download them.

URL Design
**********

The base name for this section can be ``recipes``. Here is a chart of the possible URLs and what they lead to:

+---------------------------------+---------------------------------------------------------------------------------+
| URL                             | Destination                                                                     |
+=================================+=================================================================================+
| recipes/                         | Redirects to scoreboard page                                                    |
+---------------------------------+---------------------------------------------------------------------------------+
| recipes/scoreboard               | The "Guess the Recipe" scoreboard and launch page                               |
+---------------------------------+---------------------------------------------------------------------------------+
| recipes/quiz/<n>                 | Quiz page for the nth set of 5(?)recipes                                        |
+---------------------------------+---------------------------------------------------------------------------------+
| recipes/results/<n>              | The results page for the nth set of recipes                                     |
+---------------------------------+---------------------------------------------------------------------------------+
| recipes/view/<n>                 | The page where the original recipes can be seen                                 |
+---------------------------------+---------------------------------------------------------------------------------+

Model Design
************

I will need a Recipe model to contain the list of ingredients and a ForeignKey reference to the QuizPage on which it is
to appear. The recipe's name can be kept in a CharField and the list of ingredients can be held in a TextField. It will
also be helpful to have a recipe_number (see below). There can also be a function to create the filename for the
recipe's image for use on the recipe_view page.

The QuizPage model will have a SmallIntegerField for its number (the order in which it appears) and that seems to be
about it. The QuizPage serves mainly as a place to collect recipes.

I will also need to keep track of family member's guesses and whether they were right or wrong. These need not be
anonymous but, once the submit button is pressed, they may not change their answers. This seems to call for a Response
model to contain a ForeignKey to the User, a ForeignKey to the Recipe on which they are guessing, a SmallIntegerField
indicating the number of the recipe they guessed to match it. If their guess matches the recipe number then a
BooleanField named correct is set to True, otherwise is it False.

Here is a first attempt at a design for these three models:

QuizPage model:
#. page_number: (SmallIntegerField)

Recipe model:
#. number: (SmallIntegerField)
#. name: (CharField max_length=40)
#. ingredients: (TextField)
#. quiz_page: ForeignKey to QuizPage model

Response model:
#. user: (ForiegnKey to auth.User)
#. recipe: (ForiegnKey to Recipe on which they are guessing)
#. guess: (SmallIntegerField for the number of the recipe they guessed)
#. correct: (BooleanField True if their guess is right, False otherwise)

Git Branching
*************

After Git Pulling the latest revision of the program from Github, running a migrate and updating the database to match
what was on the online website last night, I clicked on the Git button(?) in the lower right corner of PyCharm and
selected + New Branch. I gave it a name of ``recipe`` and left the Checkout box selected. Hopefully this will result in
less hassle when I try to merge this into the original program later.

Implementation Plans
********************

Here is a plan I can follow during implementation. (The original form worked for What Is It? so I just copy-pasted it
before editing it.

#. Create the app ``recipes`` and add it to InstalledApps
#. Create the models.
#. Register the models with the admin including the ability to enter Recipes within QuizPages.
#. Make migrations and migrate the changes to the database.
#. Add the migrations to git.
#. Create a static folder for the images.
#. Add a set of recipes to a QuizPage in the database
#. Create the URL patterns to arrive at the scoreboard page.
#. Link to the scoreboard page from the activity list page.
#. Stub in the template recipes/scoreboard.html.
#. Create RecipesScoreboardView.
#. Fill out the template recipes/scoreboard.html.
#. Stub in a QuizPage: recipes/quiz_page.html.
#. Create QuizPageView.
#. Fill out the recipes/quiz_page.html page.
#. Create the post method of QuizPageView to recieve and save people's guesses.
#. Stub in a recipes/quiz_results.html page. This will have "See the Recipe" buttons to display individual recipes.
#. Create a QuizResultsView.
#. Fill out recipes/quiz_results.html page.
#. Stub in a recipes/recipe_view.html page. This will display large images of individual recipes.
#. Create a RecipeView to produce views of the recipe images.
#. Fill out the recipes/recipe_view.html page.



