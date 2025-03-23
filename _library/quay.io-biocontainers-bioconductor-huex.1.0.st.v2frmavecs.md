---
layout: container
name:  "quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs/container.yaml"
updated_at: "2025-03-23 03:27:38.410096"
latest: "1.1.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-huex.1.0.st.v2frmavecs"

versions:
 - "1.1.0--r41hdfd78af_9"
 - "1.1.0--r42hdfd78af_10"
 - "1.1.0--r43hdfd78af_11"
 - "1.1.0--r43hdfd78af_12"
 - "1.1.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-huex.1.0.st.v2frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huex.1.0.st.v2frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huex.1.0.st.v2frmavecs", "latest": {"1.1.0--r44hdfd78af_13": "sha256:529a8314e1f3a5dbf7e943167b6ecd13ef55fc5989af7c4ccc509543286c4b85"}, "tags": {"1.1.0--r41hdfd78af_9": "sha256:bb7dbaaf8e0328adc8cd5f3b8c5cff4646d55c70c84f6e94e95bf3794bc3551c", "1.1.0--r42hdfd78af_10": "sha256:8c0f7f6fdfc14ddaaab629dadf64e0669ad0f5d9ef323067f3adbadc6f1c2794", "1.1.0--r43hdfd78af_11": "sha256:982989dfe9a097b56a19538c6d5e587ae9a6ff5ff28a4ddf3ea02b39847da846", "1.1.0--r43hdfd78af_12": "sha256:e290b52c6889194fa280468fd7973380e3eee3c6086dcdc71b6c7e4ace921d3b", "1.1.0--r44hdfd78af_13": "sha256:529a8314e1f3a5dbf7e943167b6ecd13ef55fc5989af7c4ccc509543286c4b85"}, "docker": "quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs.
shpc-registry automated BioContainers addition for bioconductor-huex.1.0.st.v2frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs:1.1.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs/1.1.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-huex.1.0.st.v2frmavecs/1.1.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huex.1.0.st.v2frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huex.1.0.st.v2frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huex.1.0.st.v2frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huex.1.0.st.v2frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huex.1.0.st.v2frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huex.1.0.st.v2frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huex.1.0.st.v2frmavecs

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