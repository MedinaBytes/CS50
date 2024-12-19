# MovieBuddy

#### Video Demo:

#### Description:
**MovieBuddy** is an interactive movie and TV series discovery platform where users can filter and explore content based on their preferences, such as genre, release year, and type (movie or TV series). By selecting the genre, year, and type, users are presented with relevant suggestions, and they can even view a detailed overview of a movie or show, including its cast, rating, and trailer link. The main feature of the project is the ability to swap the main movie or TV show with any of the suggested ones by clicking on them, creating an engaging and dynamic experience.

### About the Developer:
- **Name**: Jonathan Medina
- **GitHub Username**: [MedinaBytes](https://github.com/MedinaBytes)
- **Location**: Poland, Warsaw
- **Date**: 12/19/2024

### Key Features:
1. **Movie and TV Series Filtering**:
   - Users can filter content based on genre (Action, Comedy, Drama, etc.), release year, and type (movie or TV series).
   - The genres are dynamically fetched from the TMDb (The Movie Database) API.

2. **Main Movie/TV Show Display**:
   - The first movie or TV show in the filtered results is displayed in detail with its poster, title, description, release year, rating, and the cast.
   - If a trailer exists, users can view it directly from the platform.

3. **Dynamic Movie Swapping**:
   - Users can click on any movie suggestion to replace the main movie’s content with the clicked suggestion’s details, allowing for quick and easy exploration of similar movies.

4. **Responsive Design**:
   - The website adjusts automatically based on screen size, ensuring an optimal viewing experience on mobile devices, tablets, and desktops.

---

### Project Breakdown:

#### Code Structure:
- **index.html**:
   - The HTML file defines the structure and layout of the MovieBuddy website. It includes the header with the MovieBuddy logo, the main section containing the filtering form, and the display area for the main movie and its suggestions.
   - The layout is divided into sections such as filters, movie details, suggestions, and footer.

- **app.py**:
   - This is the core of the backend logic. It's a Flask-based web application that fetches movie and TV series data from the TMDb API. The backend processes the filtering criteria from the user (genre, year, type) and sends the appropriate data to the frontend.
   - It includes functions like `get_genre_names()` to fetch genre names based on genre IDs and `get_trailer_url()` to get the trailer link for a movie or show.

#### Key Functions Added:
1. **`get_genre_names()`**:
   - This function takes a list of genre IDs and returns the names of the genres associated with them. It queries the TMDb API for the genres and maps the IDs to their corresponding names.

2. **`get_trailer_url()`**:
   - This function retrieves the trailer URL for a movie or TV show. It fetches the videos from the TMDb API and searches for a trailer.

3. **`index()`**:
   - This is the main route function that handles both GET and POST requests. It receives the filter options (genre, year, type) from the user and fetches relevant movies or TV shows from the TMDb API. The function randomly selects five suggestions for the user to explore.
   - It also processes the data to display the main movie or show with its details, such as title, poster, genre names, and rating.

#### How I Created It:
- **Backend (Flask)**: I chose Flask because it’s lightweight and simple to set up for small to medium-sized applications. Using Flask’s route and rendering capabilities, I was able to build dynamic pages where the content is updated based on user input.
- **TMDb API**: I integrated the TMDb API to fetch movie and TV show data. This included movie posters, release dates, genres, cast, and trailer URLs, which I used to populate the website dynamically.
- **Frontend (HTML, CSS, JavaScript)**:
   - The frontend was designed to be visually appealing and user-friendly. I used a minimalist dark theme to provide an immersive movie discovery experience.
   - The layout is responsive, with mobile-friendly forms and movie displays that adjust based on screen size.
   - JavaScript was used to allow users to click on movie suggestions and dynamically swap the main movie's details, creating a seamless user experience.

### Additional Notes:
- **Data Fetching**: I used the `requests` library in Python to make API calls to the TMDb service, retrieving movie information such as genres, posters, cast, and trailers.
- **Error Handling**: Basic error handling was implemented for cases where the API call fails, ensuring the application doesn’t break and providing users with a fallback experience.
- **UI/UX**: I focused on providing a simple, yet effective user interface, using CSS for styling and icons from FontAwesome to add visual flair.

### Challenges Faced:
- Integrating multiple API endpoints from TMDb and ensuring that data such as cast and trailer information was fetched properly for both movies and TV series.
- Designing a responsive interface that would work seamlessly on both desktop and mobile devices.

### Future Improvements:
- Add a search functionality that allows users to directly search for a specific movie or TV series.
- Implement user accounts for saving movie preferences or creating a watchlist.
- Include movie ratings from other sources like IMDB for a more comprehensive review.

---
