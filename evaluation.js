function Submission(){
  Submission_response.innerHTML = "Thank you for submitting your evaluation. Your feedback is very important for us."
}

var name = document.getElementById("volunteer_name").value;
var responsibilty = document.getElementById("responsibilty").value;
var time_management = document.getElementById("time").value;
var cooperation = document.getElementById("cooperation").value;
var language = document.getElementById("language").value;
var organisational_skills = document.getElementById("organisation").value;
var project_management = document.getElementById("project").value;

localStorage.setItem("Volunteer", name)
localStorage.setItem("Level of responsibilty", responsibilty)
localStorage.setItem("Level of time-management", time_management)
localStorage.setItem("Level of cooperation", cooperation)
localStorage.setItem("Level of language skills", language)
localStorage.setItem("Level of organisational skills", organisational_skills)
localStorage.setItem("Level of project-management skills", project_management)

