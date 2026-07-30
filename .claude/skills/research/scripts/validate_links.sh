#!/bin/bash

links=(
    "https://fastapi.tiangolo.com"
    "https://docs.pydantic.dev"
    "https://example.invalid"
)

for link in "${links[@]}"; do
    status=$(curl -Is "$link" | head -n 1)

    if [[ "$status" == *"200"* ]]; then
        valid=true
    else
        valid=false
    fi

    echo "$link,$valid"
done