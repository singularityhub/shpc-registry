---
layout: container
name:  "quay.io/biocontainers/bioconductor-keggrest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-keggrest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-keggrest/container.yaml"
updated_at: "2025-04-17 04:47:17.621255"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-keggrest"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-keggrest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-keggrest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-keggrest", "latest": {"1.46.0--r44hdfd78af_0": "sha256:d94cc9d86ed099be970b209d28f5a58aded211f34d425436c2890abeafe295d1"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:b5b872a18bcedcf11f91df10d95a83152d26d2235a051f9ec1d153be003894a4", "1.38.0--r42hdfd78af_0": "sha256:4e46144e74744e81b4df3eb2ff5cccffef8c531afcfc19ee8b4911ee5ba7e435", "1.40.0--r43hdfd78af_0": "sha256:ce63afe899708c407c53864ff90d830ba997b0e7b56bce00bae5962667fb77e9", "1.42.0--r43hdfd78af_0": "sha256:8082d218c0d57a597257bbe6c0a58b522d0c03209b74a44f98abbe8b4490e341", "1.46.0--r44hdfd78af_0": "sha256:d94cc9d86ed099be970b209d28f5a58aded211f34d425436c2890abeafe295d1"}, "docker": "quay.io/biocontainers/bioconductor-keggrest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-keggrest.
shpc-registry automated BioContainers addition for bioconductor-keggrest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-keggrest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-keggrest:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-keggrest/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-keggrest/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-keggrest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggrest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggrest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-keggrest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-keggrest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-keggrest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-keggrest

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