---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellxgenedp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellxgenedp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellxgenedp/container.yaml"
updated_at: "2025-05-25 04:09:02.782568"
latest: "1.10.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellxgenedp"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.1--r43hdfd78af_0"
 - "1.10.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-cellxgenedp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellxgenedp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-cellxgenedp", "latest": {"1.10.0--r44hdfd78af_0": "sha256:c9201be52b3ccc088c01b8cca3c8154a366a9a4b22c89d3fce61b1ee96cda592"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:5fe8728f1725cfbe6a8fae60cf676e864ec44bfd7d73e1e9b45a9dcc7cb0bb43", "1.4.0--r43hdfd78af_0": "sha256:24e61582ef30d50bba05614891aa9867927945a2771fd90eaada2f5dc712aff8", "1.6.1--r43hdfd78af_0": "sha256:d8592ecbc8965ce681bd469a7bb88cc31b7816f36b2e236ff7aa8361e4cd0fab", "1.10.0--r44hdfd78af_0": "sha256:c9201be52b3ccc088c01b8cca3c8154a366a9a4b22c89d3fce61b1ee96cda592"}, "docker": "quay.io/biocontainers/bioconductor-cellxgenedp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellxgenedp.
singularity registry hpc automated addition for bioconductor-cellxgenedp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellxgenedp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellxgenedp:1.10.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellxgenedp/1.10.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellxgenedp/1.10.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellxgenedp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellxgenedp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellxgenedp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellxgenedp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellxgenedp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellxgenedp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellxgenedp

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