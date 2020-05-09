function usernameCheck(){
	const username = document.querySelector('#username').value;
	const request = new XMLHttpRequest();
	const message = document.querySelector('#message');
	const submit = document.querySelector('#submit');
	request.open('GET', 'register/check/' + username + '/');
	
	request.onload = () => {
		const data = JSON.parse(request.responseText);
		
		if (data.success){
			message.innerHTML = 'username unavailable';
			message.className = 'text-warning';
			submit.setAttribute('disabled', 'disabled');
		}
		else{
			message.innerHTML = 'username available';
			message.className = 'text-success';
			submit.removeAttribute('disabled')
			submit.setAttribute('active', 'active')
		}
	};
	
	request.send();
}

function logout(){
	l = confirm('Do you want to logout ?');
	if (l==true){
		return True;
	}
	else{
		return False;
	}
}