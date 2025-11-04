# JPG challenges

## 1. Controll metadata

For controlling metadata use:

```bash
exiftool file.jpg
```

## 2. Extract files

For extracting hidden files use ```steghide```.

Use:
```bash
steghide info file.jpg
```

For getting information on possible file hidden.

Use:
```bash
steghide extract -sf file.jpg
```

For extracting the file.

[Optional] the flag ```-p``` can be used for using a password, if needed.

