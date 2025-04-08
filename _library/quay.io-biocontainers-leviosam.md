---
layout: container
name:  "quay.io/biocontainers/leviosam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/leviosam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/leviosam/container.yaml"
updated_at: "2025-04-08 03:08:23.006430"
latest: "5.2.1--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/leviosam"
aliases:
 - "leviosam"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "5.2.1--h9f5acd7_1"
 - "5.2.1--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for leviosam"
config: {"url": "https://biocontainers.pro/tools/leviosam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for leviosam", "latest": {"5.2.1--h4ac6f70_2": "sha256:f9f3f90bae12be3834c416f18a1b6bc57e075104a39f36d645f3f86adcdd7890"}, "tags": {"5.2.1--h9f5acd7_1": "sha256:f9ce2891e676628c9c99c59abb272f644a5a337d1ff11dfa6a76702ccd0b2310", "5.2.1--h4ac6f70_2": "sha256:f9f3f90bae12be3834c416f18a1b6bc57e075104a39f36d645f3f86adcdd7890"}, "docker": "quay.io/biocontainers/leviosam", "aliases": {"leviosam": "/usr/local/bin/leviosam", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/leviosam.
shpc-registry automated BioContainers addition for leviosam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/leviosam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/leviosam:5.2.1--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/leviosam/5.2.1--h4ac6f70_2
$ module help quay.io/biocontainers/leviosam/5.2.1--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### leviosam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### leviosam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### leviosam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### leviosam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### leviosam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### leviosam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### leviosam

```bash
$ singularity exec <container> /usr/local/bin/leviosam
$ podman run --it --rm --entrypoint /usr/local/bin/leviosam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leviosam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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