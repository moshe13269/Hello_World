from dataclasses import dataclass
import datargs


@dataclass
class MyArgs:
    """
    When using code from the Command Line Interface (CLI), underscores (_) should be replaced by dashes (-).
    For example, to run this file with different arguments use the command
    python cmd_example.py --num-people 10 --num-simulations 3
    The usage example looks like this:
    D:\Downloads>python cmd_example.py --num-people 10 --num-simulations 3
    Running 3 simulations with 10 people each.
    Note that every variable must have a type, otherwise you won't be able to change this argument from the shell
    """
    num_people: int = int(1e5)  # Comments can be used for documentation
    num_simulations: int = 1000000  # Unlike argparse's help, comments won't be presented in the CLI


def main(args: MyArgs):
    print(f"Running {args.num_simulations} simulations with {args.num_people} people each.")


if __name__ == "__main__":
    args = datargs.parse(MyArgs)
    main(args)