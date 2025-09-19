---
layout: container
name:  "quay.io/biocontainers/bioconductor-dce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dce/container.yaml"
updated_at: "2025-09-19 03:35:38.425922"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dce"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dce"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dce", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dce", "latest": {"1.10.0--r43hdfd78af_0": "sha256:a33a3ac86eed2b1d5f5b371140f89a6ee191b66c7e216896479de407369face7"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:8e1cb0e1924983286499586059fef38b241b797df2722a67548b25443b4605cf", "1.6.0--r42hdfd78af_0": "sha256:138ecb06cb6b0c981c1b94f076ee8d6e5481bb58a2c63f05ab875b1a53d3e472", "1.7.0--r43hdfd78af_0": "sha256:dbe5721e93c6f4d65efd0eaf15369e28723232903642375b6a47aec73e574df3", "1.10.0--r43hdfd78af_0": "sha256:a33a3ac86eed2b1d5f5b371140f89a6ee191b66c7e216896479de407369face7"}, "docker": "quay.io/biocontainers/bioconductor-dce", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dce.
shpc-registry automated BioContainers addition for bioconductor-dce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dce:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dce/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dce/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dce-inspect-deffile:

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