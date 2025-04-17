---
layout: container
name:  "quay.io/biocontainers/r-disprose"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-disprose/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-disprose/container.yaml"
updated_at: "2025-04-17 02:57:04.163147"
latest: "0.1.6--r44h3342da4_3"
container_url: "https://biocontainers.pro/tools/r-disprose"

versions:
 - "0.1.6--r42h3342da4_1"
 - "0.1.6--r43h3342da4_2"
 - "0.1.6--r44h3342da4_3"
description: "singularity registry hpc automated addition for r-disprose"
config: {"url": "https://biocontainers.pro/tools/r-disprose", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-disprose", "latest": {"0.1.6--r44h3342da4_3": "sha256:5e7a097674ac977d856ec05b4d28b87e479fb25ecac981b4914ef2e973051e66"}, "tags": {"0.1.6--r42h3342da4_1": "sha256:9f491d1c4c3c4c46dc5a6fa44dfc3a4cbf280f609cce107589b5af045c871c70", "0.1.6--r43h3342da4_2": "sha256:98a73cd4550e8ad3625df3ba498900a59b9ddc844dea2e9d937c1ebf249fd667", "0.1.6--r44h3342da4_3": "sha256:5e7a097674ac977d856ec05b4d28b87e479fb25ecac981b4914ef2e973051e66"}, "docker": "quay.io/biocontainers/r-disprose"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-disprose.
singularity registry hpc automated addition for r-disprose
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-disprose
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-disprose:0.1.6--r44h3342da4_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-disprose/0.1.6--r44h3342da4_3
$ module help quay.io/biocontainers/r-disprose/0.1.6--r44h3342da4_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-disprose-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-disprose-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-disprose-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-disprose-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-disprose-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-disprose-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-disprose

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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