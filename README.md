### Musicstar Blog 

![screens](https://github.com/user-attachments/assets/22fa7508-0d72-4198-9080-9fc94ec28c28)

### Introduction
This blog application was developed using Django and is intended for users of the site who are interested in classical music and related topics. It also helps to gather users of the site who have similar interests in music and allows them to interact with the site owner by sending comments on the blog posts and messages to the site owner using the contact form. Musicstar will be useful to the target audience by providing up-to-date information and news in the field of classical music.


### Table of Contents

+ Technology Stack
+ Wireframes
+ UserStories
+ UX Goals
+ Features & site goals
+ Testing 
+ Asscessibility & Performance
  - Lighthouse
  - HTML Validation
  - CSS Validation
+ Deployment
+ Credits

## Technology Stack
+ Backend
  - `Django Framework` - fullstack technolog
  - `Python` - Used for Django manipilation & interaction.
+ Database
  - `PostgreSQL`
  

+ Frontend
  - `HTML` - Used for structuring and content.
  - `CSS` - Used for adding styles to the content for legibility and aesthetic appeal.
  - `Bootstraps5` - For styling the content for legibility and aesthetic appeal.
  - `Javascript` - For adding basic interaactivity

### Additional Technologies
+ `FontAwesome` icons - used for icons.
+ `Lighthouse` - For performance, accessibility and best practices checking.
+ `GitHub` - For code storage, version acontrol and deployment.
+ `Cloudinary` - For images storge
+ `Git` - For commiting through the terminal and pushing to GitHub for storage.
+ `Gitpod` - The IDE developed the project in.
+ `W3C Validation Service` -  to validate my HTML for potential errors.
+ `W3C CSS Validation Service` - to validate my CSS code for potential errors.
+ `Pep8` - for Python code validation and best practices formatting.
## Wireframes

<img width="1008" alt="Screenshot 2024-10-29 at 21 22 51" src="https://github.com/user-attachments/assets/be44c26d-6d70-49e9-8080-474c0acecc19">

<img width="1011" alt="Screenshot 2024-10-29 at 21 11 19" src="https://github.com/user-attachments/assets/28c75048-a928-4a7d-a099-c6cb64b15b4d">

<img width="1009" alt="Screenshot 2024-10-29 at 22 47 32" src="https://github.com/user-attachments/assets/f541a9df-5db1-4d1b-b6f4-152e261e8558">

<img width="1009" alt="Screenshot 2024-10-29 at 22 57 26" src="https://github.com/user-attachments/assets/7cbf147f-7e52-4f98-a44a-017c3671314a">

<img width="1010" alt="Screenshot 2024-10-29 at 23 02 25" src="https://github.com/user-attachments/assets/08af252b-bc45-4b13-9aed-bfbb27077384">


<img width="1009" alt="Screenshot 2024-10-29 at 21 02 03" src="https://github.com/user-attachments/assets/76fb4a26-6b28-4015-baa7-5250f2d0c880">

<img width="1013" alt="Screenshot 2024-10-29 at 21 06 17" src="https://github.com/user-attachments/assets/90650a00-a49a-470c-9161-6e3746be086b">

<img width="1009" alt="Screenshot 2024-10-29 at 21 15 29" src="https://github.com/user-attachments/assets/38615206-68b6-4726-95ef-72a69d3323d9">



<img width="444" alt="Screenshot 2024-10-29 at 20 44 35" src="https://github.com/user-attachments/assets/93329b51-4fa8-493f-9f24-f1d15e7a375d">





## User Stories

+ Agile Planning

  Musicstar was developed using an agile methodology. The project progressed through incremental updates, focusing on delivering value at each stage.  The Kanban board for this project is available [here.](https://github.com/users/aliceC119/projects/4)
  
<img width="1095" alt="Screenshot 2024-10-30 at 16 31 49" src="https://github.com/user-attachments/assets/bd03e4b2-50ec-4aec-9910-fbff3138fb98">

| Id | User Story | Implemented|
| :---  |  :---:  |  ---: |
| 1  | As a site user I can view a paginated list of posts so that I can select which post I want to view  | Done   |
| 2  |As a Site User I can click on a post so that I can read the full text       | Done    |
| 3  |As a Site User/Admin I can view comments on an individual post so that I can read the conversation       | Done    |
| 4  |As a Site User I can register an account so that I can comment on a post    | Done    |
| 5  |As a Site User I can leave comments on a post so that I can be involved in the conversation      | Done    |
| 6  |As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation      | Done    |
| 7  |As a Site Admin I can create, read, update and delete posts so that I can manage my blog content      | Done    |
| 8  |As a Site Admin I can create draft posts so that I can finish writing the content later     | Done    |
| 9  |As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments      | Done    |
| 10  |As a Site User I can click the About link so that I can read about the site      | Done    |
| 11  |As a Site Admin I can create or update the About information so that the information is available to users     | Done    |
| 12  |As a Site User I can write on the contact form so that I can send messages      | Done    |
| 13  |As a Site Admin I can see the messages on the Admin panel so that I can read the messages      | Done    |
| 14  |As a Site User I can click on the like button so that express my appreciation on the post      | Done    |
| 15  |As a Site Admin I can view a column of 'Like' in the admin panel so that I know who has clicked a 'like' on which post      | Done    |
| 16  |As a Site User I can see how many people clicked 'like' and commented on the blog post so that I would be attracted to read the post and help me to choose which post to click into    | Done    |
| 17  |As a Site User I can click on the social share buttons so that share the post to my selected social media platform      | Done    |
| 18  |As a Superuser I can create a post on the frontend so that creating new posts not using the admin panel      | Done    |
| 19  |As a Site User I can click on a post so that I can read the full text       | Done    |
| 21  |As a Superuser I can click on the approved button so that approve submitted comments      | Done    |
| 22  |As a Site User and an unregistered User I can not see the approved button so that there is no choice for me to click on the approved button   | Done    |
| 24  |As a Superuser I can upload an image so that featured images would be displayed in all new created posts     | Done    |
| 25  |As a Site User I can view on the google map in the About page so that I know where the music club is      | Done    |
| 26  |As a Superuser I can use the Richtext toolbar in the content field so that I can style the post in the create a post page      | Done    |

## UX Goals

+ As a site user, I would like quick access to all pages that would enhance my browsing experience.
  - All pages should be visible whether I am logged in or not.
  - I should be redirected to the relevant pages without any problems.
+ As a site user, I would like all pages to have a similar manner in font family, colours, image styles, spacing, and effects.
+ As a site visitor, I would like the colours on the site to attract me to continue reading the blog posts and eventually become a regular logged in user.
+ As a site user, I would like all pages to be responsive to ensure I have a user-friendly experience every time I visit the home page.
+ As a site user, I need a message to notify me that my comment has been submitted successfully.
+ As a site user, I would like to see the time of creation of the comments so that I have an idea of how recent the are.
+ As a site user, I need to see a message that the comment was deleted after I clicked delete.
+ As a superuser, I click on the create a post link, I should be taken to a page where I can easily create a post on the site.
+ As a superuser, an approved button should be visible to me after I submitted a comment, so I can easily approve a comment on a post on the site.
+ As a site user, I would like to have good accessibility and interaction when I am browsing the site so that I can have a pleasant experience with the homepage.

## Site goals
+ User goals
  - Site users can register for an account to click the Like button or comment on a post.
  - Site users can view all the blog posts availble on the site.
  - Logged in site users can leave a comment on posts.
  - Logged in site users can click Like button on posts.
  - Logged in site users can share a post by clicking the social share buttons on the posts.
  - All users can write and send a message using the contact form.
  - All users can view on the map to know where musicstar club is.
  - All users can view on the about section to get to know the founders of the musicstar club.
    
+ Site owner goals
  - Site owners can create post directly on the site.
  - Site owners can also leave comments or click Like button on posts.
  - Site owners can approve the submitted comments by themselves on the site.
  - Site owners can share a post by clicking the social share buttons on the posts.

+ Site admin goals
  - Site admin can create posts
  - Site admin can create content in the about section.
  - Site admin can click approve or delete the submitted comments.
  - Site admin can view the sent message from the site users.
## Features

+ Navigation
  - The name of this blog app is displayed in the top left corner.
  - The fully responsive navigation bar contains links to the Home page, About page, Register page, Login page and Contact page.
  - They are placed identically on each page for easy navigation.
  - A 'You are not logged in' or 'You are logged in as (username)' message will appear on the right to indicate the login status.
    
<img width="1341" alt="Screenshot 2024-10-20 at 16 48 04" src="https://github.com/user-attachments/assets/8ab0c083-5fc6-4c9c-b5b2-8fc96906eb67">
<img width="543" alt="Screenshot 2024-10-20 at 16 54 56" src="https://github.com/user-attachments/assets/f2123851-4e33-4732-bdc0-ee0ebe650d97">

+ Home Page
  - Six blog posts are presented in each page on the homepage.
  - There are 'Next' and 'Previous' buttons below the six posts to help site users browse through the blog posts.

<img width="179" alt="Screenshot 2024-10-20 at 17 01 03" src="https://github.com/user-attachments/assets/81c03091-a027-4b64-911c-8dce70d32340">

+ Blog Post
  - The name of the author of the post and a photo will be displayed.
  - The title of the post and its excerpt appear under the photo.
  - It also shows the date and time the post was created.
  - 'Like' and 'Comment' icons are also displayed to show how many users have reacted to the post.
<img width="412" alt="Screenshot 2024-10-20 at 17 09 52" src="https://github.com/user-attachments/assets/6d44eb03-5607-4403-bc41-1aabb14308c9">

+ Inside the Post
  - The title of the post, the author's name, and the date and time of posting are displayed at the top of the post.
  - The content of the post is displayed in the centre.
<img width="1156" alt="Screenshot 2024-10-20 at 17 16 06" src="https://github.com/user-attachments/assets/025c0fa6-09a6-4cb3-aa95-1d044a3ef6eb">

+ Social share buttons
  - Social share buttons are displayed below the content of the post, allowing site users to freely share the post on their chosen social media platform.
  - When the social share button is clicked, a link from the post is redirected to the selected social media platform.
<img width="703" alt="Screenshot 2024-10-20 at 17 28 27" src="https://github.com/user-attachments/assets/4c0de78a-14fd-4d8f-8910-ee70c020da5a">

<img width="113" alt="Screenshot 2024-10-20 at 17 27 05" src="https://github.com/user-attachments/assets/82369b54-d8cf-48bc-8e44-73135ce6ec36">

<img width="544" alt="Screenshot 2024-10-20 at 17 20 08" src="https://github.com/user-attachments/assets/63433beb-0f35-4e43-9c8a-90f3bcb07a64">
<img width="677" alt="Screenshot 2024-10-20 at 17 20 22" src="https://github.com/user-attachments/assets/0287aaaf-9d6d-4560-bd09-781326824baa">

+ 'Like' button
  - Below the social sharing buttons is a 'Like' button.
  - Site users can click the 'Like' button if they like the post.
  - After clicking the 'Like' button, the number of 'likes' will increase.
  - Site users can also uncheck the 'Like' button, which will decrease the number of 'likes'. 

<img width="420" alt="Screenshot 2024-10-20 at 17 54 44" src="https://github.com/user-attachments/assets/b00175b9-aa4c-465f-8cd9-f18e7611639e">

+ Comment
  - There is a comment section located at the button of the post.
    
<img width="1131" alt="Screenshot 2024-10-20 at 17 56 04" src="https://github.com/user-attachments/assets/42b2526e-e88b-450c-aa5a-0f89abde648e">

+ Comment box
  - Site users are free to write comments about the post in the comment box.
    
    
<img width="403" alt="Screenshot 2024-10-20 at 17 56 55" src="https://github.com/user-attachments/assets/5ee58f64-82cb-4519-b986-26354d3494f2">

+ Submit a comment
  - When a comment is submitted, a message stating 'Comment submitted and awaiting approval' appears at the top of the post page.
  
    
<img width="762" alt="Screenshot 2024-10-20 at 17 58 16" src="https://github.com/user-attachments/assets/dca419d1-8382-4db5-b8a5-aae8e0330f0a">

+ Approve a comment
  - The Site owner can click on 'Approved' button to approve comments for themselves.
  - The site administrator can then click on 'Approve', 'Save', or 'Delete' the comment on the admin page.
<img width="368" alt="Screenshot 2024-10-30 at 17 37 22" src="https://github.com/user-attachments/assets/5c3e3c3b-7286-4237-9e33-1e5f765c4725">

<img width="1320" alt="Screenshot 2024-10-20 at 18 01 40" src="https://github.com/user-attachments/assets/4d51d322-dbdb-4a75-88f4-6d7f1a7392ba">

+ Messages before and after the comment is approved
  
  - Before the comment is approved, a message stating 'This comment is awaiting approval' will appear in the comment section
  - A 'Delete' and 'Edit' button will also be displayed for the site user to use if they wish to further edit or delete the comment.

<img width="370" alt="Screenshot 2024-10-20 at 18 00 36" src="https://github.com/user-attachments/assets/1c90890c-87f0-4155-95ad-bd69029cb90a">

+ An approved comment (A logged in site user)
  
  - Once the site admin has clicked 'Approve', the 'This comment is awaiting approval' message will disappear for the logged in site user.
  
<img width="368" alt="Screenshot 2024-10-20 at 18 19 16" src="https://github.com/user-attachments/assets/eaf5b0f4-a6c9-47e0-8143-beb03c864835">

+ An approved comment (Unregistered site users)
  - The 'Delete' and 'Edit' buttons would still remain in the comment area for the site user in case they wish to delete or edit the comment.
  - Only logged in site users can post a comment.

<img width="987" alt="Screenshot 2024-10-20 at 18 19 06" src="https://github.com/user-attachments/assets/a31516e2-9941-4064-9773-8c1c91c10a7a">

+ Delete a comment
  - When the site user deletes a comment, a pop-up box is displayed to ensure that the site user really wants to delete the comment.
  - After a comment has been deleted, a 'Comment deleted' message is displayed.
<img width="843" alt="Screenshot 2024-10-20 at 18 48 08" src="https://github.com/user-attachments/assets/aaa228ff-0842-4336-9348-86403b8ef6c2">

<img width="755" alt="Screenshot 2024-10-20 at 18 48 55" src="https://github.com/user-attachments/assets/d9073ab6-ae71-4ae5-b0ca-a9917106c90a">

+ Create a Post (On the site)
  - Site owners can create a new post with the link direct to the create a post form on the front page of the site.
  - The Create a Post form has fields for title, image, content, status, and excerpt. An Upload button appears at the bottom of the form.
  - A Richtext toolbar is installed in the content field, giving the site owner more freedom to style the post as they wish.
  - The newly created post would then be placed at the front with other blog posts.
 <img width="447" alt="Screenshot 2024-10-30 at 19 50 43" src="https://github.com/user-attachments/assets/f0926ad0-763e-4a46-b4b1-10b6dcce46ad">
 <img width="769" alt="Screenshot 2024-10-30 at 19 46 20" src="https://github.com/user-attachments/assets/14cb2dd4-8de6-40b2-9178-a4cc3294c973">

 + Create a Post (Admin panel)
   - The site owner can also create a post in the admin panel with the following fields: title, slug, image, content, status, and excerpt. 
 <img width="1332" alt="Screenshot 2024-10-30 at 19 59 14" src="https://github.com/user-attachments/assets/79b6c3d5-a893-4896-bcd3-37924f9baae7">

+ Google Maps

  - A Google Map function is installed on the About page to give site users information about the location of the Musicstar club.
  
<img width="1204" alt="Screenshot 2024-10-30 at 19 52 47" src="https://github.com/user-attachments/assets/72bdca6f-0eff-4fbd-ba4d-275cd9566b28">

+ Contact form
  - A contact form is available on the contact page. All users can send a message to Musicstar Club by filling in their name, email address and the content of the message. A send button will appear at the bottom of the form.
  - Once a message has been sent, a pop-up box will appear informing the user that the message has been received and that a respond will be sent within 2 working days.
  - The site owner can view the messages sent from the contact form in the admin panel.

  <img width="1206" alt="Screenshot 2024-10-30 at 21 07 36" src="https://github.com/user-attachments/assets/e7287347-371a-4e07-af0e-22b9102adf0b">

  <img width="642" alt="Screenshot 2024-10-30 at 20 06 05" src="https://github.com/user-attachments/assets/92439ba9-b136-4587-88bd-0fed16432b44">
  <img width="1093" alt="Screenshot 2024-10-30 at 20 09 42" src="https://github.com/user-attachments/assets/de01d3f1-7f94-48e4-9fb6-d358502ad028">

  + Sign Up
    - Unregistered users can sign up by entering a username, email (optional), and password.
  
  <img width="1113" alt="Screenshot 2024-10-30 at 20 12 26" src="https://github.com/user-attachments/assets/36aed0ef-4174-433b-b0a4-09692feafdd0">

  + Log in
    - Registered user can type in username and password to log in to the site.
    - A message would appear to inform the user that they have successfully signed in.
  
  <img width="634" alt="Screenshot 2024-10-30 at 20 17 51" src="https://github.com/user-attachments/assets/5ff5cb5d-1a95-46bb-a2ab-bb6ccb318c73">

  <img width="1106" alt="Screenshot 2024-10-30 at 20 12 32" src="https://github.com/user-attachments/assets/6072b249-dc28-47c2-9e3f-b073d9dc18d0">

  + Log out
    - A message would appear to inform the user that they have signed out.
      
  <img width="650" alt="Screenshot 2024-10-30 at 20 12 21" src="https://github.com/user-attachments/assets/2531c0ae-ac84-4967-80af-53b0c0e8752b">

     
## Asscessibility & Performance

### Python validation

- All Python files in the Musicstar Club project pass the pep8online validator test without errors.
<img width="962" alt="Screenshot 2024-10-30 at 16 30 10" src="https://github.com/user-attachments/assets/75a3c81d-2503-4efa-b55d-d90f82f6c4db">

### CSS validation

- The style.css file passes the validator test without errors.
<img width="1186" alt="Screenshot 2024-10-30 at 20 31 40" src="https://github.com/user-attachments/assets/ec388927-f920-4207-a375-e14dea6ec4f4">

### HTML validation

- All html files pass the validator test without erros.
  
<img width="1178" alt="Screenshot 2024-10-30 at 16 07 16" src="https://github.com/user-attachments/assets/81f3da68-27f7-4f22-b98e-ce15730aaf71">

### Lighthouse

- Lighthouse has a score of 56 in Best Practices due to the external links within the blogs. This is still within the acceptable range. The other three areas: Performance, Accessibility, and SEO are doing well.


<img width="605" alt="Screenshot 2024-10-30 at 16 27 19" src="https://github.com/user-attachments/assets/a25e8a28-83e2-48aa-910c-36863b2a54f4">

## Deployment

The application is deployed on Heroku via a GitHub connection. To deploy a Heroku project, below are the steps I used.

In Heroku, this is configured under Config Vars in the Settings tab.

### Step 1: Create an App on Heroku

Log in to your Heroku dashboard with your username and password, and confirm the access code with the two-factor verification app of your choice.

Login to Heroku

<img width="1197" alt="Screenshot 2024-10-30 at 20 45 41" src="https://github.com/user-attachments/assets/57d56df5-4cd1-44d1-b61c-dd75e55a97bd">

Verify your identity by entering the verification code generated by an authenticator

<img width="1206" alt="Screenshot 2024-10-30 at 20 47 19" src="https://github.com/user-attachments/assets/64b22dbe-5108-409f-8e10-0d46217820a7">

Create a new Heroku app

<img width="1206" alt="Screenshot 2024-10-30 at 20 50 25" src="https://github.com/user-attachments/assets/bc386682-1386-4642-ad00-96301334e90b">

### Step 2: Connect to GitHub

Once a new app is created, go to `Deploy` in the top toolbar, then select the GitHub box in the middle to connect this Heroku app to a GitHub repository.

<img width="1213" alt="Screenshot 2024-10-30 at 20 56 36" src="https://github.com/user-attachments/assets/7b2330c1-1fb8-40f1-9f5d-2aac3662ba48">

### Step 3: Deploy aour app

Choose `main` as the branch to deploy and click on `Deploy Branch`. You can do the deploment actomatically or manuelly at this point.

### Step 4: View the application

The app can be found by clicking the 'Open App' button in the top right corner with the Heroku URL configuration as follows: https://*.herokuapp.com 

<img width="1197" alt="Screenshot 2024-10-30 at 21 01 21" src="https://github.com/user-attachments/assets/19eb9259-8e94-4847-9586-890abf525def">

## Credits
- The structure of this project is based on the CodeStar Bloag walkthrough project from Code Institute and I have customised it with different models and features.
- The social sharing feature is referenced by the [Django Social Post integration](https://aisaastemplate.com/blog/django-social-post-integration/#mastering-django-models-for-social-media-integration)
- The Likes feature is referenced by [Like and Dislike Button Functionality in Django](https://www.youtube.com/watch?v=ZUiTiUj-tZw&t=1212s)
- The text and images are used by [classicfm](https://www.classicfm.com/) for educational purposes.
- The picture that I used for the About page is from [pexels](https://www.pexels.com/search/a%20group%20of%20people/)
- Wireframe was created using Balsamiq
## Acknowledgements
- “I think therefore I blog” walkthrough: Provided initial steps for setting up & deploying the site.
- The tutors in Student Support in Code Institute helped me through difficult times during the process of this project.
- My mentor, Harry Dhillon, has given me insight into how to improve this project. He has also given me the help I needed when he had the time.




