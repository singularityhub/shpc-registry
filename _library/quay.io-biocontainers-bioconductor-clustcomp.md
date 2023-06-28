---
layout: container
name:  "quay.io/biocontainers/bioconductor-clustcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clustcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clustcomp/container.yaml"
updated_at: "2023-06-28 03:00:18.731174"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clustcomp"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clustcomp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clustcomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clustcomp", "latest": {"1.26.0--r42hdfd78af_0": "sha256:b1660331e51054c05f897b6e435d872160e41e454dabda7d71fb8e0dcec22865"}, "tags": {"1.8.0--r351_0": "sha256:a0724afe0156ffc26cbe71013dc64e372714d60261840b86d7fc95565ca831cc", "1.26.0--r42hdfd78af_0": "sha256:b1660331e51054c05f897b6e435d872160e41e454dabda7d71fb8e0dcec22865", "1.22.0--r41hdfd78af_0": "sha256:1c08cb3d095383abd4578b8024be58a9792635cb3b1c15b84d4529fbc1c268d0", "1.20.0--r41hdfd78af_0": "sha256:7db697676e20da22b71a0f7d6058979df4933049d36deb20dfeb2ec55e1d91b6", "1.18.0--r40hdfd78af_1": "sha256:aaf9e7137e017426e3eb55e3fa329df6aebce541e152cb6ef2eebce010a2c151", "1.16.0--r40_0": "sha256:8ab9d75d4368b59e72767d4dcb2b6f0e8d4e7910879fc7208e0a856d10b812aa"}, "docker": "quay.io/biocontainers/bioconductor-clustcomp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clustcomp.
shpc-registry automated BioContainers addition for bioconductor-clustcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clustcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clustcomp:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clustcomp/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clustcomp/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clustcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clustcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clustcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clustcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clustcomp

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