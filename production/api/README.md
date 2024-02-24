## Application

You can put some text in the input of the application for expecting some sentiment analysis prediction.

### Main File  

The `main.py` file is the main entry point of the project. This file contains a `home()` function for rendering the home page of the application with the HTML and Javascript file. And a `predict_sentence()` function for preprocessing the input of the user, load vectorizer and model, predict sentiment for the sentence and print on the screen the result.

```bash
python production/api/main.py
```

### Cleaning File

The cleaning.py file provides functionality to clean the user input. It ensures that the input is properly formatted before used with the model.

### Test File

The test_main.py file contains unit tests for the functionality in main.py. It ensures that the main functionalities are working as expected.