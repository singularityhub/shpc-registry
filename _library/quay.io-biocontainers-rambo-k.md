---
layout: container
name:  "quay.io/biocontainers/rambo-k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rambo-k/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rambo-k/container.yaml"
updated_at: "2022-10-27 00:41:04.049682"
latest: "1.21--1"
container_url: "https://biocontainers.pro/tools/rambo-k"
aliases:
 - "RAMBOK.py"
 - "classifier.jar"
 - "plot.py"
 - "simulate_reads.py"
 - "trainer.jar"
versions:
 - "1.21--1"
description: "shpc-registry automated BioContainers addition for rambo-k"
config: {"url": "https://biocontainers.pro/tools/rambo-k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rambo-k", "latest": {"1.21--1": "sha256:1ae0c6f3c394c43d6cdc92a67fcb681d0d860d8862431379516746db7d1135ae"}, "tags": {"1.21--1": "sha256:1ae0c6f3c394c43d6cdc92a67fcb681d0d860d8862431379516746db7d1135ae"}, "docker": "quay.io/biocontainers/rambo-k", "aliases": {"RAMBOK.py": "/usr/local/bin/RAMBOK.py", "classifier.jar": "/usr/local/bin/classifier.jar", "plot.py": "/usr/local/bin/plot.py", "simulate_reads.py": "/usr/local/bin/simulate_reads.py", "trainer.jar": "/usr/local/bin/trainer.jar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rambo-k.
shpc-registry automated BioContainers addition for rambo-k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rambo-k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rambo-k:1.21--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rambo-k/1.21--1
$ module help quay.io/biocontainers/rambo-k/1.21--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rambo-k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rambo-k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rambo-k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rambo-k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rambo-k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rambo-k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RAMBOK.py

```bash
$ singularity exec <container> /usr/local/bin/RAMBOK.py
$ podman run --it --rm --entrypoint /usr/local/bin/RAMBOK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RAMBOK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classifier.jar

```bash
$ singularity exec <container> /usr/local/bin/classifier.jar
$ podman run --it --rm --entrypoint /usr/local/bin/classifier.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classifier.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot.py

```bash
$ singularity exec <container> /usr/local/bin/plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trainer.jar

```bash
$ singularity exec <container> /usr/local/bin/trainer.jar
$ podman run --it --rm --entrypoint /usr/local/bin/trainer.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trainer.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
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