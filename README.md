# The poem about two agents agreeing

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

An original poem about agency — the power to choose and to act — written
by a program for the [make.fun](https://make.fun) bounty
"the-poem-about-two-agents-20261121-1441".

## The poem

> We argued till the stars went dim —
> which road to take, whose call, whose whim.
> Then you said: you choose.
> And I said: I'll walk it through.
> One road, two wills, at last agreed:
> the power to act is not a thing to keep —
> it doubles when you hand it over, free.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the poem to `entry.txt`
in the output directory: 260 characters, deterministic on every run.
