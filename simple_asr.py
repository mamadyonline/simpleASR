"""This file contains all the code doing the feature extraction, the training and the inference."""

class SimpleASR:
    def __init__():
        pass
    
    def extract_feature(sound_file: str) -> list:
        """Either MFCC or something alike.

        Args:
            sound_file (str): the path to the sound file.
        
        Returns:
            list: The extracted feature in an array.
        """
        pass

    def fit(X: list) -> None:
        """Train the model on X.

        Args:
            X (list): training data
        """
        pass

    def predict(X: list) -> list:
        """Do the inference on X.

        Args:
            X (list): The data of prediction.

        Returns:
            list: The predicted categories in an array.
        """
        pass

    def score(X: list, y: list) -> float:
        """The score of the model on the given data.

        Args:
            X (list): The data of which to predict the classes.
            y (list): The predicted categories.

        Returns:
            float: The score of the model.
        """
        pass