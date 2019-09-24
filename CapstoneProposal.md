#Name
##Dungeon Builder geb

#Project Overview
Dungeon builder geb is an app that allows users to create, save, and share dungeon maps for table top games. Users can drag and drop objects on to a grid to create their map and save the map to their account. They can also search for maps made by other users and download them, as well as rate and leave comments and suggestions on maps made by other users. By Cole Nation.
##Features
###Creating dungeon maps on a grid by dragging and dropping objects
  As a DM I want to be able to quickly and easily build dungeon maps for my campaign. This will be achieved using the Roll20 api. I will have to create objects that are draggable and a background that can have things dropped in to the different tiles.
  - Map Model that contains Objects
  - Import roll 20 api to create drag and drop UI
  - create api for models that can save maps to db
###Sign in and save dungeon maps to your account
  As a DM I want to be able to save my maps for future use. I will have to make a user model that can store map data.
  - User Model that contains maps
  - create api for maps to be downloaded
###Share maps with other users and download maps made by other users
  As a DM I want to be able to search and download maps made by other users when I don't have time to make them myself. I will have to create a way for users to search and find maps for other users and download them, but only if the creator allows it.
  - Search function in api db
  - Toggle whether maps are public or private
  - Add ability to rate and leave comments on user Maps

##Data Models
###Users
- Username
- Password  
- Maps

###Maps
- Name
- Background
- Objects
- Created date
- Shared

###Objects
- Name
- Image

##Schedule
###Milestone 1/MVP
- Ability to create an account and sign in.
- Ability to make and save maps to your account.

###Milestone 2
- Ability to download maps without signing in

##Milestone 3
- Ability to share maps with other Users

##Milestone 3
- Ability to leave comments and suggestions on other Users maps
