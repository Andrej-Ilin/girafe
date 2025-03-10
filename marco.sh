marco() {
    export MARCO=$(pwd)
}

polo() {
    cd "$MARCO" || echo "MARCO is not set"
}
