---
layout: container
name:  "quay.io/biocontainers/aquila_sv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aquila_sv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/aquila_sv/container.yaml"
updated_at: "2022-10-27 00:26:49.013361"
latest: "1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/aquila_sv"
aliases:
 - "AquilaSV_step1"
 - "AquilaSV_step2"
 - "AquilaSV_step3"
versions:
 - "1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for aquila_sv"
config: {"url": "https://biocontainers.pro/tools/aquila_sv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aquila_sv", "latest": {"1.0--pyhdfd78af_0": "sha256:b03d2d163a13ed0f201f6e8cf73582b90e2a403a5e212eeb20438ced3b2e64a9"}, "tags": {"1.0--pyhdfd78af_0": "sha256:b03d2d163a13ed0f201f6e8cf73582b90e2a403a5e212eeb20438ced3b2e64a9"}, "docker": "quay.io/biocontainers/aquila_sv", "aliases": {"AquilaSV_step1": "/usr/local/bin/AquilaSV_step1", "AquilaSV_step2": "/usr/local/bin/AquilaSV_step2", "AquilaSV_step3": "/usr/local/bin/AquilaSV_step3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aquila_sv.
shpc-registry automated BioContainers addition for aquila_sv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aquila_sv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aquila_sv:1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aquila_sv/1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/aquila_sv/1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aquila_sv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aquila_sv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aquila_sv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aquila_sv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aquila_sv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aquila_sv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AquilaSV_step1

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step1
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AquilaSV_step2

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step2
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AquilaSV_step3

```bash
$ singularity exec <container> /usr/local/bin/AquilaSV_step3
$ podman run --it --rm --entrypoint /usr/local/bin/AquilaSV_step3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AquilaSV_step3   -v ${PWD} -w ${PWD} <container> -c " $@"
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