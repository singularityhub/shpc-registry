---
layout: container
name:  "quay.io/biocontainers/bioconductor-xlaevis2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xlaevis2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xlaevis2probe/container.yaml"
updated_at: "2026-01-26 04:14:56.426055"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-xlaevis2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-xlaevis2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xlaevis2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xlaevis2probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:93367fce1c172862bcb899ac5ade28a38bf9b7e559e32bb81745a40f71e3e50c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:dcff6c20a711a5443c87ba3b9bd68e9e0cef6e57001141e3a53132ae2110ca64", "2.18.0--r42hdfd78af_10": "sha256:2225b3357de39280a685595917e4663174e452baddc623c9de9fe467a3b37fed", "2.18.0--r43hdfd78af_11": "sha256:d1b6f42de2c7d6b16edf992ac0150dee0aa69ca32569882cdfda5bc2a78ec4f4", "2.18.0--r43hdfd78af_12": "sha256:9fe8e2c54239e1abdea925977828712a17ea4478a9e1985473a636cb69b3efdf", "2.18.0--r44hdfd78af_13": "sha256:93367fce1c172862bcb899ac5ade28a38bf9b7e559e32bb81745a40f71e3e50c"}, "docker": "quay.io/biocontainers/bioconductor-xlaevis2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xlaevis2probe.
shpc-registry automated BioContainers addition for bioconductor-xlaevis2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xlaevis2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xlaevis2probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xlaevis2probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-xlaevis2probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xlaevis2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xlaevis2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xlaevis2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xlaevis2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xlaevis2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xlaevis2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xlaevis2probe

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