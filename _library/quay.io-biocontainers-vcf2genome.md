---
layout: container
name:  "quay.io/biocontainers/vcf2genome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf2genome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vcf2genome/container.yaml"
updated_at: "2022-10-27 01:02:30.960179"
latest: "0.91--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/vcf2genome"
aliases:
 - "vcf2genome"
versions:
 - "0.91--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for vcf2genome"
config: {"url": "https://biocontainers.pro/tools/vcf2genome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcf2genome", "latest": {"0.91--hdfd78af_2": "sha256:ea94a9e9ec29e3969578516d1b779079416dab82e00c97f4fb2b878e3b77a75c"}, "tags": {"0.91--hdfd78af_2": "sha256:ea94a9e9ec29e3969578516d1b779079416dab82e00c97f4fb2b878e3b77a75c"}, "docker": "quay.io/biocontainers/vcf2genome", "aliases": {"vcf2genome": "/usr/local/bin/vcf2genome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf2genome.
shpc-registry automated BioContainers addition for vcf2genome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf2genome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf2genome:0.91--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf2genome/0.91--hdfd78af_2
$ module help quay.io/biocontainers/vcf2genome/0.91--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf2genome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf2genome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf2genome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf2genome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf2genome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf2genome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcf2genome

```bash
$ singularity exec <container> /usr/local/bin/vcf2genome
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2genome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2genome   -v ${PWD} -w ${PWD} <container> -c " $@"
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