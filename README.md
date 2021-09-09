# HAX712X: Software development for data science

(Almost) everything you need to know as an applied mathematician / statistician concerning coding and system administration.

## Teachers

- Joseph Salmon : joseph.salmon@umontpellier.fr,
- Benjamin Charlier : benjamin.charlier@umontpellier.fr

This course material was improved with the help of some students including:

- Amelie Vernay
- Tanguy Lefort


## Prerequisite

Students are expected to know basic notions of probabilities, optimization, linear algebra and statistics for this course.
Some rudiments on coding is also expected (if, for, while, functions) but not mandatory.

## Course description

This course focuses on discovering good coding practices (the language used being Python, but some element of bash and git will also be useful) for professional coding.
A special focus on data processing and visualization will be at the heart of the course.
We will mostly focus on basic programming concepts, as well as on discovering the Python scientific libraries, including ```numpy, scipy, pandas, matplotlib, seaborn```.
Beyond `pandas` ninja skills, we will also introduce modern practices for coders : (unitary) tests, version control, documentation generation, etc.


1. BC : (10/09/2021) [Introduction to linux essentials and command line tools: regexp, grep, find, rename](Courses/Bash/)

2. BC : (17/09/2021) [IDE: VScode](Courses/IDE/), [Python virtual env: Anaconda](Courses/Venv/), [Python virtual environment](Courses/Venv/), terminal, etc.

3. BC : (24/09/2021) [Git: a first introduction, `github`, ssh key creation, various git commands, conflict, pull request](Courses/Git/); see also [Bonus/](Bonus/), [hands on git](Courses/Git/)

4. BC (quiz 1) + JS : (01/10/2021) [Create a Python Module](Courses/Python-modules/), [classes (`__init__`, `__call__`, etc...), operator overloading, files handling](Courses/Classes_n_Exceptions/),

5. JS : (08/20/2021)  [unit tests](Courses/Tests-CI/)

6. JS : (15/10/2021)  [Pandas: first steps / missing data](Courses/Pandas/)

7. JS : (22/10/2021) [`scipy, numpy`: Images/channel](Courses/Scipy/)

8. JS (quiz 2) : (29/10/2021) [Sparse matrices,](Courses/TimeMemory/) [graphs and memory](Courses/TimeMemory/)

9. BC : (19/11/2021) [Documentation with Sphinx](Courses/Docs/)

10. JS + BC : (12/12/2021) The end:  Project presentations


## Grading


### Tests (20 % of the final grade)
Short quiz of 20 min each (on Moodle). This will be a personal work.

- Quiz 1 BC (**01/10/2021**, 10%)
- Quiz 2 JS (**29/10/2021**, 10%)


### Project 80% (= oral 30% + code/report 50%) of the final grade)


**Warning:** the precise details of the projects might evolve before the allocation phase, and a precise grid will be given in the project section.

**Warning:** the project repository must show a balanced contribution between group members and intra-group grades variation could be made to reflect issues on the intra-group workload balance.

### Bonus

**1 supplementary point** on the final grade of the course can be obtained for contributions improving the course material (practicals, Readme, etc.).
See the [Bonus](Bonus/) section for more details on how to proceed.



## Books and other resources

The resources for the course are available on the present `github` repository. Additional elementary elements (**in French**) on Python are available in the course [HLMA310](http://josephsalmon.eu/HLMA310.html) and the associated lectures notes [IntroPython.pdf](http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf).

### Additional resources

- (General) : [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
- (Data Science) : J. Van DerPlas, *Python Data Science Handbook, With Application to Understanding Data*, 2016<https://jakevdp.github.io/PythonDataScienceHandbook/>
- (General) Skiena, *The algorithm design manual*, 1998
- (General) Courant et al. , *Informatique pour tous en classes préparatoires aux grandes écoles : Manuel d'algorithmique et programmation structurée avec Python*,
2013, (french)
- (General/data science) Guttag, *Introduction to Computation and Programming*,
2016

    Associated videos: <http://jakevdp.githubio/blog/2017/03/03/reproducible-data-analysis-in-jupyter/>

- (Code and style) Boswell et Foucher, *The Art of Readable Code*, 2011
- (Scientific computing tools for Python) <http://www.scipy-lectures.org/>
- (Visualization) <http://openclimatedata.net/>
