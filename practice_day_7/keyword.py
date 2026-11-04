def create_device_config(device_id, **kwargs):

    config = {}

    config["device_id"] = device_id

    allowed = ["baud_rate", "parity", "timeout_ms", "debug"]

    for key in kwargs:

        if key in allowed:
            config[key] = kwargs[key]

        else:
            raise ValueError("Unsupported key: " + key)

    return config


result = create_device_config(
    "D01",
    baud_rate=115200,
    parity="N",
    timeout_ms=500
)

print(result)