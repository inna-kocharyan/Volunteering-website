function Volunteermatcher() {
var Volunteer_age = parseInt(document.getElementById("required_age").value);
var English_Level_Input = parseInt(document.getElementById("English_level").value);
var Russian_Level_Input = parseInt(document.getElementById("Russian_level").value);
var Armenian_Level_Input = parseInt(document.getElementById("Armenian_level").value);
var German_Level_Input = parseInt(document.getElementById("German_level").value);
var display = document.getElementById("MatchingVolunteers");
var volunteer;
display.innerHTML = "Our volunteers list that match your criteria"+"<br>"
for ( var i = 0;i < 10;i++ in volunteers_list.volunteers) {
volunteer = volunteers_list.volunteers[i]
if ( volunteer["Age"] >= Volunteer_age && volunteer["English"]>=English_Level_Input && volunteer["Armenian"] >= Armenian_Level_Input && volunteer["German"] >= German_Level_Input && volunteer["Russian"] >= Russian_Level_Input) {
 console.log(volunteer["First Name"])
 display.innerHTML +=  volunteer["Last Name"]+ " " + volunteer["First Name"] + "<br>"
 }
}
}
function checkAge(evt) {
var Volunteer_age = parseInt(document.getElementById("required_age").value);
if ( Volunteer_age > 100 || Volunteer_age < 0) {
  console.log("Wrong value")
  evt.currentTarget.style.color = "red"
} else {
  console.log("Correct Value")
  evt.currentTarget.style.color = "black"
 }
}
