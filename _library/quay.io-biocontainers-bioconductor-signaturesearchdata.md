---
layout: container
name:  "quay.io/biocontainers/bioconductor-signaturesearchdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-signaturesearchdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-signaturesearchdata/container.yaml"
updated_at: "2024-06-05 02:58:14.959279"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-signaturesearchdata"
aliases:
 - "glpsol"
versions:
 - "1.8.4--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-signaturesearchdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-signaturesearchdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-signaturesearchdata", "latest": {"1.16.0--r43hdfd78af_0": "sha256:ce4657d68358475879c0825fd9d99740e0071e016912c09036f638571f6438e1"}, "tags": {"1.8.4--r41hdfd78af_0": "sha256:bb88caf6f711e35a82121714d3b2b1554dc8c8e0565ec18548c1288306923b06", "1.12.0--r42hdfd78af_0": "sha256:dabaf27917f3e60815c2e6768129c66a7b4724b572024119ec01c8242bf493c0", "1.14.0--r43hdfd78af_0": "sha256:ef375747971dc63473e44a2893cbaaa1b401d553dcc0263073a51510ae777abd", "1.16.0--r43hdfd78af_0": "sha256:ce4657d68358475879c0825fd9d99740e0071e016912c09036f638571f6438e1"}, "docker": "quay.io/biocontainers/bioconductor-signaturesearchdata", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-signaturesearchdata.
shpc-registry automated BioContainers addition for bioconductor-signaturesearchdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-signaturesearchdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-signaturesearchdata:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-signaturesearchdata/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-signaturesearchdata/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-signaturesearchdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signaturesearchdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signaturesearchdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-signaturesearchdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-signaturesearchdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-signaturesearchdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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