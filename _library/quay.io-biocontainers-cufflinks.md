---
layout: container
name:  "quay.io/biocontainers/cufflinks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cufflinks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cufflinks/container.yaml"
updated_at: "2025-11-28 03:16:45.311186"
latest: "2.2.1--py36_2"
container_url: "https://biocontainers.pro/tools/cufflinks"
aliases:
 - "cuffcompare"
 - "cuffdiff"
 - "cufflinks"
 - "cuffmerge"
 - "cuffnorm"
 - "cuffquant"
 - "gffread"
 - "gtf_to_sam"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.2.1--py36_2"
 - "2.2.1--py27_2"
description: "shpc-registry automated BioContainers addition for cufflinks"
config: {"url": "https://biocontainers.pro/tools/cufflinks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cufflinks", "latest": {"2.2.1--py36_2": "sha256:be910bfb779d48e4fdcad6a63885787c84a98db53df71b5fb9a281b9f968a055"}, "tags": {"2.2.1--py36_2": "sha256:be910bfb779d48e4fdcad6a63885787c84a98db53df71b5fb9a281b9f968a055", "2.2.1--py27_2": "sha256:1aa3f262e175a02be21c7d334e9e1a95302426ef98c835595d682da197503cc8"}, "docker": "quay.io/biocontainers/cufflinks", "aliases": {"cuffcompare": "/usr/local/bin/cuffcompare", "cuffdiff": "/usr/local/bin/cuffdiff", "cufflinks": "/usr/local/bin/cufflinks", "cuffmerge": "/usr/local/bin/cuffmerge", "cuffnorm": "/usr/local/bin/cuffnorm", "cuffquant": "/usr/local/bin/cuffquant", "gffread": "/usr/local/bin/gffread", "gtf_to_sam": "/usr/local/bin/gtf_to_sam", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cufflinks.
shpc-registry automated BioContainers addition for cufflinks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cufflinks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cufflinks:2.2.1--py36_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cufflinks/2.2.1--py36_2
$ module help quay.io/biocontainers/cufflinks/2.2.1--py36_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cufflinks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cufflinks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cufflinks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cufflinks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cufflinks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cufflinks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cuffcompare

```bash
$ singularity exec <container> /usr/local/bin/cuffcompare
$ podman run --it --rm --entrypoint /usr/local/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffdiff

```bash
$ singularity exec <container> /usr/local/bin/cuffdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cufflinks

```bash
$ singularity exec <container> /usr/local/bin/cufflinks
$ podman run --it --rm --entrypoint /usr/local/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffmerge

```bash
$ singularity exec <container> /usr/local/bin/cuffmerge
$ podman run --it --rm --entrypoint /usr/local/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffnorm

```bash
$ singularity exec <container> /usr/local/bin/cuffnorm
$ podman run --it --rm --entrypoint /usr/local/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffquant

```bash
$ singularity exec <container> /usr/local/bin/cuffquant
$ podman run --it --rm --entrypoint /usr/local/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf_to_sam

```bash
$ singularity exec <container> /usr/local/bin/gtf_to_sam
$ podman run --it --rm --entrypoint /usr/local/bin/gtf_to_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf_to_sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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