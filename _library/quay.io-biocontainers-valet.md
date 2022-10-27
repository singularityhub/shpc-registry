---
layout: container
name:  "quay.io/biocontainers/valet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/valet/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/valet/container.yaml"
updated_at: "2022-10-27 00:34:27.675309"
latest: "1.0--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/valet"
aliases:
 - "valet.py"
versions:
 - "1.0--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for valet"
config: {"url": "https://biocontainers.pro/tools/valet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for valet", "latest": {"1.0--hdfd78af_5": "sha256:2f445b7c87f861283eae53ab8046cf84420325db8f06c6c35f6c87d54859538a"}, "tags": {"1.0--hdfd78af_5": "sha256:2f445b7c87f861283eae53ab8046cf84420325db8f06c6c35f6c87d54859538a"}, "docker": "quay.io/biocontainers/valet", "aliases": {"valet.py": "/usr/local/bin/valet.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/valet.
shpc-registry automated BioContainers addition for valet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/valet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/valet:1.0--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/valet/1.0--hdfd78af_5
$ module help quay.io/biocontainers/valet/1.0--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### valet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### valet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### valet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### valet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### valet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### valet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### valet.py

```bash
$ singularity exec <container> /usr/local/bin/valet.py
$ podman run --it --rm --entrypoint /usr/local/bin/valet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/valet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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