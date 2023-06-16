---
layout: container
name:  "quay.io/biocontainers/cancerit-allelecount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cancerit-allelecount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cancerit-allelecount/container.yaml"
updated_at: "2023-06-16 03:21:46.551243"
latest: "4.3.0--h57116a3_5"
container_url: "https://biocontainers.pro/tools/cancerit-allelecount"
aliases:
 - "alleleCounter"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "4.3.0--ha8fb052_3"
 - "4.3.0--heecbde5_4"
 - "4.3.0--h57116a3_5"
description: "shpc-registry automated BioContainers addition for cancerit-allelecount"
config: {"url": "https://biocontainers.pro/tools/cancerit-allelecount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cancerit-allelecount", "latest": {"4.3.0--h57116a3_5": "sha256:46dd3679ae62a9476ab8dfa0f98fda00b8feb69dfc3cadad0e7e275ab976cfc8"}, "tags": {"4.3.0--ha8fb052_3": "sha256:0be75beaf4d37798e3a7f9f075e509baa6c2d4fa928778137b41f425c5000e54", "4.3.0--heecbde5_4": "sha256:3d106cd2d93b27003c220bdec1312ac55ceb58411fb460156e049f24366adf2f", "4.3.0--h57116a3_5": "sha256:46dd3679ae62a9476ab8dfa0f98fda00b8feb69dfc3cadad0e7e275ab976cfc8"}, "docker": "quay.io/biocontainers/cancerit-allelecount", "aliases": {"alleleCounter": "/usr/local/bin/alleleCounter", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cancerit-allelecount.
shpc-registry automated BioContainers addition for cancerit-allelecount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cancerit-allelecount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cancerit-allelecount:4.3.0--h57116a3_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cancerit-allelecount/4.3.0--h57116a3_5
$ module help quay.io/biocontainers/cancerit-allelecount/4.3.0--h57116a3_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cancerit-allelecount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cancerit-allelecount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cancerit-allelecount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cancerit-allelecount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cancerit-allelecount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cancerit-allelecount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alleleCounter

```bash
$ singularity exec <container> /usr/local/bin/alleleCounter
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
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