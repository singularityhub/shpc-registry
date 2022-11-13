---
layout: container
name:  "quay.io/biocontainers/somatic-sniper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/somatic-sniper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/somatic-sniper/container.yaml"
updated_at: "2022-11-13 00:31:02.818634"
latest: "1.0.5.0--0"
container_url: "https://biocontainers.pro/tools/somatic-sniper"
aliases:
 - "bam-somaticsniper"
versions:
 - "1.0.5.0--0"
description: "shpc-registry automated BioContainers addition for somatic-sniper"
config: {"url": "https://biocontainers.pro/tools/somatic-sniper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for somatic-sniper", "latest": {"1.0.5.0--0": "sha256:e82aacba18ec9b4d803f8081580c51ea896070a223f645923cfc6f4335df3465"}, "tags": {"1.0.5.0--0": "sha256:e82aacba18ec9b4d803f8081580c51ea896070a223f645923cfc6f4335df3465"}, "docker": "quay.io/biocontainers/somatic-sniper", "aliases": {"bam-somaticsniper": "/usr/local/bin/bam-somaticsniper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/somatic-sniper.
shpc-registry automated BioContainers addition for somatic-sniper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/somatic-sniper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/somatic-sniper:1.0.5.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/somatic-sniper/1.0.5.0--0
$ module help quay.io/biocontainers/somatic-sniper/1.0.5.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### somatic-sniper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### somatic-sniper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### somatic-sniper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### somatic-sniper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### somatic-sniper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### somatic-sniper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam-somaticsniper

```bash
$ singularity exec <container> /usr/local/bin/bam-somaticsniper
$ podman run --it --rm --entrypoint /usr/local/bin/bam-somaticsniper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-somaticsniper   -v ${PWD} -w ${PWD} <container> -c " $@"
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