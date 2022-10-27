---
layout: container
name:  "quay.io/biocontainers/targqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targqc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/targqc/container.yaml"
updated_at: "2022-10-27 00:45:33.334581"
latest: "1.8.1--pyh5ca1d4c_1"
container_url: "https://biocontainers.pro/tools/targqc"
aliases:
 - "annotate_bed.py"
 - "cols"
 - "qualimap"
 - "tabutils"
 - "targqc"
 - "tsv"
versions:
 - "1.8.1--pyh5ca1d4c_1"
description: "shpc-registry automated BioContainers addition for targqc"
config: {"url": "https://biocontainers.pro/tools/targqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for targqc", "latest": {"1.8.1--pyh5ca1d4c_1": "sha256:9ce968510525b18152e6826cca6d5b2d50712a7747119a0175b4ef75a29d66f5"}, "tags": {"1.8.1--pyh5ca1d4c_1": "sha256:9ce968510525b18152e6826cca6d5b2d50712a7747119a0175b4ef75a29d66f5"}, "docker": "quay.io/biocontainers/targqc", "aliases": {"annotate_bed.py": "/usr/local/bin/annotate_bed.py", "cols": "/usr/local/bin/cols", "qualimap": "/usr/local/bin/qualimap", "tabutils": "/usr/local/bin/tabutils", "targqc": "/usr/local/bin/targqc", "tsv": "/usr/local/bin/tsv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targqc.
shpc-registry automated BioContainers addition for targqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targqc:1.8.1--pyh5ca1d4c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targqc/1.8.1--pyh5ca1d4c_1
$ module help quay.io/biocontainers/targqc/1.8.1--pyh5ca1d4c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_bed.py

```bash
$ singularity exec <container> /usr/local/bin/annotate_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cols

```bash
$ singularity exec <container> /usr/local/bin/cols
$ podman run --it --rm --entrypoint /usr/local/bin/cols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualimap

```bash
$ singularity exec <container> /usr/local/bin/qualimap
$ podman run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabutils

```bash
$ singularity exec <container> /usr/local/bin/tabutils
$ podman run --it --rm --entrypoint /usr/local/bin/tabutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targqc

```bash
$ singularity exec <container> /usr/local/bin/targqc
$ podman run --it --rm --entrypoint /usr/local/bin/targqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tsv

```bash
$ singularity exec <container> /usr/local/bin/tsv
$ podman run --it --rm --entrypoint /usr/local/bin/tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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