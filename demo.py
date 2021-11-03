from data_loading import gazeRE_DataLoader
from features.feature_extractor import LongestVisitFeatureExtractor, extract_training_data

if __name__ == '__main__':
    # Set the minimal number of fixations for a visit and the minimal visit duration to be considered
    min_fixations = 0
    min_visit_duration = 3

    # Set the feature export directory
    target_dir = "./"

    # Intialize the gazeRE_Dataloader which loads the dataset
    dataloader = gazeRE_DataLoader(data_dir="data", googleNQ=True, gREL=True)

    # Initialize the FeatureExtractor with LongestVisitFeatureExtractor which takes the longest visit for each paragraph
    feature_extractor = LongestVisitFeatureExtractor(
        min_visit_duration=min_visit_duration, min_fixations=min_fixations, screen_width=2560, screen_height=1440
    )

    # Extract the feature file for the g-REL corpus
    d_grel = extract_training_data(study_data=dataloader.grel, target_dir=target_dir,
                                   feature_extractor=feature_extractor)

    # Extract the feature file for the Google NQ corpus
    d_nq = extract_training_data(study_data=dataloader.google_nq, target_dir=target_dir,
                                 feature_extractor=feature_extractor)
