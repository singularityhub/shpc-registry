---
layout: container
name:  "quay.io/biocontainers/age-metasv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/age-metasv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/age-metasv/container.yaml"
updated_at: "2024-12-09 03:57:09.398011"
latest: "2015.01.29.3--h4ac6f70_8"
container_url: "https://biocontainers.pro/tools/age-metasv"
aliases:
 - "age_align"
versions:
 - "2015.01.29.3--h9f5acd7_5"
 - "2015.01.29.3--h4ac6f70_7"
 - "2015.01.29.3--h4ac6f70_8"
description: "shpc-registry automated BioContainers addition for age-metasv"
config: {"url": "https://biocontainers.pro/tools/age-metasv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for age-metasv", "latest": {"2015.01.29.3--h4ac6f70_8": "sha256:345536fb397b8acd49a3462b956c5a1c481763055a89efb8013874506488e91e"}, "tags": {"2015.01.29.3--h9f5acd7_5": "sha256:88660caa860131060d21c2b64529ab709881c8ff1772913eed0323786b6fe774", "2015.01.29.3--h4ac6f70_7": "sha256:9122481bf9690bbdc79ec4291c3d29156cb7c9d613a2faa34c644b6c4afe0afc", "2015.01.29.3--h4ac6f70_8": "sha256:345536fb397b8acd49a3462b956c5a1c481763055a89efb8013874506488e91e"}, "docker": "quay.io/biocontainers/age-metasv", "aliases": {"age_align": "/usr/local/bin/age_align"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/age-metasv.
shpc-registry automated BioContainers addition for age-metasv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/age-metasv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/age-metasv:2015.01.29.3--h4ac6f70_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/age-metasv/2015.01.29.3--h4ac6f70_8
$ module help quay.io/biocontainers/age-metasv/2015.01.29.3--h4ac6f70_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### age-metasv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### age-metasv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### age-metasv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### age-metasv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### age-metasv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### age-metasv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### age_align

```bash
$ singularity exec <container> /usr/local/bin/age_align
$ podman run --it --rm --entrypoint /usr/local/bin/age_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/age_align   -v ${PWD} -w ${PWD} <container> -c " $@"
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