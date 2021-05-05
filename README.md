<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://csgitlab.ucd.ie/yeohbraddy/fyp-braddy">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Learning to Sparsify the Capacitated Vehicle Routing Problem Instances</h3>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

In this project, classification is utilized to classify whether an edge is part of the optimal solution of the Capacitated Vehicle Routing Problem (CVRP), an NP-hard combinatorial optimization problem. The random forest classifier learns through features that capture the essence of whether an edge is part of the optimal solution. It then classifies edges of unseen CVRP instances to prune away any negatively labeled edges as these are not part of the solution. The experiments measure the improvement of the optimality gap and running time of the solver between the unpruned instance and the pruned instance. The results demonstrated good performance on a variety of instances that have different characteristics. For example, prior to pruning, the solver took 300 seconds with a non-zero optimality gap to solve a particular instance. After pruning, the solver took less than 10 seconds and achieved a zero optimality gap.

### Built With

- [Sklearn](https://scikit-learn.org/stable/)
- [LocalSolver](https://www.localsolver.com/docs/last/index.html)
- [Gurobi](https://www.gurobi.com/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Ensure LocalSolver license is on your machine. Visit their to request a free license and follow the steps to install their software.
- Ensure Gurobi license is on your machine. Visit their site to request a free license and follow the steps to install their software.
- Jupyter notebook.
- Python modules

### Installation

1. Clone the repo

```sh
git clone https://csgitlab.ucd.ie/yeohbraddy/fyp-braddy
```

2. Install the Python modules

```sh
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->

## Usage

From the root of the project, run:

```sh
jupyter notebook
```

to access the machine learning model notebook to view the machine learning evaluation charts after pruning.

From the CLI, run:

```sh
python Main.py
```

to execute the script.

It is important to note that choosing which function to run involves switching feature flags manually. This is done in Main.py.

Lets say we want to prune an instance and assuming the training data is the most up to date (it is provided as a CSV as data.csv), use these feature flags to generate the test data of the instance to prune.

```
generate_training_data = False
generate_test_data = True
solve_pruned = False
solve_unpruned = False
```

The test instance should be placed in fyp-braddy/Instances/Instances - Prune and its respective solution in fyp-braddy/Instances/Solutions - Prune.

Then run fyp-braddy/Modules/ipynb/Model.ipynb to train the models and prune the instance (this takes some time). You are able to vary the decision threshold under the prune section of the notebook by replacing the THRESHOLD:

```
decision_function = np.where(rf_clf.predict_proba(extracted_X_val)[:,1] >= THRESHOLD, 1, 0)
```

Next, use these feature flags to run (Main.py) the solver on the unpruned instance:

```
generate_training_data = False
generate_test_data = False
solve_pruned = True
solve_unpruned = False
```

This only needs to be done once to measure the objective function value and running time. The optimal objective function value is found in the last line of the solution file called 'Cost':

```
Route #1: 21 31 19 17 13 7 26
Route #2: 12 1 16 30
Route #3: 27 24
Route #4: 29 18 8 9 22 15 10 25 5 20
Route #5: 14 28 11 4 23 3 2 6
Cost 784
```

Finally, use these feature flags to run (Main.py) on the pruned instance:

```
generate_training_data = False
generate_test_data = False
solve_pruned = False
solve_unpruned = True
```

As you vary the threshold of the pruned instance in model.ipynb, you can execute Main.py to run on the newly pruned instance to measure the objective function value and running time.

Unfortunately, each instance has different performances so the evaluation of the performances of both the unpruned and prune instance was manually recorded.

<!-- CONTACT -->

## Contact

Braddy Yeoh - braddy.yeoh@ucdconnect.ie

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

I would like to thank Dr. Deepak Ajwani for his help, my family, friends, Alan Fahey for their support, especially during difficult times, and finally Robin Lee for letting me use his compute server.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
