---
layout: container
name:  "quay.io/biocontainers/metadmg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metadmg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metadmg/container.yaml"
updated_at: "2025-02-03 03:44:35.506703"
latest: "0.4--h6ba4bad_1"
container_url: "https://biocontainers.pro/tools/metadmg"
aliases:
 - "compressbam"
 - "metaDMG-cpp"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3--h86cbbb3_1"
 - "0.4--h8e173a3_0"
 - "0.4--h6ba4bad_1"
description: "singularity registry hpc automated addition for metadmg"
config: {"url": "https://biocontainers.pro/tools/metadmg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metadmg", "latest": {"0.4--h6ba4bad_1": "sha256:120431c5ec94f98b07811b7d4999a284753ca975f9f7be2bd237a4667ce43baa"}, "tags": {"0.3--h86cbbb3_1": "sha256:127245178807baf7a37280aeefeb74b485c5d6b7a4cbd87b7a50da11b3fdd7ac", "0.4--h8e173a3_0": "sha256:52b4d2986f78289978c53ded9e18c03038672f7064208645b62b244b619f3155", "0.4--h6ba4bad_1": "sha256:120431c5ec94f98b07811b7d4999a284753ca975f9f7be2bd237a4667ce43baa"}, "docker": "quay.io/biocontainers/metadmg", "aliases": {"compressbam": "/usr/local/bin/compressbam", "metaDMG-cpp": "/usr/local/bin/metaDMG-cpp", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metadmg.
singularity registry hpc automated addition for metadmg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metadmg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metadmg:0.4--h6ba4bad_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metadmg/0.4--h6ba4bad_1
$ module help quay.io/biocontainers/metadmg/0.4--h6ba4bad_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metadmg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metadmg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metadmg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metadmg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metadmg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metadmg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compressbam

```bash
$ singularity exec <container> /usr/local/bin/compressbam
$ podman run --it --rm --entrypoint /usr/local/bin/compressbam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compressbam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaDMG-cpp

```bash
$ singularity exec <container> /usr/local/bin/metaDMG-cpp
$ podman run --it --rm --entrypoint /usr/local/bin/metaDMG-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaDMG-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
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