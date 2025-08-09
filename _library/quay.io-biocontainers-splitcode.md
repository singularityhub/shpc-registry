---
layout: container
name:  "quay.io/biocontainers/splitcode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splitcode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splitcode/container.yaml"
updated_at: "2025-08-09 03:48:06.055984"
latest: "0.31.3--h077b44d_0"
container_url: "https://biocontainers.pro/tools/splitcode"
aliases:
 - "splitcode"
versions:
 - "0.29.4--hdcf5f25_0"
 - "0.30.0--hdcf5f25_0"
 - "0.31.2--h077b44d_1"
 - "0.31.2--h077b44d_2"
 - "0.31.3--h077b44d_0"
description: "singularity registry hpc automated addition for splitcode"
config: {"url": "https://biocontainers.pro/tools/splitcode", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for splitcode", "latest": {"0.31.3--h077b44d_0": "sha256:a06d8f44337c3da80c30e5f93c06e9bc1564df466c72f2ebf618e70d9b47eb48"}, "tags": {"0.29.4--hdcf5f25_0": "sha256:d6deb640e186cc466b2a0e7cc0a03c55794cedcd1c5fc70e61c89cf52883a37b", "0.30.0--hdcf5f25_0": "sha256:0612da997efbfd2e7a38933825a7256437667bb702b6fc41f736952d7ffdb7e1", "0.31.2--h077b44d_1": "sha256:597ed4f936de2766cbcd5f2b8335f96a6b1eec74d5f0b0017887be8990c4bf17", "0.31.2--h077b44d_2": "sha256:d56f61565cac70d44a9af38ba755532b6f1788f172ebd2144ab9a57e0f2f6b08", "0.31.3--h077b44d_0": "sha256:a06d8f44337c3da80c30e5f93c06e9bc1564df466c72f2ebf618e70d9b47eb48"}, "docker": "quay.io/biocontainers/splitcode", "aliases": {"splitcode": "/usr/local/bin/splitcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splitcode.
singularity registry hpc automated addition for splitcode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splitcode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splitcode:0.31.3--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splitcode/0.31.3--h077b44d_0
$ module help quay.io/biocontainers/splitcode/0.31.3--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splitcode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splitcode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splitcode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splitcode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splitcode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splitcode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### splitcode

```bash
$ singularity exec <container> /usr/local/bin/splitcode
$ podman run --it --rm --entrypoint /usr/local/bin/splitcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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