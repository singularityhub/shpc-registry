---
layout: container
name:  "quay.io/biocontainers/igv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igv/container.yaml"
updated_at: "2025-04-10 03:28:13.245263"
latest: "2.19.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/igv"

versions:
 - "2.9.5--hdfd78af_0"
 - "2.13.2--hdfd78af_0"
 - "2.12.3--hdfd78af_0"
 - "2.11.9--hdfd78af_0"
 - "2.10.3--hdfd78af_0"
 - "2.16.2--hdfd78af_0"
 - "2.17.4--hdfd78af_0"
 - "2.19.1--hdfd78af_0"
 - "2.19.1--hdfd78af_1"
 - "2.19.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for igv"
config: {"url": "https://biocontainers.pro/tools/igv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igv", "latest": {"2.19.2--hdfd78af_0": "sha256:d6e183e8a9098bfb68a8af1108138a4426087ac5a0dad556b3036fc703bb33f7"}, "tags": {"2.9.5--hdfd78af_0": "sha256:705d2341964a242d3c1affb3d6f865017b1cb34f7d05363b879cb3fba5cd737d", "2.13.2--hdfd78af_0": "sha256:56e4a4d08eb5745855000383ba68551e3c1b5abc08b701d3c355b279020ecffd", "2.12.3--hdfd78af_0": "sha256:38d8faad5e4cdab9193d16eea21cf12f8b0ce840553bdbe5fd9029da0cb0742e", "2.11.9--hdfd78af_0": "sha256:baf40d4279868662e94be5cadeeb535e61dd39d8288db93cda27b6f119cf1713", "2.10.3--hdfd78af_0": "sha256:6dc0b8d50dc8ac97d8dc9d075cc036335911781d02c44e0c4edbee8a3155162d", "2.16.2--hdfd78af_0": "sha256:0941fa5b781f4457f51f9bd0fb938f7baffe4cd1b4e83877b40c964de1d9e11d", "2.17.4--hdfd78af_0": "sha256:907f906eddf34a2ef837d3de345352f1e0e0a18a879d618626dbaaec631719dc", "2.19.1--hdfd78af_0": "sha256:3c054fcf0cf11b4e9768037b3cfcff08dfcbbd256b818420778ec881eb779f1f", "2.19.1--hdfd78af_1": "sha256:1019b67f6629523b78479d784282e56af2524c5b6d687bf6d26b093004f83160", "2.19.2--hdfd78af_0": "sha256:d6e183e8a9098bfb68a8af1108138a4426087ac5a0dad556b3036fc703bb33f7"}, "docker": "quay.io/biocontainers/igv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/igv.
shpc-registry automated BioContainers addition for igv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igv:2.19.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igv/2.19.2--hdfd78af_0
$ module help quay.io/biocontainers/igv/2.19.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### igv

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