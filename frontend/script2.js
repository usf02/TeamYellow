document.addEventListener("DOMContentLoaded", function () {
    const pdfFilesInput = document.getElementById("pdfFiles");
    const jpgFilesInput = document.getElementById("jpgFiles");
    const submitBtn = document.getElementById("submitBtn");
    const message = document.getElementById("message");

    submitBtn.addEventListener("click", function () {
        const pdfFiles = pdfFilesInput.files;
        const jpgFiles = jpgFilesInput.files;

        if (pdfFiles.length === 0 && jpgFiles.length === 0) {
            message.innerText = "Please select one or more files to upload.";
            return;
        }

        // Prepare the FormData object to send the files
        const formData = new FormData();
        for (let i = 0; i < pdfFiles.length; i++) {
            formData.append("pdfFiles", pdfFiles[i]);
        }
        for (let i = 0; i < jpgFiles.length; i++) {
            formData.append("jpgFiles", jpgFiles[i]);
        }

        // Send the data to the server (you would need a server-side script to handle the file uploads)
        // Example: fetch('/upload', { method: 'POST', body: formData })
        // Replace '/upload' with the actual server endpoint to handle file uploads
    });
});
