---
layout: container
name:  "quay.io/biocontainers/segmentation-fold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/segmentation-fold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/segmentation-fold/container.yaml"
updated_at: "2026-01-05 04:43:13.261190"
latest: "1.7.0--py27hc30c61c_4"
container_url: "https://biocontainers.pro/tools/segmentation-fold"
aliases:
 - "segmentation-fold"
 - "segmentation-fold-utils"
 - "htseq-count"
 - "htseq-qa"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
versions:
 - "1.7.0--py27hc30c61c_4"
description: "shpc-registry automated BioContainers addition for segmentation-fold"
config: {"url": "https://biocontainers.pro/tools/segmentation-fold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for segmentation-fold", "latest": {"1.7.0--py27hc30c61c_4": "sha256:91b7e28d5b67c44d7246e462e282835dd16a47d723fcf35dcabb94ec455bdf79"}, "tags": {"1.7.0--py27hc30c61c_4": "sha256:91b7e28d5b67c44d7246e462e282835dd16a47d723fcf35dcabb94ec455bdf79"}, "docker": "quay.io/biocontainers/segmentation-fold", "aliases": {"segmentation-fold": "/usr/local/bin/segmentation-fold", "segmentation-fold-utils": "/usr/local/bin/segmentation-fold-utils", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/segmentation-fold.
shpc-registry automated BioContainers addition for segmentation-fold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/segmentation-fold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/segmentation-fold:1.7.0--py27hc30c61c_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/segmentation-fold/1.7.0--py27hc30c61c_4
$ module help quay.io/biocontainers/segmentation-fold/1.7.0--py27hc30c61c_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### segmentation-fold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### segmentation-fold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### segmentation-fold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### segmentation-fold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### segmentation-fold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### segmentation-fold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### segmentation-fold

```bash
$ singularity exec <container> /usr/local/bin/segmentation-fold
$ podman run --it --rm --entrypoint /usr/local/bin/segmentation-fold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentation-fold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segmentation-fold-utils

```bash
$ singularity exec <container> /usr/local/bin/segmentation-fold-utils
$ podman run --it --rm --entrypoint /usr/local/bin/segmentation-fold-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentation-fold-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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