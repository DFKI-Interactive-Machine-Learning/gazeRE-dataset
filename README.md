# gazeRE-dataset



We conducted a user study in which we asked users to rate the relevance of read texts with respect to a trigger question. 
We recorded the user's gaze signal and their relevance ratings. 
This repository contains a set of scripts and routines to load, process, and analyse the recorded dataset.
The ultimate goal is to estimate the user's perceived relevance using machine learning with the gaze signal as input.

| package | description |
| ------- | :---------- |
| `data_loading` | Load the recorded dataset, or parts of it, in a single data structure. Load data per paragraph and per paragraph visit, i.e., a continuous scan-path for a paragraph which starts with an initial gaze to a paragraph and ends when the gaze signal leaves the paragraph area. |
| `features` | Extraction of gaze-based features for a certain scan-path. |
| `data` | gazeRE-dataset | 

*See the particular readme files for more detailed information.*

## Dataset
The recorded dataset includes relevance ratings (perceived relevance) from `24` participants for `12` stimuli from the `g-REL` corpus and `12` stimuli from the `Google NQ` corpus. 
The stimuli data used in our study are pairs of trigger questions and documents with one or multiple paragraphs.
We use a subset from the g-REL corpus [[1]](#1) with single-paragraph documents that fit on one page and selected pairs from the Google Natural Questions (NQ) corpus which includes multi-paragraph documents that require scrolling [[2]](#2).
Both corpora include relevance annotations per paragraph which we refer to as system relevance.

Furthermore, throughout their task, the participant's gaze on the screen is recorded and saved for each document.



####  Folder structure
The recorded dataset contains one folder for each participant of the study. The first letter of the folder name denotes the user's starting corpus, and each corpus `g-rel` and `GoogleNQ` has its subfolder. 
A CSV file is created the reading phase of a stimulus, containing the participants' gaze recordings on the stimulus.
The CSV file is named  `OrderID_StimulusID.csv`, with the `OrderID` (0-11) indicating the order in which the user reads the stimulus. The `StimulusID` denotes which document the user views.
Further, a `User_Rating` file saves the participant's relevance estimation for each stimulus after the rating phase.

    <participant_id>
        -GoogleNQ
                -<condition_classifier>.csv
                -User_Rating
        -g-REL
                -<condition_classifier>.csv
                -User_Rating


#### Dataframe structure
      ['timestamp', 'gaze_x', 'gaze_y', 'gaze_y_abs', 'fixation_id', 'scroll_y', 'paragraph_id']
| field | description |
| ------- | :---------- | 
| `timestamp` | Timestamp for each gaze sample in `[s]` |
| `gaze_x` | Horizontal gaze position |
| `gaze_y` | Vertical gaze position |
| `gaze_y_abs` | Absolute vertical gaze position in the document. (Top left `[0.0, doc_max_y]` Bottom Right `[2560.0, 0.0]`) |
| `fixation_id` | ID of the current fixation `[0, num_fixation]`  or `None` if there is no fixation|
| `scroll_y` | Relative scrolling position `[1.0, 0.0]` (Top: `1.0` Bottom: `0.0`) |
| `paragraph_id` | ID of the paragraph that is hit by the gaze signal `[-2 to 6]` with `-1` referring to the headline area and `-2` referring to the remaining free space and `-3` referring to the rating button|

The screen has a resolution of `2560x1440`. Therefore, all x-coordinates lie between `[0.0, 2560.0]` and y-coordinates between `[0.0, 1440.0]`. 

    
## References
<a id="1">[1]</a> 
Jacek Gwizdka. 2014. Characterizing relevance with eye-tracking measures. In Proceedings of the 5th Information Interaction in Context Symposium (IIiX '14). Association for Computing Machinery, New York, NY, USA, 58–67. DOI: https://doi.org/10.1145/2637002.2637011

<a id="2">[2]</a> 
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, Slav Petrov; Natural Questions: A Benchmark for Question Answering Research. Transactions of the Association for Computational Linguistics 2019; 7 453–466. doi: https://doi.org/10.1162/tacl_a_00276
