/*If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",
Example: given yourBirthday(4,19) or yourBirthday(19,4)*/

var yourBirthday = "4,19";
var response;
if (yourBirthday == "4,19" || yourBirthday == "19,4") {
    response = "How did you know?";
} else {
    response = "Just another day....";
}
console.log(response);
