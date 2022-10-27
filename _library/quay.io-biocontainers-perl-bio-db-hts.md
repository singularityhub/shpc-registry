---
layout: container
name:  "quay.io/biocontainers/perl-bio-db-hts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-db-hts/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-db-hts/container.yaml"
updated_at: "2022-10-27 00:59:25.524848"
latest: "3.01--pl5321hb0d9459_6"
container_url: "https://biocontainers.pro/tools/perl-bio-db-hts"

versions:
 - "3.01--pl5321hb0d9459_6"
description: "shpc-registry automated BioContainers addition for perl-bio-db-hts"
config: {"url": "https://biocontainers.pro/tools/perl-bio-db-hts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-db-hts", "latest": {"3.01--pl5321hb0d9459_6": "sha256:63873f385e6c5723bb76e111d340945046ef25b2957a6bf5a2ea11c5dd8cebd9"}, "tags": {"3.01--pl5321hb0d9459_6": "sha256:63873f385e6c5723bb76e111d340945046ef25b2957a6bf5a2ea11c5dd8cebd9"}, "docker": "quay.io/biocontainers/perl-bio-db-hts"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-db-hts.
shpc-registry automated BioContainers addition for perl-bio-db-hts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-db-hts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-db-hts:3.01--pl5321hb0d9459_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-db-hts/3.01--pl5321hb0d9459_6
$ module help quay.io/biocontainers/perl-bio-db-hts/3.01--pl5321hb0d9459_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-db-hts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-db-hts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-db-hts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-db-hts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-db-hts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-db-hts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-bio-db-hts

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