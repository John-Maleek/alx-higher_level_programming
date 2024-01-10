// toggles the class of the <header> element
// when the user clicks on DIV#toggle_header

$("DIV#toggle_header").click(function () {
  $("header").toggleClass("red green");
});
