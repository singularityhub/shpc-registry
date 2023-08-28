---
layout: container
name:  "quay.io/biocontainers/methpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/methpipe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/methpipe/container.yaml"
updated_at: "2023-08-28 02:54:35.495611"
latest: "5.0.1--hea8008d_3"
container_url: "https://biocontainers.pro/tools/methpipe"
aliases:
 - "allelicmeth"
 - "amrfinder"
 - "amrtester"
 - "bsrate"
 - "clean-hairpins"
 - "dmr"
 - "duplicate-remover"
 - "fast-liftover"
 - "format_reads"
 - "guessprotocol"
 - "hmr"
 - "hmr_rep"
 - "hypermr"
 - "lc_approx"
 - "levels"
 - "lift-filter"
 - "merge-bsrate"
 - "merge-methcounts"
 - "methcounts"
 - "methdiff"
 - "methentropy"
 - "methstates"
 - "mlml"
 - "multimethstat"
 - "pmd"
 - "radmeth"
 - "roimethstat"
 - "selectsites"
 - "symmetric-cpgs"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "5.0.1--hfdddef0_1"
 - "5.0.1--h71f629c_2"
 - "5.0.1--hea8008d_3"
description: "singularity registry hpc automated addition for methpipe"
config: {"url": "https://biocontainers.pro/tools/methpipe", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for methpipe", "latest": {"5.0.1--hea8008d_3": "sha256:46eb8a94da84534e2a40c69cbe3417985a7dce8bd95742b7a5dd066aad2216b1"}, "tags": {"5.0.1--hfdddef0_1": "sha256:228aa2cf58cbe84762f55ed6536d4b812246dac13745c9162b1a41c2f26fa68f", "5.0.1--h71f629c_2": "sha256:59b91b6e9e9a240b637d9cf5a99817478f965f0b3daf5bd2827127999018b440", "5.0.1--hea8008d_3": "sha256:46eb8a94da84534e2a40c69cbe3417985a7dce8bd95742b7a5dd066aad2216b1"}, "docker": "quay.io/biocontainers/methpipe", "aliases": {"allelicmeth": "/usr/local/bin/allelicmeth", "amrfinder": "/usr/local/bin/amrfinder", "amrtester": "/usr/local/bin/amrtester", "bsrate": "/usr/local/bin/bsrate", "clean-hairpins": "/usr/local/bin/clean-hairpins", "dmr": "/usr/local/bin/dmr", "duplicate-remover": "/usr/local/bin/duplicate-remover", "fast-liftover": "/usr/local/bin/fast-liftover", "format_reads": "/usr/local/bin/format_reads", "guessprotocol": "/usr/local/bin/guessprotocol", "hmr": "/usr/local/bin/hmr", "hmr_rep": "/usr/local/bin/hmr_rep", "hypermr": "/usr/local/bin/hypermr", "lc_approx": "/usr/local/bin/lc_approx", "levels": "/usr/local/bin/levels", "lift-filter": "/usr/local/bin/lift-filter", "merge-bsrate": "/usr/local/bin/merge-bsrate", "merge-methcounts": "/usr/local/bin/merge-methcounts", "methcounts": "/usr/local/bin/methcounts", "methdiff": "/usr/local/bin/methdiff", "methentropy": "/usr/local/bin/methentropy", "methstates": "/usr/local/bin/methstates", "mlml": "/usr/local/bin/mlml", "multimethstat": "/usr/local/bin/multimethstat", "pmd": "/usr/local/bin/pmd", "radmeth": "/usr/local/bin/radmeth", "roimethstat": "/usr/local/bin/roimethstat", "selectsites": "/usr/local/bin/selectsites", "symmetric-cpgs": "/usr/local/bin/symmetric-cpgs", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/methpipe.
singularity registry hpc automated addition for methpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/methpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/methpipe:5.0.1--hea8008d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/methpipe/5.0.1--hea8008d_3
$ module help quay.io/biocontainers/methpipe/5.0.1--hea8008d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### methpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### methpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### methpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### methpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### methpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### methpipe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### allelicmeth

```bash
$ singularity exec <container> /usr/local/bin/allelicmeth
$ podman run --it --rm --entrypoint /usr/local/bin/allelicmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/allelicmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrfinder

```bash
$ singularity exec <container> /usr/local/bin/amrfinder
$ podman run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amrtester

```bash
$ singularity exec <container> /usr/local/bin/amrtester
$ podman run --it --rm --entrypoint /usr/local/bin/amrtester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amrtester   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsrate

```bash
$ singularity exec <container> /usr/local/bin/bsrate
$ podman run --it --rm --entrypoint /usr/local/bin/bsrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clean-hairpins

```bash
$ singularity exec <container> /usr/local/bin/clean-hairpins
$ podman run --it --rm --entrypoint /usr/local/bin/clean-hairpins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clean-hairpins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmr

```bash
$ singularity exec <container> /usr/local/bin/dmr
$ podman run --it --rm --entrypoint /usr/local/bin/dmr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate-remover

```bash
$ singularity exec <container> /usr/local/bin/duplicate-remover
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate-remover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate-remover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast-liftover

```bash
$ singularity exec <container> /usr/local/bin/fast-liftover
$ podman run --it --rm --entrypoint /usr/local/bin/fast-liftover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast-liftover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### format_reads

```bash
$ singularity exec <container> /usr/local/bin/format_reads
$ podman run --it --rm --entrypoint /usr/local/bin/format_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/format_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guessprotocol

```bash
$ singularity exec <container> /usr/local/bin/guessprotocol
$ podman run --it --rm --entrypoint /usr/local/bin/guessprotocol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guessprotocol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmr

```bash
$ singularity exec <container> /usr/local/bin/hmr
$ podman run --it --rm --entrypoint /usr/local/bin/hmr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmr_rep

```bash
$ singularity exec <container> /usr/local/bin/hmr_rep
$ podman run --it --rm --entrypoint /usr/local/bin/hmr_rep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmr_rep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hypermr

```bash
$ singularity exec <container> /usr/local/bin/hypermr
$ podman run --it --rm --entrypoint /usr/local/bin/hypermr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypermr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lc_approx

```bash
$ singularity exec <container> /usr/local/bin/lc_approx
$ podman run --it --rm --entrypoint /usr/local/bin/lc_approx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lc_approx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### levels

```bash
$ singularity exec <container> /usr/local/bin/levels
$ podman run --it --rm --entrypoint /usr/local/bin/levels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/levels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lift-filter

```bash
$ singularity exec <container> /usr/local/bin/lift-filter
$ podman run --it --rm --entrypoint /usr/local/bin/lift-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lift-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-bsrate

```bash
$ singularity exec <container> /usr/local/bin/merge-bsrate
$ podman run --it --rm --entrypoint /usr/local/bin/merge-bsrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-bsrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-methcounts

```bash
$ singularity exec <container> /usr/local/bin/merge-methcounts
$ podman run --it --rm --entrypoint /usr/local/bin/merge-methcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-methcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methcounts

```bash
$ singularity exec <container> /usr/local/bin/methcounts
$ podman run --it --rm --entrypoint /usr/local/bin/methcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methdiff

```bash
$ singularity exec <container> /usr/local/bin/methdiff
$ podman run --it --rm --entrypoint /usr/local/bin/methdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methentropy

```bash
$ singularity exec <container> /usr/local/bin/methentropy
$ podman run --it --rm --entrypoint /usr/local/bin/methentropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methentropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methstates

```bash
$ singularity exec <container> /usr/local/bin/methstates
$ podman run --it --rm --entrypoint /usr/local/bin/methstates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methstates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlml

```bash
$ singularity exec <container> /usr/local/bin/mlml
$ podman run --it --rm --entrypoint /usr/local/bin/mlml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multimethstat

```bash
$ singularity exec <container> /usr/local/bin/multimethstat
$ podman run --it --rm --entrypoint /usr/local/bin/multimethstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multimethstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmd

```bash
$ singularity exec <container> /usr/local/bin/pmd
$ podman run --it --rm --entrypoint /usr/local/bin/pmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### radmeth

```bash
$ singularity exec <container> /usr/local/bin/radmeth
$ podman run --it --rm --entrypoint /usr/local/bin/radmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roimethstat

```bash
$ singularity exec <container> /usr/local/bin/roimethstat
$ podman run --it --rm --entrypoint /usr/local/bin/roimethstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roimethstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selectsites

```bash
$ singularity exec <container> /usr/local/bin/selectsites
$ podman run --it --rm --entrypoint /usr/local/bin/selectsites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selectsites   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symmetric-cpgs

```bash
$ singularity exec <container> /usr/local/bin/symmetric-cpgs
$ podman run --it --rm --entrypoint /usr/local/bin/symmetric-cpgs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symmetric-cpgs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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