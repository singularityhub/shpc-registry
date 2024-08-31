---
layout: container
name:  "quay.io/biocontainers/psiclass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psiclass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psiclass/container.yaml"
updated_at: "2024-08-31 02:55:05.200192"
latest: "1.0.3--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/psiclass"
aliases:
 - "add-genename"
 - "classes"
 - "combine-subexons"
 - "junc"
 - "psiclass"
 - "subexon-info"
 - "trust-splice"
 - "vote-transcripts"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.3--h87f3376_0"
 - "1.0.3--h87f3376_1"
 - "1.0.3--hdbdd923_2"
 - "1.0.3--hdbdd923_3"
 - "1.0.3--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for psiclass"
config: {"url": "https://biocontainers.pro/tools/psiclass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for psiclass", "latest": {"1.0.3--hdbdd923_4": "sha256:4ba63223a2f0aed538aacca84b9ca74489bb6699637895cbff854a431808b836"}, "tags": {"1.0.3--h87f3376_0": "sha256:1b62a8b80e084a6b6aa11f51c5b578aa69398c6ada84e0dd13e8dd85d9a2fda2", "1.0.3--h87f3376_1": "sha256:964cd6947a5923c5c2d66b6bb28c988d97d6db0dd3fa7eb5225888a80d67ac3e", "1.0.3--hdbdd923_2": "sha256:5659e83ade16829081529f1a05274c98f41206bd407dfc8a52de6a8eacf7f950", "1.0.3--hdbdd923_3": "sha256:89de4bb696ecf98f9aa1cbfc76fc4f07ceae5c3563a5eebd32f6e8689c55cdcf", "1.0.3--hdbdd923_4": "sha256:4ba63223a2f0aed538aacca84b9ca74489bb6699637895cbff854a431808b836"}, "docker": "quay.io/biocontainers/psiclass", "aliases": {"add-genename": "/usr/local/bin/add-genename", "classes": "/usr/local/bin/classes", "combine-subexons": "/usr/local/bin/combine-subexons", "junc": "/usr/local/bin/junc", "psiclass": "/usr/local/bin/psiclass", "subexon-info": "/usr/local/bin/subexon-info", "trust-splice": "/usr/local/bin/trust-splice", "vote-transcripts": "/usr/local/bin/vote-transcripts", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psiclass.
shpc-registry automated BioContainers addition for psiclass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psiclass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psiclass:1.0.3--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psiclass/1.0.3--hdbdd923_4
$ module help quay.io/biocontainers/psiclass/1.0.3--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psiclass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psiclass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psiclass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psiclass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psiclass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psiclass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add-genename

```bash
$ singularity exec <container> /usr/local/bin/add-genename
$ podman run --it --rm --entrypoint /usr/local/bin/add-genename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add-genename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classes

```bash
$ singularity exec <container> /usr/local/bin/classes
$ podman run --it --rm --entrypoint /usr/local/bin/classes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine-subexons

```bash
$ singularity exec <container> /usr/local/bin/combine-subexons
$ podman run --it --rm --entrypoint /usr/local/bin/combine-subexons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine-subexons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junc

```bash
$ singularity exec <container> /usr/local/bin/junc
$ podman run --it --rm --entrypoint /usr/local/bin/junc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psiclass

```bash
$ singularity exec <container> /usr/local/bin/psiclass
$ podman run --it --rm --entrypoint /usr/local/bin/psiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subexon-info

```bash
$ singularity exec <container> /usr/local/bin/subexon-info
$ podman run --it --rm --entrypoint /usr/local/bin/subexon-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subexon-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust-splice

```bash
$ singularity exec <container> /usr/local/bin/trust-splice
$ podman run --it --rm --entrypoint /usr/local/bin/trust-splice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust-splice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vote-transcripts

```bash
$ singularity exec <container> /usr/local/bin/vote-transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/vote-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vote-transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
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