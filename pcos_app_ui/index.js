const API_ENDPOINT = "http://localhost:5000/predict";

function predict() {
    const fileInput = document.getElementById("image");
    const file = fileInput.files[0];
    const uploaded_image = document.getElementById("uploaded_image");
    const predictionContainer = document.getElementById("prediction");
    const predictionValuesContainer = document.getElementById("prediction_values");
    const imagePreview = document.getElementById("image_preview");
    const predictionValue = document.getElementById("prediction_value");
    const scoreValue = document.getElementById("score_value");
    const lds_spinner = document.querySelector(".lds-spinner");

    predictionValuesContainer.style.display = "none";
    imagePreview.style.display = "none";
    uploaded_image.style.display = "none";

    if (!file) {
        alert("Please select an image file.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    imagePreview.src = URL.createObjectURL(file);
    imagePreview.style.display = "block";
    uploaded_image.style.display = "flex";
    predictionContainer.style.display = "flex";

    lds_spinner.style.display = "inline-block";
    fetch(API_ENDPOINT, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        predictionValue.textContent = data.prediction;
        if(data.prediction === "infected") {
            predictionValue.style.color = "red";
        }
        else {
            predictionValue.style.color = "green";
        }
        scoreValue.textContent = Math.trunc(data.score*100)/100;
        predictionValuesContainer.style.display = "flex";
        lds_spinner.style.display = "none";
    })
    .catch(error => console.error(error));
}
