---
layout: container
name:  "quay.io/biocontainers/bioconductor-pcamethods"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pcamethods/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pcamethods/container.yaml"
updated_at: "2025-01-03 03:15:53.494742"
latest: "1.98.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pcamethods"

versions:
 - "1.86.0--r41hc247a5b_2"
 - "1.90.0--r42hc247a5b_0"
 - "1.90.0--r42hf17093f_1"
 - "1.92.0--r43hf17093f_0"
 - "1.94.0--r43hf17093f_0"
 - "1.94.0--r43hf17093f_1"
 - "1.98.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pcamethods"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pcamethods", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pcamethods", "latest": {"1.98.0--r44he5774e6_0": "sha256:fe4bd8ebb33e063458768909f44c2ea6e807860ff9afdd4af7b3ae4fe8b67c17"}, "tags": {"1.86.0--r41hc247a5b_2": "sha256:defd5b0c6820b00d1c6564fe3d52f5f870c5716530a4d46ce5a89713841555cb", "1.90.0--r42hc247a5b_0": "sha256:c4840d18ea9b3fde8fbff52f3287d01736f8b04b3c3f67aab87f0e89378de60e", "1.90.0--r42hf17093f_1": "sha256:c4bcc72c6256377026c27409fd4bf6efba489fe246e11ca31126d1f57f2ad5d3", "1.92.0--r43hf17093f_0": "sha256:b769164d49275e497a8583b154bbd056ec2820eb7feb3f1d5fa538e1153bb39c", "1.94.0--r43hf17093f_0": "sha256:2b7f60ad85f5fc1033e08e68ee1e2bf45d420ce2e623c790b5e486b452f828c7", "1.94.0--r43hf17093f_1": "sha256:c8bac5bd30ff036fbf62b78d92507b4d5c614331b7c6209f8133c975ba96c831", "1.98.0--r44he5774e6_0": "sha256:fe4bd8ebb33e063458768909f44c2ea6e807860ff9afdd4af7b3ae4fe8b67c17"}, "docker": "quay.io/biocontainers/bioconductor-pcamethods"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pcamethods.
shpc-registry automated BioContainers addition for bioconductor-pcamethods
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pcamethods
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pcamethods:1.98.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pcamethods/1.98.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-pcamethods/1.98.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pcamethods-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcamethods-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pcamethods-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pcamethods-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pcamethods-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pcamethods-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pcamethods

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