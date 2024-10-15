---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.sc.sgd.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.sc.sgd.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.sc.sgd.db/container.yaml"
updated_at: "2024-10-15 03:22:12.499612"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.sc.sgd.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.sc.sgd.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.sc.sgd.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.sc.sgd.db", "latest": {"3.18.0--r43hdfd78af_0": "sha256:a600fa74f7586555f2de893efb3da2c8fedf23dc3db5f9f473e66fb9bfd7510d"}, "tags": {"3.8.2--r36_1": "sha256:71198debe672e2dbbfc1dcef422d91c13cc9062ba076242802c56edcfc615d23", "3.16.0--r42hdfd78af_0": "sha256:4bb073cb4af5c63ab83ab285f09f80c2cd01ddcd4d18e8eb0a76758fd314225e", "3.14.0--r41hdfd78af_1": "sha256:dcc1535ab66888cd7bbff2b59f4c918899d2c89b9ea43fc64af4c3f22d950999", "3.13.0--r41hdfd78af_0": "sha256:5273de7c4fa37ec1b5c0a41d39b954ef8107402b1b8d4d9ef9e169b412702515", "3.12.0--r40hdfd78af_1": "sha256:a8df1fcf396ed2529df32620ab43b04eb7e6cd57345321ce16f633de58a9e973", "3.11.1--r40_0": "sha256:751afc9a73e550c266296d3c8b16b224539a4b5cb6b6798242c38da94c1a663d", "3.17.0--r43hdfd78af_0": "sha256:28539ccdb7d26a79697e54766a1d52316145a370461cdddb4f227352ab0d1641", "3.18.0--r43hdfd78af_0": "sha256:a600fa74f7586555f2de893efb3da2c8fedf23dc3db5f9f473e66fb9bfd7510d"}, "docker": "quay.io/biocontainers/bioconductor-org.sc.sgd.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.sc.sgd.db.
shpc-registry automated BioContainers addition for bioconductor-org.sc.sgd.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.sc.sgd.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.sc.sgd.db:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.sc.sgd.db/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.sc.sgd.db/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.sc.sgd.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.sc.sgd.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.sc.sgd.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.sc.sgd.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.sc.sgd.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.sc.sgd.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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