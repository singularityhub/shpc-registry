---
layout: container
name:  "quay.io/biocontainers/quorum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quorum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quorum/container.yaml"
updated_at: "2024-03-11 03:22:52.685073"
latest: "1.1.1--h7d875b9_4"
container_url: "https://biocontainers.pro/tools/quorum"
aliases:
 - "merge_mate_pairs"
 - "quorum"
 - "quorum_create_database"
 - "quorum_error_correct_reads"
 - "split_mate_pairs"
 - "jellyfish"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "1.1.1--h7d875b9_4"
description: "shpc-registry automated BioContainers addition for quorum"
config: {"url": "https://biocontainers.pro/tools/quorum", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quorum", "latest": {"1.1.1--h7d875b9_4": "sha256:e1aad85d94073c2fb1dbf04b3def06a66ab075b14796500a95349f163be03d10"}, "tags": {"1.1.1--h7d875b9_4": "sha256:e1aad85d94073c2fb1dbf04b3def06a66ab075b14796500a95349f163be03d10"}, "docker": "quay.io/biocontainers/quorum", "aliases": {"merge_mate_pairs": "/usr/local/bin/merge_mate_pairs", "quorum": "/usr/local/bin/quorum", "quorum_create_database": "/usr/local/bin/quorum_create_database", "quorum_error_correct_reads": "/usr/local/bin/quorum_error_correct_reads", "split_mate_pairs": "/usr/local/bin/split_mate_pairs", "jellyfish": "/usr/local/bin/jellyfish", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quorum.
shpc-registry automated BioContainers addition for quorum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quorum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quorum:1.1.1--h7d875b9_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quorum/1.1.1--h7d875b9_4
$ module help quay.io/biocontainers/quorum/1.1.1--h7d875b9_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quorum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quorum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quorum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quorum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quorum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quorum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### merge_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/merge_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum

```bash
$ singularity exec <container> /usr/local/bin/quorum
$ podman run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_create_database

```bash
$ singularity exec <container> /usr/local/bin/quorum_create_database
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_error_correct_reads

```bash
$ singularity exec <container> /usr/local/bin/quorum_error_correct_reads
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/split_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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