---
layout: container
name:  "quay.io/biocontainers/bamcmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamcmp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamcmp/container.yaml"
updated_at: "2024-03-02 02:42:53.141000"
latest: "2.2--h28e74a2_2"
container_url: "https://biocontainers.pro/tools/bamcmp"
aliases:
 - "bamcmp"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.2--h28e74a2_2"
 - "2.2"
description: "shpc-registry automated BioContainers addition for bamcmp"
config: {"url": "https://biocontainers.pro/tools/bamcmp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamcmp", "latest": {"2.2--h28e74a2_2": "sha256:b897fa18e68b331cf9fe6c1128e5fd8ccf51fc3d3d545608ee43f412f77ebbce"}, "tags": {"2.2--h28e74a2_2": "sha256:b897fa18e68b331cf9fe6c1128e5fd8ccf51fc3d3d545608ee43f412f77ebbce", "2.2": "sha256:851ad4da01db7dfba50e4d01774f9ccf3660209d24e2ef5a1886ea0aee65f950"}, "docker": "quay.io/biocontainers/bamcmp", "aliases": {"bamcmp": "/usr/local/bin/bamcmp", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamcmp.
shpc-registry automated BioContainers addition for bamcmp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamcmp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamcmp:2.2--h28e74a2_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamcmp/2.2--h28e74a2_2
$ module help quay.io/biocontainers/bamcmp/2.2--h28e74a2_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamcmp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamcmp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamcmp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamcmp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamcmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamcmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamcmp

```bash
$ singularity exec <container> /usr/local/bin/bamcmp
$ podman run --it --rm --entrypoint /usr/local/bin/bamcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
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