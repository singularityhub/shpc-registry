---
layout: container
name:  "quay.io/biocontainers/bioconductor-netpathminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netpathminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netpathminer/container.yaml"
updated_at: "2025-02-09 03:03:36.021888"
latest: "1.42.0--r44h0ce4ec3_0"
container_url: "https://biocontainers.pro/tools/bioconductor-netpathminer"
aliases:
 - "glpsol"
versions:
 - "1.30.0--r41hbe66c35_2"
 - "1.34.0--r42hbe66c35_0"
 - "1.34.0--r42h5b63f1c_1"
 - "1.36.0--r43h4605cfd_0"
 - "1.38.0--r43h4605cfd_1"
 - "1.38.0--r43h306fc42_2"
 - "1.42.0--r44h0ce4ec3_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netpathminer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netpathminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netpathminer", "latest": {"1.42.0--r44h0ce4ec3_0": "sha256:a05fbc7fa0dd3ba3fb9f85fcef65a2106279dbb4dbc138934c9e7078ee6406f1"}, "tags": {"1.30.0--r41hbe66c35_2": "sha256:d73e49d4f03dfebb1c0e2055e481fe5b1688ec8dc271c0927a62f48d79bf3c15", "1.34.0--r42hbe66c35_0": "sha256:ecd18613e5bec2db71f5c7c6da5b8a10c5eecf3cf38c5f66038f4022a25d84e6", "1.34.0--r42h5b63f1c_1": "sha256:7d8b33946c68561f75961c981ea6603acc3f7b66b09bd010d05488ca8208989f", "1.36.0--r43h4605cfd_0": "sha256:b5e7fa1de30874f20319c75ab133f2c61d41b7284fb939a728e35db09203e59e", "1.38.0--r43h4605cfd_1": "sha256:8f905e4ba52aea76412940e11930af763aa74d5f8913d8b21e8a4e1931a581e4", "1.38.0--r43h306fc42_2": "sha256:a56d566bcbe8888c5e00555c7c437b3b81d26af6124e8792c7006f5a402b28e1", "1.42.0--r44h0ce4ec3_0": "sha256:a05fbc7fa0dd3ba3fb9f85fcef65a2106279dbb4dbc138934c9e7078ee6406f1"}, "docker": "quay.io/biocontainers/bioconductor-netpathminer", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netpathminer.
shpc-registry automated BioContainers addition for bioconductor-netpathminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netpathminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netpathminer:1.42.0--r44h0ce4ec3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netpathminer/1.42.0--r44h0ce4ec3_0
$ module help quay.io/biocontainers/bioconductor-netpathminer/1.42.0--r44h0ce4ec3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netpathminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netpathminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netpathminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netpathminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netpathminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netpathminer-inspect-deffile:

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