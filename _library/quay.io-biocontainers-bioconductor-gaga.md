---
layout: container
name:  "quay.io/biocontainers/bioconductor-gaga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gaga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gaga/container.yaml"
updated_at: "2024-10-04 03:21:27.030090"
latest: "2.48.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-gaga"

versions:
 - "2.40.0--r41hc0cfd56_2"
 - "2.44.0--r42hc0cfd56_0"
 - "2.44.0--r42ha9d7317_1"
 - "2.46.0--r43ha9d7317_0"
 - "2.48.0--r43ha9d7317_0"
 - "2.48.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-gaga"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gaga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gaga", "latest": {"2.48.0--r43ha9d7317_1": "sha256:a72b295c7c2f5d00cda30dd1062ecc2cab5944a6bbc33c37ac44bdf61424e6b2"}, "tags": {"2.40.0--r41hc0cfd56_2": "sha256:5d557f824ecf3ff50b48db774c6eaa1fdcac09cdcff1781befb03033d6b7a53b", "2.44.0--r42hc0cfd56_0": "sha256:c7ecee70f208622f3acd028358cdf44362c524be0d24462ef83c6989d1822f1a", "2.44.0--r42ha9d7317_1": "sha256:547d1fdeb6b66e851125e069163342eac0b0eedc3c5112ded47b6bc2f43056c5", "2.46.0--r43ha9d7317_0": "sha256:9cdfb23da2940e0965aff256db6039595816a1f7b4b99f4fa11ff66d78dd23c9", "2.48.0--r43ha9d7317_0": "sha256:2fe2ea6faeb84fb978c4253bcc01bf72ec57396ddadaf581f17bd022c868f4a5", "2.48.0--r43ha9d7317_1": "sha256:a72b295c7c2f5d00cda30dd1062ecc2cab5944a6bbc33c37ac44bdf61424e6b2"}, "docker": "quay.io/biocontainers/bioconductor-gaga"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gaga.
shpc-registry automated BioContainers addition for bioconductor-gaga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gaga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gaga:2.48.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gaga/2.48.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-gaga/2.48.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gaga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gaga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gaga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gaga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gaga

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