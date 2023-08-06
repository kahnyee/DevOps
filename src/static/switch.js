document
  .getElementById("switch-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    $.ajax({
      type: "POST",
      url: "/switch-state",
      success: function (result) {
        if (result == 1) {
          document.getElementById("switch").innerText = "Start/Stop";
        } else if (result == -1) {
          document.getElementById("switch").innerText = "Start/Stop";
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
