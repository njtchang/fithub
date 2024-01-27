<script>
    let count = 0
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

<body>
    <div class="row">
        <div class="outfit-side">
            <header>
                <h1>Outfit</h1>
            </header>
            <img src="src/lib/pictures/temp-outfit.png" alt="outfit" />
        </div>
        <div class="gallery-side">
            <header>
                <h1>Gallery</h1>
            </header>
            <p>
                The count is: {count}
            </p>
            <button on:click={()=> count += 1}>
                Increment
            </button>
        </div>
    </div>
</body>

<style>
    div.nav-logo>img{
        width: 200px;
        length: 200px;
        margin: 0;
    }
    div.row {
        display: flex;
    }
    div.outfit-side {
        width: 50%;
        background-color: bisque;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    div.outfit-side>img {
        width: 50%;
        height: 75%;
    }
    div.gallery-side {
        width: 50%;
        float: right;
        background-color: beige;
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
    h1 {
        margin-top: 20px;
        margin-left: 30px;
        font-size: 3em;
    }
</style>