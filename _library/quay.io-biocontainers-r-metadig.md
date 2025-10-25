---
layout: container
name:  "quay.io/biocontainers/r-metadig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-metadig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-metadig/container.yaml"
updated_at: "2025-10-25 03:39:05.769867"
latest: "0.2.1--r44h9ee0642_1"
container_url: "https://biocontainers.pro/tools/r-metadig"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "0.2.1--r43h9ee0642_0"
 - "0.2.1--r44h9ee0642_1"
description: "singularity registry hpc automated addition for r-metadig"
config: {"url": "https://biocontainers.pro/tools/r-metadig", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-metadig", "latest": {"0.2.1--r44h9ee0642_1": "sha256:57a41b7091bc21837a914d1a1efa9e927906d63b131099d326dce6400914eeda"}, "tags": {"0.2.1--r43h9ee0642_0": "sha256:599bd06aed06a807b8278d57953e77d575e868ca1a55372e2f2cc446ef06568f", "0.2.1--r44h9ee0642_1": "sha256:57a41b7091bc21837a914d1a1efa9e927906d63b131099d326dce6400914eeda"}, "docker": "quay.io/biocontainers/r-metadig", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-metadig.
singularity registry hpc automated addition for r-metadig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-metadig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-metadig:0.2.1--r44h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-metadig/0.2.1--r44h9ee0642_1
$ module help quay.io/biocontainers/r-metadig/0.2.1--r44h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-metadig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-metadig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-metadig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-metadig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-metadig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-metadig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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