---
layout: container
name:  "quay.io/biocontainers/umis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/umis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/umis/container.yaml"
updated_at: "2025-05-14 03:53:08.538850"
latest: "1.0.9--py311haab0aaa_4"
container_url: "https://biocontainers.pro/tools/umis"

versions:
 - "1.0.7--py27h516909a_0"
 - "1.0.9--py27h9801fc8_0"
 - "1.0.9--py39hf95cd2a_2"
 - "1.0.9--py39hff71179_3"
 - "1.0.9--py311haab0aaa_4"
description: "shpc-registry automated BioContainers addition for umis"
config: {"url": "https://biocontainers.pro/tools/umis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for umis", "latest": {"1.0.9--py311haab0aaa_4": "sha256:bba7c5f6130b6c460fb3968d4a010644be6ef32def241338f44ef882b1162b61"}, "tags": {"1.0.7--py27h516909a_0": "sha256:c13a0a65712c77f17e35298202ee1ea2bd2bd4c29ca47e63b82b136cfbf638d6", "1.0.9--py27h9801fc8_0": "sha256:c7aa72b01797584444066c2bf8852031b6f8dd58aeedf7f7bad3ede7e4d7e06f", "1.0.9--py39hf95cd2a_2": "sha256:cc43549bd917e392d482fe83279f8efe4728343a1fc11e1d54d2027cf27583b8", "1.0.9--py39hff71179_3": "sha256:c5acf9313fb1c5800fc7ce07b4aad2c915db14caccf6e90d34fb1f89bdb4ba88", "1.0.9--py311haab0aaa_4": "sha256:bba7c5f6130b6c460fb3968d4a010644be6ef32def241338f44ef882b1162b61"}, "docker": "quay.io/biocontainers/umis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/umis.
shpc-registry automated BioContainers addition for umis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/umis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/umis:1.0.9--py311haab0aaa_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/umis/1.0.9--py311haab0aaa_4
$ module help quay.io/biocontainers/umis/1.0.9--py311haab0aaa_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### umis

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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