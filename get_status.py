import subprocess


def get_status() -> str:
    output = subprocess.run(["nordlayer", "status"], capture_output=True)

    text = output.stdout.decode('utf-8').split("\n")
    # print(f"{text=}")

    text = next(line for line in text if line.startswith("VPN:"))
    status = text.split(" ")[-1]
    # print(f"{status=}")

    return status


# def parse(status: str) -> str:
#     match status:
#         case "Disconnected":
#
#
#     return "ok"


if __name__ == "__main__":
    get_status()