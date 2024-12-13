---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneexpressionsignature"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneexpressionsignature/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneexpressionsignature/container.yaml"
updated_at: "2024-12-13 03:53:41.968897"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneexpressionsignature"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneexpressionsignature"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneexpressionsignature", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneexpressionsignature", "latest": {"1.48.0--r43hdfd78af_0": "sha256:09338efdfad2dd2e897cef3b4f7d626068c8b647858d50cf0d38f9809b320427"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:ffc3d3959577ee10876bb6ec2cd4cdda6febaf86350a5c68966c96133ce8aac5", "1.44.0--r42hdfd78af_0": "sha256:a9d72a02d77a0450c49ff0730155aa2a492a8762484fe08a2c18e2e96003dd73", "1.46.0--r43hdfd78af_0": "sha256:ff98ff1a93f9cbaee4a7c681dbed49bacfd095c54cd7183ebde39e673888d1be", "1.48.0--r43hdfd78af_0": "sha256:09338efdfad2dd2e897cef3b4f7d626068c8b647858d50cf0d38f9809b320427"}, "docker": "quay.io/biocontainers/bioconductor-geneexpressionsignature"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneexpressionsignature.
shpc-registry automated BioContainers addition for bioconductor-geneexpressionsignature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneexpressionsignature
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneexpressionsignature:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneexpressionsignature/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneexpressionsignature/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneexpressionsignature-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneexpressionsignature-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneexpressionsignature-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneexpressionsignature-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneexpressionsignature-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneexpressionsignature-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneexpressionsignature

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