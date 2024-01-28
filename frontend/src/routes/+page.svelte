<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nova Square">

<script>
	let shirtIsOpen = false;
	let pantIsOpen = false;
	let idNum = 0;
	let shirtItems = ['Shirt 1', 'Shirt 2', 'Shirt 3'];
	let pantItems = ['Pant 1', 'Pant 2', 'Pant 3', 'pant 4', '5', '6', '7', '8'];
</script>

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

<body>
	<div class="row">
		<div class="outfit-side">
			<header>
				<h1>Outfit</h1>
			</header>
			<img src="src/lib/pictures/combo_outfit.png" alt="outfit" />
		</div>
		<div class="gallery-side">
			<div class="directions-title">
				DIRECTIONS
			</div>
			<div class="directions-body">
				Click the dropdown menus to access shirts and pants. Once you have chosen your desired combination, 
				click the generate button to create your new outfit!
			</div>
			<header>
				<h1>Gallery</h1>
			</header>
			<div class="menu">
				<div>
                    <button on:click={() => (shirtIsOpen = !shirtIsOpen)}>Shirt
                    </button>

					{#if shirtIsOpen}
						<div class="dropbuttons">
							{#each shirtItems as item, index}
								<button value={index} on:click={() => (shirtIsOpen = !shirtIsOpen)}>{item}</button>
							{/each}
						</div>
					{/if}
				</div>
				<div>
					<button on:click={() => (pantIsOpen = !pantIsOpen)}>Pants</button>

					{#if pantIsOpen}
						<div class="dropbuttons">
							{#each pantItems as item, index}
								<button value={index} on:click={() => (pantIsOpen = !pantIsOpen)}>{item}</button>
							{/each}
						</div>
					{/if}
				</div>
			</div>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <div class="generate">
                <button>Generate!</button>
            </div>
			<!-- <div class="directions-title">
				DIRECTIONS
			</div>
			<div class="directions-body">
				Click the dropdown menus to access shirts and pants. Once you have chosen your desired combination, 
				click the generate button to create your new outfit!
			</div> -->
		</div>
	</div>
</body>

<style>
	div.nav-logo > img {
		width: 200px;
		length: 200px;
		margin: 0;
	}
	div.row {
		display: flex;
        font-family: "Nova Square", sans-serif;
	}
	div.outfit-side {
		width: 50%;
		background-color: rgb(178, 203, 186);
		display: flex;
		flex-direction: column;
		align-items: center;
        border: solid rgb(3, 76, 30) 5px;
        border-radius: 12px;
        color: rgb(2, 50, 20);
	}
	div.outfit-side > img {
		width: 50%;
		height: 700px;
	}
	div.gallery-side {
		width: 50%;
		background-color: rgb(242, 236, 221);
		display: flex;
		flex-direction: column;
		align-items: center;
        border: solid rgb(117, 78, 64) 5px;
        border-radius: 12px;
        color: rgb(69, 49, 42);
	}
	.directions-title {
		margin-top: 40px;
		font-weight: bold;
		font-size: 40px;
	}
	.directions-body {
		margin: 50px;
		margin-top: 30px;
		font-size: 20px;
	}
    div.menu {
        display: grid;
        grid-template-columns: 240px 240px;
        text-align: center;
    }
	div.menu button {
		padding-top: 0.5rem;
		padding-bottom: 0.5rem;
		margin-top: 1rem;
		color: black;
		/* background-color: #9cc7e6; */
		width: 12rem;
        border-radius: 12px;
        font-size: 20px;
        background-color: #e4c784;
	}

	div.dropbuttons {
		left: 0;
		/* padding-top: 0.5rem;
        padding-bottom: 0.5rem;  */
		margin-top: 0.5rem;
		margin-right: 2.5rem;
		border-radius: 0.5rem;
		width: 12rem;
		background-color: transparent;
		/* box-shadow:
			0 20px 25px -5px rgba(0, 0, 0, 0.1),
			0 10px 10px -5px rgba(0, 0, 0, 0.04); */
        
	}
	div.dropbuttons> button {
		/* display: flex; */
		/* flex-direction: column; */
		padding: 15px;
		border: none;
		background-color: rgb(232, 218, 179);
		width: 100%;
        margin-left:25px;
        box-shadow:
			0 20px 25px -5px rgba(0, 0, 0, 0.1),
			0 10px 10px -5px rgba(0, 0, 0, 0.04);
	}
	div.dropbuttons > button:hover {
		background-color: #b49c78;
	}
    div.generate button{
        padding-top: 0.5rem;
		padding-bottom: 0.5rem;
		margin-top: 1rem;
		color: black;
		background-color: #e4c784;
		width: 12rem;
        border-radius: 12px;
        font-size: 20px;
    }
	nav {
		display: flex;
		background-color: lightblue;
        font-family: "Nova Square", sans-serif;
        border-radius: 12px;
	}
    button {
        font-family: "Nova Square", sans-serif;
    }
    div.nav-logo {
        margin-left: 30px;
        margin-bottom: 15px;
    }
    div.title>img{
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
	h1 {
		margin-top: 20px;
		margin-left: 30px;
		font-size: 3em;
	}
</style>
