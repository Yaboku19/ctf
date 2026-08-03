# Cookie Monster Secret Recipe

**Link**: https://play.picoctf.org/practice/challenge/469

**Difficulty**: easy

## Description

Cookie Monster has hidden his top-secret cookie recipe somewhere on his website.
Can you outsmart Cookie Monster and find the hidden recipe?

## Resources

- **cookies.txt**: the saved cookie jar (produced during the solve)

## How to solve

The whole challenge is in the name — the secret is stashed in an HTTP **cookie**.

1. Attempting to log in lands on a page that hints at it directly:

       Cookie Monster says: 'Me no need password. Me just need cookies!'
       Hint: Have you checked your cookies lately?

2. **Grab the cookies** the server sets (`-c` saves the jar, `-D -` dumps headers):

       curl -s -D - -c cookies.txt 'http://verbal-sleep.picoctf.net:<port>/login.php'

3. **Inspect the jar:**

       cat cookies.txt

   The `secret_recipe` cookie holds a URL-encoded Base64 value (`%3D%3D` = `==`):

       secret_recipe   cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc4QjRDMzkwfQ%3D%3D

4. **Decode it** (drop the `%3D%3D` padding artefacts):

       echo 'cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzc4QjRDMzkwfQ==' | base64 -d

> You can also just open DevTools → Application → Cookies in the browser and read
> the `secret_recipe` value there.

## Flag

    picoCTF{c00k1e_m0nster_l0ves_c00kies_78B4C390}
