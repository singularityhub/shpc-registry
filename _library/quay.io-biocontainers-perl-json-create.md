---
layout: container
name:  "quay.io/biocontainers/perl-json-create"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-json-create/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-json-create/container.yaml"
updated_at: "2023-07-24 04:52:13.616210"
latest: "0.35--pl5321h031d066_2"
container_url: "https://biocontainers.pro/tools/perl-json-create"
aliases:
 - "validjson"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.35--pl5321hec16e2b_1"
 - "0.35--pl5321h031d066_2"
description: "shpc-registry automated BioContainers addition for perl-json-create"
config: {"url": "https://biocontainers.pro/tools/perl-json-create", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-json-create", "latest": {"0.35--pl5321h031d066_2": "sha256:847328562def0f87ddcc3cb63fd3b86ec5c7ec86882787f3c3ff3c487807857f"}, "tags": {"0.35--pl5321hec16e2b_1": "sha256:e8532e8a7283032edad5d186dafc7d5b7797e22eb1d11981b0ec438db17909a4", "0.35--pl5321h031d066_2": "sha256:847328562def0f87ddcc3cb63fd3b86ec5c7ec86882787f3c3ff3c487807857f"}, "docker": "quay.io/biocontainers/perl-json-create", "aliases": {"validjson": "/usr/local/bin/validjson", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-json-create.
shpc-registry automated BioContainers addition for perl-json-create
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-json-create
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-json-create:0.35--pl5321h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-json-create/0.35--pl5321h031d066_2
$ module help quay.io/biocontainers/perl-json-create/0.35--pl5321h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-json-create-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-create-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-create-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-json-create-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-json-create-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-json-create-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### validjson

```bash
$ singularity exec <container> /usr/local/bin/validjson
$ podman run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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