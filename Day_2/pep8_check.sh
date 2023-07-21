#!/bin/bash

# Check if the required commands are installed
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

check_commands() {
    local commands=("flake8" "interrogate" "black" "isort")

    for cmd in "${commands[@]}"; do
        if ! command_exists "$cmd"; then
            echo "Error: $cmd is not installed. Please install $cmd." >&2
            exit 1
        fi
    done
}

# Format the file using Black
format_file() {
    black "$1"
}

# Lint the file using Flake8 and Interrogate
lint_file() {
    flake8 "$1"
    interrogate -t "$1"
}

# Sort imports using isort
sort_imports() {
    isort "$1"
}

# Main script logic
main() {
    check_commands

    if [ -z "$1" ]; then
        echo "Error: No filename provided. Please provide the Python file to format and lint." >&2
        exit 1
    fi

    local filename="$1"

    format_file "$filename"
    sort_imports "$filename"
    lint_file "$filename"

    echo "Finished formatting and linting: $filename"
}

main "$@"
