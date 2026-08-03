# Time Machine

**Link**: https://play.picoctf.org/practice/challenge/425

**Difficulty**: easy

## Description

What was I last working on? I remember writing a note to help me remember...

## Resources

- **challenge.zip**: a git repository

## How to solve

1. Unzip the repo:

       unzip challenge.zip
       cd <extracted-folder>

2. The "note to help me remember" lives in the commit history, so just read the
   log:

       git log

   The flag is in a commit message:

       picoCTF{t1m3m@ch1n3_8defe16a}

> Handy follow-ups if a git challenge hides things deeper: `git log --all --oneline`,
> `git reflog`, `git stash list`, `git show <hash>`, and `git log -p` to see full
> diffs.

## Flag

    picoCTF{t1m3m@ch1n3_8defe16a}
