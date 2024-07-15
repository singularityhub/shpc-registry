---
layout: container
name:  "quay.io/biocontainers/pbstarphase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbstarphase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbstarphase/container.yaml"
updated_at: "2024-07-15 02:43:06.630985"
latest: "0.11.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbstarphase"
aliases:
 - "pbstarphase"
versions:
 - "0.7.3--h9ee0642_0"
 - "0.8.1--h9ee0642_0"
 - "0.9.1--h9ee0642_0"
 - "0.8.2--h9ee0642_0"
 - "0.10.0--h9ee0642_0"
 - "0.11.0--h9ee0642_0"
 - "0.10.2--h9ee0642_0"
description: "singularity registry hpc automated addition for pbstarphase"
config: {"url": "https://biocontainers.pro/tools/pbstarphase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbstarphase", "latest": {"0.11.0--h9ee0642_0": "sha256:e9593afb0d6160698b874fd6d6f93984f588afe83bc0303bf692d0de7c10f58d"}, "tags": {"0.7.3--h9ee0642_0": "sha256:37a9f7c48cc4fd17cef5f5ca8f11d3dac57c903f77cc0da423299c144e61dae9", "0.8.1--h9ee0642_0": "sha256:4f0c93013ea154357a42104d8e75d5c75bae7efd7ad6a65b2d82d7707abd4047", "0.9.1--h9ee0642_0": "sha256:ba9674fe27d48191a9ff2f584c690e87c5a40bb2dec96c4a035be96933f40ba9", "0.8.2--h9ee0642_0": "sha256:30abee6f17e3c545e9ba769610a1625e59578c46797e9a929a727d9144995688", "0.10.0--h9ee0642_0": "sha256:12c973e365be416a363b5464fb167b902245b83a4bf892daac64a6e1241f8719", "0.11.0--h9ee0642_0": "sha256:e9593afb0d6160698b874fd6d6f93984f588afe83bc0303bf692d0de7c10f58d", "0.10.2--h9ee0642_0": "sha256:6ea93397bfc1d15717919fe13a0b0e9d54f2cde40a378b812f886c1e9a29f2c7"}, "docker": "quay.io/biocontainers/pbstarphase", "aliases": {"pbstarphase": "/usr/local/bin/pbstarphase"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbstarphase.
singularity registry hpc automated addition for pbstarphase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbstarphase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbstarphase:0.11.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbstarphase/0.11.0--h9ee0642_0
$ module help quay.io/biocontainers/pbstarphase/0.11.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbstarphase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbstarphase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbstarphase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbstarphase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbstarphase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbstarphase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbstarphase

```bash
$ singularity exec <container> /usr/local/bin/pbstarphase
$ podman run --it --rm --entrypoint /usr/local/bin/pbstarphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbstarphase   -v ${PWD} -w ${PWD} <container> -c " $@"
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