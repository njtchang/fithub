<script>
	/**
	 * @type any
	 */
	let files;

    const formData = new FormData(files)

    fetch("https://localhost:5173/img", {
        method: "POST",
        body: formData,
        headers: {
            "Content-Type": "multipart/form-data"
        }
    });
</script>

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
</style>

{#if files && files[0]}
    <p>
        {files[0].name}
    </p>
{/if}