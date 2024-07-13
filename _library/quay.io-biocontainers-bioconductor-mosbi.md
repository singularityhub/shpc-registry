---
layout: container
name:  "quay.io/biocontainers/bioconductor-mosbi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mosbi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mosbi/container.yaml"
updated_at: "2024-07-13 03:03:45.359273"
latest: "1.8.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mosbi"
aliases:
 - "glpsol"
versions:
 - "1.0.3--r41hc247a5b_1"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mosbi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mosbi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mosbi", "latest": {"1.8.0--r43hf17093f_0": "sha256:063e891ce7fb22fe2fbe337c0a7c54e48c236d60f16e8003ea2dba236f9506e4"}, "tags": {"1.0.3--r41hc247a5b_1": "sha256:61b4684a4cd64bad5db71e78cdf0da3219eac2ec12ce812fb0bc45b1973a78f8", "1.4.0--r42hc247a5b_0": "sha256:2ac27f805332fa9294d1338731ee194a5482baad49f8aaa045062084410fe765", "1.4.0--r42hf17093f_1": "sha256:acce461bcc739211e2156945a591d944782daf2be31b1317bbbb15427f019816", "1.6.0--r43hf17093f_0": "sha256:05041e3de328be24df1ecc4ad44259da4195570b1c26bb85bbfcbc7bf23b5fb9", "1.8.0--r43hf17093f_0": "sha256:063e891ce7fb22fe2fbe337c0a7c54e48c236d60f16e8003ea2dba236f9506e4"}, "docker": "quay.io/biocontainers/bioconductor-mosbi", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mosbi.
shpc-registry automated BioContainers addition for bioconductor-mosbi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mosbi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mosbi:1.8.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mosbi/1.8.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-mosbi/1.8.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mosbi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosbi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosbi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mosbi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mosbi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mosbi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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