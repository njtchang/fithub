<script>
    // let isDropdownOpen = false // default state (dropdown close)

    // const handleDropdownClick = () => {
    //     isDropdownOpen = !isDropdownOpen // togle state on click
    // }

    // const handleDropdownFocusLoss = ({ relatedTarget, currentTarget }) => {
    //     // use "focusout" event to ensure that we can close the dropdown when clicking outside or when we leave the dropdown with the "Tab" button
    //     if (relatedTarget instanceof HTMLElement && currentTarget.contains(relatedTarget)) return // check if the new focus target doesn't present in the dropdown tree (exclude ul\li padding area because relatedTarget, in this case, will be null) 
    //     isDropdownOpen = false
    // }

  let isOpen = false;
  let items = ["Item 1", "Item 2", "Item 3"];

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
            <!-- <div class="flex justify-between items-center">
                <div class="dropdown" on:focusout={handleDropdownFocusLoss}>
                    <button class="btn m-1" on:click={handleDropdownClick} >
                    {#if isDropdownOpen}
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="inline-block h-6 w-6 stroke-current">
                            <title>Close Dropdown</title>
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                        {:else}
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            class="inline-block h-6 w-6 stroke-current">
                            <title>Open Dropdown</title>
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                        {/if}
                    </button>
                    <ul class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52" style:visibility={isDropdownOpen ? 'visible' : 'hidden'}>
                        <li><button class="btn text-slate-300">Item 1</button></li>
                        <li><button class="btn text-slate-300">Item 2</button></li>
                    </ul>
                </div>
                <p class="text-slate-300">
                    isDropdownOpen: {isDropdownOpen}
                </p>
            </div> -->
                <div class="menu">
            <button on:click={() => (isOpen = !isOpen)}>Dropdown</button>

            {#if isOpen}
                <div
                class="absolute left-0 w-48 py-2 mt-2 mr-10 bg-white rounded-lg shadow-xl"
                >
                {#each items as item (item)}
                    <a
                    href="#"
                    class="block px-4 py-2 text-gray-800 hover:bg-indigo-500 hover:text-white"
                    >
                    {item}
                    </a>
                {/each}
                </div>
            {/if}
            </div>
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
        background-color: beige;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    div.menu>button {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem; 
        margin-top: 1rem; 
        color: #ffffff; 
        background-color: #3B82F6; 
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