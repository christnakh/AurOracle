document.addEventListener('DOMContentLoaded', function () {
    const inputForm = document.getElementById('inputForm');
    const resultDiv = document.getElementById('result');

    inputForm.addEventListener('submit', function (e) {
        e.preventDefault();

        
        const inputData = 
        {
            feature1: parseFloat(inputForm.elements.magnitude.value),
            feature2: parseFloat(inputForm.elements.vectorMag.value),
            feature3: parseFloat(inputForm.elements.bx.value),
            feature4: parseFloat(inputForm.elements.by.value),
            feature5: parseFloat(inputForm.elements.bz.value),
            feature6: parseFloat(inputForm.elements.rmsScalar.value),
            feature7: parseFloat(inputForm.elements.rmsVector.value),
            feature8: parseFloat(inputForm.elements.rmsBx.value),
            feature9: parseFloat(inputForm.elements.rmsBy.value),
            feature10: parseFloat(inputForm.elements.rmsBz.value),
            feature11: parseFloat(inputForm.elements.speed.value),
            feature12: parseFloat(inputForm.elements.density.value),
            feature13: parseFloat(inputForm.elements.temperature.value),
        };


        
        fetch('https://auroracle.onrender.com/predictkp', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(inputData),
        })
        .then(response => response.json())
        .then(data => {
            const kp_data = data.predicted_kp;
            if (kp_data<5){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp}`;
            }
            else if(kp_data >=5 && kp_data<=6 ){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp} class: G1`;
            }else if(kp_data >6 && kp_data<=7){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp} class: G2`;
            }else if(kp_data >7 && kp_data<=8){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp} class: G3`;
            }else if(kp_data >8 && kp_data<=9){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp} class: G4`;
            }else if(kp_data >=9){
                resultDiv.innerHTML = `Predicted KP Value: ${data.predicted_kp} class: G5`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'An error occurred while making the prediction.';
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const predictForm = document.getElementById("prediction-form");
    const dataContainer = document.getElementById("data-container");

    predictForm.addEventListener("submit", function (event) {
        event.preventDefault(); 
        const kp = document.getElementById("kpap").value
        
        fetch("https://auroracle.onrender.com/predictdata", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                KpIndex: kp, 
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                const speed = data["Speed (km/s)"];
                const temperature = data["Temperature (K)"];
                const protonDensity = data["Proton Density (n/cc)"];

                dataContainer.innerHTML = `
                    <p>Speed (km/s): ${speed}</p>
                    <p>Temperature (K): ${temperature}</p>
                    <p>Proton Density (n/cc): ${protonDensity}</p>
                `;
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    });
});



function message(){
    alert("its not yet finished")
}
