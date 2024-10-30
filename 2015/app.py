import argparse
import importlib
import datetime
from utils.submission import Submission
from utils.files import Files
import sys


def main():
    _today = datetime.date.today().day

    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument(
        "-d",
        "--day",
        dest="day",
        default=_today,
        metavar="day_number",
        type=int,
        help="Required, day number of the AoC event",
    )
    parser.add_argument(
        "-p",
        "--part",
        dest="part",
        default=1,
        metavar="part_number",
        type=int,
        help="Required, part number of the day of the AoC event",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Optional, use raw input instead of stripped input",
    )
    parser.add_argument("--add", action="store_true", help="Optional, create daily file")
    parser.add_argument(
        "--add-test-file",
        metavar="test_number",
        type=int,
        help="Optional, create additional test files",
    )
    parser.add_argument("-s", "--skip-test", action="store_true", help="Optional, skipping tests")
    parser.add_argument("-t", "--test", action="store_true", help="Optional, running tests only")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="Optional, benchmarking the code, and also skipping tests",
    )
    parser.add_argument("--submit", action="store_true", help="Optional, submit your answer to AoC")
    args = parser.parse_args()
    print()
    if not 0 < args.day < 26:  # noqa: PLR2004
        print("🚫 Day number must be between 1 and 25")
        sys.exit()
    elif args.add is True:
        print("➕ Adding day", args.day)  # noqa: RUF001
        Files.add_day(args.day)
    elif args.add_test_file is not None:
        print("➕ Adding test file for day", args.day, ", no", args.add_test_file)  # noqa: RUF001
        Files.add_test_file(args.day, args.add_test_file)
    elif args.part not in [1, 2]:
        print("🚫 Part number must be 1 or 2")
        sys.exit()
    else:
        print(f"🤖 Solving day {args.day} part {args.part}\n")

        sol = importlib.import_module(f"solutions.day{args.day:02d}").Solution(
            args.day, args.raw, args.skip_test, args.test, args.benchmark
        )

        if args.test is True:
            print("🧪 Running tests only\n")
            sol.test_runner(args.part)
        else:
            print(
                f"📝 The answer is {answer}\n"
                if (answer := sol.solve(part_num=args.part)) is not None
                else ""
            )

        sol.benchmark(_print=True)

        if not args.test and answer and args.submit is True:
            print("\n🚀 Submitting answer to AoC")
            Submission.send_answer(args.day, args.part, answer)


if __name__ == "__main__":
    main()
