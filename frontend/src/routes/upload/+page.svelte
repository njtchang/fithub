<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">

<script>
    
    /**
	 * @type {any}
	 */
    let multiValue;
	/**
	 * @type {any}
	 */
	let files;

    /**
	 * @type {any}
	 */


    /**
	 * @param {HTMLFormElement | undefined} files
	 */
    function sendFiles(files) {
        const formData = new FormData(files)
        fetch("https://localhost:5173/img", {
            method: "POST",
            body: formData,
            headers: {
                "Content-Type": "multipart/form-data"
            }
        });
    }

</script>

<nav>
    <div class="nav-logo">
        <img src="src/lib/pictures/logo.png" alt="Your Logo" />
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

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

<div>
    <div class="option">
        Upload Shirt Photo Here
    </div>
    <form>
        <div class = "buttonlabel">
            <label for="file"></label>
            <input
                type="file"
                id="file"
                name="fileToUpload"
                accept=".jpg, .jpeg, .png, .webp"
                bind:files
                required
            />
        </div>
        <div class = "submit-button">
            <button type="submit">Submit</button>
        </div>
    </form>
</div>

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

<div>
    <div class="option">
        Upload Pants Photo Here
    </div>
    <form>
        <div class = "buttonlabel">
            <label for="file"></label>
            <input
                type="file"
                id="file"
                name="fileToUpload"
                accept=".jpg, .jpeg, .png, .webp"
                bind:files
                required
            />
        </div>
        <div class = "submit-button">
            <button type="submit">Submit</button>
        </div>
    </form>
</div>

<style>

    div.nav-logo>img{
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

    }

    .option {
        text-align: center;
    }

    nav {
        display: flex;
        background-color: lightblue;
    }
    ul {
        display: flex;
        margin-top: 30px;
        margin-left: auto;
        list-style: none;
        font-size: 2em;
    }
    li {
        margin-right: 80px;
        font-weight: 900;
        font-family: "Quicksand", sans-serif;
        color: blue;
    }

</style>