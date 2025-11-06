# Flag in Flame

**Difficulty**: easy

## Description

The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

# Resources

**logs.txt**: a log file

## How to solve

By running:

    cat logs.txt

The output will be:

    iVBORw0KGgoAAAANSUhEUgAAA4AAAASACAIAAAAh8bSOAAEAAElEQ....

It looks like Base64. Decode and check the file type:

    cat logs.txt | base64 -d | head

The output will start with PNG magic bytes:

    �PNG
    ␦
    ...

Save the decoded data as a PNG:

    cat logs.txt | base64 -d > img.png

Open `img.png` (or inspect it) and you’ll see a long hexadecimal string:

    7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F61633165333538347D

Save that hex into `tmp.txt` and convert it to binary, then show readable text:

    echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F61633165333538347D" > tmp.txt
    xxd -r -p tmp.txt > result.bin
    strings result.bin
    cat result.bin

The final output (the flag) will be:

    picoCTF{forensics_analysis_is_amazing_ac1e3584}
