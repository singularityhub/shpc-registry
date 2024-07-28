---
layout: container
name:  "quay.io/biocontainers/physlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/physlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/physlr/container.yaml"
updated_at: "2024-07-28 03:21:39.307742"
latest: "1.0.4--py39h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/physlr"
aliases:
 - "ntcard"
 - "nthits"
 - "nthll"
 - "physlr"
 - "pypy"
 - "pypy3"
 - "pypy3.7"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "pigz"
 - "unpigz"
 - "tqdm"
 - "f2py3.7"
 - "python3.7"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.4--py39h2df963e_2"
 - "1.0.4--py39h2df963e_3"
 - "1.0.4--py39h376f1d3_5"
 - "1.0.4--py39h4ac6f70_6"
description: "singularity registry hpc automated addition for physlr"
config: {"url": "https://biocontainers.pro/tools/physlr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for physlr", "latest": {"1.0.4--py39h4ac6f70_6": "sha256:bd5fb1e58a1952de847ad464a8238f7290f6a9c84fe60e3781f002bfcb64830b"}, "tags": {"1.0.4--py39h2df963e_2": "sha256:9d04b07d3ba6f3148cfa9cdeb537fbe6be927ca7126d7483f04f968055df4787", "1.0.4--py39h2df963e_3": "sha256:0354b252da85bffe9d99e170523edaf7186cfd5d7cc4a3ac2af44ab49ac8ce3e", "1.0.4--py39h376f1d3_5": "sha256:2a54f45db8e7c05cad4ca7256d5675aba7496fff045ff408b9d3a184f6d70b06", "1.0.4--py39h4ac6f70_6": "sha256:bd5fb1e58a1952de847ad464a8238f7290f6a9c84fe60e3781f002bfcb64830b"}, "docker": "quay.io/biocontainers/physlr", "aliases": {"ntcard": "/usr/local/bin/ntcard", "nthits": "/usr/local/bin/nthits", "nthll": "/usr/local/bin/nthll", "physlr": "/usr/local/bin/physlr", "pypy": "/usr/local/bin/pypy", "pypy3": "/usr/local/bin/pypy3", "pypy3.7": "/usr/local/bin/pypy3.7", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "tqdm": "/usr/local/bin/tqdm", "f2py3.7": "/usr/local/bin/f2py3.7", "python3.7": "/usr/local/bin/python3.7", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/physlr.
singularity registry hpc automated addition for physlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/physlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/physlr:1.0.4--py39h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/physlr/1.0.4--py39h4ac6f70_6
$ module help quay.io/biocontainers/physlr/1.0.4--py39h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### physlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### physlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### physlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### physlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### physlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### physlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ntcard

```bash
$ singularity exec <container> /usr/local/bin/ntcard
$ podman run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthits

```bash
$ singularity exec <container> /usr/local/bin/nthits
$ podman run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthll

```bash
$ singularity exec <container> /usr/local/bin/nthll
$ podman run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### physlr

```bash
$ singularity exec <container> /usr/local/bin/physlr
$ podman run --it --rm --entrypoint /usr/local/bin/physlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/physlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy

```bash
$ singularity exec <container> /usr/local/bin/pypy
$ podman run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3

```bash
$ singularity exec <container> /usr/local/bin/pypy3
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3.7

```bash
$ singularity exec <container> /usr/local/bin/pypy3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_dump

```bash
$ singularity exec <container> /usr/local/bin/gdbm_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_load

```bash
$ singularity exec <container> /usr/local/bin/gdbm_load
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbmtool

```bash
$ singularity exec <container> /usr/local/bin/gdbmtool
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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