// Portfolio Search
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("portfolio-search-form");
  const overlay = document.getElementById("loading-overlay");
  const portfolioGrid = document.getElementById("portfolio-grid");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const query = document.getElementById("search-input").value;
    const url = form.action + "?q=" + encodeURIComponent(query);

    overlay.style.display = "block"; // Show full-page dim and spinner

    fetch(url, {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.text())
      .then((data) => {
        const parser = new DOMParser();
        const html = parser.parseFromString(data, "text/html");
        const newPortfolioGrid = html.querySelector("#portfolio-grid");

        if (newPortfolioGrid) {
          portfolioGrid.innerHTML = newPortfolioGrid.innerHTML;
        } else {
          portfolioGrid.innerHTML = "<p>No matching portfolio items found.</p>";
        }

        overlay.style.display = "none"; // Hide overlay after content loads
      })
      .catch((error) => {
        console.error("Error:", error);
        overlay.style.display = "none"; // Always hide overlay even on error
      });
  });
});
