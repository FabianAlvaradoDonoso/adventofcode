import urllib.request, urllib.parse  # noqa
import os, sys, re, json  # noqa
from .config import AOC_HEADERS, AOC_SESSION


class Submission:
    @staticmethod
    def send_answer(day, level, answer):
        session = Submission.get_session()
        year = Submission.get_path().split(os.sep)[-1].split("-")[-1]

        headers = Submission.get_headers()
        headers["Referer"] = f"https://adventofcode.com/{year}/day/{day}"
        headers["Cookie"] = f"session={session}"

        url = f"https://adventofcode.com/{year}/day/{day}/answer"
        method = "POST"
        values = {"level": level, "answer": answer}
        data = urllib.parse.urlencode(values).encode("utf-8")

        req = urllib.request.Request(url, method=method, headers=headers, data=data)

        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf-8")

        article = re.findall(r"<article>(.*?)</article>", content, re.DOTALL)[0]
        article = "".join(article.split("</p>"))
        article = article.replace("\n", "")
        article = re.sub(r"<.*?>", "", article, re.DOTALL)
        article = re.sub(r"\[Return.*?\]", "", article, re.DOTALL)
        article = re.sub(r"You\scan\s\[Share.*$", "", article, re.DOTALL)
        article = article.replace("!", "!\n")
        article = article.replace(".", ".\n")
        article = article.replace(".\n)", ".)")

        lines = [
            line
            for line in [line.strip() for line in article.strip().split("\n")]
            if not line.startswith("If you're stuck")
        ]

        print()
        for line in lines:
            print(line)

    @staticmethod
    def get_session():
        # session = ""
        # path = Submission.get_path()
        return AOC_SESSION

    @staticmethod
    def get_headers():
        headers = {}
        # path = Submission.get_path()
        headers = json.loads(AOC_HEADERS)
        return headers

    @staticmethod
    def get_path():
        return (
            path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
        )
