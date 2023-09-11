---
layout: container
name:  "quay.io/biocontainers/bioconductor-multisight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multisight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multisight/container.yaml"
updated_at: "2023-09-11 02:25:24.698433"
latest: "1.7.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multisight"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multisight"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multisight", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multisight", "latest": {"1.7.0--r43hdfd78af_0": "sha256:722d512b15908a31e7e2196ab2d3c69da8ba9c10c011778c938c0e352a8734b6"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:02ce72f1a3a1fee4a5e9791c813cb83d1754492ec35cdb90537308b65f24dd6c", "1.6.0--r42hdfd78af_0": "sha256:3ef7ac5f3a10bb7fb40b5c1fd2c90b5a1bc364ce7cc1a3c7abe900b626a97e66", "1.7.0--r43hdfd78af_0": "sha256:722d512b15908a31e7e2196ab2d3c69da8ba9c10c011778c938c0e352a8734b6"}, "docker": "quay.io/biocontainers/bioconductor-multisight", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multisight.
shpc-registry automated BioContainers addition for bioconductor-multisight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multisight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multisight:1.7.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multisight/1.7.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multisight/1.7.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multisight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multisight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multisight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multisight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multisight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multisight-inspect-deffile:

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