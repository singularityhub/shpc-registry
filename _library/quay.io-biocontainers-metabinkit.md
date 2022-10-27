---
layout: container
name:  "quay.io/biocontainers/metabinkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabinkit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metabinkit/container.yaml"
updated_at: "2022-10-27 00:47:23.599716"
latest: "0.2.2--r41hbd632db_4"
container_url: "https://biocontainers.pro/tools/metabinkit"
aliases:
 - "metabin"
 - "metabinkit_blast"
 - "metabinkit_blastgendb"
 - "metabinkit_shared.sh"
 - "taxonkit"
 - "taxonkit_children.sh"
versions:
 - "0.2.2--r41hbd632db_4"
description: "shpc-registry automated BioContainers addition for metabinkit"
config: {"url": "https://biocontainers.pro/tools/metabinkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabinkit", "latest": {"0.2.2--r41hbd632db_4": "sha256:df0cb8a1995cb2badb2fcf5934bb0b6f5343c10cb167055b11230536204f3087"}, "tags": {"0.2.2--r41hbd632db_4": "sha256:df0cb8a1995cb2badb2fcf5934bb0b6f5343c10cb167055b11230536204f3087"}, "docker": "quay.io/biocontainers/metabinkit", "aliases": {"metabin": "/usr/local/bin/metabin", "metabinkit_blast": "/usr/local/bin/metabinkit_blast", "metabinkit_blastgendb": "/usr/local/bin/metabinkit_blastgendb", "metabinkit_shared.sh": "/usr/local/bin/metabinkit_shared.sh", "taxonkit": "/usr/local/bin/taxonkit", "taxonkit_children.sh": "/usr/local/bin/taxonkit_children.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabinkit.
shpc-registry automated BioContainers addition for metabinkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabinkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabinkit:0.2.2--r41hbd632db_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabinkit/0.2.2--r41hbd632db_4
$ module help quay.io/biocontainers/metabinkit/0.2.2--r41hbd632db_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabinkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabinkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabinkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabinkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabinkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabinkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metabin

```bash
$ singularity exec <container> /usr/local/bin/metabin
$ podman run --it --rm --entrypoint /usr/local/bin/metabin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_blast

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_blast
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_blastgendb

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_blastgendb
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_blastgendb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_blastgendb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_shared.sh

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_shared.sh
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_shared.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_shared.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit_children.sh

```bash
$ singularity exec <container> /usr/local/bin/taxonkit_children.sh
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit_children.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit_children.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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