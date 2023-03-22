const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const searchResults = document.getElementById("search-results");

// fonction de recherche en direct
function search(query) {
  // simulate an API call to get search results
  const results = ["Google Search Result 1", "Google Search Result 2", "Google Search Result 3"];

  // effacer les recherches précédentes
  searchResults.innerHTML = "";

  // afficher les résultats
  results.forEach(result => {
    const li = document.createElement("li");
    li.textContent = result;
    searchResults.appendChild(li);
  });
}

// événement de clic sur le bouton de recherche
searchButton.addEventListener("click", event => {
  event.preventDefault();
  const query = searchInput.value;
  search(query);
});

// événement de saisie dans la barre de recherche
searchInput.addEventListener("input", event => {
  const query = searchInput.value;
  search(query);
});