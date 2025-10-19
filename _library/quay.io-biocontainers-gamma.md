---
layout: container
name:  "quay.io/biocontainers/gamma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gamma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gamma/container.yaml"
updated_at: "2025-10-19 04:09:50.778493"
latest: "2.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/gamma"
aliases:
 - "GAMMA-S.py"
 - "GAMMA.py"
 - "faToNib"
 - "gfClient"
 - "gfServer"
 - "nibFrag"
 - "pslPretty"
 - "pslReps"
 - "pslSort"
 - "twoBitToFa"
 - "blat"
 - "unidecode"
 - "twoBitInfo"
 - "faToTwoBit"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
versions:
 - "2.2--hdfd78af_0"
 - "2.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for gamma"
config: {"url": "https://biocontainers.pro/tools/gamma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gamma", "latest": {"2.2--hdfd78af_1": "sha256:bdf16555ef6bea21fa842f45e913634f87de3a25f63288d42d37cfe2dde82b19"}, "tags": {"2.2--hdfd78af_0": "sha256:364dc74594536573c033373fe2fd099d0e6fb0cc5713bc89637f5b4584aad249", "2.2--hdfd78af_1": "sha256:bdf16555ef6bea21fa842f45e913634f87de3a25f63288d42d37cfe2dde82b19"}, "docker": "quay.io/biocontainers/gamma", "aliases": {"GAMMA-S.py": "/usr/local/bin/GAMMA-S.py", "GAMMA.py": "/usr/local/bin/GAMMA.py", "faToNib": "/usr/local/bin/faToNib", "gfClient": "/usr/local/bin/gfClient", "gfServer": "/usr/local/bin/gfServer", "nibFrag": "/usr/local/bin/nibFrag", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "pslSort": "/usr/local/bin/pslSort", "twoBitToFa": "/usr/local/bin/twoBitToFa", "blat": "/usr/local/bin/blat", "unidecode": "/usr/local/bin/unidecode", "twoBitInfo": "/usr/local/bin/twoBitInfo", "faToTwoBit": "/usr/local/bin/faToTwoBit", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gamma.
shpc-registry automated BioContainers addition for gamma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gamma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gamma:2.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gamma/2.2--hdfd78af_1
$ module help quay.io/biocontainers/gamma/2.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gamma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gamma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gamma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gamma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gamma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gamma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GAMMA-S.py

```bash
$ singularity exec <container> /usr/local/bin/GAMMA-S.py
$ podman run --it --rm --entrypoint /usr/local/bin/GAMMA-S.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GAMMA-S.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GAMMA.py

```bash
$ singularity exec <container> /usr/local/bin/GAMMA.py
$ podman run --it --rm --entrypoint /usr/local/bin/GAMMA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GAMMA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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