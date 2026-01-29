---
layout: container
name:  "quay.io/biocontainers/10x_bamtofastq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/10x_bamtofastq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/10x_bamtofastq/container.yaml"
updated_at: "2026-01-29 04:31:08.407130"
latest: "1.4.1"
container_url: "https://biocontainers.pro/tools/10x_bamtofastq"
aliases:
 - "bamtofastq"
versions:
 - "1.4.1--h87f3376_0"
 - "1.4.1"
 - "1.4.1--hdbdd923_2"
 - "1.4.1--h503566f_3"
 - "1.4.1--h3ab6199_4"
description: "singularity registry hpc automated addition for 10x_bamtofastq"
config: {"url": "https://biocontainers.pro/tools/10x_bamtofastq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for 10x_bamtofastq", "latest": {"1.4.1": "sha256:405ece97fda53a5e3e26a7d11171a3f46e86652c9aaaa02444f096efac450da5"}, "tags": {"1.4.1--h87f3376_0": "sha256:d17a4d02513ca386d2628f2c7e8eb6af0556e108f35d9d4b2b2a593394911981", "1.4.1": "sha256:405ece97fda53a5e3e26a7d11171a3f46e86652c9aaaa02444f096efac450da5", "1.4.1--hdbdd923_2": "sha256:cccdfecf37a2ecd75a8c0a828e2e85e974252d6988c7100c7b47c9f14c2c4999", "1.4.1--h503566f_3": "sha256:0b3b50b5003eb5066c84bf06756289b9674ed8b68a1f7ec78b3fcf6e771050a3", "1.4.1--h3ab6199_4": "sha256:45bff5f906da6a9695dc3a03c023e969880e2a43d0d5d1a95cb5ff30cc4aca5f"}, "docker": "quay.io/biocontainers/10x_bamtofastq", "aliases": {"bamtofastq": "/usr/local/bin/bamtofastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/10x_bamtofastq.
singularity registry hpc automated addition for 10x_bamtofastq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/10x_bamtofastq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/10x_bamtofastq:1.4.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/10x_bamtofastq/1.4.1
$ module help quay.io/biocontainers/10x_bamtofastq/1.4.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### 10x_bamtofastq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### 10x_bamtofastq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### 10x_bamtofastq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### 10x_bamtofastq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### 10x_bamtofastq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### 10x_bamtofastq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamtofastq

```bash
$ singularity exec <container> /usr/local/bin/bamtofastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamtofastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtofastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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