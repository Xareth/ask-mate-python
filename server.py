from server_python import config
# todo > check why the app doesn't work without the statements below
from server_python import sv_questions
from server_python import sv_general
from server_python import sv_answers


if __name__ == "__main__":
    config.app.run(
        debug=True,
        port=5004
)