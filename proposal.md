# NatureShare

# Project Overview
#### What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?
* Allows users to share organisms(trees, plants, shrubs, animals) they find in nature: pictures, names, locations, edibility, ecosystem/environment , and time.
* Creates an app where people can share their love of nature without the interference of non-nature related content.
* Django/Pillow

# Functionality
#### Walk through the application from the user's perspective. What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?
* Landing page is a login page --- user's cannot use the app without logging in
* After logging in user's are taken to a page where they can add a new organism
* User's will have to add a name and location --- rest of the fields will be optional
* Pictures
    * optional
* Names
    * mandatory
    * text field
* Locations
    * mandatory
    * lat/lon --- API button to let users share their lat/lon
        * getCurrentPosition() --- HTML geolocation
* Edibility
    * optional
    * drop down menu --- yes/no/unknown
* Ecosystem/Environment
    * optional
    * drop down??? list a bunch of ecosystems and an other option with an associated text field??? ask sarah

* Weather
    * optional

* Date
    * Time
        * optional
        * time/date field

* Page where you can see a list of names and locations
* Page for each item in the model with all the associated data



# Data Model
#### What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'.
* Organism
* Ecosystem --- foreignkey????
* Date

# Schedule
#### Here you'll want to come up with some (very rough) estimates of the timeframe for each section. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.
* Set up Django
* Set up landing pages
* Set up Models
* Set up ability for users to interact with DB
* Style

# Stretch Goals
* Implement Date model
* Implement map using lat/lon data
* optional field for scientifc name --- api call for basic facts about that species