<script>
	// @ts-nocheck

	function sendImage(clothing) {
		const formData = new FormData();
		const files = document.getElementById(clothing + 'file');
		formData.append('file', files?.files[0]);
		const requestOptions = {
			headers: {
				'Content-Type': files.files[0].contentType
			},
			mode: 'no-cors',
			method: 'POST',
			files: files.files[0],
			body: formData
		};
		console.log(requestOptions);

		fetch('http://localhost:5001/upload/' + clothing, requestOptions).then((response) => {
			console.log(response.data);
		});
	}
</script>

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nova Square" />

<nav>
	<div class="nav-logo">
		<img src="src/lib/pictures/logo.png" alt="Your Logo" />
	</div>
	<div class="title">
		<img src="src/lib/pictures/title.png" alt="title" />
	</div>
	<ul>
		<li>
			<a href="/">Home</a>
		</li>
		<li>
			<a href="/upload">Upload</a>
		</li>
	</ul>
</nav>

<div class="warning">
	<br />
	****PLEASE READ****
</div>

<div class="block-text">
	<br />
	1. Please ensure that the shirt/pants is ENTIRELY within the edges of the photo. <br /><br />
	2. Please ensure the lighting to be not too bright nor too dim. <br /><br />
	3. Please ensure the background of the photo to be reasonably in good contrast with the shirt/pants.
	<br />
	<br />
	<br />
</div>

<div class="card">
	<div class="instruction">Upload Shirt Photo Here</div>
	<form method="GET" action="http://localhost:5173">
		<div class="buttonlabel">
			<label for="file"></label>
			<input
				type="file"
				id="shirtfile"
				name="fileToUpload"
				accept=".jpg, .jpeg, .png, .webp"
				required
			/>
		</div>
		<div class="submit-button">
			<button type="submit" on:click={() => sendImage('shirt')}>Submit</button>
		</div>
	</form>
</div>

<br />

<div class="card2">
	<div class="instruction2">Upload Pants Photo Here</div>
	<form method="GET" action="http://localhost:5173">
		<div class="buttonlabel">
			<label for="file"></label>
			<input type="file" id="pantsfile" name="file" accept=".jpg, .jpeg, .png, .webp" required />
		</div>
		<div class="submit-button">
			<button type="submit" on:click={() => sendImage('pants')}>Submit</button>
		</div>
	</form>
</div>

<style>
	.block-text {
		font-family: 'Nova Square', sans-serif;
		font-size: 20px;
		text-align: center;
	}
	.warning {
		font-size: 40px;
		color: red;
		font-family: 'Nova Square', sans-serif;
		text-align: center;
	}
	.card {
		border: solid rgb(3, 76, 30) 5px;
		border-radius: 12px;
		background-color: rgb(178, 203, 186);
	}
	.card2 {
		border: solid rgb(117, 78, 64) 5px;
		border-radius: 12px;
		background-color: rgb(242, 236, 221);
	}

	div.nav-logo > img {
		width: 200px;
		length: 200px;
		margin: 0;
	}

	.buttonlabel {
		text-align: center;
		padding-left: 65px;
	}

	.submit-button {
		text-align: center;
		padding-top: 10px;
		padding-bottom: 10px;
		border-radius: 12px;
		font-family: 'Nova Square', sans-serif;
	}

	.instruction {
		text-align: center;
		font-family: 'Nova Square', sans-serif;
		font-size: 25px;
		padding-top: 15px;
		padding-bottom: 15px;
		color: rgb(3, 76, 30);
	}
	.instruction2 {
		text-align: center;
		font-family: 'Nova Square', sans-serif;
		font-size: 25px;
		padding-top: 15px;
		padding-bottom: 15px;
		color: rgb(117, 78, 64);
	}
	nav {
		display: flex;
		background-color: lightblue;
		font-family: 'Nova Square', sans-serif;
		border-radius: 12px;
	}
	div.nav-logo {
		margin-left: 30px;
		margin-bottom: 15px;
	}
	div.title > img {
		width: 750px;
		height: 150px;
		z-index: -1;
		margin-left: 90px;
		margin-top: 25px;
	}

	ul {
		display: flex;
		margin-top: 30px;
		margin-left: auto;
		list-style: none;
		font-size: 35px;
	}
	li {
		margin-right: 80px;
		margin-top: 40px;
	}
	a {
		text-decoration: none;
		color: darkblue;
	}
	a:focus {
		color: rgb(87, 87, 205);
	}
	a:hover {
		color: purple;
	}
</style>
