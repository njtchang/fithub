<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">

<script>
// @ts-nocheck

	function send() {
        const formData = new FormData();
        const files = document.getElementById("file");
        formData.append("file", files?.files[0]);
        const requestOptions = {
            headers: {
                "Content-Type": files.files[0].contentType,
            },
            mode: "no-cors",
            method: "POST",
            files: files.files[0],
            body: formData,
        };
        console.log(requestOptions);

        fetch("http://localhost:5001/upload", requestOptions).then(
            (response) => {
                console.log(response.data);
            }
        );
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
    <form method="GET" action="http://localhost:5173">
        <div class = "buttonlabel">
            <label for="file"></label>
            <input
                type="file"
                id="file"
                name="file"
                accept=".jpg, .jpeg, .png, .webp"
                required
            />
        </div>
        <div class = "submit-button">
            <button type="submit" on:click={send}>Submit</button>
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