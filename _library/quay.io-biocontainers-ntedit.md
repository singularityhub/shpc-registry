---
layout: container
name:  "quay.io/biocontainers/ntedit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntedit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ntedit/container.yaml"
updated_at: "2024-06-16 03:09:58.546494"
latest: "2.0.2--pl5321h21ec9f0_0"
container_url: "https://biocontainers.pro/tools/ntedit"
aliases:
 - "ntedit"
 - "nthits"
versions:
 - "1.3.5--hd03093a_1"
 - "1.3.5--hd03093a_2"
 - "1.3.5--hdcf5f25_4"
 - "1.4.3--hdcf5f25_0"
 - "2.0.2--pl5321h21ec9f0_0"
description: "shpc-registry automated BioContainers addition for ntedit"
config: {"url": "https://biocontainers.pro/tools/ntedit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ntedit", "latest": {"2.0.2--pl5321h21ec9f0_0": "sha256:248ac199ea85ee894a631008a214d498163a7319f8cba12ab68be509dc92f535"}, "tags": {"1.3.5--hd03093a_1": "sha256:2fcaf313a24d22271b8d6e8edf76f678f92d74885e8ad5071485ca38aa823372", "1.3.5--hd03093a_2": "sha256:2cb8c20ff13344b4f256d71a61c2f901eac63322a8bc3132b0deb1e4330d72c3", "1.3.5--hdcf5f25_4": "sha256:081765d7b7032d5dde90f490f713e3c85a7a4fb937ca798caf5237b3a4a041e3", "1.4.3--hdcf5f25_0": "sha256:be3bbcca202eb9b5e68ebfe1919baa4fe96ac33b7db601c35c6dd237c70ecacc", "2.0.2--pl5321h21ec9f0_0": "sha256:248ac199ea85ee894a631008a214d498163a7319f8cba12ab68be509dc92f535"}, "docker": "quay.io/biocontainers/ntedit", "aliases": {"ntedit": "/usr/local/bin/ntedit", "nthits": "/usr/local/bin/nthits"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntedit.
shpc-registry automated BioContainers addition for ntedit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntedit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntedit:2.0.2--pl5321h21ec9f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntedit/2.0.2--pl5321h21ec9f0_0
$ module help quay.io/biocontainers/ntedit/2.0.2--pl5321h21ec9f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntedit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntedit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntedit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntedit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntedit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntedit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ntedit

```bash
$ singularity exec <container> /usr/local/bin/ntedit
$ podman run --it --rm --entrypoint /usr/local/bin/ntedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthits

```bash
$ singularity exec <container> /usr/local/bin/nthits
$ podman run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
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