# Flag in Flame

**Link**: https://play.picoctf.org/practice/challenge/523

**Difficulty**: easy

## Description

The SOC team discovered a suspiciously large log file after a recent breach. When
they opened it, they found an enormous block of encoded text instead of typical
logs. Could there be something hidden within? The file is large, so examining it
thoroughly is crucial.

## Resources

- **logs.txt**: the "log" file (actually one giant Base64 blob)
- **img.png**: the decoded image (produced during the solve)
- **result.bin**: the final decoded flag bytes (produced during the solve)

## How to solve

This is a nested-encoding chain: **Base64 → PNG image → hex string → ASCII flag.**

1. **Recognise the Base64.** The whole file is one block starting with `iVBORw0KGgo…`
   — and `iVBORw0KGgo` is the Base64 of a PNG header (`\x89PNG`):

       head -c 80 logs.txt          # iVBORw0KGgoAAAANSUhEUgAAA4A...

2. **Decode and confirm the file type:**

       base64 -d logs.txt | head    # starts with the PNG magic bytes ‰PNG

3. **Save the PNG and open it:**

       base64 -d logs.txt > img.png

   The image shows a long **hex string**:

       7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F61633165333538347D

   (`70 69 63 6F` = `pico`, so we already know it decodes to the flag. If the string
   is only rendered as pixels, OCR it with `tesseract img.png out` or just read it.)

4. **Hex → ASCII:**

       echo "7069636F4354467B...347D" | xxd -r -p

## Flag

    picoCTF{forensics_analysis_is_amazing_ac1e3584}
