[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=453748&assignment_repo_type=GroupAssignmentRepo)


<div align="center">
<h1>IS216 - Group 11 - Pepe Guitarra</h1>


  <img
    height="80"
    width="80"
    alt="tiger"
    src="Images/musicscore.png"
  />



<p>A Sleek and Useful Website for the Classical Guitar Learners</p>


[**Project Proposal**](https://docs.google.com/document/d/1lQ0a6iFEXMNqPLMGYodRGDmeCuGlK0wfKJ4xA3pBQNg/edit#heading=h.fofrqzcdjfsz) |
[Figma Prototype](https://www.figma.com/file/wC54T78RJqK4JypMSfm3Jg/Pepe-Guitarra?node-id=7%3A276)

</div>

---


## 🎸 Group Members
* Yu Yiling yiling.yu.2019
* Goh Jia En jiaen.goh.2020
* Lim Zhan Rong zrlim.2018
* Lim Jia Yi jiayi.lim.2020


## 🎸 Project Overview ##
* Pepe Guitarra, a one stop classical guitar resources platform for all music-learners, providing them with reliable classical guitar resources - ranging from Scores to Useful Youtube Playlist.

## 🎸 Why Pepe Guitarra?  ##
* With the introduction of affordable or free music learning via online resources, people interested in music but lack money to opt for often expensive music tutors, are now able to effectively learn music through utilizing the many free but valuable resources available online.
* We understand that learning music can be expensive and with the internet in our hands, it can be difficult to find good and reliable music resources specifically Classical Guitar.
* Moreover, during this Covid-19 pandemic, with everyone facing increasing amounts of stress and anxiety while being coop up at home, many of us turn to new hobbies to relieve emotional stress. An effective healing activity for people.
* With all this considerations in mind, Pepe Guitarra is created.

## 🎸 For who?  ##
* For everyone.
* Pepe Guitarra is designed for everyone, anywhere, regardless of age.
    * People who are interested in learning the classical guitar for free online
    * Older people or people with disabilities that want to use online resources to learn the classical guitar

## 🎸 System Architecture Diagram  ##
<img
    src="Images\System Diagram.jpg"
  />

###### 🎵 Spotify API ######
1. Request Access Token using Client details (Id, Secret Key)
1. Retrieve Access Token using Axios
1. Using the suitable Web API Console (Search the keyword "Classical Guitar", Input type as "Playlist")
    * https://api.spotify.com/v1/search?q=classical%20guitar&type=playlist&limit=20 
1. Return JSON object of all the playlists with keyword "Classical Guitar"
1. Display Spotify widget using Spotify API data

###### 📹 Youtube API ######
1. Identify 3 professional and popular classical guitar channels from [Youtube](https://www.youtube.com/)
1. Use [Channels: list](https://developers.google.com/youtube/v3/docs/channels/list) to retrieve channel details by specifying channel names via Axios
    * sample url:https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails&forUsername=SiccasGuitars&key=[YOUR_API_KEY]
    * response contains channel id, description and thumbnails
1. Use [ChannelSections: list](https://developers.google.com/youtube/v3/docs/channelSections/list) to retrieve channel section details by specifying channel id via Axios
    * sample url:https://www.googleapis.com/youtube/v3/channelSections?part=snippet%2CcontentDetails&channelId=UCR39sLAZ5wS_vrMo4tRylHw&key=[YOUR_API_KEY]
    * response contains playlist id for each channel section
1. Construct data for the 3 identified channel in Vuejs. For each channel, specify their id, name, thumbnail, description, and section playlists
1. Note:
    * Why we dont let users to search and choose Youtube channels on their own? 
        + Since the api call for [Search: list](https://developers.google.com/youtube/v3/docs/search/list) has a quota cost of 100 units and we have limited free quota units, we decide to just identify and fix the top 3 classical guitar ourselves in our website and not let users to search and call api themselves to save quota units.
    * Why we would like to put our Youtube API response data in Vue but not call it everytime when user request it? Is it hardcoding?
        + Since we have already fixed our channels, the channel id and playlist id will not really change for each api call. Thus we would just like to save those channel details in Vue to save api call unit cost and website loading time. Also, since every iframe can actaully be seen as an api call and we are using playlist id in iframes to retrieve the videos, if the channel uploads new videos in the playlists, our website will also reflect the new uploads dynamically. Thus it is not hardcoded. 
    * Why we just show 2 playlist per channel?
        + Though there are more than 2 playlists for each channel, if we display all of them using iframe, it will significantly slow down the page loading. Thus we would just like to show 2 playlist per channel save loading time to prioritise user experience.


###### 📁 Scores Page - Dealing with files ######
* In order to dynamically populate the lists of scores in the Scores page, an external python script getFileNames uses the glob function to retrieve all filenames in the three folders (beginner, intermediate, advanced), and then appends that to the resources html files. Everytime the folders are updated with new songs, simply running getFileNames once will automatically get the filenames and update the html files.


## 🎸 [OPTIONAL] How to Deploy Our Web Application (for Developers) - Netlify ##

* Netlify, a fully multi-cloud infrastructure, provides hosting for websites whose source files are stored in the version control system Git and then generated into static web content files.

### Few Simple steps to deploy Pepe Guitarra onto Netlify! 👇 ###

#### 1. Sign Up With Netlify (Using GitHub) ####
<img
    src="Images\netlify1.jpg"
  />

#### 2. Authorize Netlify ####
  <img
    src="Images\netlify2.jpg"
  />


#### 3. Depoly GitHub Web App onto Netlify ####
 <img
    src="Images\netlify3.jpg"
  />

#### 4. Authorize Netlify Deployment ####
<img
    src="Images\netlify4.jpg"
  />

#### 5. Select desired repos to deploy ####

  <img
    src="Images\netlify6.jpg"
  />




#### 6. Connect your repository ####
<img
    src="Images\netlify8.jpg"
  />

#### 7. View deploy link ####
<img
    src="Images\netlify9.jpg"
  />

#### AND YOU ARE DONE! ####
<img
    src="Images\netlify10.jpg"
  />

## 🎸 How to Install and Run Our Web Application (for Developers) ##

#### To start deploying the Pepe Guitarra GitHub repo, you need to edit the items mentioned below 👇 ####

###### 🎵 Spotify API Token Authorization ######
1. Head to [Spotify Developer](https://developer.spotify.com/dashboard/applications) to Login in your Developer's Dashboard
1. Register an application with Spotify

<img
    src="Images\Dashboard.jpg"
  />

3. Authenticate a user and get authorization to access user data - Client ID & Client Secret

<img
    src="Images\Spotify.jpg"
  />

4. Replace the **client_id and client_secret**  with your Access token details in Spotify_APIs/apiapp.js

```
const app = Vue.createApp({
    data(){
        return{

            // Spotify data
            client_id : '8c8963de217343da89154d4dd9d27cf4',
            client_secret : 'd390b69d6d3d43469f7296e006f71704',
            data: "",
            token: "", // Store token

            // Default display, to be modified upon random_generate()
            display: [
                {name: 'Classical Guitar', link: '3sFlYchrFtMnxK6xY5uO27'},
                {name: 'Peaceful Guitar', link: '37i9dQZF1DX0jgyAiPl8Af'},
                {name: 'Classical guitar music', link: '37i9dQZF1EIcSXgw8fnVjD'}
            ],

            // Store Playlist Info from Spotify API
            playlists_list: [],
            playlist_links: [],
        };
    },
```


###### 📹 Youtube API Token ######
1. Create a project in the [Google Developers Console](https://console.cloud.google.com/apis/dashboard?pli=1)
2. Obtain authorization credentials, Click on "Create Project" 

<img
    src="Images\Credentails.jpg"
  />

3. Then click on "Create Credentials" and "API Key"

<img
    src="Images\ytapikey.jpg"
  />
  
4. Restrict the API Key

<img
    src="Images\restrictytapikey.JPG"
  />

5. API key configurated. Now can pass this key with key=API_KEY parameter in Youtube API urls to retrieve the infomation we need.

<img
    src="Images\ytapikeydone.JPG"
  />

## 🎸 X-Factors used ##
* [GitHub](https://github.com/)
    + What is it? It is a software development and version control service that uses Git.
    + How does this benefit our project? Our group splits work in such a way that each member owns certain components/parts of our project web application. We used GitHub to regularly check in and merge our source code so as to exercise continuous integration.
* [Vue.js](https://v3.vuejs.org/)
    + What is it? Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.
    + How does this benefit our project? We used Vue in our Youtube API section to separate the user interface from the application logic. It saves lots of work to do the Bootstrap Carousel and makes it easier for us to change the Youtube playlists.
* [animate.css](https://animate.style/#javascript)
    + What is it? Animate.css is a library of ready-to-use, cross-browser animations for use in web projects. Great for emphasis, home pages, sliders, and attention-guiding hints.
    + How does this benefit our project? Our group used animate.css for lots of animations such as fading and sliding.
* [jQuery](https://jquery.com/)
    + What is it? jQuery is a lightweight, "write less, do more", JavaScript library. 
    + How does this benefit our project? jQuery makes it much easier to use JavaScript on our website. We used The jQuery library mainly for HTML/DOM manipulation.

## 🎸 How to Use Our Web Application (for Visitors to our Website) ##
1. Upon entering Pepe Guitarra, Click 'Begin' to start your music learning journey!
1.  It will then being you to the Resources Page
    1. Choose your desired level of Classical Guitar scores
        * Beginner
        * Intermediate
        * Advanced
    1. You then can choose to: 
        1. Download Score
        1. Download MP3
        1. Listen the the MP3 directly
1. Under the Appreciation Page
    1. Explore different Classical Guitar Youtube Playlists
        * Choose different Youtubers by click on the icon
        * Read on the Channel information / Background
        * Watch Channel Playlist
    1. Listen to Spotify playlists on Classical Guitar
        * Click on "Show Me Something New" for more interesting Classical Guitar Playlist

## 🤓 Useful Resources ##
* [**Markdown** Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
* [**GOOD** README Example 1](https://github.com/testing-library/cypress-testing-library)
* [**GOOD** README Example 2](https://github.com/typeorm/typeorm)
* [**GOOD** README Example 3](https://github.com/amark/gun)
* [**GOOD** README Example 4](https://github.com/google/leveldb)
