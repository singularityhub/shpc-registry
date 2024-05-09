---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowvs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowvs/container.yaml"
updated_at: "2024-05-09 03:11:02.045499"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowvs"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowvs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowvs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowvs", "latest": {"1.34.0--r43hdfd78af_0": "sha256:0cba60d43e90e3dddd2a90f9b0091b9cd8bd8cb95851776b9a7ed3b1a3614cba"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:fb17c462bac7cc5a099269be716dbe621fec44400cdf300117e6786ae2e17282", "1.30.0--r42hdfd78af_0": "sha256:129ce177a913ac79d0fb26b30dc7076e2020a8742db5b61694d3942089f58474", "1.32.0--r43hdfd78af_0": "sha256:324fcb01f9bfa7a4a6ccf589653e6a5350392bbb162766ae03c49d1137b1c847", "1.34.0--r43hdfd78af_0": "sha256:0cba60d43e90e3dddd2a90f9b0091b9cd8bd8cb95851776b9a7ed3b1a3614cba"}, "docker": "quay.io/biocontainers/bioconductor-flowvs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowvs.
shpc-registry automated BioContainers addition for bioconductor-flowvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowvs:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowvs/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowvs/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowvs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowvs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowvs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowvs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowvs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowvs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowvs

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