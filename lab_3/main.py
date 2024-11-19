from checksum import get_invalid_list, calculate_checksum, serialize_result
from file_handler import read_csv, read_json
from consts import DATA, PATTERNS, VARIANT




def main():
    data = read_csv(DATA)
    
    patterns = read_json(PATTERNS)
    
    checksum = calculate_checksum(get_invalid_list(data, patterns))
    serialize_result(VARIANT, checksum)
  


if __name__ == "__main__":
    main()