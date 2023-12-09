---
layout: container
name:  "quay.io/biocontainers/rnabridge-align"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnabridge-align/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnabridge-align/container.yaml"
updated_at: "2023-12-09 02:47:35.301115"
latest: "1.0.1--h5642b88_6"
container_url: "https://biocontainers.pro/tools/rnabridge-align"
aliases:
 - "rnabridge-align"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.1--hefd527f_4"
 - "1.0.1--h66ab1b6_5"
 - "1.0.1--h5642b88_6"
description: "shpc-registry automated BioContainers addition for rnabridge-align"
config: {"url": "https://biocontainers.pro/tools/rnabridge-align", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnabridge-align", "latest": {"1.0.1--h5642b88_6": "sha256:86b134e7a537141451c8f71f845ebbfeca94ff165be253351a64380f88c4c7e9"}, "tags": {"1.0.1--hefd527f_4": "sha256:a0ec6458724051da16962849e49ece50527f373c78978481d570157f5e8ac9f5", "1.0.1--h66ab1b6_5": "sha256:fc41f70d61a2983354720e352ac57dfa8c1eee87a72ea9b0e8cc51728cf6a4d8", "1.0.1--h5642b88_6": "sha256:86b134e7a537141451c8f71f845ebbfeca94ff165be253351a64380f88c4c7e9"}, "docker": "quay.io/biocontainers/rnabridge-align", "aliases": {"rnabridge-align": "/usr/local/bin/rnabridge-align", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnabridge-align.
shpc-registry automated BioContainers addition for rnabridge-align
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnabridge-align
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnabridge-align:1.0.1--h5642b88_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnabridge-align/1.0.1--h5642b88_6
$ module help quay.io/biocontainers/rnabridge-align/1.0.1--h5642b88_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnabridge-align-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnabridge-align-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnabridge-align-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnabridge-align-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnabridge-align-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnabridge-align-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rnabridge-align

```bash
$ singularity exec <container> /usr/local/bin/rnabridge-align
$ podman run --it --rm --entrypoint /usr/local/bin/rnabridge-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnabridge-align   -v ${PWD} -w ${PWD} <container> -c " $@"
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