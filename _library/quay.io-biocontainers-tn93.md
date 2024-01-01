---
layout: container
name:  "quay.io/biocontainers/tn93"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tn93/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tn93/container.yaml"
updated_at: "2024-01-01 03:26:03.939944"
latest: "1.0.12--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/tn93"
aliases:
 - "ShortestPathTN93"
 - "fasta_diff"
 - "nucfreqsfasta"
 - "readreduce"
 - "selectreads"
 - "seqcoverage"
 - "seqdiff"
 - "tn93"
 - "tn93-cluster"
versions:
 - "1.0.9--h87f3376_0"
 - "1.0.9--hdbdd923_2"
 - "1.0.12--hdbdd923_0"
description: "shpc-registry automated BioContainers addition for tn93"
config: {"url": "https://biocontainers.pro/tools/tn93", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tn93", "latest": {"1.0.12--hdbdd923_0": "sha256:83bf531c82c6a87647085f2c222b0452ab3ea0de71e0fff9cd127580249706d9"}, "tags": {"1.0.9--h87f3376_0": "sha256:424dbe9f31de15de37e3b5b91daa8770450eae97c241fc9a1197d4b410f7b9e9", "1.0.9--hdbdd923_2": "sha256:a975935402c6a7a1d51e58df242f8aa03adc864ba8b55db5e37d7de0dc339217", "1.0.12--hdbdd923_0": "sha256:83bf531c82c6a87647085f2c222b0452ab3ea0de71e0fff9cd127580249706d9"}, "docker": "quay.io/biocontainers/tn93", "aliases": {"ShortestPathTN93": "/usr/local/bin/ShortestPathTN93", "fasta_diff": "/usr/local/bin/fasta_diff", "nucfreqsfasta": "/usr/local/bin/nucfreqsfasta", "readreduce": "/usr/local/bin/readreduce", "selectreads": "/usr/local/bin/selectreads", "seqcoverage": "/usr/local/bin/seqcoverage", "seqdiff": "/usr/local/bin/seqdiff", "tn93": "/usr/local/bin/tn93", "tn93-cluster": "/usr/local/bin/tn93-cluster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tn93.
shpc-registry automated BioContainers addition for tn93
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tn93
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tn93:1.0.12--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tn93/1.0.12--hdbdd923_0
$ module help quay.io/biocontainers/tn93/1.0.12--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tn93-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tn93-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tn93-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tn93-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tn93-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tn93-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ShortestPathTN93

```bash
$ singularity exec <container> /usr/local/bin/ShortestPathTN93
$ podman run --it --rm --entrypoint /usr/local/bin/ShortestPathTN93   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ShortestPathTN93   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_diff

```bash
$ singularity exec <container> /usr/local/bin/fasta_diff
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucfreqsfasta

```bash
$ singularity exec <container> /usr/local/bin/nucfreqsfasta
$ podman run --it --rm --entrypoint /usr/local/bin/nucfreqsfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucfreqsfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readreduce

```bash
$ singularity exec <container> /usr/local/bin/readreduce
$ podman run --it --rm --entrypoint /usr/local/bin/readreduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readreduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selectreads

```bash
$ singularity exec <container> /usr/local/bin/selectreads
$ podman run --it --rm --entrypoint /usr/local/bin/selectreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selectreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqcoverage

```bash
$ singularity exec <container> /usr/local/bin/seqcoverage
$ podman run --it --rm --entrypoint /usr/local/bin/seqcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdiff

```bash
$ singularity exec <container> /usr/local/bin/seqdiff
$ podman run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tn93

```bash
$ singularity exec <container> /usr/local/bin/tn93
$ podman run --it --rm --entrypoint /usr/local/bin/tn93   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tn93   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tn93-cluster

```bash
$ singularity exec <container> /usr/local/bin/tn93-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/tn93-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tn93-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
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