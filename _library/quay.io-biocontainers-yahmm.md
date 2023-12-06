---
layout: container
name:  "quay.io/biocontainers/yahmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yahmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yahmm/container.yaml"
updated_at: "2023-12-06 02:42:18.928234"
latest: "1.1.3--py38he5da3d1_9"
container_url: "https://biocontainers.pro/tools/yahmm"
aliases:
 - "cygdb"
 - "cython"
 - "cythonize"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.7"
 - "img2webp"
versions:
 - "1.1.3--py37h8902056_7"
 - "1.1.3--py38he5da3d1_9"
description: "shpc-registry automated BioContainers addition for yahmm"
config: {"url": "https://biocontainers.pro/tools/yahmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yahmm", "latest": {"1.1.3--py38he5da3d1_9": "sha256:c1e75fece5149888390c6f53bca7d1cb056267158e7e6a13b18156cd3feb25ab"}, "tags": {"1.1.3--py37h8902056_7": "sha256:65093eae11815f19fd33d8d1362c957d08d1b2a2ed18f2ef391d1d134101466b", "1.1.3--py38he5da3d1_9": "sha256:c1e75fece5149888390c6f53bca7d1cb056267158e7e6a13b18156cd3feb25ab"}, "docker": "quay.io/biocontainers/yahmm", "aliases": {"cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.7": "/usr/local/bin/f2py3.7", "img2webp": "/usr/local/bin/img2webp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yahmm.
shpc-registry automated BioContainers addition for yahmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yahmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yahmm:1.1.3--py38he5da3d1_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yahmm/1.1.3--py38he5da3d1_9
$ module help quay.io/biocontainers/yahmm/1.1.3--py38he5da3d1_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yahmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yahmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yahmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yahmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yahmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yahmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
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