---
layout: container
name:  "quay.io/biocontainers/bioconductor-uncoverapplib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-uncoverapplib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-uncoverapplib/container.yaml"
updated_at: "2022-11-28 00:23:08.753245"
latest: "1.7.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-uncoverapplib"
aliases:
 - "pandoc"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.7.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-uncoverapplib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-uncoverapplib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-uncoverapplib", "latest": {"1.7.0--r42hdfd78af_0": "sha256:26dad16b482655f35994f696148a2ffe0f0430f7daa858d253be5d2afb46f45a"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:2e83b5823bfc0d57c39d8f5022a0282962202c025741ea7481932f9114dab87b", "1.7.0--r42hdfd78af_0": "sha256:26dad16b482655f35994f696148a2ffe0f0430f7daa858d253be5d2afb46f45a"}, "docker": "quay.io/biocontainers/bioconductor-uncoverapplib", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-uncoverapplib.
shpc-registry automated BioContainers addition for bioconductor-uncoverapplib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-uncoverapplib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-uncoverapplib:1.7.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-uncoverapplib/1.7.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-uncoverapplib/1.7.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-uncoverapplib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uncoverapplib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uncoverapplib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-uncoverapplib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-uncoverapplib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-uncoverapplib-inspect-deffile:

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