---
layout: container
name:  "quay.io/biocontainers/humann"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/humann/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/humann/container.yaml"
updated_at: "2025-09-16 03:22:49.722505"
latest: "3.9--py312hdfd78af_0"
container_url: "https://biocontainers.pro/tools/humann"

versions:
 - "3.6--pyh7cba7a3_0"
 - "3.6--pyh7cba7a3_1"
 - "3.6--pyh7cba7a3_2"
 - "3.7--pyh7cba7a3_0"
 - "3.7--pyh7cba7a3_1"
 - "3.8--pyh7cba7a3_0"
 - "3.9--py312hdfd78af_0"
description: "shpc-registry automated BioContainers addition for humann"
config: {"url": "https://biocontainers.pro/tools/humann", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for humann", "latest": {"3.9--py312hdfd78af_0": "sha256:5d4ad5983b133477b1738c0cc3505f60245836c3790db39361fa7a2c0fa84abf"}, "tags": {"3.6--pyh7cba7a3_0": "sha256:7b9093898aa115471daf054d4baf0aa4ab4d1af39d077812f7445d5b3fd766f0", "3.6--pyh7cba7a3_1": "sha256:8475bb77f9eeeb272819f4ce97e92db56c0be6d98fde5be0b8631d8908b1f553", "3.6--pyh7cba7a3_2": "sha256:ff4ec1968d8e8b29b85d146cbf3486e601a6e63f7e3cf5d8fef954bf61a2f09d", "3.7--pyh7cba7a3_0": "sha256:afb42d2804535caada5c8edc0344dceb0777e94ae5b0680cacddd628441a6079", "3.7--pyh7cba7a3_1": "sha256:577a71dbd24530f0905bc01f4a715d47a684a4feb237e4e5a3927fcb7ade473a", "3.8--pyh7cba7a3_0": "sha256:a8338668a9e62e8cbddb6d70ed4aaea939d5e7aea2cf479cdb208bbf40452fad", "3.9--py312hdfd78af_0": "sha256:5d4ad5983b133477b1738c0cc3505f60245836c3790db39361fa7a2c0fa84abf"}, "docker": "quay.io/biocontainers/humann"}
---

This module is a singularity container wrapper for quay.io/biocontainers/humann.
shpc-registry automated BioContainers addition for humann
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/humann
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/humann:3.9--py312hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/humann/3.9--py312hdfd78af_0
$ module help quay.io/biocontainers/humann/3.9--py312hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### humann-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### humann-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### humann-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### humann-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### humann-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### humann-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### humann

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