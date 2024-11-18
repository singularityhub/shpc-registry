---
layout: container
name:  "quay.io/biocontainers/r-sigqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sigqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sigqc/container.yaml"
updated_at: "2024-11-18 03:37:50.441458"
latest: "0.1.24--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-sigqc"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.22--r41h3342da4_1"
 - "0.1.22--r42h3342da4_2"
 - "0.1.23--r42h3342da4_0"
 - "0.1.23--r43h3342da4_1"
 - "0.1.24--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-sigqc"
config: {"url": "https://biocontainers.pro/tools/r-sigqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sigqc", "latest": {"0.1.24--r43h3342da4_0": "sha256:fe971cc2f1bae1e72060992902c840613fbced92ed476f4d7bf9deb2e8693c8e"}, "tags": {"0.1.22--r41h3342da4_1": "sha256:7192002233a4875401e50299185967bac244b65555c4dcdaa143f1f782ed6bfc", "0.1.22--r42h3342da4_2": "sha256:690a6f397db980739b5f99c3a4984cb4fd5ae0a2ed071144ef41fd7dabfa9818", "0.1.23--r42h3342da4_0": "sha256:d1b723b9c159420a674d4a9c9abf482c6e4a36dd1b4131056cf3181f4dcf4872", "0.1.23--r43h3342da4_1": "sha256:61fce78e123c89093743f6feec6805503ffe0fab544658955d33a78f7ee364ef", "0.1.24--r43h3342da4_0": "sha256:fe971cc2f1bae1e72060992902c840613fbced92ed476f4d7bf9deb2e8693c8e"}, "docker": "quay.io/biocontainers/r-sigqc", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sigqc.
shpc-registry automated BioContainers addition for r-sigqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sigqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sigqc:0.1.24--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sigqc/0.1.24--r43h3342da4_0
$ module help quay.io/biocontainers/r-sigqc/0.1.24--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sigqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sigqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sigqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sigqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sigqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sigqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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