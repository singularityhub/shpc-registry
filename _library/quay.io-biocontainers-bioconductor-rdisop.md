---
layout: container
name:  "quay.io/biocontainers/bioconductor-rdisop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rdisop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rdisop/container.yaml"
updated_at: "2023-08-29 04:16:19.435170"
latest: "1.60.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rdisop"

versions:
 - "1.54.0--r41hc247a5b_2"
 - "1.58.0--r42hc247a5b_0"
 - "1.58.0--r42hc247a5b_1"
 - "1.60.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rdisop"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rdisop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rdisop", "latest": {"1.60.0--r43hf17093f_0": "sha256:a1e1f0a318ab9f8a852a3cd8b875089f1d1da990e0670ad1ddd64af6c0fc4271"}, "tags": {"1.54.0--r41hc247a5b_2": "sha256:82d827f05d3bf562d971eeb36daffd7b2639fff3807ee8e1cb9affb43ea80e29", "1.58.0--r42hc247a5b_0": "sha256:60b7a1e7f83a249e383e2eb98a9b65f862f3b9082ded620f014822f2d412c104", "1.58.0--r42hc247a5b_1": "sha256:acc73757cf00d9195f6bc378118162cf203b18ef65c025c30c7487f334311071", "1.60.0--r43hf17093f_0": "sha256:a1e1f0a318ab9f8a852a3cd8b875089f1d1da990e0670ad1ddd64af6c0fc4271"}, "docker": "quay.io/biocontainers/bioconductor-rdisop"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rdisop.
shpc-registry automated BioContainers addition for bioconductor-rdisop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rdisop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rdisop:1.60.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rdisop/1.60.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rdisop/1.60.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rdisop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdisop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdisop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rdisop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rdisop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rdisop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rdisop

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