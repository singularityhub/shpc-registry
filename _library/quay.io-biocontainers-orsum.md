---
layout: container
name:  "quay.io/biocontainers/orsum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orsum/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/orsum/container.yaml"
updated_at: "2022-10-27 00:24:21.124368"
latest: "1.4.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/orsum"
aliases:
 - "orsum.py"
 - "plotFunctions.py"
 - "termCombinationLib.py"
versions:
 - "1.4.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for orsum"
config: {"url": "https://biocontainers.pro/tools/orsum", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orsum", "latest": {"1.4.0--hdfd78af_0": "sha256:dfa94f9ce9ff8053e2f39b85c49a835fa286586014b278b952b136431cd29ccf"}, "tags": {"1.4.0--hdfd78af_0": "sha256:dfa94f9ce9ff8053e2f39b85c49a835fa286586014b278b952b136431cd29ccf"}, "docker": "quay.io/biocontainers/orsum", "aliases": {"orsum.py": "/usr/local/bin/orsum.py", "plotFunctions.py": "/usr/local/bin/plotFunctions.py", "termCombinationLib.py": "/usr/local/bin/termCombinationLib.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orsum.
shpc-registry automated BioContainers addition for orsum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orsum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orsum:1.4.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orsum/1.4.0--hdfd78af_0
$ module help quay.io/biocontainers/orsum/1.4.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orsum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orsum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orsum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orsum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orsum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orsum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### orsum.py

```bash
$ singularity exec <container> /usr/local/bin/orsum.py
$ podman run --it --rm --entrypoint /usr/local/bin/orsum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orsum.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotFunctions.py

```bash
$ singularity exec <container> /usr/local/bin/plotFunctions.py
$ podman run --it --rm --entrypoint /usr/local/bin/plotFunctions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotFunctions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### termCombinationLib.py

```bash
$ singularity exec <container> /usr/local/bin/termCombinationLib.py
$ podman run --it --rm --entrypoint /usr/local/bin/termCombinationLib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/termCombinationLib.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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