---
layout: container
name:  "quay.io/biocontainers/bioconductor-sampleclassifierdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sampleclassifierdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sampleclassifierdata/container.yaml"
updated_at: "2023-07-19 04:21:34.514528"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sampleclassifierdata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sampleclassifierdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sampleclassifierdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sampleclassifierdata", "latest": {"1.22.0--r42hdfd78af_0": "sha256:026a2668e0b443019bdd519318642cd1e34f6eaa0dc874e7925bf71f48f0d10b"}, "tags": {"1.8.0--r36_1": "sha256:4defde2cbc9210877f3c2d6d17dab085f459325c8b98a22809df8317b75f84a3", "1.22.0--r42hdfd78af_0": "sha256:026a2668e0b443019bdd519318642cd1e34f6eaa0dc874e7925bf71f48f0d10b", "1.18.0--r41hdfd78af_1": "sha256:4ddebc7ce324681c43ae90b5dc577f5e0804e8fbb3eec82b5469bc7dd6b52385", "1.16.0--r41hdfd78af_0": "sha256:b0d6750e83c865a4ea6d1f2547f42469dfaf5461f45e600cb48e50658eda170b", "1.14.1--r40hdfd78af_0": "sha256:d8f7dbe1c4a4b606835de4c95afa0d4802fac6fe7be13cb5563e88cb48c163e3", "1.12.0--r40_0": "sha256:b84a9639a6f1e24f0d3f29e81544564df0079c5c9a7e07b5436ed0cecd9cca84"}, "docker": "quay.io/biocontainers/bioconductor-sampleclassifierdata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sampleclassifierdata.
shpc-registry automated BioContainers addition for bioconductor-sampleclassifierdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sampleclassifierdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sampleclassifierdata:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sampleclassifierdata/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sampleclassifierdata/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sampleclassifierdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sampleclassifierdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sampleclassifierdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sampleclassifierdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sampleclassifierdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sampleclassifierdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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