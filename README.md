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

$ CGO_ENABLED=1 GOOS=linux GOARCH=amd64 CC=aarch64-linux-gnu-gcc go build main.go

// aarch64-linux-gnu-gcc: error: unrecognized command-line option '-m64'

$ CGO_ENABLED=1 GOOS=linux GOARCH=amd64 CC=aarch64-linux-gnu-gcc go env
// GOGCCFLAGS='-fPIC -m64 -pthread -Wl,--no-gc-sections -fmessage-length=0 -ffile-prefix-map=/tmp/go-build1972709167=/tmp/go-build -gno-record-gcc-switches'

```
