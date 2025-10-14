---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.gg.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.gg.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.gg.eg.db/container.yaml"
updated_at: "2025-10-14 03:51:02.591846"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.gg.eg.db"
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
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.gg.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.gg.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.gg.eg.db", "latest": {"3.20.0--r44hdfd78af_0": "sha256:6f4c2f3ebb4040a072f43e7f5547964732e4c1de836cbca064597e2ed5185061"}, "tags": {"3.8.2--r36_1": "sha256:0fc75709ad35753c757c94948b0e8d1024ad8f66a5623ce093a6806802176bfe", "3.16.0--r42hdfd78af_0": "sha256:aedf14c2dcea2c1e4d867ebe16e2f64097e7c83dcf647159820c1c73ffcb6e2f", "3.14.0--r41hdfd78af_1": "sha256:7f5a7bbad66bc2b77b3d63779799a7e2c9b2e521bc630410a013e09a7c1024d3", "3.13.0--r41hdfd78af_0": "sha256:e9e90d225c4b4598f097af8fb8f09bdcce9dd42f2afcdd2d706e367f9ee83df5", "3.12.0--r40hdfd78af_1": "sha256:5cb8bc76954ae22b1de12f5b12993673d2cf3ca17ff4744a3c8247d3d9de9347", "3.11.1--r40_0": "sha256:0c0df72cc626d1f6a56a89cb11086efaddead03dec05f3e728b0cf9b0c8bc907", "3.17.0--r43hdfd78af_0": "sha256:5655514cee1e5596209d73aad396a068f4ae4b8c7b546cd3c8e7e00cf37f16fc", "3.18.0--r43hdfd78af_0": "sha256:ba374d76c227d9b112ea87fa3da3bb35c7b208d78affb1e7212a2b614318ee33", "3.20.0--r44hdfd78af_0": "sha256:6f4c2f3ebb4040a072f43e7f5547964732e4c1de836cbca064597e2ed5185061"}, "docker": "quay.io/biocontainers/bioconductor-org.gg.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.gg.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.gg.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.gg.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.gg.eg.db:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.gg.eg.db/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.gg.eg.db/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.gg.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.gg.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.gg.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.gg.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.gg.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.gg.eg.db-inspect-deffile:

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