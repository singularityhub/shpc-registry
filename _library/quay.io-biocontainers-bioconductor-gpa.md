---
layout: container
name:  "quay.io/biocontainers/bioconductor-gpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gpa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gpa/container.yaml"
updated_at: "2025-04-29 03:47:48.286339"
latest: "1.18.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gpa"

versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_2"
 - "1.12.0--r43hf17093f_0"
 - "1.14.0--r43hf17093f_1"
 - "1.14.0--r43h7d2ed04_2"
 - "1.18.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gpa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gpa", "latest": {"1.18.0--r44he5774e6_0": "sha256:44941fab03d4f582fa02a066ad73d185ad7ca84790183de8c0273d6d8084b033"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:cdd5031f63d7af6a1b60f12cc20973fe2f197f7777dbca669f3e669f28a59c8a", "1.10.0--r42hc247a5b_0": "sha256:fea64c512c3b1f5ac309ab0fd9244c7e9d9295a4233fd9515d183aa382fed242", "1.10.0--r42hf17093f_2": "sha256:9ba9a4c03d8eaa6dd5e54a284c8dd1a62bd5b212aa7ab8a671b67e10e1afd9d3", "1.12.0--r43hf17093f_0": "sha256:01b7c82f1b8e12c1c87cf431863d74d57c3794c87abd9f3ac41c2392151cedaa", "1.14.0--r43hf17093f_1": "sha256:54dad9ff2cde5ab4920dbb5e3f286003712e3038d9c7efe74bbf31eb191671d4", "1.14.0--r43h7d2ed04_2": "sha256:73cd4438167eaa3e644611dc937f4e9723145587aec60f3bf0a54f64c9004de2", "1.18.0--r44he5774e6_0": "sha256:44941fab03d4f582fa02a066ad73d185ad7ca84790183de8c0273d6d8084b033"}, "docker": "quay.io/biocontainers/bioconductor-gpa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gpa.
shpc-registry automated BioContainers addition for bioconductor-gpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gpa:1.18.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gpa/1.18.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-gpa/1.18.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gpa

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