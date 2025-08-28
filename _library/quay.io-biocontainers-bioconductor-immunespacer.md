---
layout: container
name:  "quay.io/biocontainers/bioconductor-immunespacer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-immunespacer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-immunespacer/container.yaml"
updated_at: "2025-08-28 12:00:12.682905"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-immunespacer"
aliases:
 - "pandoc"
versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-immunespacer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-immunespacer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-immunespacer", "latest": {"1.30.0--r43hdfd78af_0": "sha256:6da54ae1ea91f118a9d23aae890c3387ad91697868c4e291e81ed986460fd0dc"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:673301a4f9c5b35acb479842931c1d83d1486be61bec65bc05e620d75caa4a2d", "1.26.0--r42hdfd78af_0": "sha256:6280e9b10bad4143c2ffa43579983ea93a1bd5e275c528a83c9b5d1083185def", "1.28.0--r43hdfd78af_0": "sha256:0e874120a88bad1b9a7cfa2b697de5186989b2d3f779a767e6f99c10c795e024", "1.30.0--r43hdfd78af_0": "sha256:6da54ae1ea91f118a9d23aae890c3387ad91697868c4e291e81ed986460fd0dc"}, "docker": "quay.io/biocontainers/bioconductor-immunespacer", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-immunespacer.
shpc-registry automated BioContainers addition for bioconductor-immunespacer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-immunespacer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-immunespacer:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-immunespacer/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-immunespacer/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-immunespacer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-immunespacer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-immunespacer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-immunespacer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-immunespacer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-immunespacer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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