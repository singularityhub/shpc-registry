---
layout: container
name:  "quay.io/biocontainers/r-corncob"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-corncob/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-corncob/container.yaml"
updated_at: "2023-09-04 02:45:33.005052"
latest: "0.3.1--r43h3342da4_2"
container_url: "https://biocontainers.pro/tools/r-corncob"
aliases:
 - "glpsol"
versions:
 - "0.3.0--r41h3342da4_0"
 - "0.3.0--r42h3342da4_1"
 - "0.3.1--r42h3342da4_0"
 - "0.3.1--r42h3342da4_1"
 - "0.3.1--r43h3342da4_2"
description: "shpc-registry automated BioContainers addition for r-corncob"
config: {"url": "https://biocontainers.pro/tools/r-corncob", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-corncob", "latest": {"0.3.1--r43h3342da4_2": "sha256:8b269bb6649e5bb39f69885fcdc4eb139bb48b5cf8ed8dd60e7aba9b364e8b62"}, "tags": {"0.3.0--r41h3342da4_0": "sha256:515be655b655296720a14cacbcd65b02c77b53fbd67b77a2c8447341f4c7acb8", "0.3.0--r42h3342da4_1": "sha256:aa9f89d8deb470c3a89bb99a88e54f345d4cc008e909eea41b92e830bcf25e2f", "0.3.1--r42h3342da4_0": "sha256:a715fcd926fbeee06ddbc234cbd57bdfa6dddef7c33c2b3b90b54132345faaee", "0.3.1--r42h3342da4_1": "sha256:4ee760ee9c878bc3524ba710d0a021615c12798fd28fb3e9577e71278994f572", "0.3.1--r43h3342da4_2": "sha256:8b269bb6649e5bb39f69885fcdc4eb139bb48b5cf8ed8dd60e7aba9b364e8b62"}, "docker": "quay.io/biocontainers/r-corncob", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-corncob.
shpc-registry automated BioContainers addition for r-corncob
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-corncob
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-corncob:0.3.1--r43h3342da4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-corncob/0.3.1--r43h3342da4_2
$ module help quay.io/biocontainers/r-corncob/0.3.1--r43h3342da4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-corncob-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-corncob-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-corncob-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-corncob-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-corncob-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-corncob-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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