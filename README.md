# Elsass-TV
Website - elsass TV - the best ever

________________________________________________________________________________________________________________________________________________________________________________________________

    						PROJECTS MEMBERS 

						Hugo Martinet: Product Owner
						Jérémy Rich: Lead Dev
						Florence Schwartz: Senior Dev 
						Quentin Dufrois: Scrum master

________________________________________________________________________________________________________________________________________________________________________________________________

   						    DESCRIPTION OF THE PROJECT

	¤ Main goal of the project: Creation of a website displaying informations on trending movies

	¤ Content of the website (as expressed by the P.O., when he must be consulted an arrow '--->' is displayed):

		* 'Home' menu displaying around a thousand trending movies, and organized as cards (representative pictures of the movie)
		* The 'cards' are clickable and lead to a new page displaying several informations about the movie such as:
			- The picture of the movie (but bigger)
			- A description of the movie
			- A list of the actors (each actors are clickable and lead to a new page described below)
			- The director of the movie (clickable and lead to a new page described below)
			- The rates given by the users
			- The comments left by users
			- A list of the similar movies (each of them clickable and leading to a page similar to this one)
			**** The following points have not been expressed by the P.O. but we add them as he wants something similar to 'allocine' ---> to be discussed with the P.O.
			- The release date of the movie
			- The country of the movie
			- The type of the movie
		* An actor page displaying informations (---> to be discussed with the P.O.) on the actor and movies he/she played in (clickable and lead to the movie description)
		* A director page displaying informations (---> to be discussed with the P.O.) on the director and movies he/she directed (clickable and lead to the movie description)
		* A login/logout page (or buttons in the header ---> to be discussed with the P.O.) for users:
			- When connected a user can add a comment on a movie
			- When connected a user can add a movie in his/her bookmarks list via a star like button
			- A user can add other users as friends. Friends can see each other bookmarks lists, but those lists are otherwise not accessible for other logged in and non-logged in users
			- When connected a user can rate a movie
		* A sign up page for new users
		* A search bar to find out movies by name

	¤ Design of the website:

		* The dominante colour must be blue (but not the only one!)
		* P.O. wants something closer to Netflix than allocine

________________________________________________________________________________________________________________________________________________________________________________________________

						    NOTES FOR THE DEVELOPERS TEAM
	
	Quentin API's key: d6c5128f507174794ba9f372ac42e601

	Server adress: http://107.191.62.201:8080
		
	Models to be created in Django and added in the db (the attributes are still a bit unclear, see above the 'to be discussed with the P.O. points'):

		* Movie, attributes:
			- primary_key(must match the id of the movie in the API)
			- description
			- release date?
			- country?
			- type
			(- rate
			- number of rates (to calculate rate as an average))??? Or make an object Rate to avoid a user to rate several times the same movie?
			****Foreign keys
			- actors
			- director 							
		* User (Generated by Django ---> To discuss if we want to change the attributes, to add foreign keys to comments and bookmarks list (respectively pointing towards Comment and Movie) for instance?)
		* Comment, attributes:
			-title
			-content
			-author
			**** Foreign key
			-Movie			
		* Actor
		* Director
				
				
		





























	

