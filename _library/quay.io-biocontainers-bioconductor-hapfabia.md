---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapfabia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapfabia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapfabia/container.yaml"
updated_at: "2026-01-10 03:46:21.394009"
latest: "1.48.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapfabia"

versions:
 - "1.36.0--r41hc0cfd56_2"
 - "1.40.0--r42hc0cfd56_0"
 - "1.40.0--r42ha9d7317_1"
 - "1.42.0--r43ha9d7317_0"
 - "1.44.0--r43ha9d7317_0"
 - "1.48.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapfabia"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapfabia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapfabia", "latest": {"1.48.0--r44h3df3fcb_0": "sha256:d76bf107631f715a3258cdf042f15806040f44f81ee4c4fc48559a5782b8724c"}, "tags": {"1.36.0--r41hc0cfd56_2": "sha256:c4e92ea65ba47de1f41aab6dd1f80a2e2fcb214cc820459ef38d57947b376802", "1.40.0--r42hc0cfd56_0": "sha256:9ad18f35eb7b70f5aff1d2e03f26b38f575647102fdf17f3e098702bcbb35e09", "1.40.0--r42ha9d7317_1": "sha256:1f20ae3b083775278e73d84470eec5415d5426167ff34c3b09a4aa9900ae299d", "1.42.0--r43ha9d7317_0": "sha256:72ef90defca4ca8eeeeb38809c097b880a35ebfe912a1cc62db4b1385347614f", "1.44.0--r43ha9d7317_0": "sha256:6bef3340961c518dd9ceafdc61015f8a37550218489ec96f7050b65801ee1063", "1.48.0--r44h3df3fcb_0": "sha256:d76bf107631f715a3258cdf042f15806040f44f81ee4c4fc48559a5782b8724c"}, "docker": "quay.io/biocontainers/bioconductor-hapfabia"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapfabia.
shpc-registry automated BioContainers addition for bioconductor-hapfabia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapfabia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapfabia:1.48.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapfabia/1.48.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-hapfabia/1.48.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapfabia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapfabia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapfabia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapfabia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapfabia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapfabia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapfabia

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