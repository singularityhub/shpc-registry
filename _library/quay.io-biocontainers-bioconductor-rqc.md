---
layout: container
name:  "quay.io/biocontainers/bioconductor-rqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rqc/container.yaml"
updated_at: "2024-10-02 02:55:31.045638"
latest: "1.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rqc"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_1"
 - "1.34.0--r43hf17093f_0"
 - "1.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rqc", "latest": {"1.36.0--r43hf17093f_0": "sha256:5f4509d5ed15ba5bad49b4774b4eb900f8ac6b01c7914f9a1eadcd4c73b7a21b"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:a55f1c5c12dc6063c1249e17f88771f13c6715b1337aa78056eae3293e7a8d64", "1.32.0--r42hc247a5b_0": "sha256:40213efc9b9be6c13eac59aba9d7492eb77376a197406265ef12ce88b5fb7e28", "1.32.0--r42hf17093f_1": "sha256:a5223b8b11433cf0dfab4beaa111798b090dff0933e11a0cf98ddfc383acf8e2", "1.34.0--r43hf17093f_0": "sha256:c5faecae6798e1730350fae3024eb87d6faeb5f97fc0799f9195a9e8a89bfc4d", "1.36.0--r43hf17093f_0": "sha256:5f4509d5ed15ba5bad49b4774b4eb900f8ac6b01c7914f9a1eadcd4c73b7a21b"}, "docker": "quay.io/biocontainers/bioconductor-rqc", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rqc.
shpc-registry automated BioContainers addition for bioconductor-rqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rqc:1.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rqc/1.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rqc/1.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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