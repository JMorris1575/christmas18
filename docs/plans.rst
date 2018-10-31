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