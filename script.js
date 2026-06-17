const API_BASE_URL = "https://netflix-clone-u1m5.onrender.com";

console.log("Script Loaded");

async function login() {
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  if (!emailInput || !passwordInput) {
    return;
  }

  const email = emailInput.value.trim();
  const password = passwordInput.value;

  if (!email || !password) {
    alert("Please enter both email and password.");
    return;
  }

  try {
    const response = await fetch(
      `${API_BASE_URL}/login?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`,
      { method: "POST" }
    );

    if (!response.ok) {
      throw new Error(`Login request failed with status ${response.status}`);
    }

    const data = await response.json();

    if (data.message === "Login Successful") {
      window.location.href = "browse.html";
    } else {
      alert("Invalid email or password.");
    }
  } catch (error) {
    console.error("Login failed:", error);
    alert("Unable to log in right now. Please try again later.");
  }
}

async function loadMovies() {
  const moviesContainer = document.getElementById("movies");

  if (!moviesContainer) {
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/movies`);

    if (!response.ok) {
      throw new Error(`Movies request failed with status ${response.status}`);
    }

    const movies = await response.json();

    if (!Array.isArray(movies)) {
      throw new Error("Movies response was not a list.");
    }

    moviesContainer.innerHTML = movies
      .map((movie) => {
        const title = movie.title || "Untitled";
        const poster = movie.poster_url || "https://picsum.photos/200/300";
        const category = movie.category || movie.catagory || "";

        return `
          <div class="movie-card">
            <img src="${poster}" alt="${title}">
            <h3>${title}</h3>
            <p>${category}</p>
          </div>
        `;
      })
      .join("");
  } catch (error) {
    console.error("Could not load movies:", error);
    alert("Unable to load movies right now. Please try again later.");
  }
}

function searchMovies() {
  const searchInput = document.getElementById("search");

  if (!searchInput) {
    return;
  }

  const search = searchInput.value.toLowerCase();
  const cards = document.querySelectorAll(".movie-card");

  cards.forEach((card) => {
    const movieName = card.innerText.toLowerCase();
    card.style.display = movieName.includes(search) ? "block" : "none";
  });
}

function logout() {
  window.location.href = "index.html";
}

loadMovies();
