<h1 align="center">TitanicSurvivalPredictor</h1>
<p align="center">
  <img alt="titanicsurvivalpredictor" height="200" src="https://media.giphy.com/media/OJw4CDbtu0jde/giphy.gif?cid=790b7611tfw5xgdvh4yax2h6nlpa3e2ik94wkl4ik0hs6g3e&ep=v1_gifs_search&rid=giphy.gif" />
</p>

<p align="center">
  <a href="https://github.com/yakovypg/YFaceRecognizer/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-darkyellow.svg" alt="license" />
  </a>
  <img src="https://img.shields.io/badge/Version-1.0.0-red.svg" alt="version" />
  <img src="https://img.shields.io/badge/Python-3.11-blue" alt="python" />
</p>

## About
**TitanicSurvivalPredictor** is a Python script that can predict a survival on the Titanic.

## Table of contents
*    [Quick Start](#quick-start)
     * [Setup](#setup)
     * [Run Tool](#run-tool)
*    [License](#license)

## Quick Start
Follow these steps:
- Clone repository.
    ```
    git clone https://github.com/yakovypg/TitanicSurvivalPredictor.git
    ```
- Open the following folder.
    ```
    cd TitanicSurvivalPredictor
    ```
- Create virtual environment.
    ```
    python3 -m venv .venv
    ```
- Activate virtual environment.
    ```
    source .venv/bin/activate
    ```
- Install required packages.
    ```
    pip install -r requirements.txt
    ```
- Open `src` folder and [run](#run-tool) `titanic_predict.py`.

### Setup
You can install all the necessary components in one command.
```
./setup.sh
```

### Run Tool
You should specify the parameters of the passenger, the probability of surviving which you want to know. Suppose you want to know the probability of surviving a woman who had a first class ticket and who didn't have brothers and sisters on the Titanic. Then the command will be the following.
```
python3 titanic_predict.py --sex 1 --pclass 1 --sibsp 0
```

## License
The project is available under the [MIT](LICENSE) license.
