# K.O.M.O Photo Gallery

![Image Gallery](https://odude.com/demo/faq/wp-content/uploads/sites/2/2017/12/grid.png)

This is a Python photo gallery application based on Django Framework that allows users to view different photos that interest them, click on a single photo to expand it and also view the details of the photo and the photo details appear on a modal within the same route as the main page, Search for different categories of photos. (e.g. Travel, Food), copy a link to the photo to share with my friends and view photos based on the location they were taken.

You can see the live Application here [K.O.M.O Gallery](https://komo-gallery.herokuapp.com/).

Author Information
========
James Komo 

Features
========

- Built with Python 3.6, Djang0 2.0 Framework
- Styled using Bootstrap4
- Uses PostgreSQL DB and Deployed to Heroku

User Stories
============

Allows users to:
- View different photos that interest them.
- Click on a single photo to expand it and also view the details of the photo. The photo details  appear on a modal within the same route as the main page.
- Search for different categories of photos. (ie. Travel, Food)
- Copy a link to the photo to share with my friends.
- View photos based on the location they were taken.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to:

-   Have python installed
-   Have PostgreSQL DB installed
-   Have a terminal to interact with the app.
-   Any text editor
-   Browser to view


Installation
========

    $ git clone https://github.com/jameskomo/photo-gallery.git


Build & Deployment
========

**NOTE:** You need to have fully cloned it to run it locally.


    (virtual) $ python3.6 manage.py runserver

    # it will launch the web page from local server. You can also visit the livelink [here](https://komo-gallery.herokuapp.com/).
 to use the system

##Built With

- Built with Python 3.6
- Django2.0
- Styled using Bootstrap

Behavior Driven Development (BDD)
==================================
1. Load the app on any web browser such as Chrome, Mozilla, or Internet Explorer. Images will then load.
2. Click on your preferred image and its details will pop up for you to view.
3. To search image by category or location, just type the category name such as Music, Food and Travel. 
4. To edit the code, just clone the whole folder and open the files using any text editors


Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

Known Bugs
========
There are currently no known bugs for the app. However, I will be updating the README incase any bugs arise.

## License

MIT License

Copyright (c) 2019 James Komo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
