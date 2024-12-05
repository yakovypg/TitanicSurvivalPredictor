import warnings
import argparse
import pandas as pd

from predictor import Predictor

DATASET_PATH = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
TARGET = 'Survived'


def _load_data(path):
    return pd.read_csv(path)


def _preprocess_data(data):
    data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Fare'].fillna(data['Fare'].median(), inplace=True)

    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

    return data


def _create_evidence(args):
    evidence = {}

    if args.pclass is not None:
        evidence['Pclass'] = args.pclass

    if args.sex is not None:
        evidence['Sex'] = args.sex

    if args.age is not None:
        evidence['Age'] = args.age

    if args.sibsp is not None:
        evidence['SibSp'] = args.sibsp

    if args.parch is not None:
        evidence['Parch'] = args.parch

    if args.fare is not None:
        evidence['Fare'] = args.fare

    if len(evidence) == 0:
        raise RuntimeError('No parameter is specified')

    return evidence


def _configure_parser():
    parser = argparse.ArgumentParser(
        prog="titanic_predict",
        description="Survival predictor on the Titanic")

    parser.add_argument(
        "--pclass",
        type=int,
        choices=[1, 2, 3],
        help="Ticket class: 1 = 1st, 2 = 2nd, 3 = 3rd")

    parser.add_argument(
        "--sex",
        type=int,
        choices=[0, 1],
        help="Gender: 0 = male, 1 = female")

    parser.add_argument(
        "--age",
        type=int,
        help="Age in years")

    parser.add_argument(
        "--sibsp",
        type=int,
        help="Number of siblings and spouses aboard the Titanic")

    parser.add_argument(
        "--parch",
        type=int,
        help="Number of parents and children aboard the Titanic")

    parser.add_argument(
        "--fare",
        type=int,
        help="Passenger fare")

    return parser


if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    parser = _configure_parser()
    args = parser.parse_args()

    evidence = _create_evidence(args)

    data = _load_data(DATASET_PATH)
    data = _preprocess_data(data)

    predictor = Predictor(data, TARGET)
    result = predictor.perform_inference(evidence)

    print(result)
