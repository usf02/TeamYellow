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

        console.log(pdfFiles);

        // Prepare the FormData object to send the files
        const formData = new FormData();
        for (let i = 0; i < pdfFiles.length; i++) {
            formData.append("pdfFiles", pdfFiles[i]);
        }
        for (let i = 0; i < jpgFiles.length; i++) {
            formData.append("jpgFiles", jpgFiles[i]);
        }


    });
});

/*const form = document.querySelector('form');
form.addEventListener("submit", handleSubmit);

function handleSubmit(event) {
    const form = event.currentTarget;
    const url = new URL(form.action);
    const formData = new FormData(form);
    const searchParams = new URLSearchParams(formData);
  
    const fetchOptions = {
      method: form.method,
    };
  
    if (form.method.toLowerCase() === 'post') {
      if (form.enctype === 'multipart/form-data') {
        fetchOptions.body = formData;
      } else {
        fetchOptions.body = searchParams;
      }
    } else {
      url.search = searchParams;
    }
  
    fetch(url, fetchOptions);
  
    event.preventDefault();
  }*/
