---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocgenerics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocgenerics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocgenerics/container.yaml"
updated_at: "2024-11-14 03:22:10.460869"
latest: "0.48.1--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-biocgenerics"

versions:
 - "0.40.0--r41hdfd78af_0"
 - "0.44.0--r42hdfd78af_0"
 - "0.46.0--r43hdfd78af_0"
 - "0.48.1--r43hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-biocgenerics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocgenerics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocgenerics", "latest": {"0.48.1--r43hdfd78af_2": "sha256:7cb0421cc0ee9546d7b55add3286efac1feaae6cd8ba74407901b77d1c531ed8"}, "tags": {"0.40.0--r41hdfd78af_0": "sha256:6b845ba3261f517db4e9410d3359f40d7ce5a9f27e3ea45f15e17ccbb872951d", "0.44.0--r42hdfd78af_0": "sha256:5cd6cb58d911919cb09d8abafe392858b167292c28973eb62726072f834bd332", "0.46.0--r43hdfd78af_0": "sha256:6ddb7b519b7f6447cf7f8ac142f89ad26d5728ebff827b92a7bbc0f92adbc37f", "0.48.1--r43hdfd78af_2": "sha256:7cb0421cc0ee9546d7b55add3286efac1feaae6cd8ba74407901b77d1c531ed8"}, "docker": "quay.io/biocontainers/bioconductor-biocgenerics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocgenerics.
shpc-registry automated BioContainers addition for bioconductor-biocgenerics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocgenerics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocgenerics:0.48.1--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocgenerics/0.48.1--r43hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-biocgenerics/0.48.1--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocgenerics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocgenerics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocgenerics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocgenerics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocgenerics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocgenerics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocgenerics

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