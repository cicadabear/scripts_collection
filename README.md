# scripts_collection
scripts_collection

```
package main

// int c = 1;
import "C"
import "fmt"

func main() {
        fmt.Println(C.c)
}

$ CGO_ENABLED=1 GOOS=linux GOARCH=arm64 CC=aarch64-linux-gnu-gcc go build main.go

# Error: aarch64-linux-gnu-gcc: error: unrecognized command-line option '-m64' 

```
