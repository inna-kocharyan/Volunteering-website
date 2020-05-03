document.addEventListener('DOMContentLoaded', (event) => {
    var button = document.getElementById("button");
    button.onclick = function () {
    formValidation()   
} 
});
   
function formValidation() {
    var name = document.getElementById("name");
    var nameValue = name.value
    var surname = document.getElementById("surname");
    var surnameValue = surname.value
    var region = document.getElementById("region");
    var regionValue = region.value
    var address = document.getElementById("address");
    var addressValue = address.value
    var gender = document.getElementById("gender");
    var genderValue = gender.value
    var email = document.getElementById("email");
    var emailValue = email.value

    var armlang = document.getElementById("armlang");
    var armlangValue = armlang.value
    var ruslang = document.getElementById("ruslang");
    var ruslangValue = ruslang.value
    var englang = document.getElementById("englang");
    var englangValue = englang.value
    var gerlang = document.getElementById("gerlang");
    var gerlangValue = gerlang.value
    var frlang = document.getElementById("frlang");
    var frlangValue = frlang.value
    var arblang = document.getElementById("arblang");
    var arblangValue = arblang.value
    var otherlang = document.getElementById("otherlang");
    var otherlangValue = otherlang.value

    var student = document.getElementById("student");
    var studentValue = student.value
    var undergraduate = document.getElementById("undergraduate");
    var undergraduateValue = undergraduate.value
    var graduate = document.getElementById("graduate");
    var graduateValue = graduate.value
    var employee = document.getElementById("employee");
    var employeeValue = employee.value
    var other = document.getElementById("other");
    var otherValue = other.value

    var exp = document.getElementById("exp");
    var expValue = exp.value
    var about = document.getElementById("about");
    var aboutValue = about.value
    if (name_validation(name, 3, 15)) {
        if (letter_validation1(name)) {
            if (surname_validation(surname, 5, 20)) {
                if (letter_validation2(surname)) {
                    if (gender_validation(gender)) {
                        if (region_validation(region)) {
                            if (address_validation(address)) {
                                if (email_validation(email)) {
                                    if (lang_validation(armlang, ruslang, englang, gerlang, frlang, arblang, otherlang)) {
                                        if (status_validation(student, undergraduate, graduate, employee, other)) {
                                            if (about_validation(about, 4, 500)) {
                                                if (exp_validation(exp, 4, 500)) {
                                                    var obj = { "name ": nameValue,"surname ": surnameValue, "region ": regionValue, "address ": addressValue, "email ": emailValue, "languages ": armlang, "status ": studentValue, "experience": expValue, "about": aboutValue }
                                                    window.localStorage.setItem("INFO", JSON.stringify(obj))
                                                    alert('Form Succesfully Submitted');
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

function name_validation(name, x, y) {
    var name_len = name.value.length;
    if (name_len == 0 || name_len > y || name_len < x) {
        alert("Name blank should not be empty and the length should be between from " + x + " to " + y);
        name.focus();
        return false;
    }
    return true;
}

function letter_validation1(name) {
    var letters = /^[a-zA-Z]+$/;
    if (name.value.match(letters)) {
        return true;
    }
    else {
        alert('Name must include alphabetic characters only!');
        name.focus();
        return false;
    }
}

function surname_validation(surname, x, y) {
    var surname_len = surname.value.length;
    if (surname_len == 0 || surname_len > y || surname_len < x) {
        alert("Surname blank should not be empty and the length should be between from " + x + " to " + y);
        surname.focus();
        return false;
    }
    return true;
}

function letter_validation2(surname) {
    var letters = /^[a-zA-Z]+$/;
    if (surname.value.match(letters)) {
        return true;
    }
    else {
        alert('Surname must include alphabetic characters only!');
        surname.focus();
        return false;
    }
}

function gender_validation(gender) {
    if (gender.value == "Default") {
        alert('Select your gender from the list!');
        gender.focus();
        return false;
    }
    else {
        return true;
    }
}

function region_validation(region) {
    if (region.value == "Default") {
        alert('Select your region from the list!');
        region.focus();
        return false;
    }
    else {
        return true;
    }
}

function address_validation(address) {
    var letters = /^[0-9a-zA-Z]+$/;
    if (address.value.match(letters)) {
        return true;
    }
    else {
        alert('Your address blank should not be empty and must contain alphanumeric characters only!');
        address.focus();
        return false;
    }
}

function email_validation(email) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email.value.match(mailformat)) {
        return true;
    }
    else {
        alert("Your email blank is empty or you have entered an invalid email address!");
        email.focus();
        return false;
    }
}

function lang_validation(armlang, ruslang, englang, gerlang, frlang, arblang, otherlang) {
    x = 0;
    if (armlang.checked) {
        x++;
    }
    if (ruslang.checked) {
        x++;
    }
    if (englang.checked) {
        x++;
    }
    if (gerlang.checked) {
        x++;
    }
    if (frlang.checked) {
        x++;
    }
    if (arblang.checked) {
        x++;
    }
    if (otherlang.checked) {
        x++;
    }
    if (x == 0) {
        alert('Select at least one of the language options');
        armlang.focus();
        return false;
    }
    return true;
}

function status_validation(student, undergraduate, graduate, employee, other) {
    x = 0;
    if (student.checked) {
        x++;
    }
    if (undergraduate.checked) {
        x++;
    }
    if (graduate.checked) {
        x++;
    }
    if (employee.checked) {
        x++;
    }
    if (other.checked) {
        x++;
    }
    if (x == 0) {
        alert('Select one of the status options');
        student.focus();
        return false;
    }
    return true;
}

function about_validation(about, x, y) {
    var about_len = about.value.length;
    if (about_len == 0 || about_len >= y || about_len < x) {
        alert("About blank should not be empty and the length should be between from " + x + " to " + y);
        about.focus();
        return false;
    }
    return true;
}

function exp_validation(about, x, y) {
    var exp_len = exp.value.length;
    if (exp_len == 0 || exp_len >= y || exp_len < x) {
        alert("Experience blank should not be empty and the length should be between from " + x + " to " + y);
        exp.focus();
        return false;
    }
    return true;  
}
