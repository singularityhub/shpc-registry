---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs/container.yaml"
updated_at: "2024-11-27 03:33:18.628835"
latest: "1.1.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mogene.1.0.st.v1frmavecs"

versions:
 - "1.1.0--r41hdfd78af_9"
 - "1.1.0--r42hdfd78af_10"
 - "1.1.0--r43hdfd78af_11"
 - "1.1.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mogene.1.0.st.v1frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogene.1.0.st.v1frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogene.1.0.st.v1frmavecs", "latest": {"1.1.0--r43hdfd78af_12": "sha256:3ff34f3a15ca3d0ff381f0ec88b15babeeff57393b78635094b63faef743cff2"}, "tags": {"1.1.0--r41hdfd78af_9": "sha256:85a0787f2e97a57150c6268547f4228e7f11fa3b79fa657b642e418ce7b4892e", "1.1.0--r42hdfd78af_10": "sha256:bde96ba56896f18c4b2e7545916f27c971f9c696655f865b22584fd10b7aa088", "1.1.0--r43hdfd78af_11": "sha256:d54c08be3ec1b1a0d485c477833fb1c6e7a7a6f546810d98b9c0839b8fbcc640", "1.1.0--r43hdfd78af_12": "sha256:3ff34f3a15ca3d0ff381f0ec88b15babeeff57393b78635094b63faef743cff2"}, "docker": "quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs.
shpc-registry automated BioContainers addition for bioconductor-mogene.1.0.st.v1frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs:1.1.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs/1.1.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mogene.1.0.st.v1frmavecs/1.1.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogene.1.0.st.v1frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene.1.0.st.v1frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene.1.0.st.v1frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogene.1.0.st.v1frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogene.1.0.st.v1frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogene.1.0.st.v1frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogene.1.0.st.v1frmavecs

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