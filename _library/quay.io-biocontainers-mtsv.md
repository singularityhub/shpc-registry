---
layout: container
name:  "quay.io/biocontainers/mtsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mtsv/container.yaml"
updated_at: "2023-10-03 03:00:15.639285"
latest: "1.0.6--py36hf1ae8f4_2"
container_url: "https://biocontainers.pro/tools/mtsv"

versions:
 - "1.0.6--py36hf1ae8f4_2"
description: "shpc-registry automated BioContainers addition for mtsv"
config: {"url": "https://biocontainers.pro/tools/mtsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtsv", "latest": {"1.0.6--py36hf1ae8f4_2": "sha256:268717e4ad395ed2d87f797458cf8f8613f4fceb0fe934cf956407fc17875b4f"}, "tags": {"1.0.6--py36hf1ae8f4_2": "sha256:268717e4ad395ed2d87f797458cf8f8613f4fceb0fe934cf956407fc17875b4f"}, "docker": "quay.io/biocontainers/mtsv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtsv.
shpc-registry automated BioContainers addition for mtsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtsv:1.0.6--py36hf1ae8f4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtsv/1.0.6--py36hf1ae8f4_2
$ module help quay.io/biocontainers/mtsv/1.0.6--py36hf1ae8f4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mtsv

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