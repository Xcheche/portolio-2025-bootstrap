

// Testimonial
$("#testimonial-form").on("submit", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "",
    data: new FormData(this),
    processData: false,
    contentType: false,
    headers: { "X-CSRFToken": "{{ csrf_token }}" },
    success: () => {
      $("#msg").html(
        "✅ Submitted! Check the home page for updates. Thank you."
      );
      setTimeout(() => {
        $("#msg").html("");
      }, 3000); // 3000ms = 3 seconds
    },
    error: () => {
      $("#msg").html("❌ Error!");
      setTimeout(() => {
        $("#msg").html("");
      }, 5000);
    },
  });
});
