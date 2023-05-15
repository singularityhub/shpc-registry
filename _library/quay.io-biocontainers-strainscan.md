---
layout: container
name:  "quay.io/biocontainers/strainscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainscan/container.yaml"
updated_at: "2023-05-15 03:38:25.954133"
latest: "1.0.10--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/strainscan"
aliases:
 - "graphdump"
 - "maf2synteny"
 - "sibeliaz"
 - "sibeliaz-lcb"
 - "spoa"
 - "strainscan"
 - "strainscan_build"
 - "twopaco"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "pyvenv"
versions:
 - "1.0.3--pyhdfd78af_0"
 - "1.0.10--pyhdfd78af_0"
description: "singularity registry hpc automated addition for strainscan"
config: {"url": "https://biocontainers.pro/tools/strainscan", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strainscan", "latest": {"1.0.10--pyhdfd78af_0": "sha256:714db542572a4cb414577cc2018248a6870115a6ff1a7e8c028f84f9941b517e"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:b1a52f463ffd1dfd1b04fdc09db9c3b3b9b046a6b2e8ec323c74881766c91809", "1.0.10--pyhdfd78af_0": "sha256:714db542572a4cb414577cc2018248a6870115a6ff1a7e8c028f84f9941b517e"}, "docker": "quay.io/biocontainers/strainscan", "aliases": {"graphdump": "/usr/local/bin/graphdump", "maf2synteny": "/usr/local/bin/maf2synteny", "sibeliaz": "/usr/local/bin/sibeliaz", "sibeliaz-lcb": "/usr/local/bin/sibeliaz-lcb", "spoa": "/usr/local/bin/spoa", "strainscan": "/usr/local/bin/strainscan", "strainscan_build": "/usr/local/bin/strainscan_build", "twopaco": "/usr/local/bin/twopaco", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainscan.
singularity registry hpc automated addition for strainscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainscan:1.0.10--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainscan/1.0.10--pyhdfd78af_0
$ module help quay.io/biocontainers/strainscan/1.0.10--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphdump

```bash
$ singularity exec <container> /usr/local/bin/graphdump
$ podman run --it --rm --entrypoint /usr/local/bin/graphdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf2synteny

```bash
$ singularity exec <container> /usr/local/bin/maf2synteny
$ podman run --it --rm --entrypoint /usr/local/bin/maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sibeliaz

```bash
$ singularity exec <container> /usr/local/bin/sibeliaz
$ podman run --it --rm --entrypoint /usr/local/bin/sibeliaz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sibeliaz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sibeliaz-lcb

```bash
$ singularity exec <container> /usr/local/bin/sibeliaz-lcb
$ podman run --it --rm --entrypoint /usr/local/bin/sibeliaz-lcb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sibeliaz-lcb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spoa

```bash
$ singularity exec <container> /usr/local/bin/spoa
$ podman run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strainscan

```bash
$ singularity exec <container> /usr/local/bin/strainscan
$ podman run --it --rm --entrypoint /usr/local/bin/strainscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strainscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strainscan_build

```bash
$ singularity exec <container> /usr/local/bin/strainscan_build
$ podman run --it --rm --entrypoint /usr/local/bin/strainscan_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strainscan_build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twopaco

```bash
$ singularity exec <container> /usr/local/bin/twopaco
$ podman run --it --rm --entrypoint /usr/local/bin/twopaco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twopaco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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