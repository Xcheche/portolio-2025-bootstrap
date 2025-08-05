$(document).on("click", ".pagination a", function (e) {
  e.preventDefault(); // Prevent full page reload
  var url = $(this).attr("href");
  $.ajax({
    url: url,
    type: "GET",
    success: function (data) {
      // Replace only the paginated part of the page
      $("#pagination-content").html($(data).find("#pagination-content").html());
    },
  });
});
