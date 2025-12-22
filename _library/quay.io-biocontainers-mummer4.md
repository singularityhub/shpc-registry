---
layout: container
name:  "quay.io/biocontainers/mummer4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mummer4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mummer4/container.yaml"
updated_at: "2025-12-22 05:12:53.528341"
latest: "4.0.1--pl5321h9948957_0"
container_url: "https://biocontainers.pro/tools/mummer4"
aliases:
 - "delta2vcf"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
 - "mummerplot"
 - "nucmer"
 - "promer"
 - "repeat-match"
 - "show-aligns"
versions:
 - "4.0.0rc1--pl5321h87f3376_3"
 - "4.0.0beta2--pl526he1b5a44_5"
 - "4.0.1--pl5321h9948957_0"
description: "shpc-registry automated BioContainers addition for mummer4"
config: {"url": "https://biocontainers.pro/tools/mummer4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mummer4", "latest": {"4.0.1--pl5321h9948957_0": "sha256:71cec8dd8e446a6174504ec55c90481a991815ac8cbda95c5cc1661e4bbfa382"}, "tags": {"4.0.0rc1--pl5321h87f3376_3": "sha256:e9b44d62ae397a36ea380cd83a86b701be2ad18907be207c552f7d8b07f6d7d1", "4.0.0beta2--pl526he1b5a44_5": "sha256:c7c9dae75dc77acf1852b6e29f1c10f502281e801f12035ec1ec924fd8596449", "4.0.1--pl5321h9948957_0": "sha256:71cec8dd8e446a6174504ec55c90481a991815ac8cbda95c5cc1661e4bbfa382"}, "docker": "quay.io/biocontainers/mummer4", "aliases": {"delta2vcf": "/usr/local/bin/delta2vcf", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer", "mummerplot": "/usr/local/bin/mummerplot", "nucmer": "/usr/local/bin/nucmer", "promer": "/usr/local/bin/promer", "repeat-match": "/usr/local/bin/repeat-match", "show-aligns": "/usr/local/bin/show-aligns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mummer4.
shpc-registry automated BioContainers addition for mummer4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mummer4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mummer4:4.0.1--pl5321h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mummer4/4.0.1--pl5321h9948957_0
$ module help quay.io/biocontainers/mummer4/4.0.1--pl5321h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mummer4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mummer4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mummer4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mummer4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mummer4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mummer4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delta2vcf

```bash
$ singularity exec <container> /usr/local/bin/delta2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummerplot

```bash
$ singularity exec <container> /usr/local/bin/mummerplot
$ podman run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummerplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucmer

```bash
$ singularity exec <container> /usr/local/bin/nucmer
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promer

```bash
$ singularity exec <container> /usr/local/bin/promer
$ podman run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repeat-match

```bash
$ singularity exec <container> /usr/local/bin/repeat-match
$ podman run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repeat-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### show-aligns

```bash
$ singularity exec <container> /usr/local/bin/show-aligns
$ podman run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/show-aligns   -v ${PWD} -w ${PWD} <container> -c " $@"
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