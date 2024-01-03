---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirna20cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirna20cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirna20cdf/container.yaml"
updated_at: "2024-01-03 03:00:14.741521"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mirna20cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mirna20cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirna20cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirna20cdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:7eb8dccdaccd261c71475fdc6a1e14e60cbd55f4d4c4cb17bbebe9cf1d7fc5e8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:9a1addf6fcfce3a3569a77caad15c3b1ab690081aa4c717972b07df06ea2ad37", "2.18.0--r42hdfd78af_10": "sha256:cf83356e57ad3282b391f33852f892ae99c13b4855875efac6befb24b9dd5ef2", "2.18.0--r43hdfd78af_11": "sha256:7eb8dccdaccd261c71475fdc6a1e14e60cbd55f4d4c4cb17bbebe9cf1d7fc5e8"}, "docker": "quay.io/biocontainers/bioconductor-mirna20cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirna20cdf.
shpc-registry automated BioContainers addition for bioconductor-mirna20cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna20cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna20cdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirna20cdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mirna20cdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirna20cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna20cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna20cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirna20cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirna20cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirna20cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirna20cdf

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