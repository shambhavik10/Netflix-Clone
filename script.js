const API_BASE_URL = "https://netflix-clone-u1m5.onrender.com";

console.log("Script Loaded");

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const response = await fetch(
    `${API_BASE_URL}/login?email=${email}&password=${password}`,
    { method: "POST" }
  );

  const data = await response.json();

  if (data.message === "Login Successful") {
    window.location.href = "browse.html";
  } else {
    alert("Invalid Email or Password");
  }
}

async function loadMovies() {
  const moviesContainer = document.getElementById("movies");

  if (!moviesContainer) return;

  const response = await fetch(`${API_BASE_URL}/movies`);
  const movies = await response.json();

  let html = "";

  movies.forEach(movie => {
    const poster = movie.poster_url || "https://picsum.photos/200/300";

    html += `
      <div class="movie-card">
        <img src="${poster}" alt="${movie.title}">
        <h3>${movie.title}</h3>
        <p>${movie.catagory || ""}</p>
      </div>
    `;
  });

  moviesContainer.innerHTML = html;
}

loadMovies();

function searchMovies() {
  const search = document.getElementById("search").value.toLowerCase();
  const cards = document.querySelectorAll(".movie-card");

  cards.forEach(card => {
    const movieName = card.innerText.toLowerCase();
    card.style.display = movieName.includes(search) ? "block" : "none";
  });
}

function logout() {
  window.location.href = "index.html";
}