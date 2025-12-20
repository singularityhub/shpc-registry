---
layout: container
name:  "quay.io/biocontainers/fastani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastani/container.yaml"
updated_at: "2025-12-20 03:53:27.450422"
latest: "1.34--hb66fcc3_7"
container_url: "https://biocontainers.pro/tools/fastani"
aliases:
 - "fastANI"
versions:
 - "1.33--h0fdf51a_1"
 - "1.33--h4dfc31f_3"
 - "1.34--h4dfc31f_0"
 - "1.34--h4dfc31f_1"
 - "1.34--h4dfc31f_2"
 - "1.34--h4dfc31f_3"
 - "1.34--h4dfc31f_4"
 - "1.34--hb66fcc3_5"
 - "1.34--hb66fcc3_6"
 - "1.34--hb66fcc3_7"
description: "shpc-registry automated BioContainers addition for fastani"
config: {"url": "https://biocontainers.pro/tools/fastani", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastani", "latest": {"1.34--hb66fcc3_7": "sha256:0723121d8154f7e4917304142824d12bff93494d2b2ed4ab072d51eccf6c8494"}, "tags": {"1.33--h0fdf51a_1": "sha256:4ba79083702b537aa7478c29870a41e651c3a1c9f6ed63fabd8fca6539686efe", "1.33--h4dfc31f_3": "sha256:d7e42634baa4c5518145a30ae5f43ca0c8bea3e07241047f3aea9a531953b1ff", "1.34--h4dfc31f_0": "sha256:49d9f3ecc1aea6a48f51918dd1b2b9cdc4683011f2eeb4956b5d7dd76d3fc0d8", "1.34--h4dfc31f_1": "sha256:a5ae728542a056b176687624664facc2ff2a7dd84b9c57d27f028a0211fa0d07", "1.34--h4dfc31f_2": "sha256:07a26bab4539918cce52988c39ebb3b0c56425a17c06fffe9f0e6970aff51b9d", "1.34--h4dfc31f_3": "sha256:9d3c0939e7e7cea0dc8fc6cb6a5916c80772c2db40507bee0f3792b1e0f3b683", "1.34--h4dfc31f_4": "sha256:43a7891b49222ab831eec6d6ed1de82e0cd415a34516a673e1a81f7ec181749b", "1.34--hb66fcc3_5": "sha256:1aa6615be04dedd4907a7bbce2b57938a42d5f94913b068c31cbcfd437e1130b", "1.34--hb66fcc3_6": "sha256:71c96f0deeba5cb88e960ab769ac20f3c59e29bbc0d995366aac0ec47308077d", "1.34--hb66fcc3_7": "sha256:0723121d8154f7e4917304142824d12bff93494d2b2ed4ab072d51eccf6c8494"}, "docker": "quay.io/biocontainers/fastani", "aliases": {"fastANI": "/usr/local/bin/fastANI"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastani.
shpc-registry automated BioContainers addition for fastani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastani:1.34--hb66fcc3_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastani/1.34--hb66fcc3_7
$ module help quay.io/biocontainers/fastani/1.34--hb66fcc3_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastani-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
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