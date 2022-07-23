# PowerAsana Backend
____________

**Project Description**
The backend of a power vinyasa yoga app made for practitioners at home and yoga teachers looking for sequence inspiration and a place to store their personalized sequences.

**Deployed API**
[Link to deployed API on Heroku](https://powerasana.herokuapp.com/poses)
**There's no home page for the API - try toggling from /poses to /sequences to see more.

**Technologies Used**
Django (Django React Framework), Python

**Frontend Materials**
[Live User-Facing Application](https://powerasana.netlify.app/)
[Frontend GitHub Repository](https://github.com/bbkc27/powerasana-frontend)

**Key Features**
- Users are able to sign up so they can create their own sequences that are only viewable, editable, and deletable to them
- Users can view all poses and pose information (English Name, Sanskrit, Suggested Cues, Illustrations)
- Users can view all admin-created sequences
- Poses and sequences have a many to may relationship
- Users can use the app easily no matter the screen size
- Users can stay signed in longer than their access token life time (refresh occurs frequently)