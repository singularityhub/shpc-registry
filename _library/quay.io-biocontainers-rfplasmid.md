---
layout: container
name:  "quay.io/biocontainers/rfplasmid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rfplasmid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rfplasmid/container.yaml"
updated_at: "2022-10-29 05:42:57.296628"
latest: "0.0.18--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/rfplasmid"
aliases:
 - "rfplasmid"
 - "2to3-3.9"
 - "alimask"
 - "checkm"
 - "dendropy-format"
 - "diamond"
 - "easel"
 - "esl-afetch"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
versions:
 - "0.0.18--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for rfplasmid"
config: {"url": "https://biocontainers.pro/tools/rfplasmid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rfplasmid", "latest": {"0.0.18--pyhdfd78af_0": "sha256:037bef18bcae57e403e40856d6434c08441a17ff24f1e62b8b9a7139843de870"}, "tags": {"0.0.18--pyhdfd78af_0": "sha256:037bef18bcae57e403e40856d6434c08441a17ff24f1e62b8b9a7139843de870"}, "docker": "quay.io/biocontainers/rfplasmid", "aliases": {"rfplasmid": "/usr/local/bin/rfplasmid", "2to3-3.9": "/usr/local/bin/2to3-3.9", "alimask": "/usr/local/bin/alimask", "checkm": "/usr/local/bin/checkm", "dendropy-format": "/usr/local/bin/dendropy-format", "diamond": "/usr/local/bin/diamond", "easel": "/usr/local/bin/easel", "esl-afetch": "/usr/local/bin/esl-afetch", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rfplasmid.
shpc-registry automated BioContainers addition for rfplasmid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rfplasmid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rfplasmid:0.0.18--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rfplasmid/0.0.18--pyhdfd78af_0
$ module help quay.io/biocontainers/rfplasmid/0.0.18--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rfplasmid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rfplasmid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rfplasmid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rfplasmid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rfplasmid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rfplasmid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rfplasmid

```bash
$ singularity exec <container> /usr/local/bin/rfplasmid
$ podman run --it --rm --entrypoint /usr/local/bin/rfplasmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfplasmid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-afetch

```bash
$ singularity exec <container> /usr/local/bin/esl-afetch
$ podman run --it --rm --entrypoint /usr/local/bin/esl-afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
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