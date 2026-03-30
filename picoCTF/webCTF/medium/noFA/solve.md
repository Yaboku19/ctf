# No FA

**Link**: https://play.picoctf.org/practice/challenge/765

**Difficulty**: medium

## Description

Seems like some data has been leaked! Can you get the flag?

## Resources

**app.py**: Backend of the site

**users.db**: a data leak with informations of users

## How to solve

By looking at the data leak we will fin an interesting entry

    5 admin ...

And by looking at the code only the user with username admin will get the flag

It is also stored is password but it is hashed. But since is not salted can be easly broken by some tool online like [crackstation](https://crackstation.net)

By using it we find that the password of admin is

    apple@123

But the site as a double factor autantication only for admin. Once we do the login, by looking at the code, we see that the OTP is saved in the session and since flask save everything as a cookie on the client side it can be retrieved. By looking to the cookie and in particular the session entry we will see a long string like

    .eJwty0sKgCAQANC7zFoCP-joZUJqEsEfaqvo7rlo--A9kGoIdIKDy6dBwKDOtg86Os2FaLn6bcZMY_rcwHFjFFothN6kREQhGNyDevGZVvJnjgXeD0hWHG8.acrEYg.SLRxaSyracFyX3pmeEQDvlieb_s

It looks like base64 and indeed it is, where every entry of the session is separated by a point, so by splitting it and fixing it with a `=` at the end of every string it can be easly transled for getting something like

    {"logged":"false","otp_secret":"8914","otp_timestamp":1774896226.3388822,"username":"admin"}

Here we can retrieve the otp and finish the login for getting the flag

    picoCTF{n0_r4t3_n0_4uth_2b765193}

