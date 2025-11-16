---
layout: container
name:  "quay.io/biocontainers/kmer-db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmer-db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmer-db/container.yaml"
updated_at: "2025-11-16 04:04:47.133525"
latest: "2.3.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/kmer-db"
aliases:
 - "kmer-db"
versions:
 - "1.9.4--hd03093a_1"
 - "1.11.1--hd03093a_0"
 - "1.11.1--hdcf5f25_2"
 - "2.2.2--h9ee0642_0"
 - "2.2.5--h9ee0642_0"
 - "2.3.1--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for kmer-db"
config: {"url": "https://biocontainers.pro/tools/kmer-db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmer-db", "latest": {"2.3.1--h9ee0642_0": "sha256:e2829328bf369776143b22a051330bf7a182cbe8fafb6549f8fa98f6ac6194bb"}, "tags": {"1.9.4--hd03093a_1": "sha256:88e69e42a7990d16651420b61616795fa82e01f1947ddceb9765756384db3346", "1.11.1--hd03093a_0": "sha256:aea5183fa63441fcf90e265c58bdf11156d429bf416e7ad15781fce078d79774", "1.11.1--hdcf5f25_2": "sha256:dd7887758d4459f5390a978acb3d2be9aee1be106f23a95b6a2cbfa7cbfc0031", "2.2.2--h9ee0642_0": "sha256:d9b7bec14f9d5ad78179e80beff399691d7fceb080dc93e9e0249cc0deab11c9", "2.2.5--h9ee0642_0": "sha256:11871e68b8dc308b39ae14e8fd983efd861c815e0bbc16d55087913e64179a94", "2.3.1--h9ee0642_0": "sha256:e2829328bf369776143b22a051330bf7a182cbe8fafb6549f8fa98f6ac6194bb"}, "docker": "quay.io/biocontainers/kmer-db", "aliases": {"kmer-db": "/usr/local/bin/kmer-db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmer-db.
shpc-registry automated BioContainers addition for kmer-db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmer-db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmer-db:2.3.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmer-db/2.3.1--h9ee0642_0
$ module help quay.io/biocontainers/kmer-db/2.3.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmer-db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmer-db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmer-db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmer-db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmer-db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmer-db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmer-db

```bash
$ singularity exec <container> /usr/local/bin/kmer-db
$ podman run --it --rm --entrypoint /usr/local/bin/kmer-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer-db   -v ${PWD} -w ${PWD} <container> -c " $@"
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