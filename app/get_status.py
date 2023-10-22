import subprocess


def get_status() -> str:
    output = subprocess.run(["nordlayer", "status"], capture_output=True)

    text = output.stdout.decode('utf-8').split("\n")

    text = next(line for line in text if line.startswith("VPN:"))
    status = text.replace("VPN: ", "")
    # print(f"{status=}")
    return status


if __name__ == "__main__":
    get_status()
