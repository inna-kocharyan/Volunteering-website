function matching() {
var age1 = parseInt(document.getElementById('age').value);
var experience1 = parseInt(document.getElementById('experience').value);
var excel1 = parseInt(document.getElementById('ex').value);
var english1 = parseInt(document.getElementById('English').value);
var russian1 = parseInt(document.getElementById('Russian').value);
var display = document.getElementById("display1");
var job;
display.innerHTML = "Opportunities that match you:"+"<br>"

for (var i in jobs.opportunities){
  job = jobs.opportunities[i]
  if (job["required_age"] <= age1 && job["required_experience"] <= experience1 && job["excel"] <= excel1 && job["English"] <= english1 && job["Russian"] <= russian1){
    console.log(job["Name"])
    display.innerHTML +=  job["Name"] + "<br>"}
   else{
    alert("Nope")
  }
}
}


