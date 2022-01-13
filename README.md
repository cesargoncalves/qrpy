# qrpy

## Download the source

```bash
git clone https://github.com/cesargoncalves/qrpy.git 
```

## Setup dependencies

```bash
./run.sh --setup_dependencies
```

## Encode data

```bash
./run.sh --write
```

write data to encoded qr code and save it in output.png

## Decode data

must install **libzbar0** package

alternatively, for a solution with no dependecies, use opencv branch (less performance, may not read some qr codes)

```bash
./run.sh --read
```

decode data from qrcode on input.png
