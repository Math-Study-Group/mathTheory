import nox

BOOK = "book"
HTML = f"{BOOK}/_build/html"


@nox.session(name="book", venv_backend="none")
def book(session):
    session.run("jupyter-book", "build", BOOK, external=True)


@nox.session(name="book-clean", venv_backend="none")
def book_clean(session):
    session.run("jupyter-book", "clean", BOOK, external=True)
    session.run("jupyter-book", "build", BOOK, external=True)


@nox.session(name="book-live", venv_backend="none")
def book_live(session):
    """
    Stable live preview (optimized watcher version)
    """

    session.run(
        "python",
        "-c",
        r'''
import socket
import subprocess
import webbrowser
from livereload import Server

BOOK = "book"
HTML = "book/_build/html"
HOST = "127.0.0.1"
START_PORT = 8000


def find_free_port():
    port = START_PORT
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, port))
                return port
            except OSError:
                port += 1


def build():
    print("\n[build] JupyterBook rebuilding...")
    subprocess.run(["jupyter-book", "build", BOOK])


port = find_free_port()

# initial build
build()

server = Server()

# =========================
# ONLY WATCH REAL SOURCES
# =========================

server.watch("book/**/*.md", build, delay=1)
server.watch("book/**/*.rst", build, delay=1)
server.watch("book/**/*.ipynb", build, delay=1)

# optional (safe configs)
server.watch("book/_toc.yml", build, delay=1)
server.watch("book/_config.yml", build, delay=1)

# =========================
# IGNORE BUILD ARTIFACTS
# =========================

server.ignore = [
    "book/_build/**",
    "**/.jupyter_cache/**",
    "**/__pycache__/**",
]

url = f"http://{HOST}:{START_PORT}"

print(f"[live] serving at {url}")
print("[live] watching md/rst/ipynb only")

webbrowser.open(url)

server.serve(
    root=HTML,
    host=HOST,
    port=START_PORT,
    open_url_delay=None
)
''',
        external=True,
    )