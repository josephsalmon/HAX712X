# Project guidelines

- Work by groups of 3 or 4 students, assigned at random (list on the Moodle website).

# Instructions

The project will be two-fold: handle datasets from the French electricity consumption with the motivation to create a visualization inspired by the image below, and to predict electricity consumption on a future day.

<img src=https://www.upenergie.com/wp-content/uploads/2022/04/la-consommation-delectricite-en-quelques-chiffres.png>



**Data link for prediction:** for this part the dataset is available at <https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure>.
The goal is simply to predict the consumption on Thursday 8 December for the whole day, at the country-wise scale.
We will measure your score as a Mean Square Error on the 96 quarters of hour during that day, so your output should simply be a `.csv` file with the following structure:

|Date |Heure| Consommation (MW)|
|-----|--------------|----------------|
|2022-12-08 | 00:00 |30811|
|2022-12-08 | 00:15 |30889|
|... |...|...|
|2022-12-08 | 23:45 |30878|



You will also display your prediction for all the sources (Gas, wind, etc.) on a simple graph of your choice.


**Data link for visualization:** for this part the dataset is available at <https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/>.

The motivation is to analyze and understand better the electricity consumption of the French household.

The main task for this part of the project, is to provide an interactive map of France at the city-wise level displaying the yearly average household electricity consumption between 2018 and 2021.
The map should be clickable, and when clicking on a city, you would display the distribution (with a violin plot, a swarmplot or a KDE plot for instance) of consumption per household in this city over the four years.

**Hint**: you could be inspired by this gif

<img src=https://tinyurl.com/3hy49v4s>

Could you also spot for Occitanie and Herault which cities have the largest/smallest consumption?


## Intermediate tasks
 - data **cleaning steps**: removing missing values if need be.

## Major objectives:
- displays **interactive maps**.

Useful packages (non-exhaustive list):
- `osmnx`
- `plotly`
- `folium`
- `networkx`


## Timing
- **Mid-term** project snapshot: Due date  **November 15, 23:59**. This will include the creation of a ```github``` repository (README.md, etc.), a short description on how the work is shared in the team and a detailed work program for the project including the tasks' attribution (coding).

- **Preliminary presentation** : An oral presentation with *Beamer* (duration: 5mn), in-person on date/place TBC (December 2 (13:15 to 14:45).

- Due date (final project) : The ```github``` repository should be completed before **Tuesday 6 December (23:59)**. Nothing pushed after the deadline will be taken into account. The oral presentation (max: 20mn) will be in-person **Friday 9 December (8:00AM)** (room: 36.4).


## Elements expected / Grading


### Summary

|General |Details|Points (out of 20)|
|-----|--------------|----------------|
|**Mid-term**|Git / branches|1.5             |
|     |Task affectation|1
|     |Dataset creation|1               |
|**Preliminary-term**|Beamer (structure, spelling)|  0.5           |
|**Code**|Science Technical Problem Resolution|4.5             |
|     |Readme/Comments/Pep8|1               |
|     |Unit Tests/CI/Deploy : wheel|1               |
|     |Class (create at least 1 class)|0.5             |
|     |Reproducibility/Dataset loading|1               |
|     |Graphical aspects: Widgets, clickable map, etc. |2.5             |
|     |Time/Memory efficiency|1               |
|     |Documentation |1.5             |
|**Oral** |Beamer (structure, spelling)|1             |
|     |Clarity / lively presentation / Rhythm / Show |2               |
| **Total**|| 20|


### Details

- The ultimate goal is to provide a Python module that can be imported with `pip` and containing your work.
A description of the procedure will be needed (imagine you are addressing to a user not aware of your package).
An example of project, made in 2020, is available at <https://github.com/tanglef/chaoseverywhere>.

- The project must be stored on a `github` repository.

- You have to choose a name for your project. Hereafter, it is denoted by `my_module_name`.

- It should contain all the aspects described below.

### Science
Solve (even partially) the problem raised in your project description.


### Project structure

- All the code will be placed in a subdirectory called `/my_module_name` (choosing your module name accordingly).

- A presentation (in an open source format: like Beamer, with TeX, see for instance some templates here <https://github.com/josephsalmon/OrganizationFiles>, or LibreOffice Impress) will be put in a `/beamer` directory. The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

- A documentation (using `sphinx`) will be stored in a `/doc` subdirectory.

### Git aspects

- A (markdown) `readme.md` file introducing your work and the team member (first/last name + email).

- A `.gitignore` that prevent garbage files to be included in your project.

- Equilibrated commits in two branches should be done (*e.g.,* in development branch and the master one), and merged for the milestone day.

### Object programming aspects

- You should code at least one `Python` class.

### Dataset(s)

- The data used should be available in a way that the end user do not need to perform a manual download of any kind (use package `download` or variants for instance).

### Graphical aspects

The repository will contain code of the following nature:

- A code producing a (possibly interactive) map.

- histograms/kde/swarmplots/etc. plots illustrating the data.

### Time/memory evaluation

- A full study of the time and memory footprint of the code produced will be provided for the whole pipeline used.

### Documentation

- Documentation should be added correctly for the functions written. Please use `sphinx`.

### Test and CI

- Provide unitary tests to check that the function you proposed satisfies the requirement you target.
- Implement a Continuous Integration solution with `github` that run your unitary test at each commit.

### Deploy

- It should be possible to package your Python module using `wheel` (*i.e.*, you need to provide a `setup.py`, file).
