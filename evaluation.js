function Submission(){
Submission_response.innerHTML = "Thank you for submitting your evaluation. Your feedback is very important for us."
var evaluation = {};
evaluation.name = document.getElementById("volunteer_name").value;
evaluation.responsibility = document.getElementById("responsibilty").value;
evaluation.time_management=document.getElementById("time").value;
evaluation.cooperation=document.getElementById("cooperation").value;
evaluation.language=document.getElementById("language").value;
evaluation.organisational_skills = document.getElementById("organisation").value;
evaluation.project_management = document.getElementById("project").value;
console.log(evaluation)
localStorage.setItem( 'evaluation', JSON.stringify(evaluation) );
}
