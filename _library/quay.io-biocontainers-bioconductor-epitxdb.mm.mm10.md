---
layout: container
name:  "quay.io/biocontainers/bioconductor-epitxdb.mm.mm10"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epitxdb.mm.mm10/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epitxdb.mm.mm10/container.yaml"
updated_at: "2025-08-30 03:09:03.516189"
latest: "0.99.6--r44hdfd78af_8"
container_url: "https://biocontainers.pro/tools/bioconductor-epitxdb.mm.mm10"

versions:
 - "0.99.6--r41hdfd78af_4"
 - "0.99.6--r42hdfd78af_5"
 - "0.99.6--r43hdfd78af_6"
 - "0.99.6--r43hdfd78af_7"
 - "0.99.6--r44hdfd78af_8"
description: "shpc-registry automated BioContainers addition for bioconductor-epitxdb.mm.mm10"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epitxdb.mm.mm10", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epitxdb.mm.mm10", "latest": {"0.99.6--r44hdfd78af_8": "sha256:7becd5f50574ad3ef691c089245174b37f1f5c6391ee917a3b7161d13f2c85b7"}, "tags": {"0.99.6--r41hdfd78af_4": "sha256:f5e3ca6caf50db440e05110946f3507c4afbc4aae86daeec55bcf46cecb5b5c3", "0.99.6--r42hdfd78af_5": "sha256:9bb88372bc816267f571708aca186d52f8cfabd2fb5a73e8ee14ff1db399fc3d", "0.99.6--r43hdfd78af_6": "sha256:6e97a6a614e6e45826adaf318f24d6853adeac2d7dbf3e4b56e768b34312ae73", "0.99.6--r43hdfd78af_7": "sha256:09a51180020825e7ca296ab780b7244e9ce0160833bb8c55056bb01c69d2de74", "0.99.6--r44hdfd78af_8": "sha256:7becd5f50574ad3ef691c089245174b37f1f5c6391ee917a3b7161d13f2c85b7"}, "docker": "quay.io/biocontainers/bioconductor-epitxdb.mm.mm10"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epitxdb.mm.mm10.
shpc-registry automated BioContainers addition for bioconductor-epitxdb.mm.mm10
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb.mm.mm10
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb.mm.mm10:0.99.6--r44hdfd78af_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epitxdb.mm.mm10/0.99.6--r44hdfd78af_8
$ module help quay.io/biocontainers/bioconductor-epitxdb.mm.mm10/0.99.6--r44hdfd78af_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epitxdb.mm.mm10-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb.mm.mm10-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb.mm.mm10-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epitxdb.mm.mm10-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epitxdb.mm.mm10-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epitxdb.mm.mm10-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-epitxdb.mm.mm10

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