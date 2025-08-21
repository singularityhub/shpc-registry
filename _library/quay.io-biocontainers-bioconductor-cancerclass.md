---
layout: container
name:  "quay.io/biocontainers/bioconductor-cancerclass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cancerclass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cancerclass/container.yaml"
updated_at: "2025-08-21 03:17:52.081778"
latest: "1.50.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cancerclass"

versions:
 - "1.38.0--r41hc0cfd56_2"
 - "1.42.0--r42hc0cfd56_0"
 - "1.42.0--r42ha9d7317_1"
 - "1.44.0--r43ha9d7317_0"
 - "1.46.0--r43ha9d7317_0"
 - "1.50.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cancerclass"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cancerclass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cancerclass", "latest": {"1.50.0--r44h3df3fcb_0": "sha256:dc7d9249b8ecfb418240d0816f57f150e71d08f1592b10074741acec9fed3dff"}, "tags": {"1.38.0--r41hc0cfd56_2": "sha256:bdd51d5e9f36e8612b70a74b9c3ea95467ed697120de6cb32648a4ac576b6f18", "1.42.0--r42hc0cfd56_0": "sha256:1cf7f5e119e7904c5b2d9690866f72d57120d1a0a993cd6d62e7bcf16075a303", "1.42.0--r42ha9d7317_1": "sha256:7261ce1ab6d163d557bf7caf9e9cac322276f4f4009d32f5a5d8035efe2192ff", "1.44.0--r43ha9d7317_0": "sha256:c7142c3fc61632e479cd7f82bf4e3db2ce15996ab5c665923152ee78ce072b39", "1.46.0--r43ha9d7317_0": "sha256:7079ddac6cf63dd33cb208bd03bd00b67668dd501916e1d09829646a74d70dfb", "1.50.0--r44h3df3fcb_0": "sha256:dc7d9249b8ecfb418240d0816f57f150e71d08f1592b10074741acec9fed3dff"}, "docker": "quay.io/biocontainers/bioconductor-cancerclass"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cancerclass.
shpc-registry automated BioContainers addition for bioconductor-cancerclass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cancerclass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cancerclass:1.50.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cancerclass/1.50.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-cancerclass/1.50.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cancerclass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cancerclass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cancerclass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cancerclass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cancerclass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cancerclass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cancerclass

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