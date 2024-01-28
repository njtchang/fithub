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
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

<div>
    <div class="instruction">
        Upload Photo Here
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
    .buttonlabel {
        text-align: center;
        padding-left: 65px;
    }

    .instruction {
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .submit-button {
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;

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
    }
</style>