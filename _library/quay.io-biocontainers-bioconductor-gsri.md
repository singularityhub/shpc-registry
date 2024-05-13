---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsri"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsri/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsri/container.yaml"
updated_at: "2024-05-13 02:36:11.444995"
latest: "2.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsri"

versions:
 - "2.42.0--r41hdfd78af_0"
 - "2.46.0--r42hdfd78af_0"
 - "2.48.0--r43hdfd78af_0"
 - "2.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsri"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsri", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsri", "latest": {"2.50.0--r43hdfd78af_0": "sha256:cf62fd413875e0d1ab5f19f4135b1726c84d2b2c63267595122622777a398b80"}, "tags": {"2.42.0--r41hdfd78af_0": "sha256:f1960cd105921c9d018e45d23a803bfc8ba2b364f28a06d2a18ea6c4c28a955d", "2.46.0--r42hdfd78af_0": "sha256:ec2edd296f15932b4ca37d871cd0abbbf696cd16945cdc59d63b2cabb6252ee3", "2.48.0--r43hdfd78af_0": "sha256:b69bbabd163d6f22d0267acb2b8f694a67d3c68b949843a5049b583d20fe0ed4", "2.50.0--r43hdfd78af_0": "sha256:cf62fd413875e0d1ab5f19f4135b1726c84d2b2c63267595122622777a398b80"}, "docker": "quay.io/biocontainers/bioconductor-gsri"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsri.
shpc-registry automated BioContainers addition for bioconductor-gsri
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsri
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsri:2.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsri/2.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsri/2.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsri-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsri-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsri-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsri-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsri-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsri-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsri

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