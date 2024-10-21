---
layout: container
name:  "quay.io/biocontainers/gecode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gecode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gecode/container.yaml"
updated_at: "2024-10-21 03:25:36.004377"
latest: "6.2.0--h53e199c_4"
container_url: "https://biocontainers.pro/tools/gecode"
aliases:
 - "all-interval"
 - "alpha"
 - "bacp"
 - "bibd"
 - "bin-packing"
 - "black-hole"
 - "car-sequencing"
 - "cartesian-heart"
 - "colored-matrix"
 - "crew"
 - "crossword"
 - "crowded-chess"
 - "descartes-folium"
 - "dominating-queens"
 - "domino"
 - "donald"
 - "efpa"
 - "eq20"
 - "fzn-gecode"
 - "golf"
 - "golomb-ruler"
 - "graph-color"
 - "grocery"
 - "hamming"
 - "ind-set"
 - "job-shop"
 - "kakuro"
 - "knights"
 - "langford-number"
 - "magic-sequence"
 - "magic-square"
 - "minesweeper"
 - "money"
 - "multi-bin-packing"
 - "mzn-gecode"
 - "nonogram"
 - "open-shop"
 - "ortho-latin"
 - "partition"
 - "pentominoes"
 - "perfect-square"
 - "photo"
 - "qcp"
 - "queen-armies"
 - "queens"
 - "radiotherapy"
 - "sat"
 - "schurs-lemma"
 - "sports-league"
 - "steel-mill"
 - "steiner"
 - "sudoku"
 - "sudoku-advanced"
 - "tsp"
 - "warehouses"
 - "word-square"
versions:
 - "6.2.0--h3272c59_1"
 - "6.2.0--h8561491_2"
 - "6.2.0--h53e199c_4"
description: "shpc-registry automated BioContainers addition for gecode"
config: {"url": "https://biocontainers.pro/tools/gecode", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gecode", "latest": {"6.2.0--h53e199c_4": "sha256:568ab90648ba7c986c3bcc908d8258fe1500cf96c606a0d5773e258d2a83a90e"}, "tags": {"6.2.0--h3272c59_1": "sha256:1a6df1734b89669e4a73d66a3f5a3888bab83540abfdc268944ebfafb3e6d363", "6.2.0--h8561491_2": "sha256:70a939e5996a05b370b458bab27d97cc8056de40a1241b4bcee556dcb0bd54f8", "6.2.0--h53e199c_4": "sha256:568ab90648ba7c986c3bcc908d8258fe1500cf96c606a0d5773e258d2a83a90e"}, "docker": "quay.io/biocontainers/gecode", "aliases": {"all-interval": "/usr/local/bin/all-interval", "alpha": "/usr/local/bin/alpha", "bacp": "/usr/local/bin/bacp", "bibd": "/usr/local/bin/bibd", "bin-packing": "/usr/local/bin/bin-packing", "black-hole": "/usr/local/bin/black-hole", "car-sequencing": "/usr/local/bin/car-sequencing", "cartesian-heart": "/usr/local/bin/cartesian-heart", "colored-matrix": "/usr/local/bin/colored-matrix", "crew": "/usr/local/bin/crew", "crossword": "/usr/local/bin/crossword", "crowded-chess": "/usr/local/bin/crowded-chess", "descartes-folium": "/usr/local/bin/descartes-folium", "dominating-queens": "/usr/local/bin/dominating-queens", "domino": "/usr/local/bin/domino", "donald": "/usr/local/bin/donald", "efpa": "/usr/local/bin/efpa", "eq20": "/usr/local/bin/eq20", "fzn-gecode": "/usr/local/bin/fzn-gecode", "golf": "/usr/local/bin/golf", "golomb-ruler": "/usr/local/bin/golomb-ruler", "graph-color": "/usr/local/bin/graph-color", "grocery": "/usr/local/bin/grocery", "hamming": "/usr/local/bin/hamming", "ind-set": "/usr/local/bin/ind-set", "job-shop": "/usr/local/bin/job-shop", "kakuro": "/usr/local/bin/kakuro", "knights": "/usr/local/bin/knights", "langford-number": "/usr/local/bin/langford-number", "magic-sequence": "/usr/local/bin/magic-sequence", "magic-square": "/usr/local/bin/magic-square", "minesweeper": "/usr/local/bin/minesweeper", "money": "/usr/local/bin/money", "multi-bin-packing": "/usr/local/bin/multi-bin-packing", "mzn-gecode": "/usr/local/bin/mzn-gecode", "nonogram": "/usr/local/bin/nonogram", "open-shop": "/usr/local/bin/open-shop", "ortho-latin": "/usr/local/bin/ortho-latin", "partition": "/usr/local/bin/partition", "pentominoes": "/usr/local/bin/pentominoes", "perfect-square": "/usr/local/bin/perfect-square", "photo": "/usr/local/bin/photo", "qcp": "/usr/local/bin/qcp", "queen-armies": "/usr/local/bin/queen-armies", "queens": "/usr/local/bin/queens", "radiotherapy": "/usr/local/bin/radiotherapy", "sat": "/usr/local/bin/sat", "schurs-lemma": "/usr/local/bin/schurs-lemma", "sports-league": "/usr/local/bin/sports-league", "steel-mill": "/usr/local/bin/steel-mill", "steiner": "/usr/local/bin/steiner", "sudoku": "/usr/local/bin/sudoku", "sudoku-advanced": "/usr/local/bin/sudoku-advanced", "tsp": "/usr/local/bin/tsp", "warehouses": "/usr/local/bin/warehouses", "word-square": "/usr/local/bin/word-square"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gecode.
shpc-registry automated BioContainers addition for gecode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gecode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gecode:6.2.0--h53e199c_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gecode/6.2.0--h53e199c_4
$ module help quay.io/biocontainers/gecode/6.2.0--h53e199c_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gecode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gecode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gecode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gecode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gecode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gecode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### all-interval

```bash
$ singularity exec <container> /usr/local/bin/all-interval
$ podman run --it --rm --entrypoint /usr/local/bin/all-interval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/all-interval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alpha

```bash
$ singularity exec <container> /usr/local/bin/alpha
$ podman run --it --rm --entrypoint /usr/local/bin/alpha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alpha   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bacp

```bash
$ singularity exec <container> /usr/local/bin/bacp
$ podman run --it --rm --entrypoint /usr/local/bin/bacp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bacp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bibd

```bash
$ singularity exec <container> /usr/local/bin/bibd
$ podman run --it --rm --entrypoint /usr/local/bin/bibd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bibd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bin-packing

```bash
$ singularity exec <container> /usr/local/bin/bin-packing
$ podman run --it --rm --entrypoint /usr/local/bin/bin-packing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bin-packing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-hole

```bash
$ singularity exec <container> /usr/local/bin/black-hole
$ podman run --it --rm --entrypoint /usr/local/bin/black-hole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-hole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### car-sequencing

```bash
$ singularity exec <container> /usr/local/bin/car-sequencing
$ podman run --it --rm --entrypoint /usr/local/bin/car-sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/car-sequencing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cartesian-heart

```bash
$ singularity exec <container> /usr/local/bin/cartesian-heart
$ podman run --it --rm --entrypoint /usr/local/bin/cartesian-heart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cartesian-heart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colored-matrix

```bash
$ singularity exec <container> /usr/local/bin/colored-matrix
$ podman run --it --rm --entrypoint /usr/local/bin/colored-matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colored-matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crew

```bash
$ singularity exec <container> /usr/local/bin/crew
$ podman run --it --rm --entrypoint /usr/local/bin/crew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crew   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossword

```bash
$ singularity exec <container> /usr/local/bin/crossword
$ podman run --it --rm --entrypoint /usr/local/bin/crossword   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossword   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crowded-chess

```bash
$ singularity exec <container> /usr/local/bin/crowded-chess
$ podman run --it --rm --entrypoint /usr/local/bin/crowded-chess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crowded-chess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### descartes-folium

```bash
$ singularity exec <container> /usr/local/bin/descartes-folium
$ podman run --it --rm --entrypoint /usr/local/bin/descartes-folium   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/descartes-folium   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dominating-queens

```bash
$ singularity exec <container> /usr/local/bin/dominating-queens
$ podman run --it --rm --entrypoint /usr/local/bin/dominating-queens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dominating-queens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### domino

```bash
$ singularity exec <container> /usr/local/bin/domino
$ podman run --it --rm --entrypoint /usr/local/bin/domino   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/domino   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### donald

```bash
$ singularity exec <container> /usr/local/bin/donald
$ podman run --it --rm --entrypoint /usr/local/bin/donald   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/donald   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### efpa

```bash
$ singularity exec <container> /usr/local/bin/efpa
$ podman run --it --rm --entrypoint /usr/local/bin/efpa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/efpa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eq20

```bash
$ singularity exec <container> /usr/local/bin/eq20
$ podman run --it --rm --entrypoint /usr/local/bin/eq20   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eq20   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fzn-gecode

```bash
$ singularity exec <container> /usr/local/bin/fzn-gecode
$ podman run --it --rm --entrypoint /usr/local/bin/fzn-gecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fzn-gecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### golf

```bash
$ singularity exec <container> /usr/local/bin/golf
$ podman run --it --rm --entrypoint /usr/local/bin/golf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/golf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### golomb-ruler

```bash
$ singularity exec <container> /usr/local/bin/golomb-ruler
$ podman run --it --rm --entrypoint /usr/local/bin/golomb-ruler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/golomb-ruler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph-color

```bash
$ singularity exec <container> /usr/local/bin/graph-color
$ podman run --it --rm --entrypoint /usr/local/bin/graph-color   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph-color   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grocery

```bash
$ singularity exec <container> /usr/local/bin/grocery
$ podman run --it --rm --entrypoint /usr/local/bin/grocery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grocery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hamming

```bash
$ singularity exec <container> /usr/local/bin/hamming
$ podman run --it --rm --entrypoint /usr/local/bin/hamming   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hamming   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ind-set

```bash
$ singularity exec <container> /usr/local/bin/ind-set
$ podman run --it --rm --entrypoint /usr/local/bin/ind-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ind-set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### job-shop

```bash
$ singularity exec <container> /usr/local/bin/job-shop
$ podman run --it --rm --entrypoint /usr/local/bin/job-shop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/job-shop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kakuro

```bash
$ singularity exec <container> /usr/local/bin/kakuro
$ podman run --it --rm --entrypoint /usr/local/bin/kakuro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kakuro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knights

```bash
$ singularity exec <container> /usr/local/bin/knights
$ podman run --it --rm --entrypoint /usr/local/bin/knights   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knights   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### langford-number

```bash
$ singularity exec <container> /usr/local/bin/langford-number
$ podman run --it --rm --entrypoint /usr/local/bin/langford-number   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/langford-number   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magic-sequence

```bash
$ singularity exec <container> /usr/local/bin/magic-sequence
$ podman run --it --rm --entrypoint /usr/local/bin/magic-sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magic-sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magic-square

```bash
$ singularity exec <container> /usr/local/bin/magic-square
$ podman run --it --rm --entrypoint /usr/local/bin/magic-square   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magic-square   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minesweeper

```bash
$ singularity exec <container> /usr/local/bin/minesweeper
$ podman run --it --rm --entrypoint /usr/local/bin/minesweeper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minesweeper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### money

```bash
$ singularity exec <container> /usr/local/bin/money
$ podman run --it --rm --entrypoint /usr/local/bin/money   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/money   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi-bin-packing

```bash
$ singularity exec <container> /usr/local/bin/multi-bin-packing
$ podman run --it --rm --entrypoint /usr/local/bin/multi-bin-packing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi-bin-packing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzn-gecode

```bash
$ singularity exec <container> /usr/local/bin/mzn-gecode
$ podman run --it --rm --entrypoint /usr/local/bin/mzn-gecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzn-gecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nonogram

```bash
$ singularity exec <container> /usr/local/bin/nonogram
$ podman run --it --rm --entrypoint /usr/local/bin/nonogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nonogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### open-shop

```bash
$ singularity exec <container> /usr/local/bin/open-shop
$ podman run --it --rm --entrypoint /usr/local/bin/open-shop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/open-shop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ortho-latin

```bash
$ singularity exec <container> /usr/local/bin/ortho-latin
$ podman run --it --rm --entrypoint /usr/local/bin/ortho-latin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ortho-latin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### partition

```bash
$ singularity exec <container> /usr/local/bin/partition
$ podman run --it --rm --entrypoint /usr/local/bin/partition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/partition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pentominoes

```bash
$ singularity exec <container> /usr/local/bin/pentominoes
$ podman run --it --rm --entrypoint /usr/local/bin/pentominoes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pentominoes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perfect-square

```bash
$ singularity exec <container> /usr/local/bin/perfect-square
$ podman run --it --rm --entrypoint /usr/local/bin/perfect-square   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perfect-square   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### photo

```bash
$ singularity exec <container> /usr/local/bin/photo
$ podman run --it --rm --entrypoint /usr/local/bin/photo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/photo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcp

```bash
$ singularity exec <container> /usr/local/bin/qcp
$ podman run --it --rm --entrypoint /usr/local/bin/qcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queen-armies

```bash
$ singularity exec <container> /usr/local/bin/queen-armies
$ podman run --it --rm --entrypoint /usr/local/bin/queen-armies   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queen-armies   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### queens

```bash
$ singularity exec <container> /usr/local/bin/queens
$ podman run --it --rm --entrypoint /usr/local/bin/queens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/queens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### radiotherapy

```bash
$ singularity exec <container> /usr/local/bin/radiotherapy
$ podman run --it --rm --entrypoint /usr/local/bin/radiotherapy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radiotherapy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sat

```bash
$ singularity exec <container> /usr/local/bin/sat
$ podman run --it --rm --entrypoint /usr/local/bin/sat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schurs-lemma

```bash
$ singularity exec <container> /usr/local/bin/schurs-lemma
$ podman run --it --rm --entrypoint /usr/local/bin/schurs-lemma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schurs-lemma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sports-league

```bash
$ singularity exec <container> /usr/local/bin/sports-league
$ podman run --it --rm --entrypoint /usr/local/bin/sports-league   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sports-league   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### steel-mill

```bash
$ singularity exec <container> /usr/local/bin/steel-mill
$ podman run --it --rm --entrypoint /usr/local/bin/steel-mill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/steel-mill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### steiner

```bash
$ singularity exec <container> /usr/local/bin/steiner
$ podman run --it --rm --entrypoint /usr/local/bin/steiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/steiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sudoku

```bash
$ singularity exec <container> /usr/local/bin/sudoku
$ podman run --it --rm --entrypoint /usr/local/bin/sudoku   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sudoku   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sudoku-advanced

```bash
$ singularity exec <container> /usr/local/bin/sudoku-advanced
$ podman run --it --rm --entrypoint /usr/local/bin/sudoku-advanced   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sudoku-advanced   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsp

```bash
$ singularity exec <container> /usr/local/bin/tsp
$ podman run --it --rm --entrypoint /usr/local/bin/tsp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### warehouses

```bash
$ singularity exec <container> /usr/local/bin/warehouses
$ podman run --it --rm --entrypoint /usr/local/bin/warehouses   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/warehouses   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### word-square

```bash
$ singularity exec <container> /usr/local/bin/word-square
$ podman run --it --rm --entrypoint /usr/local/bin/word-square   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/word-square   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)