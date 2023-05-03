---
layout: container
name:  "quay.io/biocontainers/strainge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainge/container.yaml"
updated_at: "2023-05-03 03:06:06.329052"
latest: "1.3.7--py39h6359176_0"
container_url: "https://biocontainers.pro/tools/strainge"
aliases:
 - "kmercoverage"
 - "kmerseq"
 - "kmersimilarity"
 - "kmerspectrum"
 - "kmertree"
 - "pankmer"
 - "pybind11-config"
 - "refseq-download"
 - "refseq-extract"
 - "strainge"
 - "straingr"
 - "straingst"
 - "treepath"
 - "doesitcache"
 - "ipython3"
 - "ipython"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "py.test"
 - "pytest"
 - "natsort"
 - "mirror_server"
versions:
 - "1.3.3--py39hcaef8bb_0"
 - "1.3.7--py39h6359176_0"
description: "shpc-registry automated BioContainers addition for strainge"
config: {"url": "https://biocontainers.pro/tools/strainge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strainge", "latest": {"1.3.7--py39h6359176_0": "sha256:a391c7e561166b9c0099fbd5ca7df8ce8529f6b83382e8a5edf04609ef685892"}, "tags": {"1.3.3--py39hcaef8bb_0": "sha256:5c01b0f52ad77ae4121ce991c07a5fe2c1119addba67fa23f9afb714ce5c3b1d", "1.3.7--py39h6359176_0": "sha256:a391c7e561166b9c0099fbd5ca7df8ce8529f6b83382e8a5edf04609ef685892"}, "docker": "quay.io/biocontainers/strainge", "aliases": {"kmercoverage": "/usr/local/bin/kmercoverage", "kmerseq": "/usr/local/bin/kmerseq", "kmersimilarity": "/usr/local/bin/kmersimilarity", "kmerspectrum": "/usr/local/bin/kmerspectrum", "kmertree": "/usr/local/bin/kmertree", "pankmer": "/usr/local/bin/pankmer", "pybind11-config": "/usr/local/bin/pybind11-config", "refseq-download": "/usr/local/bin/refseq-download", "refseq-extract": "/usr/local/bin/refseq-extract", "strainge": "/usr/local/bin/strainge", "straingr": "/usr/local/bin/straingr", "straingst": "/usr/local/bin/straingst", "treepath": "/usr/local/bin/treepath", "doesitcache": "/usr/local/bin/doesitcache", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainge.
shpc-registry automated BioContainers addition for strainge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainge:1.3.7--py39h6359176_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainge/1.3.7--py39h6359176_0
$ module help quay.io/biocontainers/strainge/1.3.7--py39h6359176_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmercoverage

```bash
$ singularity exec <container> /usr/local/bin/kmercoverage
$ podman run --it --rm --entrypoint /usr/local/bin/kmercoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmercoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerseq

```bash
$ singularity exec <container> /usr/local/bin/kmerseq
$ podman run --it --rm --entrypoint /usr/local/bin/kmerseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmersimilarity

```bash
$ singularity exec <container> /usr/local/bin/kmersimilarity
$ podman run --it --rm --entrypoint /usr/local/bin/kmersimilarity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmersimilarity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerspectrum

```bash
$ singularity exec <container> /usr/local/bin/kmerspectrum
$ podman run --it --rm --entrypoint /usr/local/bin/kmerspectrum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerspectrum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmertree

```bash
$ singularity exec <container> /usr/local/bin/kmertree
$ podman run --it --rm --entrypoint /usr/local/bin/kmertree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmertree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pankmer

```bash
$ singularity exec <container> /usr/local/bin/pankmer
$ podman run --it --rm --entrypoint /usr/local/bin/pankmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pankmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refseq-download

```bash
$ singularity exec <container> /usr/local/bin/refseq-download
$ podman run --it --rm --entrypoint /usr/local/bin/refseq-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refseq-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refseq-extract

```bash
$ singularity exec <container> /usr/local/bin/refseq-extract
$ podman run --it --rm --entrypoint /usr/local/bin/refseq-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refseq-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strainge

```bash
$ singularity exec <container> /usr/local/bin/strainge
$ podman run --it --rm --entrypoint /usr/local/bin/strainge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strainge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### straingr

```bash
$ singularity exec <container> /usr/local/bin/straingr
$ podman run --it --rm --entrypoint /usr/local/bin/straingr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/straingr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### straingst

```bash
$ singularity exec <container> /usr/local/bin/straingst
$ podman run --it --rm --entrypoint /usr/local/bin/straingst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/straingst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treepath

```bash
$ singularity exec <container> /usr/local/bin/treepath
$ podman run --it --rm --entrypoint /usr/local/bin/treepath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treepath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
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