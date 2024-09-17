---
layout: container
name:  "quay.io/biocontainers/bioconductor-enrichmentbrowser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enrichmentbrowser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enrichmentbrowser/container.yaml"
updated_at: "2024-09-17 03:08:23.076121"
latest: "2.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enrichmentbrowser"

versions:
 - "2.24.0--r41hdfd78af_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.30.1--r43hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enrichmentbrowser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enrichmentbrowser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enrichmentbrowser", "latest": {"2.32.0--r43hdfd78af_0": "sha256:1f73efc7b15b9616a5293853dcd59252a4b35bcb3ed97e5f8bd16a1c93639d51"}, "tags": {"2.24.0--r41hdfd78af_0": "sha256:0b71a9e2208aac01902cd5bd1ee5e8f33aca194e6e9d2703bc8c54359c686471", "2.28.0--r42hdfd78af_0": "sha256:9e79d0a70a5158bc3feea43bfc5a4662bc66e02de3b27455a02e78d3e1601b17", "2.30.1--r43hdfd78af_0": "sha256:50af543c3e1143b055ebd38a07dea8109ce4950dce3986c972a19097ec73276a", "2.32.0--r43hdfd78af_0": "sha256:1f73efc7b15b9616a5293853dcd59252a4b35bcb3ed97e5f8bd16a1c93639d51"}, "docker": "quay.io/biocontainers/bioconductor-enrichmentbrowser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enrichmentbrowser.
shpc-registry automated BioContainers addition for bioconductor-enrichmentbrowser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichmentbrowser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichmentbrowser:2.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enrichmentbrowser/2.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-enrichmentbrowser/2.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enrichmentbrowser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichmentbrowser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichmentbrowser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enrichmentbrowser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enrichmentbrowser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enrichmentbrowser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-enrichmentbrowser

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