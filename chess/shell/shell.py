from subprocess import Popen, PIPE, STDOUT


class Shell:
    def __init__(self, file: str):
        self.file = file
        self.process = Popen(file, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)

    def communicate(self, cmd: str) -> str:
        if not cmd.endswith("\n"):
            cmd += "\n"
        self.process.stdin.write(bytes(cmd, "ascii"))
        self.process.stdin.flush()
        return self.process.stdout.readline().decode()
