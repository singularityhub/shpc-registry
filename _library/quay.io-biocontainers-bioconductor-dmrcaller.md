---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmrcaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmrcaller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmrcaller/container.yaml"
updated_at: "2024-12-25 03:13:55.117039"
latest: "1.32.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmrcaller"

versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
 - "1.30.0--r42hf17093f_1"
 - "1.32.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmrcaller"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmrcaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmrcaller", "latest": {"1.32.0--r43hf17093f_0": "sha256:52d39149e38a2182654546e9baf5e9af769086258e7f46701f581cfb432c4ab5"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:ea08aa357f5fcb65e695bf0931f03e48e35254135e4fdc4969a641abaf0fecf7", "1.30.0--r42hc247a5b_0": "sha256:84948a3f47c2e2b401893caa287d8bba8ba4dd0aeb8bc03e8cdc78717d4354d2", "1.30.0--r42hf17093f_1": "sha256:8bc4ac5076ce07d6118e925ae6a19cc6f4a2b3339fc8a470f3667640c8e9d198", "1.32.0--r43hf17093f_0": "sha256:52d39149e38a2182654546e9baf5e9af769086258e7f46701f581cfb432c4ab5"}, "docker": "quay.io/biocontainers/bioconductor-dmrcaller"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmrcaller.
shpc-registry automated BioContainers addition for bioconductor-dmrcaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrcaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrcaller:1.32.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmrcaller/1.32.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-dmrcaller/1.32.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmrcaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrcaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrcaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmrcaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmrcaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmrcaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dmrcaller

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