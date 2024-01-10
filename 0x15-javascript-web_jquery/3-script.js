// J adds the class red to the <header> element
// when the user clicks on DIV#red_header

$("DIV#red_header").click(function () {
  $("header").addClass("red");
});
