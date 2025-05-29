def read_properties(file_path):
    props = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    props[key.strip()] = value.strip()
            return props
    except Exception as e:
        print(f"An error occurred : {e}")
        return None
