---
layout: container
name:  "quay.io/biocontainers/conga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/conga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/conga/container.yaml"
updated_at: "2026-06-18 07:31:26.870628"
latest: "1.1--h3050eb1_0"
container_url: "https://biocontainers.pro/tools/conga"
aliases:
 - "conga"
 - "ref-cache"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.1--h3050eb1_0"
description: "singularity registry hpc automated addition for conga"
config: {"url": "https://biocontainers.pro/tools/conga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for conga", "latest": {"1.1--h3050eb1_0": "sha256:a7798ffdffecf28a77600bef57465626694068f4fafd141cbae08e7dd6967ed3"}, "tags": {"1.1--h3050eb1_0": "sha256:a7798ffdffecf28a77600bef57465626694068f4fafd141cbae08e7dd6967ed3"}, "docker": "quay.io/biocontainers/conga", "aliases": {"conga": "/usr/local/bin/conga", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/conga.
singularity registry hpc automated addition for conga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/conga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/conga:1.1--h3050eb1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/conga/1.1--h3050eb1_0
$ module help quay.io/biocontainers/conga/1.1--h3050eb1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### conga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### conga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### conga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### conga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### conga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### conga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### conga

```bash
$ singularity exec <container> /usr/local/bin/conga
$ podman run --it --rm --entrypoint /usr/local/bin/conga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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