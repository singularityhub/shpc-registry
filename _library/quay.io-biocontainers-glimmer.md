---
layout: container
name:  "quay.io/biocontainers/glimmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/glimmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/glimmer/container.yaml"
updated_at: "2023-09-11 02:41:37.975794"
latest: "3.02--h87f3376_6"
container_url: "https://biocontainers.pro/tools/glimmer"
aliases:
 - "anomaly"
 - "build-fixed"
 - "build-icm"
 - "entropy-profile"
 - "entropy-score"
 - "extract"
 - "g3-from-scratch.csh"
 - "g3-from-training.csh"
 - "g3-iterated.csh"
 - "get-motif-counts.awk"
 - "glim-diff.awk"
 - "glimmer3"
 - "long-orfs"
 - "match-list-col.awk"
 - "multi-extract"
 - "not-acgt.awk"
 - "score-fixed"
 - "start-codon-distrib"
 - "uncovered"
 - "upstream-coords.awk"
 - "window-acgt"
 - "test"
versions:
 - "3.02--h87f3376_6"
description: "shpc-registry automated BioContainers addition for glimmer"
config: {"url": "https://biocontainers.pro/tools/glimmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for glimmer", "latest": {"3.02--h87f3376_6": "sha256:f86bef3b96dba3728d8dc45d81825ee2c81ceaaa710a2b513365452814f3b308"}, "tags": {"3.02--h87f3376_6": "sha256:f86bef3b96dba3728d8dc45d81825ee2c81ceaaa710a2b513365452814f3b308"}, "docker": "quay.io/biocontainers/glimmer", "aliases": {"anomaly": "/usr/local/bin/anomaly", "build-fixed": "/usr/local/bin/build-fixed", "build-icm": "/usr/local/bin/build-icm", "entropy-profile": "/usr/local/bin/entropy-profile", "entropy-score": "/usr/local/bin/entropy-score", "extract": "/usr/local/bin/extract", "g3-from-scratch.csh": "/usr/local/bin/g3-from-scratch.csh", "g3-from-training.csh": "/usr/local/bin/g3-from-training.csh", "g3-iterated.csh": "/usr/local/bin/g3-iterated.csh", "get-motif-counts.awk": "/usr/local/bin/get-motif-counts.awk", "glim-diff.awk": "/usr/local/bin/glim-diff.awk", "glimmer3": "/usr/local/bin/glimmer3", "long-orfs": "/usr/local/bin/long-orfs", "match-list-col.awk": "/usr/local/bin/match-list-col.awk", "multi-extract": "/usr/local/bin/multi-extract", "not-acgt.awk": "/usr/local/bin/not-acgt.awk", "score-fixed": "/usr/local/bin/score-fixed", "start-codon-distrib": "/usr/local/bin/start-codon-distrib", "uncovered": "/usr/local/bin/uncovered", "upstream-coords.awk": "/usr/local/bin/upstream-coords.awk", "window-acgt": "/usr/local/bin/window-acgt", "test": "/usr/local/bin/test"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/glimmer.
shpc-registry automated BioContainers addition for glimmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/glimmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/glimmer:3.02--h87f3376_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/glimmer/3.02--h87f3376_6
$ module help quay.io/biocontainers/glimmer/3.02--h87f3376_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### glimmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### glimmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### glimmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### glimmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### glimmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### glimmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anomaly

```bash
$ singularity exec <container> /usr/local/bin/anomaly
$ podman run --it --rm --entrypoint /usr/local/bin/anomaly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anomaly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build-fixed

```bash
$ singularity exec <container> /usr/local/bin/build-fixed
$ podman run --it --rm --entrypoint /usr/local/bin/build-fixed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build-fixed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build-icm

```bash
$ singularity exec <container> /usr/local/bin/build-icm
$ podman run --it --rm --entrypoint /usr/local/bin/build-icm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build-icm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entropy-profile

```bash
$ singularity exec <container> /usr/local/bin/entropy-profile
$ podman run --it --rm --entrypoint /usr/local/bin/entropy-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entropy-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entropy-score

```bash
$ singularity exec <container> /usr/local/bin/entropy-score
$ podman run --it --rm --entrypoint /usr/local/bin/entropy-score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entropy-score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract

```bash
$ singularity exec <container> /usr/local/bin/extract
$ podman run --it --rm --entrypoint /usr/local/bin/extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g3-from-scratch.csh

```bash
$ singularity exec <container> /usr/local/bin/g3-from-scratch.csh
$ podman run --it --rm --entrypoint /usr/local/bin/g3-from-scratch.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g3-from-scratch.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g3-from-training.csh

```bash
$ singularity exec <container> /usr/local/bin/g3-from-training.csh
$ podman run --it --rm --entrypoint /usr/local/bin/g3-from-training.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g3-from-training.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g3-iterated.csh

```bash
$ singularity exec <container> /usr/local/bin/g3-iterated.csh
$ podman run --it --rm --entrypoint /usr/local/bin/g3-iterated.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g3-iterated.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-motif-counts.awk

```bash
$ singularity exec <container> /usr/local/bin/get-motif-counts.awk
$ podman run --it --rm --entrypoint /usr/local/bin/get-motif-counts.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-motif-counts.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glim-diff.awk

```bash
$ singularity exec <container> /usr/local/bin/glim-diff.awk
$ podman run --it --rm --entrypoint /usr/local/bin/glim-diff.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glim-diff.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glimmer3

```bash
$ singularity exec <container> /usr/local/bin/glimmer3
$ podman run --it --rm --entrypoint /usr/local/bin/glimmer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glimmer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long-orfs

```bash
$ singularity exec <container> /usr/local/bin/long-orfs
$ podman run --it --rm --entrypoint /usr/local/bin/long-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long-orfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### match-list-col.awk

```bash
$ singularity exec <container> /usr/local/bin/match-list-col.awk
$ podman run --it --rm --entrypoint /usr/local/bin/match-list-col.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/match-list-col.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multi-extract

```bash
$ singularity exec <container> /usr/local/bin/multi-extract
$ podman run --it --rm --entrypoint /usr/local/bin/multi-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multi-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### not-acgt.awk

```bash
$ singularity exec <container> /usr/local/bin/not-acgt.awk
$ podman run --it --rm --entrypoint /usr/local/bin/not-acgt.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/not-acgt.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### score-fixed

```bash
$ singularity exec <container> /usr/local/bin/score-fixed
$ podman run --it --rm --entrypoint /usr/local/bin/score-fixed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/score-fixed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### start-codon-distrib

```bash
$ singularity exec <container> /usr/local/bin/start-codon-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/start-codon-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/start-codon-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncovered

```bash
$ singularity exec <container> /usr/local/bin/uncovered
$ podman run --it --rm --entrypoint /usr/local/bin/uncovered   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncovered   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upstream-coords.awk

```bash
$ singularity exec <container> /usr/local/bin/upstream-coords.awk
$ podman run --it --rm --entrypoint /usr/local/bin/upstream-coords.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upstream-coords.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### window-acgt

```bash
$ singularity exec <container> /usr/local/bin/window-acgt
$ podman run --it --rm --entrypoint /usr/local/bin/window-acgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/window-acgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test

```bash
$ singularity exec <container> /usr/local/bin/test
$ podman run --it --rm --entrypoint /usr/local/bin/test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test   -v ${PWD} -w ${PWD} <container> -c " $@"
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