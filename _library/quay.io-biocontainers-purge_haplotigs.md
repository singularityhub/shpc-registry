---
layout: container
name:  "quay.io/biocontainers/purge_haplotigs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/purge_haplotigs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/purge_haplotigs/container.yaml"
updated_at: "2023-09-07 02:30:31.003473"
latest: "1.1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/purge_haplotigs"
aliases:
 - "purge_haplotigs"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
versions:
 - "1.1.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for purge_haplotigs"
config: {"url": "https://biocontainers.pro/tools/purge_haplotigs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for purge_haplotigs", "latest": {"1.1.2--hdfd78af_0": "sha256:1e3e70e85ecaecc1f9272670a1530182f5a31eef556d793a9c0f43409bede2e0"}, "tags": {"1.1.2--hdfd78af_0": "sha256:1e3e70e85ecaecc1f9272670a1530182f5a31eef556d793a9c0f43409bede2e0"}, "docker": "quay.io/biocontainers/purge_haplotigs", "aliases": {"purge_haplotigs": "/usr/local/bin/purge_haplotigs", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/purge_haplotigs.
shpc-registry automated BioContainers addition for purge_haplotigs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/purge_haplotigs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/purge_haplotigs:1.1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/purge_haplotigs/1.1.2--hdfd78af_0
$ module help quay.io/biocontainers/purge_haplotigs/1.1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### purge_haplotigs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### purge_haplotigs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### purge_haplotigs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### purge_haplotigs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### purge_haplotigs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### purge_haplotigs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### purge_haplotigs

```bash
$ singularity exec <container> /usr/local/bin/purge_haplotigs
$ podman run --it --rm --entrypoint /usr/local/bin/purge_haplotigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/purge_haplotigs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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