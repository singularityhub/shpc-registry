---
layout: container
name:  "quay.io/biocontainers/validate-fasta-database"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/validate-fasta-database/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/validate-fasta-database/container.yaml"
updated_at: "2022-10-27 00:27:30.652232"
latest: "1.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/validate-fasta-database"
aliases:
 - "validate-fasta-database"
versions:
 - "1.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for validate-fasta-database"
config: {"url": "https://biocontainers.pro/tools/validate-fasta-database", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for validate-fasta-database", "latest": {"1.0--hdfd78af_2": "sha256:d5fdb70c29b291ae582920fd0aeaed0e35e731539f7fa5e776dab7717a61c839"}, "tags": {"1.0--hdfd78af_2": "sha256:d5fdb70c29b291ae582920fd0aeaed0e35e731539f7fa5e776dab7717a61c839"}, "docker": "quay.io/biocontainers/validate-fasta-database", "aliases": {"validate-fasta-database": "/usr/local/bin/validate-fasta-database"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/validate-fasta-database.
shpc-registry automated BioContainers addition for validate-fasta-database
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/validate-fasta-database
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/validate-fasta-database:1.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/validate-fasta-database/1.0--hdfd78af_2
$ module help quay.io/biocontainers/validate-fasta-database/1.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### validate-fasta-database-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### validate-fasta-database-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### validate-fasta-database-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### validate-fasta-database-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### validate-fasta-database-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### validate-fasta-database-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### validate-fasta-database

```bash
$ singularity exec <container> /usr/local/bin/validate-fasta-database
$ podman run --it --rm --entrypoint /usr/local/bin/validate-fasta-database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate-fasta-database   -v ${PWD} -w ${PWD} <container> -c " $@"
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