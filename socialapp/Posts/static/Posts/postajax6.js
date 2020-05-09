function like(id){
	var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
	const post = document.querySelector(`#post${id}`).value;
	const username = document.querySelector(`#post_username${id}`).value;
	const showlikes = document.querySelector(`#showlikes${id}`);
	const likebutton = document.querySelector(`#likebutton${id}`);
	const peopleliked = document.querySelector(`#peopleliked${id}`);
	const url = location.protocol + '//' + document.domain + ':' + location.port + '/post/like';
	const request = new XMLHttpRequest();
	request.open('POST', url);
	
	request.onload = () =>{
		const data = JSON.parse(request.responseText);
		if (data.likes > 0){
		showlikes.innerHTML= data.likes;
		peopleliked.style.visibility = 'visible';
		}
		else{
			showlikes.innerHTML= ' ';
			peopleliked.style.visibility = 'hidden';
		}
		
		if (data.liked && data.likes > 1){
			peopleliked.innerHTML = `You and ${data.likes - 1	} others`;
		}
		if (data.liked && data.likes == 1){
			peopleliked.innerHTML = 'You liked this post';
		}
		if (!data.liked && data.likes >= 1){
			peopleliked.innerHTML = `${data.likes} likes`;
		}
		
		
	};
	data = new FormData();
	data.append('post', post);
	data.append('username', username);
	data.append('csrfmiddlewaretoken', csrftoken);
	request.send(data);
	
	return None;
}

function comment(id){
	var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
	const username = document.querySelector(`#post_username${id}`).value;
	let comment = document.querySelector(`#comment${id}`);
	const post = document.querySelector(`#post${id}`).value;
	const comments = document.querySelector(`#comments_container${id}`);
	const url = location.protocol + '//' + document.domain + ':' + location.port + '/post/comment/';
	const request = new XMLHttpRequest();
	request.open('POST', url);
	
	request.onload = () => {
		const data = JSON.parse(request.responseText);
		comment.value = '';
		const newComment = document.createElement('div');
		const newHr = document.createElement('hr');
		newComment.classList.add('p2')
		newComment.innerHTML = data.comment;
		comments.append(newComment);
		comments.append(newHr);
		
	};
	
	data = new FormData();
	data.append('post', post);
	data.append('username', username);
	data.append('comment', comment.value);
	data.append('csrfmiddlewaretoken', csrftoken);
	request.send(data);
	
	return None;
}

