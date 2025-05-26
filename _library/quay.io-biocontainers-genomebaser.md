---
layout: container
name:  "quay.io/biocontainers/genomebaser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomebaser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomebaser/container.yaml"
updated_at: "2025-05-26 03:42:09.213472"
latest: "0.1.2--py27_1"
container_url: "https://biocontainers.pro/tools/genomebaser"
aliases:
 - "GenomeBaser"
 - "sample"
 - "easy_install-2.7"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "tclsh8.5"
 - "wish8.5"
versions:
 - "0.1.2--py27_1"
description: "shpc-registry automated BioContainers addition for genomebaser"
config: {"url": "https://biocontainers.pro/tools/genomebaser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomebaser", "latest": {"0.1.2--py27_1": "sha256:0d3041f0750b0673c363dfcb9e6bfb76b6b297e114805144b1242fe8d4761313"}, "tags": {"0.1.2--py27_1": "sha256:0d3041f0750b0673c363dfcb9e6bfb76b6b297e114805144b1242fe8d4761313"}, "docker": "quay.io/biocontainers/genomebaser", "aliases": {"GenomeBaser": "/usr/local/bin/GenomeBaser", "sample": "/usr/local/bin/sample", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomebaser.
shpc-registry automated BioContainers addition for genomebaser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomebaser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomebaser:0.1.2--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomebaser/0.1.2--py27_1
$ module help quay.io/biocontainers/genomebaser/0.1.2--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomebaser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomebaser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomebaser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomebaser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomebaser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomebaser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeBaser

```bash
$ singularity exec <container> /usr/local/bin/GenomeBaser
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeBaser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeBaser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample

```bash
$ singularity exec <container> /usr/local/bin/sample
$ podman run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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