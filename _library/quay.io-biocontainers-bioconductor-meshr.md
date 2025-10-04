---
layout: container
name:  "quay.io/biocontainers/bioconductor-meshr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meshr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meshr/container.yaml"
updated_at: "2025-10-04 02:56:56.995314"
latest: "2.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meshr"
aliases:
 - "pandoc"
versions:
 - "2.0.0--r41hdfd78af_0"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
 - "2.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meshr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meshr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meshr", "latest": {"2.12.0--r44hdfd78af_0": "sha256:e85e100004f272604bb2bca5318e8f8e2c4a585827c59c4de836a49767881792"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:b55dbd89a56f53bca59bb3023d531aedda73aa61b394bc3bd74673fe4a743a9a", "2.4.0--r42hdfd78af_0": "sha256:a1eb762671ca9333f5795a5584e96166dce08ebbe685cc8efb2fa127f65add5b", "2.6.0--r43hdfd78af_0": "sha256:9b1a969bb214fb3a70101e35ace3a58094759e2242a96a8a68efbcdd7153647d", "2.8.0--r43hdfd78af_0": "sha256:39eff57c28a21fde1c0c21221887a811712bdb8f8467c4845fd427af4066eef8", "2.12.0--r44hdfd78af_0": "sha256:e85e100004f272604bb2bca5318e8f8e2c4a585827c59c4de836a49767881792"}, "docker": "quay.io/biocontainers/bioconductor-meshr", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meshr.
shpc-registry automated BioContainers addition for bioconductor-meshr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meshr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meshr:2.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meshr/2.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meshr/2.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meshr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meshr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meshr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meshr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meshr-inspect-deffile:

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