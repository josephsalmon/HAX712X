# Project guidelines

- Work by groups of 3 or 4 students, assigned at random (list on the Moodle website).

# Instruction

The project topics will be to handle a dataset from from the French highways society (ASF).

**Data link:** for prices <https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf>.

The motivation is to analyse and understand better the pricing policy of this company.
We will restrict the analysis on the south part of France (A9, A61, A62, A66, A75 and A709 highway between Montpellier, Perpignan, Pamier and Toulouse), see **page 3** of the previous pdf.

The main task is to provide a description of the costs distribution for each section of the highway: it does depend on where you enter and get out. For instance,

- between Exits #36 and #37 the cost is 2€ and distance is 22.6km yielding an average cost of 0.088 €/km.
- between Exits #36 and #43 the cost is 10.3€ and distance is 107km yielding an average cost of 0.096 €/km.

 Hence, a **graphical visualization** of this final outcome is the major output of this project.

 Intermediate tasks:
 - data **cleaning steps**: removing missing values or free sections
 - the creation of a data structure containing the **prices between every exits**.
 - the creation of a data structure containing the **distances between every exits**.


Major objectives:
- displays **interactive maps** with possibly clickable (for instance with `plotly`) roads.
- plot the **distribution of prices** at each section of the road (the variability being on the in/out possible ways).
- It appears to be cheaper to exit and re-enter the highway during a trip than to to go straight from the initial point to final destination... Thence, provide an algorithm that compute the minimal fees to go from one exit to another with the constraint k maximum in/out.

Useful packages (non exhaustive list):
- `osmnx`
- `plotly`
- `folium`
- `networkx`

Useful links (non exhaustive list):
- <https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf>
- <https://data.laregion.fr/explore/dataset/trace-du-reseau-autoroutier-doccitanie/information/>
- <https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routier-national-concede/>



## Timing
- **Mid-term** project snapshot: Due date  **Monday November 15, 23:59**. This will include the creation of a ```github``` repository (README.md, etc.), a short description on how the work is split and a detailed work program for the project including how the task are attributed (coding).

- Due date (final project) :  The ```github``` repository should be completed before **Thursday 9 December (23:59)**. Nothing pushed after the deadline will be taken into account. The oral presentation (max: 20mn) will be in-person **Monday 13 December 8:00AM** (room 36.02).


## Elements expected /  Grading


### Summary

|General |Details|Points (out of 20)|
|-----|--------------|----------------|
|**Mid-term**|Git / branches|1.5             |
|     |Task affectation|1
|     |Dataset creation|1               |
|**Code**|Science Technical Problem Resolution|4.5             |
|     |Readme/Comments/Pep8|1               |
|     |Unit Tests/CI/Deploy : wheel|1               |
|     |Class (create at least 1 class)|0.5             |
|     |Reproducibility/Dataset loading|1               |
|     |Graphical aspects: Widgets, clickable map, etc...|2.5             |
|     |Time/Memory efficiency|1               |
|     |Documentation |1.5             |
|**Oral** |Beamer (structure, spelling)|1.5             |
|     |Clarity / lively presentation / Rhythm / Show |2               |
| **Total**| | 20|


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

- All the code will be placed in a sub-directory called `/my_module_name` (choosing your module name accordingly).

- A presentation (in an open source format: like Beamer, with TeX, see for instance some templates here <https://github.com/josephsalmon/OrganizationFiles>, or LibreOffice Impress) will be put in a `/beamer` directory. The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

- A documentation (using `sphinx`) will be stored in a `/doc` sub-directory.

### Git aspects

- a (markdown) `readme.md` file introducing your work and the team member (first/last name + email).

- A `.gitignore` that prevent garbage files to be included in your project.

- equilibrated commits in two branches should be done (*e.g.,* in development branch and the master one), and merged for the milestone day.

### Object programming aspects

- you should code at least one `Python` class.

### Dataset(s)

- The data used should be available in a way that the end user do not need to perform a manual download of any kind.

### Graphical aspects

The repository will contain code of the following nature:

- a code producing a (possibly interactive) map.

- histograms/kde/swarm/etc. plots illustrating the data.

### Time/memory evaluation

- A full study of the time and memory footprint of the code produced will be provided.

### Documentation

- Documentation should be added correctly for the functions written. Please use `sphinx`.

### Test and CI

- Provide unitary tests to check that the function you proposed satisfies the requirement you target.
- Implement a Continuous Integration solution with `github` that run your unitary test at each commit.

### Deploy

- It should be possible to package your Python module using `wheel` (*i.e.*, you need to provide a `setup.py`,  file).
