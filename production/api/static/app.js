validation = '<div class="validation">\
                <div class="question">Etes vous d\'accord avec cette affirmation :</div>\
                <form class="validation_form">\
                  <button type="button" onclick="yes()">Oui</button>\
                  <button type="button" onclick="no()">Non</button>\
                </form>\
              </div>'

var bad_prediction = ''

function getResult() {
    var form = document.getElementById('inputForm');
    var formData = new FormData(form);
    bad_prediction = document.getElementById('Input_class').value

    fetch('/predict', {
      method: 'POST',
      body: formData
    })
    .then(response => response.text())
    .then(data => {
      document.getElementById('result').innerHTML = data;
      document.getElementById('validation').innerHTML = validation
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  function yes() {
    console.log("YES")
    document.getElementById('result').innerHTML = '';
    document.getElementById('validation').innerHTML = '<div class="thx_class">Merci de votre participation</div>'
    var inputElement = document.getElementById('Input_class');
    inputElement.value = '';
  }

  function no() {
    console.log("NO")
    document.getElementById('result').innerHTML = '';
    document.getElementById('validation').innerHTML = '<div class="thx_class">Merci de votre participation</div>'
    var inputElement = document.getElementById('Input_class');
    inputElement.value = '';
    appInsights.trackTrace({
      message:'Bad prediction',
      properties: {["Tweet"]: bad_prediction},
      severityLevel: "Error"
    });
  }