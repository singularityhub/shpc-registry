---
layout: container
name:  "quay.io/biocontainers/astropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/astropy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/astropy/container.yaml"
updated_at: "2024-07-14 02:55:15.674788"
latest: "5.2.2"
container_url: "https://biocontainers.pro/tools/astropy"
aliases:
 - "fits2bitmap"
 - "fitscheck"
 - "fitsdiff"
 - "fitsheader"
 - "fitsinfo"
 - "samp_hub"
 - "showtable"
 - "volint"
 - "wcslint"
 - "py.test"
 - "pytest"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
versions:
 - "3.0.5--py37h7b6447c_1"
 - "5.2.2"
description: "shpc-registry automated BioContainers addition for astropy"
config: {"url": "https://biocontainers.pro/tools/astropy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for astropy", "latest": {"5.2.2": "sha256:ada7ab6c02052d01ffc9e226a49f1dd18e5823b43d8526950f2b03f71c80fe03"}, "tags": {"3.0.5--py37h7b6447c_1": "sha256:b625091c19ca3f2daf47399b777aefd812e37077c6b7b02e239f6833efb87790", "5.2.2": "sha256:ada7ab6c02052d01ffc9e226a49f1dd18e5823b43d8526950f2b03f71c80fe03"}, "docker": "quay.io/biocontainers/astropy", "aliases": {"fits2bitmap": "/usr/local/bin/fits2bitmap", "fitscheck": "/usr/local/bin/fitscheck", "fitsdiff": "/usr/local/bin/fitsdiff", "fitsheader": "/usr/local/bin/fitsheader", "fitsinfo": "/usr/local/bin/fitsinfo", "samp_hub": "/usr/local/bin/samp_hub", "showtable": "/usr/local/bin/showtable", "volint": "/usr/local/bin/volint", "wcslint": "/usr/local/bin/wcslint", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/astropy.
shpc-registry automated BioContainers addition for astropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/astropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/astropy:5.2.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/astropy/5.2.2
$ module help quay.io/biocontainers/astropy/5.2.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### astropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### astropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### astropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### astropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### astropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### astropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fits2bitmap

```bash
$ singularity exec <container> /usr/local/bin/fits2bitmap
$ podman run --it --rm --entrypoint /usr/local/bin/fits2bitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fits2bitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitscheck

```bash
$ singularity exec <container> /usr/local/bin/fitscheck
$ podman run --it --rm --entrypoint /usr/local/bin/fitscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsdiff

```bash
$ singularity exec <container> /usr/local/bin/fitsdiff
$ podman run --it --rm --entrypoint /usr/local/bin/fitsdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsheader

```bash
$ singularity exec <container> /usr/local/bin/fitsheader
$ podman run --it --rm --entrypoint /usr/local/bin/fitsheader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsheader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitsinfo

```bash
$ singularity exec <container> /usr/local/bin/fitsinfo
$ podman run --it --rm --entrypoint /usr/local/bin/fitsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samp_hub

```bash
$ singularity exec <container> /usr/local/bin/samp_hub
$ podman run --it --rm --entrypoint /usr/local/bin/samp_hub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samp_hub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### showtable

```bash
$ singularity exec <container> /usr/local/bin/showtable
$ podman run --it --rm --entrypoint /usr/local/bin/showtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/showtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### volint

```bash
$ singularity exec <container> /usr/local/bin/volint
$ podman run --it --rm --entrypoint /usr/local/bin/volint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/volint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wcslint

```bash
$ singularity exec <container> /usr/local/bin/wcslint
$ podman run --it --rm --entrypoint /usr/local/bin/wcslint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wcslint   -v ${PWD} -w ${PWD} <container> -c " $@"
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