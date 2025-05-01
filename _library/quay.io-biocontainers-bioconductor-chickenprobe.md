---
layout: container
name:  "quay.io/biocontainers/bioconductor-chickenprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chickenprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chickenprobe/container.yaml"
updated_at: "2025-05-01 03:33:19.145332"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-chickenprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-chickenprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chickenprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chickenprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:a045419c254c61ca9c7cf362d883af8dd61c96f2e3d4eec86032a54f4aa8212a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:75205cff718609f59ebceb148c1fef0f80887ddace223d23ba82f524dd2285a9", "2.18.0--r42hdfd78af_10": "sha256:3dbc6d94d8623a34d9629c838f7e4ad426aa7d573a471106603bbb531f0069d4", "2.18.0--r43hdfd78af_11": "sha256:27b058ab8d6b756a3232ee3466e8b5f48f834e8e18602cc82cda3845a78010c0", "2.18.0--r43hdfd78af_12": "sha256:0814b3f6cb634d996130807b401e9cca8a38b973bd44eb41191bed2b30ebbbc9", "2.18.0--r44hdfd78af_13": "sha256:a045419c254c61ca9c7cf362d883af8dd61c96f2e3d4eec86032a54f4aa8212a"}, "docker": "quay.io/biocontainers/bioconductor-chickenprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chickenprobe.
shpc-registry automated BioContainers addition for bioconductor-chickenprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chickenprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chickenprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chickenprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-chickenprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chickenprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chickenprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chickenprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chickenprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chickenprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chickenprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chickenprobe

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