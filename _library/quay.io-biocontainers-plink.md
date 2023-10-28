---
layout: container
name:  "quay.io/biocontainers/plink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plink/container.yaml"
updated_at: "2023-10-28 02:43:40.680224"
latest: "1.90b6.21--h031d066_5"
container_url: "https://biocontainers.pro/tools/plink"

versions:
 - "1.90b6.21--hec16e2b_2"
 - "1.90b6.21--hec16e2b_3"
 - "1.90b6.21--hec16e2b_4"
 - "1.90b6.21--h031d066_5"
description: "shpc-registry automated BioContainers addition for plink"
config: {"url": "https://biocontainers.pro/tools/plink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plink", "latest": {"1.90b6.21--h031d066_5": "sha256:2029eac3d7d29d6acc5555c07d7605af4742dfab245eea0d0d2d8eca8483e653"}, "tags": {"1.90b6.21--hec16e2b_2": "sha256:5c07df8983b120774e6d0dea8a32aa3ec44f7ee75b0438af038eb8f36acdc8c0", "1.90b6.21--hec16e2b_3": "sha256:9f77ca902366073cda803e2b1266010ff57fc3bc1d07c084ed8f97a9e4827bde", "1.90b6.21--hec16e2b_4": "sha256:bdccab437af505633bf1bc259e587493585b1899d055dc78a5db66aac3c2c2fa", "1.90b6.21--h031d066_5": "sha256:2029eac3d7d29d6acc5555c07d7605af4742dfab245eea0d0d2d8eca8483e653"}, "docker": "quay.io/biocontainers/plink"}
---

This module is a singularity container wrapper for quay.io/biocontainers/plink.
shpc-registry automated BioContainers addition for plink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plink:1.90b6.21--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plink/1.90b6.21--h031d066_5
$ module help quay.io/biocontainers/plink/1.90b6.21--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### plink

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