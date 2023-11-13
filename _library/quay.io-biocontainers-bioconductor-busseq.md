---
layout: container
name:  "quay.io/biocontainers/bioconductor-busseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-busseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-busseq/container.yaml"
updated_at: "2023-11-13 03:13:10.788612"
latest: "1.6.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-busseq"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-busseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-busseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-busseq", "latest": {"1.6.1--r43hf17093f_0": "sha256:087f12ac7e347635fa938066288a633253e0aa5f9bc01094f48682ed9a204ede"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:2c31d1f21e405f01519043bb7a14f2860e94b8826ba5891faa137ec11940e81c", "1.4.0--r42hc247a5b_0": "sha256:1002555479cf3e6902ce8dd13fd7024c040d2c68053e8627fff7a4c42566abd4", "1.4.0--r42hf17093f_1": "sha256:f42fd4189c19abf6ec3fe190b45e2fb8977171963ca9c57c7d91d8211b233eb3", "1.6.1--r43hf17093f_0": "sha256:087f12ac7e347635fa938066288a633253e0aa5f9bc01094f48682ed9a204ede"}, "docker": "quay.io/biocontainers/bioconductor-busseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-busseq.
shpc-registry automated BioContainers addition for bioconductor-busseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-busseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-busseq:1.6.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-busseq/1.6.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-busseq/1.6.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-busseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-busseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-busseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-busseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-busseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-busseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-busseq

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