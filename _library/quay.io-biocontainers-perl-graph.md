---
layout: container
name:  "quay.io/biocontainers/perl-graph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-graph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-graph/container.yaml"
updated_at: "2025-08-28 11:53:24.011732"
latest: "0.9735--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-graph"

versions:
 - "0.9725--pl5321hdfd78af_0"
 - "0.9726--pl5321hdfd78af_0"
 - "0.9727--pl5321hdfd78af_0"
 - "0.9729--pl5321hdfd78af_0"
 - "0.9728--pl5321hdfd78af_0"
 - "0.9732--pl5321hdfd78af_0"
 - "0.9731--pl5321hdfd78af_0"
 - "0.9730--pl5321hdfd78af_0"
 - "0.9733--pl5321hdfd78af_0"
 - "0.9734--pl5321hdfd78af_0"
 - "0.9735--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-graph"
config: {"url": "https://biocontainers.pro/tools/perl-graph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-graph", "latest": {"0.9735--pl5321hdfd78af_0": "sha256:5a09348ae74d972a53c6cae34147c986cf4f4014bfa8c2347d7d854729a22d55"}, "tags": {"0.9725--pl5321hdfd78af_0": "sha256:12bddd0a13f2c6e9603806d960f22e045cd82f267cf904561e33554322c9ed0e", "0.9726--pl5321hdfd78af_0": "sha256:067044194856d198119c049b6f434a9540e50443099163483d7311a6b782afd1", "0.9727--pl5321hdfd78af_0": "sha256:da57abb20bd065bb2fa7bf72dbe9d389db238920a83e9af3ed288eb39ec6ae4a", "0.9729--pl5321hdfd78af_0": "sha256:5b0c5fbbe5d61c562948c45d927fc852edd3cd5523ff45d4fae464be98c0904c", "0.9728--pl5321hdfd78af_0": "sha256:3f6158a8a412c662cfe4ab63772e9bb8d8ec95785aa3c55980ab0e3d5c6e2998", "0.9732--pl5321hdfd78af_0": "sha256:52342e41caa28afa5680a97a200056826b22f59848376f64734a5214947b9b35", "0.9731--pl5321hdfd78af_0": "sha256:171d2f634879f2d24d2e98a93d9ac495e8a05f7d0f14a00776e2880d74a5f96e", "0.9730--pl5321hdfd78af_0": "sha256:308357e4da22c07dbc962524b849a258420ccf49a80c8bc824af162f0ebdf17b", "0.9733--pl5321hdfd78af_0": "sha256:3e01ff36c3a68a3eed37832f681b68c609db045f12ab93e81ea72256767e8382", "0.9734--pl5321hdfd78af_0": "sha256:c80f7b33f48d166852c4d3c909e568412f9ecfd876a398c168c5f8a5c3ea1549", "0.9735--pl5321hdfd78af_0": "sha256:5a09348ae74d972a53c6cae34147c986cf4f4014bfa8c2347d7d854729a22d55"}, "docker": "quay.io/biocontainers/perl-graph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-graph.
shpc-registry automated BioContainers addition for perl-graph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-graph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-graph:0.9735--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-graph/0.9735--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-graph/0.9735--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-graph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-graph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-graph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-graph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-graph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-graph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-graph

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