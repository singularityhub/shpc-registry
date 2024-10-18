---
layout: container
name:  "quay.io/biocontainers/bioconductor-tkwidgets"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tkwidgets/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tkwidgets/container.yaml"
updated_at: "2024-10-18 03:13:53.055498"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tkwidgets"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tkwidgets"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tkwidgets", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tkwidgets", "latest": {"1.80.0--r43hdfd78af_0": "sha256:4346a5b54a53d068167f370b398b3e864de141c5509f3e569ef661153f428276"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:94d8de59347395eb14b9bea42df2beacc1717ff276da54be4794218db5c2f1be", "1.76.0--r42hdfd78af_0": "sha256:4bee3715062827fb25bcad1bb4336ed94a159ea839102da013ec7774fd713b8d", "1.78.0--r43hdfd78af_0": "sha256:f80b696dcd260d22fa072c34d3ae6c35039c4642baae864b4e969068d3755ab2", "1.80.0--r43hdfd78af_0": "sha256:4346a5b54a53d068167f370b398b3e864de141c5509f3e569ef661153f428276"}, "docker": "quay.io/biocontainers/bioconductor-tkwidgets"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tkwidgets.
shpc-registry automated BioContainers addition for bioconductor-tkwidgets
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tkwidgets
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tkwidgets:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tkwidgets/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tkwidgets/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tkwidgets-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tkwidgets-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tkwidgets-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tkwidgets-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tkwidgets-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tkwidgets-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tkwidgets

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