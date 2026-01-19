---
layout: container
name:  "quay.io/biocontainers/bioconductor-affymetrixdatatestfiles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affymetrixdatatestfiles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affymetrixdatatestfiles/container.yaml"
updated_at: "2026-01-19 05:15:22.363663"
latest: "0.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affymetrixdatatestfiles"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
 - "0.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affymetrixdatatestfiles"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affymetrixdatatestfiles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affymetrixdatatestfiles", "latest": {"0.44.0--r44hdfd78af_0": "sha256:b56a9cfbed96ba8a5ab5fed1b831a062640d83fb218700f3e16f3dfaad92e558"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:55eab41c1e0ef118f812ba138cceb383712127f08ea794c46b4b2c16bcc02a7a", "0.35.0--r42hdfd78af_0": "sha256:3527daa7d8d772fb901aa1d87854d3aafb0f2f112cbd84be7a538e49b0dfb8f1", "0.38.0--r43hdfd78af_0": "sha256:e1a319f4c8922338a8eaf926a815686e93a5b5ed1f856086f8ae9af1c8859e30", "0.40.0--r43hdfd78af_0": "sha256:684c03eea619877b825a479b5037350092ded1ee527fee8c8914b4f33029f179", "0.44.0--r44hdfd78af_0": "sha256:b56a9cfbed96ba8a5ab5fed1b831a062640d83fb218700f3e16f3dfaad92e558"}, "docker": "quay.io/biocontainers/bioconductor-affymetrixdatatestfiles"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affymetrixdatatestfiles.
shpc-registry automated BioContainers addition for bioconductor-affymetrixdatatestfiles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affymetrixdatatestfiles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affymetrixdatatestfiles:0.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affymetrixdatatestfiles/0.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affymetrixdatatestfiles/0.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affymetrixdatatestfiles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affymetrixdatatestfiles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affymetrixdatatestfiles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affymetrixdatatestfiles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affymetrixdatatestfiles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affymetrixdatatestfiles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affymetrixdatatestfiles

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