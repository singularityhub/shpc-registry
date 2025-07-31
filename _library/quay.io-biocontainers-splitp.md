---
layout: container
name:  "quay.io/biocontainers/splitp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splitp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splitp/container.yaml"
updated_at: "2025-07-31 11:42:14.242514"
latest: "0.2.0--h9948957_1"
container_url: "https://biocontainers.pro/tools/splitp"
aliases:
 - "splitp"
versions:
 - "0.1.0--h9f5acd7_1"
 - "0.1.0--h9f5acd7_2"
 - "0.2.0--h4ac6f70_0"
 - "0.1.0--h4ac6f70_3"
 - "0.2.0--h9948957_1"
description: "singularity registry hpc automated addition for splitp"
config: {"url": "https://biocontainers.pro/tools/splitp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for splitp", "latest": {"0.2.0--h9948957_1": "sha256:5c73002e0e04724b4c1cf6ca646ef16c77de58d80169a0509d898468ffe0c103"}, "tags": {"0.1.0--h9f5acd7_1": "sha256:55edf2f66f0a3f01074842a7a4a476b5e10628b87dde671200ed1be4e5d1cc6c", "0.1.0--h9f5acd7_2": "sha256:7e8f8922d365cc6d0c8219c0dfb3f9b038298bbf9ad76ec9c13d5d0f228a3861", "0.2.0--h4ac6f70_0": "sha256:0283630ca532349d725797036979c4ee7873e88edda79d84a2204ffba9d25ca8", "0.1.0--h4ac6f70_3": "sha256:2ea9c965bb3d6034bb36f801d594b63b34ce3edbf5a938cfcb5bbec00abdd521", "0.2.0--h9948957_1": "sha256:5c73002e0e04724b4c1cf6ca646ef16c77de58d80169a0509d898468ffe0c103"}, "docker": "quay.io/biocontainers/splitp", "aliases": {"splitp": "/usr/local/bin/splitp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splitp.
singularity registry hpc automated addition for splitp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splitp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splitp:0.2.0--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splitp/0.2.0--h9948957_1
$ module help quay.io/biocontainers/splitp/0.2.0--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splitp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splitp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splitp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splitp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splitp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splitp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### splitp

```bash
$ singularity exec <container> /usr/local/bin/splitp
$ podman run --it --rm --entrypoint /usr/local/bin/splitp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitp   -v ${PWD} -w ${PWD} <container> -c " $@"
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