function validation() {  
	var success = "";	
	success += nameValidation(); 	
	success += emailValidation();
	success += passwordValidation();
	success += termValidation();
	
	if (success == "") return true;
	
	alert("Validation:" + success);
	return false;	
}

function nameValidation() {
	var name = document.getElementsByName("name")[0].value;
	if (name.length <= 3)
		return "Please enter at lease 3 characters\n";	
	return "";
}

function passwordValidation() {
	var password = valueOf("password");
	var retype = valueOf("retype_password");
	
	if (password.length <= 6) 
		return "Please enter password of at least 6 characters\n";
	
	if (password != retype) 
		return "Passwords not matched\n";	
	return "";
}

function emailValidation() {
	var email = valueOf("email");
	var retype = valueOf("retype_email");
	
	if (email.indexOf('@') == -1) 
		return "Enter a valid email address\n";
	
	if (email != retype)
		return "Email addresses not matched\n";
	return "";	
}

function valueOf(name) {
	return document.getElementsByName(name)[0].value;
}