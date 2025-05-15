---
layout: container
name:  "quay.io/biocontainers/fastq-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-tools/container.yaml"
updated_at: "2025-05-15 03:18:17.378292"
latest: "0.8--hed695b0_3"
container_url: "https://biocontainers.pro/tools/fastq-tools"
aliases:
 - "fastq-grep"
 - "fastq-kmers"
 - "fastq-match"
 - "fastq-qscale"
 - "fastq-qual"
 - "fastq-qualadj"
 - "fastq-sample"
 - "fastq-sort"
 - "fastq-uniq"
versions:
 - "0.8.3--hbd632db_2"
 - "0.8--hed695b0_3"
 - "0.8.3--h6ead514_4"
 - "0.8.3--h1104d80_5"
description: "shpc-registry automated BioContainers addition for fastq-tools"
config: {"url": "https://biocontainers.pro/tools/fastq-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-tools", "latest": {"0.8--hed695b0_3": "sha256:00c2f42213cbc579a6807d8ec25f55e5d28298257a734124f22f711310f97431"}, "tags": {"0.8.3--hbd632db_2": "sha256:00762c30c401e8ed388a09f4b557f8d035f6d138ce0524e3beaa9513d14bcb59", "0.8--hed695b0_3": "sha256:00c2f42213cbc579a6807d8ec25f55e5d28298257a734124f22f711310f97431", "0.8.3--h6ead514_4": "sha256:3d1236810e70c0f224b036e89915df6c8ff4d53da9174844efa4abb6b59febbe", "0.8.3--h1104d80_5": "sha256:725266e6754331326f75a0cb83f9e31311a74537e7b1fac1958f78669d910a44"}, "docker": "quay.io/biocontainers/fastq-tools", "aliases": {"fastq-grep": "/usr/local/bin/fastq-grep", "fastq-kmers": "/usr/local/bin/fastq-kmers", "fastq-match": "/usr/local/bin/fastq-match", "fastq-qscale": "/usr/local/bin/fastq-qscale", "fastq-qual": "/usr/local/bin/fastq-qual", "fastq-qualadj": "/usr/local/bin/fastq-qualadj", "fastq-sample": "/usr/local/bin/fastq-sample", "fastq-sort": "/usr/local/bin/fastq-sort", "fastq-uniq": "/usr/local/bin/fastq-uniq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-tools.
shpc-registry automated BioContainers addition for fastq-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-tools:0.8--hed695b0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-tools/0.8--hed695b0_3
$ module help quay.io/biocontainers/fastq-tools/0.8--hed695b0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-grep

```bash
$ singularity exec <container> /usr/local/bin/fastq-grep
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-kmers

```bash
$ singularity exec <container> /usr/local/bin/fastq-kmers
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-match

```bash
$ singularity exec <container> /usr/local/bin/fastq-match
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qscale

```bash
$ singularity exec <container> /usr/local/bin/fastq-qscale
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qscale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qscale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qual

```bash
$ singularity exec <container> /usr/local/bin/fastq-qual
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qualadj

```bash
$ singularity exec <container> /usr/local/bin/fastq-qualadj
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qualadj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qualadj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-sample

```bash
$ singularity exec <container> /usr/local/bin/fastq-sample
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-sort

```bash
$ singularity exec <container> /usr/local/bin/fastq-sort
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-uniq

```bash
$ singularity exec <container> /usr/local/bin/fastq-uniq
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
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