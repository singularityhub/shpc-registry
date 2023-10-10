---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellarepertorium"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellarepertorium/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellarepertorium/container.yaml"
updated_at: "2023-10-10 03:06:45.079936"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellarepertorium"

versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellarepertorium"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellarepertorium", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellarepertorium", "latest": {"1.10.0--r43hf17093f_0": "sha256:69c14af714faf9365c46a03b6a25db4b23228e368c39985fa0a4066bea1a9f9c"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:70de99cd78206abeaa0aad446aa85c7f465cdc9266367a154130057d2d5558ac", "1.8.0--r42hc247a5b_0": "sha256:34786689ecab877e6ed382697670eb1a4e585ce045514a0e770b1b8cb31c316c", "1.8.0--r42hf17093f_1": "sha256:f8c3210651fa1735ba925eb8633fe898d66b5e12e9c769cf91509ed988d1940c", "1.10.0--r43hf17093f_0": "sha256:69c14af714faf9365c46a03b6a25db4b23228e368c39985fa0a4066bea1a9f9c"}, "docker": "quay.io/biocontainers/bioconductor-cellarepertorium"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellarepertorium.
shpc-registry automated BioContainers addition for bioconductor-cellarepertorium
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellarepertorium
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellarepertorium:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellarepertorium/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cellarepertorium/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellarepertorium-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellarepertorium-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellarepertorium-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellarepertorium-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellarepertorium-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellarepertorium-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellarepertorium

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