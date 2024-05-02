---
layout: container
name:  "quay.io/biocontainers/bioconductor-hilbertcurve"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hilbertcurve/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hilbertcurve/container.yaml"
updated_at: "2024-05-02 03:27:37.379006"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hilbertcurve"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hilbertcurve"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hilbertcurve", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hilbertcurve", "latest": {"1.32.0--r43hdfd78af_0": "sha256:80a306007aadb33936e2a6b1f8335c17e2fb7589a5e5d6bc0c5097be5ea8d21a"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:dbb2b77da3b55e190f036d0b25968ccad01a3a41183382b9be4b568fbba76425", "1.28.0--r42hdfd78af_0": "sha256:f54a8e8cbb9686674af24aff82c81edce42b90b966f702a906ce39b3467b7234", "1.30.0--r43hdfd78af_0": "sha256:83d3dd2c89ee58cfd6d612bd5e8bc265766bb679eba4eb2b993612aba96bd2e6", "1.32.0--r43hdfd78af_0": "sha256:80a306007aadb33936e2a6b1f8335c17e2fb7589a5e5d6bc0c5097be5ea8d21a"}, "docker": "quay.io/biocontainers/bioconductor-hilbertcurve"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hilbertcurve.
shpc-registry automated BioContainers addition for bioconductor-hilbertcurve
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hilbertcurve
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hilbertcurve:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hilbertcurve/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hilbertcurve/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hilbertcurve-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilbertcurve-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hilbertcurve-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hilbertcurve-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hilbertcurve-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hilbertcurve-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hilbertcurve

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