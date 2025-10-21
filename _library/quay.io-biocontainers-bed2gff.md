---
layout: container
name:  "quay.io/biocontainers/bed2gff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bed2gff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bed2gff/container.yaml"
updated_at: "2025-10-21 03:52:52.186229"
latest: "0.1.5--h9948957_1"
container_url: "https://biocontainers.pro/tools/bed2gff"
aliases:
 - "bed2gff"
versions:
 - "0.1.3--h4ac6f70_0"
 - "0.1.4--h4ac6f70_0"
 - "0.1.5--h4ac6f70_0"
 - "0.1.5--h9948957_1"
description: "singularity registry hpc automated addition for bed2gff"
config: {"url": "https://biocontainers.pro/tools/bed2gff", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bed2gff", "latest": {"0.1.5--h9948957_1": "sha256:45820351d09994fb526ca4a4e179cf5bb452390bf9d9b70d2c7801ad7d8120e0"}, "tags": {"0.1.3--h4ac6f70_0": "sha256:caa3ee07079f92a022b6f59b75854c9fe40a1ef10b254e49425778290b8a68ac", "0.1.4--h4ac6f70_0": "sha256:4b0ffef8710c0b724b17eb65a0c2aadf2df73e39d44b700398ef52e8e8acf9fa", "0.1.5--h4ac6f70_0": "sha256:ef24f285b6f345ec4c2d419e707f8f0e632d5812e35eaf57517a738cbce85048", "0.1.5--h9948957_1": "sha256:45820351d09994fb526ca4a4e179cf5bb452390bf9d9b70d2c7801ad7d8120e0"}, "docker": "quay.io/biocontainers/bed2gff", "aliases": {"bed2gff": "/usr/local/bin/bed2gff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bed2gff.
singularity registry hpc automated addition for bed2gff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bed2gff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bed2gff:0.1.5--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bed2gff/0.1.5--h9948957_1
$ module help quay.io/biocontainers/bed2gff/0.1.5--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bed2gff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bed2gff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bed2gff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bed2gff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bed2gff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bed2gff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bed2gff

```bash
$ singularity exec <container> /usr/local/bin/bed2gff
$ podman run --it --rm --entrypoint /usr/local/bin/bed2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
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