---
layout: container
name:  "quay.io/biocontainers/bamsurgeon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamsurgeon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamsurgeon/container.yaml"
updated_at: "2025-05-05 03:24:54.525602"
latest: "1.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bamsurgeon"
aliases:
 - "addindel.py"
 - "addsnv.py"
 - "addsv.py"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "esd2esi"
 - "exonerate"
 - "exonerate-server"
 - "fasta2esd"
 - "fastaannotatecdna"
 - "fastachecksum"
 - "fastaclip"
 - "fastacomposition"
 - "fastadiff"
 - "fastaexplode"
 - "fastafetch"
 - "fastahardmask"
 - "fastaindex"
 - "fastalength"
 - "fastanrdb"
 - "fastaoverlap"
 - "fastareformat"
 - "fastaremove"
 - "fastarevcomp"
 - "fastasoftmask"
 - "fastasort"
 - "fastasubseq"
 - "fastatranslate"
 - "fastavalidcds"
 - "ipcress"
versions:
 - "1.4.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bamsurgeon"
config: {"url": "https://biocontainers.pro/tools/bamsurgeon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bamsurgeon", "latest": {"1.4.1--pyhdfd78af_0": "sha256:b7b9d222ba998d44b4c726f7196ecfdc92a49e21d5a3e8729b2904aaf88c8b77"}, "tags": {"1.4.1--pyhdfd78af_0": "sha256:b7b9d222ba998d44b4c726f7196ecfdc92a49e21d5a3e8729b2904aaf88c8b77"}, "docker": "quay.io/biocontainers/bamsurgeon", "aliases": {"addindel.py": "/usr/local/bin/addindel.py", "addsnv.py": "/usr/local/bin/addsnv.py", "addsv.py": "/usr/local/bin/addsv.py", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "esd2esi": "/usr/local/bin/esd2esi", "exonerate": "/usr/local/bin/exonerate", "exonerate-server": "/usr/local/bin/exonerate-server", "fasta2esd": "/usr/local/bin/fasta2esd", "fastaannotatecdna": "/usr/local/bin/fastaannotatecdna", "fastachecksum": "/usr/local/bin/fastachecksum", "fastaclip": "/usr/local/bin/fastaclip", "fastacomposition": "/usr/local/bin/fastacomposition", "fastadiff": "/usr/local/bin/fastadiff", "fastaexplode": "/usr/local/bin/fastaexplode", "fastafetch": "/usr/local/bin/fastafetch", "fastahardmask": "/usr/local/bin/fastahardmask", "fastaindex": "/usr/local/bin/fastaindex", "fastalength": "/usr/local/bin/fastalength", "fastanrdb": "/usr/local/bin/fastanrdb", "fastaoverlap": "/usr/local/bin/fastaoverlap", "fastareformat": "/usr/local/bin/fastareformat", "fastaremove": "/usr/local/bin/fastaremove", "fastarevcomp": "/usr/local/bin/fastarevcomp", "fastasoftmask": "/usr/local/bin/fastasoftmask", "fastasort": "/usr/local/bin/fastasort", "fastasubseq": "/usr/local/bin/fastasubseq", "fastatranslate": "/usr/local/bin/fastatranslate", "fastavalidcds": "/usr/local/bin/fastavalidcds", "ipcress": "/usr/local/bin/ipcress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamsurgeon.
singularity registry hpc automated addition for bamsurgeon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamsurgeon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamsurgeon:1.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamsurgeon/1.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/bamsurgeon/1.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamsurgeon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamsurgeon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamsurgeon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamsurgeon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamsurgeon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamsurgeon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addindel.py

```bash
$ singularity exec <container> /usr/local/bin/addindel.py
$ podman run --it --rm --entrypoint /usr/local/bin/addindel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addindel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addsnv.py

```bash
$ singularity exec <container> /usr/local/bin/addsnv.py
$ podman run --it --rm --entrypoint /usr/local/bin/addsnv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addsnv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addsv.py

```bash
$ singularity exec <container> /usr/local/bin/addsv.py
$ podman run --it --rm --entrypoint /usr/local/bin/addsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addsv.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esd2esi

```bash
$ singularity exec <container> /usr/local/bin/esd2esi
$ podman run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate

```bash
$ singularity exec <container> /usr/local/bin/exonerate
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate-server

```bash
$ singularity exec <container> /usr/local/bin/exonerate-server
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2esd

```bash
$ singularity exec <container> /usr/local/bin/fasta2esd
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaannotatecdna

```bash
$ singularity exec <container> /usr/local/bin/fastaannotatecdna
$ podman run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastachecksum

```bash
$ singularity exec <container> /usr/local/bin/fastachecksum
$ podman run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclip

```bash
$ singularity exec <container> /usr/local/bin/fastaclip
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacomposition

```bash
$ singularity exec <container> /usr/local/bin/fastacomposition
$ podman run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadiff

```bash
$ singularity exec <container> /usr/local/bin/fastadiff
$ podman run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaexplode

```bash
$ singularity exec <container> /usr/local/bin/fastaexplode
$ podman run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastafetch

```bash
$ singularity exec <container> /usr/local/bin/fastafetch
$ podman run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastahardmask

```bash
$ singularity exec <container> /usr/local/bin/fastahardmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaindex

```bash
$ singularity exec <container> /usr/local/bin/fastaindex
$ podman run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastalength

```bash
$ singularity exec <container> /usr/local/bin/fastalength
$ podman run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastanrdb

```bash
$ singularity exec <container> /usr/local/bin/fastanrdb
$ podman run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaoverlap

```bash
$ singularity exec <container> /usr/local/bin/fastaoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastareformat

```bash
$ singularity exec <container> /usr/local/bin/fastareformat
$ podman run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaremove

```bash
$ singularity exec <container> /usr/local/bin/fastaremove
$ podman run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastarevcomp

```bash
$ singularity exec <container> /usr/local/bin/fastarevcomp
$ podman run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasoftmask

```bash
$ singularity exec <container> /usr/local/bin/fastasoftmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasort

```bash
$ singularity exec <container> /usr/local/bin/fastasort
$ podman run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasubseq

```bash
$ singularity exec <container> /usr/local/bin/fastasubseq
$ podman run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastatranslate

```bash
$ singularity exec <container> /usr/local/bin/fastatranslate
$ podman run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastavalidcds

```bash
$ singularity exec <container> /usr/local/bin/fastavalidcds
$ podman run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcress

```bash
$ singularity exec <container> /usr/local/bin/ipcress
$ podman run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
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