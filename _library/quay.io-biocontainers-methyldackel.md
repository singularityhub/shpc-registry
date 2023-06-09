---
layout: container
name:  "quay.io/biocontainers/methyldackel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/methyldackel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/methyldackel/container.yaml"
updated_at: "2023-06-09 03:23:57.176286"
latest: "0.6.1--hc88714e_5"
container_url: "https://biocontainers.pro/tools/methyldackel"
aliases:
 - "MethylDackel"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.6.1--hb0d9459_4"
 - "0.6.1--hc88714e_5"
description: "shpc-registry automated BioContainers addition for methyldackel"
config: {"url": "https://biocontainers.pro/tools/methyldackel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for methyldackel", "latest": {"0.6.1--hc88714e_5": "sha256:4a3fcad9ffe74bff2689c8e43c05f1c15424f8ed099772cc7f1deff9330546fa"}, "tags": {"0.6.1--hb0d9459_4": "sha256:35881d0588da6d8f54dd397bd02318870467c5a07dacddd1bba019020eb1b652", "0.6.1--hc88714e_5": "sha256:4a3fcad9ffe74bff2689c8e43c05f1c15424f8ed099772cc7f1deff9330546fa"}, "docker": "quay.io/biocontainers/methyldackel", "aliases": {"MethylDackel": "/usr/local/bin/MethylDackel", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/methyldackel.
shpc-registry automated BioContainers addition for methyldackel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/methyldackel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/methyldackel:0.6.1--hc88714e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/methyldackel/0.6.1--hc88714e_5
$ module help quay.io/biocontainers/methyldackel/0.6.1--hc88714e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### methyldackel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### methyldackel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### methyldackel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### methyldackel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### methyldackel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### methyldackel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MethylDackel

```bash
$ singularity exec <container> /usr/local/bin/MethylDackel
$ podman run --it --rm --entrypoint /usr/local/bin/MethylDackel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MethylDackel   -v ${PWD} -w ${PWD} <container> -c " $@"
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