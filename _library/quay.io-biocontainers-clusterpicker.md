---
layout: container
name:  "quay.io/biocontainers/clusterpicker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clusterpicker/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clusterpicker/container.yaml"
updated_at: "2022-10-27 01:05:33.004062"
latest: "1.2.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/clusterpicker"
aliases:
 - "ClusterPicker"
 - "cluster-picker"
versions:
 - "1.2.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for clusterpicker"
config: {"url": "https://biocontainers.pro/tools/clusterpicker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clusterpicker", "latest": {"1.2.5--hdfd78af_1": "sha256:82929993d0894e87420743983338639b797957d99a5dda6e0438f7d257e3cd73"}, "tags": {"1.2.5--hdfd78af_1": "sha256:82929993d0894e87420743983338639b797957d99a5dda6e0438f7d257e3cd73"}, "docker": "quay.io/biocontainers/clusterpicker", "aliases": {"ClusterPicker": "/usr/local/bin/ClusterPicker", "cluster-picker": "/usr/local/bin/cluster-picker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clusterpicker.
shpc-registry automated BioContainers addition for clusterpicker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clusterpicker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clusterpicker:1.2.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clusterpicker/1.2.5--hdfd78af_1
$ module help quay.io/biocontainers/clusterpicker/1.2.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clusterpicker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clusterpicker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clusterpicker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clusterpicker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clusterpicker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clusterpicker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ClusterPicker

```bash
$ singularity exec <container> /usr/local/bin/ClusterPicker
$ podman run --it --rm --entrypoint /usr/local/bin/ClusterPicker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClusterPicker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster-picker

```bash
$ singularity exec <container> /usr/local/bin/cluster-picker
$ podman run --it --rm --entrypoint /usr/local/bin/cluster-picker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster-picker   -v ${PWD} -w ${PWD} <container> -c " $@"
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