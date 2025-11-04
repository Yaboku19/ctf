# Flag in Flame

**Difficulty**: easy

## Description

The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

# Resources

**logs.txt**: a log file

## How to solve

By running

```bash
cat logs.txt
```

The output will be

```bash
iVBORw0KGgoAAAANSUhEUgAAA4AAAASACAIAAAAh8bSOAAEAAElEQ....
```

It looks like it is in base64 format.

By running

```bash
cat logs.txt | base64 -d | head
```

The output will be

```bash
�PNG
␦
...
```

It shows that indeed the file was in base64 and that the file decripted is a png file.

By running

```bash
cat logs.txt | base64 -d > img.png
```

The file will be converted in a png file.

By looking at the image it is easy to see a string

```
7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F61633165333538347D
```

It looks exadecimal. 

So by saving the string in a file called ```tmp.txt``` and running

```bash
xxd -r -p tmp.txt > result.bin
strings result.bin
cat result.bin
```

The output will be

```bash
picoCTF{forensics_analysis_is_amazing_ac1e3584}
```