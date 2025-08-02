---
layout: container
name:  "quay.io/biocontainers/bioconductor-brain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-brain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-brain/container.yaml"
updated_at: "2025-08-02 04:10:21.883578"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-brain"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-brain"
config: {"url": "https://biocontainers.pro/tools/bioconductor-brain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-brain", "latest": {"1.52.0--r44hdfd78af_0": "sha256:2ed305fc4849ce42bebe9dc735dac9a1ec3984a6a1f380a62f46f88a861d082f"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:0f385a0efb7516c3352c6a61bb7f5d502603aebc7474291cc2d6df644e4e2363", "1.44.0--r42hdfd78af_0": "sha256:3449f851e0010ddc5a03126c3291ab28693cf562013fa31bbb1bc46070e93115", "1.46.0--r43hdfd78af_0": "sha256:ae0ce38fa1f01dc84ec9f79a1391de335f9e813b84333959104195ea192e7058", "1.48.0--r43hdfd78af_0": "sha256:20ab7c37cd6cacc7aabdcc11a63f4b3a1101ec0b491f2fdcb6ba67dfddb895a8", "1.52.0--r44hdfd78af_0": "sha256:2ed305fc4849ce42bebe9dc735dac9a1ec3984a6a1f380a62f46f88a861d082f"}, "docker": "quay.io/biocontainers/bioconductor-brain"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-brain.
shpc-registry automated BioContainers addition for bioconductor-brain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-brain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-brain:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-brain/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-brain/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-brain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-brain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-brain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-brain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-brain

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