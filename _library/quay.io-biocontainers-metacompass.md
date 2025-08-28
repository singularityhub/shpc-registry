---
layout: container
name:  "quay.io/biocontainers/metacompass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metacompass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metacompass/container.yaml"
updated_at: "2025-08-28 03:23:59.280502"
latest: "1.12--h9948957_0"
container_url: "https://biocontainers.pro/tools/metacompass"
aliases:
 - "go_metacompass.py"
 - "kmer-mask"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "megahit"
 - "megahit_toolkit"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
 - "systematic-mutations"
 - "archive-ncbinlp"
 - "archive-nihocc"
 - "archive-nmcds"
 - "archive-pmc"
 - "archive-taxonomy"
versions:
 - "1.12--h9948957_0"
description: "singularity registry hpc automated addition for metacompass"
config: {"url": "https://biocontainers.pro/tools/metacompass", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metacompass", "latest": {"1.12--h9948957_0": "sha256:42054ac7f3fc2df10895e8504319e97a37fb88a8b81301e5a9c16280588c9e67"}, "tags": {"1.12--h9948957_0": "sha256:42054ac7f3fc2df10895e8504319e97a37fb88a8b81301e5a9c16280588c9e67"}, "docker": "quay.io/biocontainers/metacompass", "aliases": {"go_metacompass.py": "/usr/local/bin/go_metacompass.py", "kmer-mask": "/usr/local/bin/kmer-mask", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits", "systematic-mutations": "/usr/local/bin/systematic-mutations", "archive-ncbinlp": "/usr/local/bin/archive-ncbinlp", "archive-nihocc": "/usr/local/bin/archive-nihocc", "archive-nmcds": "/usr/local/bin/archive-nmcds", "archive-pmc": "/usr/local/bin/archive-pmc", "archive-taxonomy": "/usr/local/bin/archive-taxonomy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metacompass.
singularity registry hpc automated addition for metacompass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metacompass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metacompass:1.12--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metacompass/1.12--h9948957_0
$ module help quay.io/biocontainers/metacompass/1.12--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metacompass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metacompass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metacompass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metacompass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metacompass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metacompass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### go_metacompass.py

```bash
$ singularity exec <container> /usr/local/bin/go_metacompass.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_metacompass.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_metacompass.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer-mask

```bash
$ singularity exec <container> /usr/local/bin/kmer-mask
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsmp2info

```bash
$ singularity exec <container> /usr/local/bin/bsmp2info
$ podman run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsa2xml

```bash
$ singularity exec <container> /usr/local/bin/fsa2xml
$ podman run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2info

```bash
$ singularity exec <container> /usr/local/bin/gbf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just-top-hits

```bash
$ singularity exec <container> /usr/local/bin/just-top-hits
$ podman run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### systematic-mutations

```bash
$ singularity exec <container> /usr/local/bin/systematic-mutations
$ podman run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/systematic-mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-ncbinlp

```bash
$ singularity exec <container> /usr/local/bin/archive-ncbinlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-ncbinlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nihocc

```bash
$ singularity exec <container> /usr/local/bin/archive-nihocc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nihocc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nmcds

```bash
$ singularity exec <container> /usr/local/bin/archive-nmcds
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nmcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pmc

```bash
$ singularity exec <container> /usr/local/bin/archive-pmc
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-taxonomy

```bash
$ singularity exec <container> /usr/local/bin/archive-taxonomy
$ podman run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-taxonomy   -v ${PWD} -w ${PWD} <container> -c " $@"
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