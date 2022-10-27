---
layout: container
name:  "quay.io/biocontainers/quasildr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quasildr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/quasildr/container.yaml"
updated_at: "2022-10-27 01:00:14.099620"
latest: "0.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/quasildr"
aliases:
 - "run_graphdr.py"
 - "run_structdr.py"
versions:
 - "0.2.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for quasildr"
config: {"url": "https://biocontainers.pro/tools/quasildr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quasildr", "latest": {"0.2.2--pyhdfd78af_0": "sha256:1f60c90035fd03c1e3c1706e942b71683688fdbfa926fc9a4bc0da5988611548"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:1f60c90035fd03c1e3c1706e942b71683688fdbfa926fc9a4bc0da5988611548"}, "docker": "quay.io/biocontainers/quasildr", "aliases": {"run_graphdr.py": "/usr/local/bin/run_graphdr.py", "run_structdr.py": "/usr/local/bin/run_structdr.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quasildr.
shpc-registry automated BioContainers addition for quasildr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quasildr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quasildr:0.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quasildr/0.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/quasildr/0.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quasildr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quasildr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quasildr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quasildr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quasildr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quasildr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run_graphdr.py

```bash
$ singularity exec <container> /usr/local/bin/run_graphdr.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_graphdr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_graphdr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_structdr.py

```bash
$ singularity exec <container> /usr/local/bin/run_structdr.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_structdr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_structdr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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