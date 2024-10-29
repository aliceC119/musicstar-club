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
+ Testing & Debugging
+ Asscessibility & Performance
  - Lighthouse
  - HTML Validation
  - CSS Validation
+ Deployment
+ Credits

### Technology Stack
+ Backend
  - `Django Framework` - fullstack technolog
  - `Python` - Used for Django manipilation & interaction.
+ Database
  - `PostgreSQL`
  

+ Frontend
  - `HTM`L - Used for structuring and content.
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
### Wireframes

<img width="1008" alt="Screenshot 2024-10-29 at 21 22 51" src="https://github.com/user-attachments/assets/be44c26d-6d70-49e9-8080-474c0acecc19">

<img width="1011" alt="Screenshot 2024-10-29 at 21 11 19" src="https://github.com/user-attachments/assets/28c75048-a928-4a7d-a099-c6cb64b15b4d">

<img width="1009" alt="Screenshot 2024-10-29 at 22 47 32" src="https://github.com/user-attachments/assets/f541a9df-5db1-4d1b-b6f4-152e261e8558">

<img width="1009" alt="Screenshot 2024-10-29 at 22 57 26" src="https://github.com/user-attachments/assets/7cbf147f-7e52-4f98-a44a-017c3671314a">

<img width="1010" alt="Screenshot 2024-10-29 at 23 02 25" src="https://github.com/user-attachments/assets/08af252b-bc45-4b13-9aed-bfbb27077384">


<img width="1009" alt="Screenshot 2024-10-29 at 21 02 03" src="https://github.com/user-attachments/assets/76fb4a26-6b28-4015-baa7-5250f2d0c880">

<img width="1013" alt="Screenshot 2024-10-29 at 21 06 17" src="https://github.com/user-attachments/assets/90650a00-a49a-470c-9161-6e3746be086b">

<img width="1009" alt="Screenshot 2024-10-29 at 21 15 29" src="https://github.com/user-attachments/assets/38615206-68b6-4726-95ef-72a69d3323d9">



<img width="444" alt="Screenshot 2024-10-29 at 20 44 35" src="https://github.com/user-attachments/assets/93329b51-4fa8-493f-9f24-f1d15e7a375d">





### User Stories

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
  - The site administrator can then click on 'Approve', 'Save', or 'Delete' the comment on the admin page.

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


------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
