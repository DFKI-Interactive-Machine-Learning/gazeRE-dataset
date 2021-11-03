# Eye Movement Features
We implement a set of features which are solely based on eye movements, i.e., on the gaze signal and not on the viewed content. The features were previously used in the literature on gaze-based relevance estimation of read texts. We cluster the features into three subsets: features are based on fixation-events, saccade-events, and area-based. **The features are extracted from a single dataframe that satisfy the recording format (see main readme).**

Some features a time-normalized by the total time covered by the provided gaze data. We compute `total_time` as the difference between the last and the first timestamp in the recording.


### Fixation-based

| feature | description |
| ------- | ----------- |
| `fixn_n` | number of fixations |
| `fixn_dur_sum` | sum of fixation durations |
| `fixn_dur_avg` | mean of fixation durations |
| `fixn_dur_sd` | standard deviation of fixation durations |

### Saccade-based
Saccade-based features reveal the distance and coverage of scan-paths.

| feature | description |
| ------- | ----------- |
| `scan_dist_h` | Sum of the horizontal amplitudes of all saccades. Normalized by the factor `w`, e.g., the screen width. |
| `scan_dist_v` | Sum of the vertical amplitudes of all saccades. Normalized by the factor `h`, e.g., the screen height. |
| `scan_dist_euclid` | Sum of normalized saccade amplitudes (Euclidean distance). |
| `scan_hv_ratio` | Ratio of summed horizontal and vertical saccade amplitudes. |
| `avg_sacc_length` | Mean of saccade amplitudes (Mean of Euclidean distances). |
| `scan_speed_h` | Horizontal saccade velocity: `scan_dist_h / total_time`. |
| `scan_speed_v` | Vertical saccade velocity: `scan_dist_v / total_time`. |
| `scan_speed` | Saccade velocity: `scan_dist_euclid / total_time`. |

### Area-based

| feature | description |
| ------- | ----------- |
| `box_area` | Area spanned by horizontal and vertical scan distance: `scan_dist_h * scan_dist_v` |
| `box_area_per_time` | The `box_area` normalized by the time required for scanning it: `box_area / total_time`. |
| `fixns_per_box_area` | Number of fixations per box_area: `fixn_n / box_area`. |
| `hull_area_per_time` | The `hull_area` is the area of the convex hull around all fixations. It is normalized by the time required for scanning the area: `hull_area / total_time`. |
| `fixns_per_hull_area` | Number of fixations per hull_area: `fixn_n / hull_area`. |
